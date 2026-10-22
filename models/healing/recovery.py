"""Recovery after a large hit on one tank (Analysis, Healing, part 5).
Healing that lands on the tank in the first 3 and 6 sec after the hit. The healer starts to cast at 0.
No overhealing (the tank has a large health deficit). Heals over time count only the ticks inside the window.
Two cases: all cooldowns ready, and only short cooldowns (less than 1 min) ready.

The healer heals the tank before the hit (warm start):
- Each healer has its heals over time on the tank, as in its one-tank cast plan: Renew (Priest), Rejuvenation
  and Regrowth (Druid), Riptide and Healing Stream Totem (Shaman). Their remaining time at the hit is random
  (uniform). Their ticks after the hit count. A new cast of the same spell replaces the old one.
- The Paladin has cast Flash of Light (Infusion of Light can be active). With C2, its Lingering Light pool
  is on the tank. Lingering Light follows its text: a non-periodic critical heal adds 20% of the heal to the
  remaining healing, and the total is spread over a new 6 sec (one tick each 2 sec). A critical tick does not
  start it again. The pool is simulated (Monte Carlo) for the casts before and after the hit.
- The Druid has a Rejuvenation on the tank: Swiftmend is ready.
Run: python3 recovery.py"""
import itertools, random
import healing_model as H
from healing_model import HPG, CRIT_BASE, ll_ticks, ll_spam_history

class B:
    """name, cast time (GCD for instants), direct heal, heal over time and its duration,
    cooldown class ('long' = 1 min or more), tags for rules.
    ll: Lingering Light added on a critical heal (before tick crits); cc: chance of a critical heal."""
    def __init__(s, name, t, direct, hot=0.0, dur=1.0, cd=None, tags=(), ll=0.0, cc=0.0):
        s.name, s.t, s.direct, s.hot, s.dur, s.cd, s.tags = name, t, direct, hot, dur, cd, set(tags)
        s.ll, s.cc = ll, cc

START = "start"   # marker for the state at the hit

def timeline(seq, W, infusion_cut):
    """(spell, end time) for each cast that ends inside the window."""
    t = 0.0; prev = START; out = []
    for s in seq:
        cut = infusion_cut(prev, s)
        ct = max(1.5, s.t - cut) if cut > 0 else s.t     # s.t is the cast time, or the global cooldown
        end = t + ct
        if end > W + 1e-9: break
        out.append((s, end)); t = end; prev = s
    return out

def pre_hots(pre, ends, W):
    """Expected ticks in the window of the heals over time that are on the tank at the hit.
    pre: (spell name that replaces it, healing per sec, duration or None for a totem)."""
    v = 0.0
    for name, rate, D in pre:
        L = min([W] + [e for s, e in ends if s.name == name])
        v += rate * L if D is None else rate * (L - L*L/(2*D))   # remaining time uniform in (0, D)
    return v

def landed(seq, W, infusion_cut, pre=(), kt=1.0):
    """Healing that lands in W sec. Lingering Light here is approximate (each critical heal alone);
    lingering_exact() gives the exact value for the best sequences."""
    ends = timeline(seq, W, infusion_cut)
    v = sum(s.direct + s.hot * min(1.0, (W - e) / s.dur) for s, e in ends)
    v += sum(s.ll * s.cc * kt * min(1.0, (W - e) / 6) for s, e in ends)
    return v + pre_hots(pre, ends, W)

def lingering_exact(seq, W, infusion_cut, ll_pre, kt, samples=4000, seed=7):
    """Lingering Light ticks that land in (0, W], with the pool from before the hit and the refresh rule."""
    if ll_pre is None: return 0.0
    heal, c, ling = ll_pre
    ends = timeline(seq, W, infusion_cut)
    rng = random.Random(seed); tot = 0.0
    for _ in range(samples):
        ev = ll_spam_history(heal, c, ling, rng=rng)
        ev += [(e, s.ll) for s, e in ends if s.ll and rng.random() < s.cc]
        tot += sum(a for t, a in ll_ticks(ev) if 0 < t <= W + 1e-9)
    return tot / samples * kt

def best(case, W, long_cd=True, top=12):
    spells, cut, needs, pre, ll_pre, kt = case
    pool = [s for s in spells if long_cd or s.cd != "long"]
    cands = []
    for n in range(1, 6):
        for seq in itertools.product(pool, repeat=n):
            names = [s.name for s in seq]
            # each cooldown spell at most one time in the window; one "long" cooldown only
            if any(names.count(s.name) > 1 for s in seq if s.cd): continue
            if sum(1 for s in seq if s.cd == "long") > 1: continue
            if needs and not needs(seq): continue
            cands.append((landed(seq, W, cut, pre, kt), seq))
    cands.sort(key=lambda x: -x[0])
    if ll_pre is None:
        v, seq = cands[0]
        return v, tuple(s.name for s, e in timeline(seq, W, cut))
    # exact Lingering Light for the best sequences
    res = []
    for _, seq in cands[:top]:
        ends = timeline(seq, W, cut)
        v = sum(s.direct for s, e in ends) + pre_hots(pre, ends, W) + lingering_exact(seq, W, cut, ll_pre, kt)
        res.append((round(v, 6), -len(ends), tuple(s.name for s, e in ends)))
    v, _, names = max(res)
    return v, names

# ---------------------------------------------------------------- classes (715 healing power)
def paladin_burst(hp=HPG, light=1.12, bol=True, ling=0.0, conv=0.0, inf_all=False, before=10):
    c = CRIT_BASE + 0.05 + conv; c_hs = CRIT_BASE + 0.15 + conv
    fol = (308 + (115 if bol else 0) + 1.5/3.5*hp) * light
    hl = (1580 + (400 if bol else 0) + 2.5/3.5*hp) * light
    hs = (320 + 1.5/3.5*hp) * light
    kt = (1 + 0.5*c) if H.HOT_CRIT else 1.0                 # Lingering Light ticks can be critical heals
    L = lambda h: ling*h*1.5                                 # Lingering Light added by one critical heal
    sp = [B("Flash of Light", 1.5, fol*(1+0.5*c), tags=("trigger",), ll=L(fol), cc=c),
          B("Holy Light", 2.5, hl*(1+0.5*c), tags=("infusable",), ll=L(hl), cc=c),
          B("Holy Shock", 1.5, hs*(1+0.5*c_hs), cd="short", tags=("trigger", "hs"), ll=L(hs), cc=c_hs),
          B("Divine Favor + Holy Light", 2.5, hl*1.5, cd="long", tags=("infusable",), ll=L(hl), cc=1.0)]
    # Infusion of Light: the Holy Light after a Flash of Light or Holy Shock is 1 sec faster.
    # Beta: only after a critical heal (chance c or c_hs). C3: after each hit.
    # Before the hit, the Paladin casts Flash of Light on the tank: "before" casts in the last 15 sec.
    # Infusion of Light is then active at the hit: always with C3, else if one of them was a critical heal.
    p_start = 1.0 if inf_all else 1 - (1 - c)**before
    def cut(prev, s):
        if "infusable" not in s.tags: return 0.0
        if prev is START: return 1.0 * p_start
        if prev is None or "trigger" not in prev.tags: return 0.0
        if inf_all: return 1.0
        return 1.0 * (c_hs if "hs" in prev.tags else c)
    ll_pre = (fol, c, ling) if ling else None
    return sp, cut, None, (), ll_pre, kt

def priest_burst(hp=HPG):
    hp = hp + 84; d = hp - 799; c = 0.1903; k = 1 + 0.5*c; k_if = 1 + 0.5*(c + 0.25)
    gh = 2688.8 + 0.934*d
    kh = k if H.HOT_CRIT else 1.0
    renew = (1941.2 + 1.316*d)*kh
    sp = [B("Flash Heal", 1.5, (1272.4 + 0.467*d)*k),
          B("Greater Heal", 2.5, gh*k),
          B("Penance", 2.0, (1887.3 + 0.623*d)*k, cd="short"),
          B("Renew", 1.5, 0, renew, 15),
          B("Inner Focus + Greater Heal", 2.5, gh*k_if, cd="long")]
    return sp, (lambda p, s: 0.0), None, [("Renew", renew/15, 15)], None, 1.0

def druid_burst(hp=HPG):
    c = 0.183; k = 1 + 0.5*c; kh = k if H.HOT_CRIT else 1.0
    rej0 = (776 + 0.8*hp)*1.328; rej = rej0*kh
    rg_dir = (1021 + 0.3*hp)*1.114*(1 + 0.5*(c + 0.5)); rg_hot = (994 + 0.621*hp)*1.114*kh
    ht = (2934.8 + 1.1*(hp - 715))*k
    sp = [B("Healing Touch", 3.0, ht),
          B("Regrowth", 2.0, rg_dir, rg_hot, 21),
          B("Rejuvenation", 1.0, 0, rej, 12, tags=("fast_gcd", "hot")),
          B("Swiftmend", 1.0, rej0*k, cd="short", tags=("fast_gcd", "sm")),   # uses the Rejuvenation on the tank; direct heal, can crit
          B("Nature's Swiftness + Healing Touch", 1.5, ht, cd="long")]
    def needs(seq):   # a Rejuvenation is already on the tank at the hit: Swiftmend is ready
        if [x.name for x in seq].count("Regrowth") > 1: return False      # a new Regrowth replaces the old one
        if [x.name for x in seq].count("Rejuvenation") > 1: return False
        return True
    pre = [("Rejuvenation", rej/12, 12), ("Regrowth", rg_hot/21, 21)]
    return sp, (lambda p, s: 0.0), needs, pre, None, 1.0

def shaman_burst(hp=HPG):
    c = 0.243; k = 1 + 0.5*c; kh = k if H.HOT_CRIT else 1.0
    hw = (1371.5 + 3/3.5*hp)*1.1*1.24*k
    rt_hot = (805 + 0.5*hp)*1.1*kh
    sp = [B("Healing Wave", 2.5, hw),
          B("Lesser Healing Wave", 1.5, (820 + 1.5/3.5*hp)*1.1*k),
          B("Riptide", 1.5, (841 + 0.2*hp)*1.1*k, rt_hot, 15, cd="short"),
          B("Chain Heal (on the tank, after Riptide)", 2.5, (490 + 2.5/3.5*hp)*1.1*1.25*k),
          B("Nature's Swiftness + Healing Wave", 1.5, hw, cd="long")]
    pre = [("Riptide", rt_hot/15, 15), ("Healing Stream Totem", (11 + 0.02*hp)*kh/2, None)]
    return sp, (lambda p, s: 0.0), None, pre, None, 1.0

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
