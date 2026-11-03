"""Oath of Light (C-H8) on the beta of 30 October, with Light's Vigil (C-H7) and Reverence 50% (C-H1).
Run: python3 oath_light_ch8.py

Live text: "Swear an Oath to protect target ally for 5 min, increasing the healing of your Holy Light on them by up to
400, your Flash of Light by up to 115, and your Holy Shock by up to 229."
Proposed text: "... increasing the healing of your Holy Light, Flash of Light and Holy Shock on them by 30%."

Model:
- The % applies to the full heal (base, healing power, Healing Light). The Oath target has no Boundless Light, as live.
- One tank: all tank heals go on the Oath target. Raid: no heal goes on the Oath target (no change).
- At 715 healing power, the live flat values are Holy Light +19%, Flash of Light +19%, Holy Shock +37%.
- The Light's Vigil (C-H7) party heal is 60% of the Holy Shock heal, thus the Oath bonus is in it when the target has the Oath.
- Recovery after a large hit: recovery_b2.py with the % in place of the flat values.
"""
import sys, os
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(D, "..", "healing")); sys.path.insert(0, D)
import healing_model as H
from healing_model import solve, max_hps, CRIT_BASE, PAL_CRIT
import healing_b2 as B
import light_vigil_ch7 as L
import recovery as R
from recovery import best, GCD

ORIG = B.paladin_b2
TS = (180, 300, 600)

def oath_pct(p):
    """paladin_b2 with Oath of Light as +p% on Holy Light, Flash of Light and Holy Shock (None: live flat values)."""
    def pal(hp=715, tank=False, oath=None, bonus=0.75, conv=0.06, boundless=0.30, light=1.12, rev=0.30,
            illum=0.50, bened=0.10, lv=True, df_cd=120, bl_fol=0.0):
        if oath is None: oath = tank
        if p is None or not oath:
            return ORIG(hp, tank, oath, bonus, conv, boundless, light, rev, illum, bened, lv, df_cd, bl_fol)
        k = ORIG(hp, tank, False, bonus, conv, 0.0, light, rev, illum, bened, lv, df_cd, bl_fol)
        sp = {s.name: s for s in k["spells"]}
        for n in ("Divine Favor + Holy Light", "Holy Shock", "Flash of Light", "Holy Light"):
            sp[n].raw *= 1 + p; sp[n].eff *= 1 + p
        f, h, c = sp["Flash of Light"], sp["Holy Light"], k["crit"]
        combo = sp["Flash of Light, Holy Light on Infusion"]
        combo.raw = f.raw + c*h.raw; combo.eff = f.eff + c*h.eff
        return k
    return pal

def hps(p, hp=715, T=300, tank=True, bonus=0.75, rev=0.5):
    B.paladin_b2 = oath_pct(p)
    try: return solve(L.ch7(hp=hp, tank=tank, bonus=bonus, rev=rev), T, tank)["eff"]
    finally: B.paladin_b2 = ORIG

def peak(p, hp=715, bonus=0.75):
    B.paladin_b2 = oath_pct(p)
    try: return max_hps(L.ch7(hp=hp, tank=True, bonus=bonus, rev=0.5))
    finally: B.paladin_b2 = ORIG

def burst(p, hp=715, bonus=0.75, conv=0.06, light=1.12):
    c = CRIT_BASE + PAL_CRIT + conv
    if p is None: f, h, s = (308 + 115 + 1.5/3.5*hp), (1580 + 400 + 2.5/3.5*hp), (320 + 229 + 1.5/3.5*hp)
    else: f, h, s = [(b + x*hp)*(1 + p) for b, x in ((308, 1.5/3.5), (1580, 2.5/3.5), (320, 1.5/3.5))]
    f, h, s = f*light, h*light, s*light
    k = 1 + bonus*c
    sp = [R.B("Flash of Light", 1.5, f*k, tags=("trigger",), cc=c), R.B("Holy Light", 2.5, h*k, tags=("infusable",), cc=c),
          R.B("Holy Shock", GCD, s*k, cd="short", tags=("trigger",), cc=c),
          R.B("Divine Favor + Holy Light", 2.5, h*(1 + bonus), cd="long", tags=("infusable",), cc=1.0)]
    return sp, None, (), dict(c=c, ling=0.0, fol=f, inf_all=False, kt=1.0)

pc = lambda v: f"{v:+.0%}".replace("-", "−")
OPTS = (("Live (flat)", None), ("+20%", 0.20), ("+25%", 0.25), ("+30% (C-H8)", 0.30), ("+35%", 0.35))

if __name__ == "__main__":
    for hp in (715, 900):
        O = {T: B.others(hp, T, True) for T in TS}
        for key in ("Druid", "Shaman", "Priest"):
            print(f"\nOne tank against the {key}, {hp} healing power, 3 / 5 / 10 min | 175% | 225%")
            for n, p in OPTS:
                a = " / ".join(pc(hps(p, hp, T)/O[T][key] - 1) for T in TS)
                b = " / ".join(pc(hps(p, hp, T, bonus=1.25)/O[T][key] - 1) for T in TS)
                print(f"  {n:14s} {a} | {b}")
    print("\nOne tank HPS, 715, 3 / 5 / 10 min, 175%:")
    for n, p in OPTS: print(f"  {n:14s} " + " / ".join(f"{hps(p, 715, T):.0f}" for T in TS))
    print("  Druid " + " / ".join(f"{B.others(715, T, True)['Druid']:.0f}" for T in TS))
    print("\nOne tank, without Reverence 50% (C-H1), 175%, against the Druid:")
    for n, p in OPTS:
        print(f"  {n:14s} " + " / ".join(pc(hps(p, 715, T, rev=0.3)/B.others(715, T, True)['Druid'] - 1) for T in TS))
    print("\nRaid against the Druid, 175% (no Oath target):", " / ".join(pc(hps(None, 715, T, tank=False)/B.others(715, T, False)['Druid'] - 1) for T in TS),
          "| +30%:", " / ".join(pc(hps(0.30, 715, T, tank=False)/B.others(715, T, False)['Druid'] - 1) for T in TS))
    print(f"\nMaximum raw HPS on one tank, 30 sec (Druid {max_hps(H.druid(715, tank=True)):.0f}, 900: {max_hps(H.druid(900, tank=True)):.0f})")
    for n, p in OPTS: print(f"  {n:14s} 175%: {peak(p):.0f} (900: {peak(p, 900):.0f})  225%: {peak(p, bonus=1.25):.0f}")
    print("\nRecovery after a large hit: 3 sec / 6 sec with all cooldowns, 3 sec / 6 sec short cooldowns only, 715")
    dr = R.druid_burst(715); d = [best(dr, W, lc)[0] for lc in (True, False) for W in (3.0, 6.0)]
    print("  Druid " + " / ".join(f"{v:.0f}" for v in d))
    for b, bn in ((0.75, "175%"), (1.25, "225%")):
        for n, p in OPTS:
            v = [best(burst(p, bonus=b), W, lc)[0] for lc in (True, False) for W in (3.0, 6.0)]
            print(f"  {bn} {n:14s} " + " / ".join(f"{x:.0f} ({pc(x/y - 1)})" for x, y in zip(v, d)))
    print("\nOath bonus on one heal (no critical heal), by healing power: Holy Light | Flash of Light | Holy Shock")
    for hp in (300, 500, 715, 900):
        base = [(b + x*hp)*1.12 for b, x in ((1580, 2.5/3.5), (308, 1.5/3.5), (320, 1.5/3.5))]
        print(f"  {hp}: live +{400*1.12:.0f} | +{115*1.12:.0f} | +{229*1.12:.0f}; 30%: " + " | ".join(f"+{0.3*v:.0f}" for v in base)
              + "; 20%: " + " | ".join(f"+{0.2*v:.0f}" for v in base))
