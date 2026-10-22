"""Recovery after a large hit on one tank (Analysis, Healing, part 5).
Healing that lands on the tank in the first 3 and 6 sec after the hit. The healer starts to cast at 0.
No overhealing (the tank has a large health deficit). Heals over time count only the ticks inside the window.
Two cases: all cooldowns ready, and only short cooldowns (less than 1 min) ready.
Run: python3 recovery.py"""
import itertools
from healing_model import HPG, CRIT_BASE

class B:
    """name, cast time (GCD for instants), direct heal, heal over time and its duration,
    cooldown class ('long' = 1 min or more), tags for rules."""
    def __init__(s, name, t, direct, hot=0.0, dur=1.0, cd=None, tags=()):
        s.name, s.t, s.direct, s.hot, s.dur, s.cd, s.tags = name, t, direct, hot, dur, cd, set(tags)

def landed(seq, W, infusion_cut):
    """Healing that lands in W sec for a cast sequence. infusion_cut(prev, spell) gives the cast time cut."""
    t = 0.0; total = 0.0; prev = None
    for s in seq:
        cut = infusion_cut(prev, s)
        ct = max(1.5, s.t - cut) if cut > 0 else s.t     # s.t is the cast time, or the global cooldown
        end = t + ct
        if end > W + 1e-9: break
        total += s.direct + s.hot * min(1.0, (W - end) / s.dur)
        t = end; prev = s
    return total

def best(spells, W, long_cd=True, infusion_cut=lambda p, s: 0.0, needs=None):
    pool = [s for s in spells if long_cd or s.cd != "long"]
    best_v, best_seq = 0.0, ()
    for n in range(1, 6):
        for seq in itertools.product(pool, repeat=n):
            names = [s.name for s in seq]
            # each cooldown spell at most one time in the window; one "long" cooldown only
            if any(names.count(s.name) > 1 for s in seq if s.cd): continue
            if sum(1 for s in seq if s.cd == "long") > 1: continue
            if needs and not needs(seq): continue
            v = landed(seq, W, infusion_cut)
            if v > best_v: best_v, best_seq = v, tuple(names)
    return best_v, best_seq

# ---------------------------------------------------------------- classes (715 healing power)
def paladin_burst(hp=HPG, light=1.12, bol=True, ling=0.0, conv=0.0, inf_all=False):
    c = CRIT_BASE + 0.05 + conv; c_hs = CRIT_BASE + 0.15 + conv
    fol = (308 + (115 if bol else 0) + 1.5/3.5*hp) * light
    hl = (1580 + (400 if bol else 0) + 2.5/3.5*hp) * light
    hs = (320 + 1.5/3.5*hp) * light
    ll = lambda h, cc: ling*h*1.5*cc                        # Lingering Light: heal over time, 6 sec
    sp = [B("Flash of Light", 1.5, fol*(1+0.5*c), ll(fol, c), 6, tags=("trigger",)),
          B("Holy Light", 2.5, hl*(1+0.5*c), ll(hl, c), 6, tags=("infusable",)),
          B("Holy Shock", 1.5, hs*(1+0.5*c_hs), ll(hs, c_hs), 6, cd="short", tags=("trigger", "hs")),
          B("Divine Favor + Holy Light", 2.5, hl*1.5, ling*hl*1.5, 6, cd="long", tags=("infusable",))]
    # Infusion of Light: the Holy Light after a Flash of Light or Holy Shock is 1 sec faster.
    # Beta: only after a critical heal (chance c or c_hs). C3: after each hit.
    def cut(prev, s):
        if prev is None or "trigger" not in prev.tags or "infusable" not in s.tags: return 0.0
        if inf_all: return 1.0
        return 1.0 * (c_hs if "hs" in prev.tags else c)
    return sp, cut

def priest_burst(hp=HPG):
    hp = hp + 84; d = hp - 799; c = 0.1903; k = 1 + 0.5*c; k_if = 1 + 0.5*(c + 0.25)
    gh = 2688.8 + 0.934*d
    return [B("Flash Heal", 1.5, (1272.4 + 0.467*d)*k),
            B("Greater Heal", 2.5, gh*k),
            B("Penance", 2.0, (1887.3 + 0.623*d)*k, cd="short"),
            B("Renew", 1.5, 0, 1941.2 + 1.316*d, 15),
            B("Inner Focus + Greater Heal", 2.5, gh*k_if, cd="long")], (lambda p, s: 0.0)

def druid_burst(hp=HPG):
    c = 0.183; k = 1 + 0.5*c
    rej = (776 + 0.8*hp)*1.328
    rg_dir = (1021 + 0.3*hp)*1.114*(1 + 0.5*(c + 0.5)); rg_hot = (994 + 0.621*hp)*1.114
    ht = (2934.8 + 1.1*(hp - 715))*k
    sp = [B("Healing Touch", 3.0, ht),
          B("Regrowth", 2.0, rg_dir, rg_hot, 21),
          B("Rejuvenation", 1.0, 0, rej, 12, tags=("fast_gcd", "hot")),
          B("Swiftmend", 1.0, rej, cd="short", tags=("fast_gcd", "sm")),   # uses the Rejuvenation on the tank
          B("Nature's Swiftness + Healing Touch", 1.5, ht, cd="long")]
    def needs(seq):   # Swiftmend needs a Rejuvenation on the tank, cast before it in the window
        if sum(1 for x in seq if x.name in ("Regrowth", "Rejuvenation")) > 2: return False
        if [x.name for x in seq].count("Regrowth") > 1: return False      # a new Regrowth replaces the old one
        if [x.name for x in seq].count("Rejuvenation") > 1: return False
        for i, s in enumerate(seq):
            if "sm" in s.tags and not any("hot" in x.tags for x in seq[:i]): return False
        return True
    return sp, (lambda p, s: 0.0), needs

def shaman_burst(hp=HPG):
    c = 0.243; k = 1 + 0.5*c
    hw = (1371.5 + 3/3.5*hp)*1.1*1.24*k
    return [B("Healing Wave", 2.5, hw),
            B("Lesser Healing Wave", 1.5, (820 + 1.5/3.5*hp)*1.1*k),
            B("Riptide", 1.5, (841 + 0.2*hp)*1.1*k, (805 + 0.5*hp)*1.1, 15, cd="short"),
            B("Chain Heal (on the tank, after Riptide)", 2.5, (490 + 2.5/3.5*hp)*1.1*1.25*k),
            B("Nature's Swiftness + Healing Wave", 1.5, hw, cd="long")], (lambda p, s: 0.0)

PROP_B = dict(light=1.30, bol=False, ling=0.2, conv=0.05, inf_all=True)

def table(hp=HPG):
    rows = []
    cases = [("Priest", priest_burst(hp) + (None,)), ("Druid", druid_burst(hp)),
             ("Shaman", shaman_burst(hp) + (None,)),
             ("Paladin, beta", paladin_burst(hp) + (None,)), ("Paladin, proposed", paladin_burst(hp, **PROP_B) + (None,))]
    for name, (sp, cut, needs) in cases:
        r = [name]
        for long_cd in (True, False):
            for W in (3.0, 6.0):
                v, seq = best(sp, W, long_cd, cut, needs)
                r.append((round(v), seq))
        rows.append(r)
    return rows

if __name__ == "__main__":
    for hp in (715, 900):
        print("## healing power", hp, "| 3 sec, 6 sec (all cooldowns) | 3 sec, 6 sec (short cooldowns only)")
        for r in table(hp):
            print(f"  {r[0]:18s} " + " | ".join(f"{v:5d}" for v, _ in r[1:]))
            for v, seq in r[1:]: print("        ", v, " > ".join(seq))
