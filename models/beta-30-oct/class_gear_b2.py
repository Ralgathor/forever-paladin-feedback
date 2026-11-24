"""Class gear case: each healer in the gear of its class (DoubleZug sheets "Forever <class> 1.0", November 2026).
Run: python3 class_gear_b2.py

The main case of the models gives all healers the same gear (715 healing power, 438 Intellect, 336 Spirit).
That gear has little Spirit. The Druid uses Spirit three times (regeneration, Innervate, Bloom), and in raids the
Druid is limited by mana. The Paladin is limited by cast time. Thus the same gear is not neutral. This script uses
the totals of the DoubleZug profiles (raid buffs included). Spells, talents, buffs and consumables stay as in
healing_model.py and healing_b2.py.

| Class   | Healing power | Intellect | Spirit | Critical chance (total) |
| Paladin | 623           | 399       | 359    | 24.66% (with Conviction) |
| Druid   | 573           | 345       | 878    | 14.75% |
| Shaman  | 616           | 459       | 334    | 24.64% |
| Priest  | 851 (with Spiritual Guidance) | 408 | 630 | 18.8% |
"""
import sys
import os; D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "healing")); sys.path.insert(0, D)
import healing_model as H
from healing_model import solve
import healing_b2 as B
import light_vigil_ch7 as V

TS = (180, 300, 600)
PAL = dict(spi=359, intel=399, crit=0.2466 - 0.06)          # 24.66% total: Conviction 3/3 (+6%) is added in the model
PAL_HP = 623

def others(T, tank):
    return {"Druid": solve(H.druid(573, tank=tank, spi=878, intel=345, crit=0.1475), T, tank)["eff"],
            "Priest": solve(H.priest(851 - 0.25*630, tank=tank, spi=630, intel=408, crit=0.188), T, tank)["eff"],
            "Shaman": solve(H.shaman(616, tank=tank, T=T, spi=334, intel=459, crit=0.2464), T, tank)["eff"]}

CASES = (("Live", lambda tank, b: B.paladin_b2(PAL_HP, tank, bonus=b, **PAL)),
         ("Light's Vigil (C-H7)", lambda tank, b: V.ch7(PAL_HP, tank, bonus=b, **PAL)),
         ("C-H7 + Reverence 50% (C-H1)", lambda tank, b: V.ch7(PAL_HP, tank, bonus=b, rev=0.50, **PAL)))

if __name__ == "__main__":
    O = {(T, t): others(T, t) for T in TS for t in (False, True)}
    for tank in (False, True):
        print(f"## {'One tank' if tank else 'Raid'}, class gear: HPS after overhealing, 3 | 5 | 10 min")
        for n in ("Druid", "Priest", "Shaman"):
            print(f"  {n:40s} " + " | ".join(f"{O[(T, tank)][n]:5.0f}" for T in TS))
        for b, bl in ((0.75, "175%"), (1.25, "225%")):
            for n, f in CASES:
                v = {T: solve(f(tank, b), T, tank)["eff"] for T in TS}
                print(f"  Paladin, {n}, {bl}".ljust(42) + " | ".join(
                    f"{v[T]:4.0f} (Dru {v[T]/O[(T, tank)]['Druid']-1:+.0%}, Pri {v[T]/O[(T, tank)]['Priest']-1:+.0%}, "
                    f"Sha {v[T]/O[(T, tank)]['Shaman']-1:+.0%})" for T in TS))
    for tank in (False, True):
        r = solve(H.druid(573, tank=tank, spi=878, intel=345, crit=0.1475), 300, tank)
        print(f"## Druid cast plan, {'tank' if tank else 'raid'}, 5 min: " +
              ", ".join(f"{a} {b:.0f}" for a, b in r["casts"].items()) + f"; idle {r['idle']:.0f} sec")
