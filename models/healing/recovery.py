"""Recovery after a large hit on one tank (Analysis, Healing, part 5).
Healing that lands on the tank in the first 3 and 6 sec after the hit. The healer starts to cast at 0.
No overhealing (the tank has a large health deficit).
Two cases: all cooldowns ready, and only short cooldowns (less than 1 min) ready.

The healer heals the tank before the hit (warm start):
- Each healer has its heals over time on the tank, as in its one-tank cast plan: Renew (Priest), Rejuvenation
  and Regrowth (Druid), Riptide and Healing Stream Totem (Shaman). Their remaining time at the hit is random
  (uniform). Their ticks after the hit count. A new cast of the same spell replaces the old one.
- Heals over time cast after the hit land in ticks of 3 sec (Lingering Light: 2 sec).
- The Paladin has cast Flash of Light on the tank (one each 1.5 sec). Infusion of Light can be active at the
  hit, and with C-H2 the Lingering Light pool is on the tank. Lingering Light follows its text: a non-periodic
  critical heal adds 20% of the heal to the remaining healing, and the total is spread over a new 6 sec (one
  tick each 2 sec). A critical tick does not start it again.
- Infusion of Light: a Flash of Light or Holy Shock makes the next Holy Light 1 sec faster (C-H3: each cast;
  beta: a critical heal only). It stays active until a Holy Light uses it.
- The Paladin values come from a simulation (Monte Carlo) of the critical heals, Infusion of Light and the
  Lingering Light pool, before and after the hit. The same random numbers are used for each sequence.
- The Druid has a Rejuvenation on the tank: Swiftmend is ready.
  If the Rejuvenation ran out before the Swiftmend, it uses the Regrowth. Swiftmend heals for the full heal over
  time (Forever text). Druid talents: Nature's Splendor (Rejuvenation 15 sec, Regrowth 27 sec) and Gift of the
  Earthmother (1 sec global cooldown for Rejuvenation and Swiftmend). The Priest has no Penance (DoubleZug build).
Run: python3 recovery.py"""
import itertools, math, random
import healing_model as H
from healing_model import HPG, CRIT_BASE, PAL_CRIT, ll_ticks

GCD = 1.5

class B:
    """name, cast time (GCD for instants), expected direct heal, heal over time (total), its duration and tick,
    cooldown class ('long' = 1 min or more), tags.
    Paladin: ll = Lingering Light added on a critical heal, cc = chance of a critical heal.
    fn(end, earlier spell names): direct heal that depends on the state (Swiftmend)."""
    def __init__(s, name, t, direct, hot=0.0, dur=1.0, tick=3.0, cd=None, tags=(), ll=0.0, cc=0.0, fn=None):
        s.name, s.t, s.direct, s.hot, s.dur, s.tick, s.cd, s.tags = name, t, direct, hot, dur, tick, cd, set(tags)
        s.ll, s.cc, s.fn = ll, cc, fn

def pre_hots(pre, ends, W):
    """Expected ticks in the window of the heals over time that are on the tank at the hit.
    pre: (spell name that replaces it, healing per sec, duration or None for a totem)."""
    v = 0.0
    for name, rate, D in pre:
        L = min([W] + [e for s, e in ends if s.name == name])
        v += rate * L if D is None else rate * (L - L*L/(2*D))   # remaining time uniform in (0, D)
    return v

def hot_ticks(s, end, W):
    """Ticks of a heal over time cast at 'end' that land in the window."""
    if not s.hot: return 0.0
    n = round(s.dur / s.tick)
    k = min(n, math.floor((W - end) / s.tick + 1e-9))
    return s.hot * max(0, k) / n

# ---------------------------------------------------------------- evaluation
def eval_fixed(seq, W, pre):
    """Classes with no random state in the window (Priest, Druid, Shaman)."""
    t = 0.0; v = 0.0; ends = []
    for s in seq:
        end = t + s.t
        if end > W + 1e-9: break
        before = [x.name for x, _ in ends]
        v += (s.fn(end, before) if s.fn else s.direct) + hot_ticks(s, end, W)
        ends.append((s, end)); t = end
    return v + pre_hots(pre, ends, W)

def eval_paladin(seq, W, pal, samples=3000, seed=7):
    """Paladin: simulation of critical heals, Infusion of Light and Lingering Light."""
    c, ling, fol_h, inf_all, kt = pal["c"], pal["ling"], pal["fol"], pal["inf_all"], pal["kt"]
    rng = random.Random(seed); tot = 0.0
    for _ in range(samples):
        # 20 Flash of Light casts before the hit, one each 1.5 sec; the last one ends at the hit
        crits = [rng.random() < c for _ in range(20)]
        ev = [(-1.5*i, ling*fol_h*1.5) for i in range(20) if crits[i]] if (ling and pal.get("pre_ll", True)) else []
        inf = True if inf_all else any(crits[:10])        # Infusion of Light lasts 15 sec
        t = 0.0; v = 0.0
        for s in seq:
            ct = s.t
            if "infusable" in s.tags and inf:
                ct = max(GCD, s.t - 1.0); inf = False
            end = t + ct
            if end > W + 1e-9: break
            v += s.direct
            crit = rng.random() < s.cc
            if s.ll and crit: ev.append((end, s.ll))
            if "trigger" in s.tags and (inf_all or crit): inf = True
            t = end
        if ev: v += sum(a for tt, a in ll_ticks(ev) if 0 < tt <= W + 1e-9) * kt
        tot += v
    return tot / samples

def best(case, W, long_cd=True):
    """Best sequence of up to 5 casts. Sequences with the same casts in the window are evaluated one time."""
    spells, needs, pre, pal = case
    pool = [s for s in spells if long_cd or s.cd != "long"]
    def fast(s): return GCD if (pal and "infusable" in s.tags) else s.t     # shortest possible cast time
    keys = set()
    for n in range(1, 6):
        for seq in itertools.product(pool, repeat=n):
            names = [s.name for s in seq]
            # each cooldown spell at most one time in the window; one "long" cooldown only
            if any(names.count(s.name) > 1 for s in seq if s.cd): continue
            if sum(1 for s in seq if s.cd == "long") > 1: continue
            if needs and not needs(seq): continue
            t = 0.0; key = []
            for s in seq:
                t += fast(s)
                if t > W + 1e-9: break
                key.append(s)
            if key: keys.add(tuple(key))
    res = []
    for key in keys:
        v = eval_paladin(key, W, pal) if pal else eval_fixed(key, W, pre)
        res.append((round(v, 6), -len(key), tuple(s.name for s in key)))
    v, _, names = max(res)
    return v, names

# ---------------------------------------------------------------- classes (715 healing power)
def paladin_burst(hp=HPG, light=1.12, bol=True, ling=0.0, conv=0.0, inf_all=False):
    c = CRIT_BASE + PAL_CRIT + 0.05 + conv; c_hs = CRIT_BASE + PAL_CRIT + 0.15 + conv
    fol = (308 + (115 if bol else 0) + 1.5/3.5*hp) * light
    hl = (1580 + (400 if bol else 0) + 2.5/3.5*hp) * light
    hs = (320 + 1.5/3.5*hp) * light
    kt = (1 + 0.5*c) if H.HOT_CRIT else 1.0                 # Lingering Light ticks can be critical heals
    L = lambda h: ling*h*1.5                                 # Lingering Light added by one critical heal
    sp = [B("Flash of Light", 1.5, fol*(1+0.5*c), tags=("trigger",), ll=L(fol), cc=c),
          B("Holy Light", 2.5, hl*(1+0.5*c), tags=("infusable",), ll=L(hl), cc=c),
          B("Holy Shock", GCD, hs*(1+0.5*c_hs), cd="short", tags=("trigger",), ll=L(hs), cc=c_hs),
          B("Divine Favor + Holy Light", 2.5, hl*1.5, cd="long", tags=("infusable",), ll=L(hl), cc=1.0)]
    pal = dict(c=c, ling=ling, fol=fol, inf_all=inf_all, kt=kt)
    return sp, None, (), pal

def priest_burst(hp=HPG):
    hp = hp + 84; d = hp - 799; c = 0.1903; k = 1 + 0.5*c; k_if = 1 + 0.5*(c + 0.25)
    gh = 2688.8 + 0.934*d
    kh = k if H.HOT_CRIT else 1.0
    renew = (1941.2 + 1.316*d)*kh
    sp = [B("Flash Heal", 1.5, (1272.4 + 0.467*d)*k),
          B("Greater Heal", 2.5, gh*k),
          B("Renew", GCD, 0, renew, 15),
          B("Inner Focus + Greater Heal", 2.5, gh*k_if, cd="long")]
    return sp, None, [("Renew", renew/15, 15)], None

def druid_burst(hp=HPG):
    c = 0.183; k = 1 + 0.5*c; kh = k if H.HOT_CRIT else 1.0
    # Nature's Splendor: Rejuvenation 15 sec, Regrowth 27 sec. Gift of the Earthmother: 1 sec global cooldown
    # for Rejuvenation and Swiftmend. Genesis: +5% periodic healing.
    rej0 = (776*15/12 + 1.0*hp)*1.1*1.15*1.05; rej = rej0*kh
    rg_dir = (1021 + 0.286*hp)*1.1*(1 + 0.5*(c + 0.5)); rg_hot0 = (994 + 0.497*hp)*27/21*1.1*1.05; rg_hot = rg_hot0*kh
    ht = (2934.8 + 1.1*(hp - 715))*k
    sm_rej = rej0*k                     # Swiftmend: the full Rejuvenation, a direct heal (can be critical)
    sm_rg = rg_hot0*k                   # or the full Regrowth heal over time
    def swiftmend(end, before):
        if "Rejuvenation" in before: return sm_rej
        p_rej = max(0.0, 1 - end/15)    # the Rejuvenation on the tank is still there
        p_rg = 1.0 if "Regrowth" in before else max(0.0, 1 - end/27)
        return p_rej*sm_rej + (1 - p_rej)*p_rg*sm_rg
    sp = [B("Healing Touch", 3.0, ht),
          B("Regrowth", 2.0, rg_dir, rg_hot, 27),
          B("Rejuvenation", 1.0, 0, rej, 15),
          B("Swiftmend", 1.0, 0, cd="short", fn=swiftmend),
          B("Nature's Swiftness + Healing Touch", 1.5, ht, cd="long")]
    def needs(seq):   # a new Regrowth or Rejuvenation replaces the old one
        names = [x.name for x in seq]
        return names.count("Regrowth") <= 1 and names.count("Rejuvenation") <= 1
    pre = [("Rejuvenation", rej/15, 15), ("Regrowth", rg_hot/27, 27)]
    return sp, needs, pre, None

def shaman_burst(hp=HPG):
    c = 0.243; k = 1 + 0.5*c; kh = k if H.HOT_CRIT else 1.0
    hw = (1371.5 + 3/3.5*hp)*1.1*1.25*k
    rt_hot = (805 + 0.5*hp)*1.1*kh
    sp = [B("Healing Wave", 2.5, hw),
          B("Lesser Healing Wave", 1.5, (820 + 1.5/3.5*hp)*1.1*k),
          B("Riptide", GCD, (841 + 0.2*hp)*1.1*k, rt_hot, 15, cd="short"),
          B("Chain Heal (on the tank, after Riptide)", 2.5, (506.5 + 2.5/3.5*hp)*1.1*1.25*k),
          B("Nature's Swiftness + Healing Wave", 1.5, hw, cd="long")]
    pre = [("Riptide", rt_hot/15, 15), ("Healing Stream Totem", (11 + 0.02*hp)*kh/2, None)]
    return sp, None, pre, None

PROP_B = dict(light=1.30, bol=False, ling=0.2, conv=0.05, inf_all=True)

def table(hp=HPG):
    rows = []
    cases = [("Priest", priest_burst(hp)), ("Druid", druid_burst(hp)), ("Shaman", shaman_burst(hp)),
             ("Paladin, beta", paladin_burst(hp)), ("Paladin, proposed", paladin_burst(hp, **PROP_B))]
    for name, case in cases:
        r = [name]
        for long_cd in (True, False):
            for W in (3.0, 6.0):
                v, seq = best(case, W, long_cd)
                r.append((round(v), seq))
        rows.append(r)
    return rows

if __name__ == "__main__":
    for hp in (715, 900):
        print("## healing power", hp, "| 3 sec, 6 sec (all cooldowns) | 3 sec, 6 sec (short cooldowns only)")
        for r in table(hp):
            print(f"  {r[0]:18s} " + " | ".join(f"{v:5d}" for v, _ in r[1:]))
            for v, seq in r[1:]: print("        ", v, " > ".join(seq))
