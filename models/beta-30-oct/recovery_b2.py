"""Recovery after a large hit on one tank (repo models/healing/recovery.py), beta of 30 October 2026.
The Paladin has Oath of Light on the tank (no Boundless Light), Holy Power 5/5 (critical heal 225%), Conviction 3/3.
Run: python3 recovery_b2.py <repo>/models/healing"""
import sys
sys.path.insert(0, sys.argv[1] if len(sys.argv) > 1 else ".")
import recovery as R
from recovery import B, GCD, best, HPG, CRIT_BASE, PAL_CRIT

def paladin_burst_b2(hp=HPG, bonus=1.25, conv=0.06, light=1.12):
    c = CRIT_BASE + PAL_CRIT + conv
    fol = (308 + 115 + 1.5/3.5*hp) * light
    hl = (1580 + 400 + 2.5/3.5*hp) * light
    hs = (320 + 229 + 1.5/3.5*hp) * light
    k = 1 + bonus*c
    sp = [B("Flash of Light", 1.5, fol*k, tags=("trigger",), cc=c),
          B("Holy Light", 2.5, hl*k, tags=("infusable",), cc=c),
          B("Holy Shock", GCD, hs*k, cd="short", tags=("trigger",), cc=c),
          B("Divine Favor + Holy Light", 2.5, hl*(1+bonus), cd="long", tags=("infusable",), cc=1.0)]
    return sp, None, (), dict(c=c, ling=0.0, fol=fol, inf_all=False, kt=1.0)

if __name__ == "__main__":
    for hp in (715, 900):
        print("## healing power", hp, "| 3 sec, 6 sec (all cooldowns) | 3 sec, 6 sec (short cooldowns only)")
        cases = [("Priest", R.priest_burst(hp)), ("Druid", R.druid_burst(hp)), ("Shaman", R.shaman_burst(hp)),
                 ("Paladin, beta 18 Oct", R.paladin_burst(hp)), ("Paladin, beta 30 Oct", paladin_burst_b2(hp)),
                 ("Paladin, beta 30 Oct, crit 175%", paladin_burst_b2(hp, bonus=0.75))]
        for name, case in cases:
            vals = [best(case, W, lc) for lc in (True, False) for W in (3.0, 6.0)]
            print(f"  {name:34s} " + " | ".join(f"{round(v):5d}" for v, _ in vals))
