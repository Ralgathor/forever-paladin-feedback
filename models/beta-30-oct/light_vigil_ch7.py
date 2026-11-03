"""Light's Vigil redesign (C-H7) on the beta of 30 October, with the development notes of 2 November.
Run: python3 light_vigil_ch7.py

Proposed text:
  Your Holy Shock, Judgement and Holy Strike grant a stack of Light's Vigil for 30 sec. This effect cannot occur
  more than once every 6 sec. Stacks up to 3 times. While Light's Vigil is active, your next Holy Shock triggers
  no cooldown and consumes one stack. On an allied target, Holy Shock also heals the target's party for 35% of the amount healed.

Model:
- A Holy Shock with the buff also triggers the buff again when the 6 sec cooldown is over. Thus the Paladin can use
  one empowered Holy Shock each 6 sec with no other trigger (melee and ranged are the same). Limit: T/6 + 1.
- While the buff is active, each Holy Shock is empowered: the plain Holy Shock is not in the cast plan.
- Party heal: X (35%) of the Holy Shock heal on each of the 5 party members (the target included). It uses the
  Holy Shock crit chance (Boundless Light on a target with no Oath of Light). Overhealing 50%, as Wild Growth. No Illumination on
  the party part.
- On an enemy, the buff only removes the Holy Shock cooldown. This has no healing value.
- Stacks do not change the fight values (still one stack each 6 sec). burst() gives the group burst with full
  stacks: Flash of Light or a plain Holy Shock fills the other global cooldowns.
- Live: Light's Vigil rank 3 + Holy Shock, as in healing_b2.py.
"""
import sys
import os; D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(D, "..", "healing")); sys.path.insert(0, D)
import healing_model as H
from healing_model import Spell, solve
import healing_b2 as B

TS = (180, 300, 600)
X = 0.35   # party heal, % of the Holy Shock heal

def ch7(hp=715, tank=False, x=None, icd=6, oh=0.50, bonus=1.25, rev=0.30):
    x = X if x is None else x
    k = B.paladin_b2(hp, tank, bonus=bonus, rev=rev, lv=False)
    hs = [s for s in k["spells"] if s.name == "Holy Shock"][0]
    k["spells"] = [s for s in k["spells"] if s.name != "Holy Shock"]
    one = x*hs.raw                                   # party heal on one member: x of the Holy Shock heal (crit included)
    k["spells"].append(Spell("Holy Shock + Light's Vigil", hs.raw + 5*one, hs.eff + 5*one*(1-oh), hs.cost, 1.5,
                             maxn=lambda T, i=icd: T/i + 1, tank=(hs.raw + one)/(hs.raw + 5*one)))
    return k

def live(hp=715, tank=False, bonus=1.25, rev=0.30):
    return B.paladin_b2(hp, tank, bonus=bonus, rev=rev, lv=True)

def vs(f, tank, key):
    out = []
    for T in TS:
        o = B.others(715, T, tank)[key]
        out.append(solve(f(), T, tank)["eff"]/o - 1)
    return " / ".join(f"{v:+.0%}".replace("-", "−") for v in out)

def burst(stacks=3, W=10, melee=True, hse=3227, hsp=1173, fol=893, chs=205, cfol=123, cj=0.06*1512):
    """Healing (raw) and mana in W sec, with full stacks at the start. Judgement has no global cooldown."""
    t, st, icd, hscd, jcd, heal, mana = 0.0, stacks, 0.0, 0.0, 0.0, 0, 0
    while t < W - 1e-9:
        if melee and st == 0 and icd <= t and jcd <= t:
            st += 1; icd = t + 6; jcd = t + 10; mana += cj
        if st > 0:
            st -= 1; heal += hse; mana += chs
            if icd <= t: st += 1; icd = t + 6
        elif hscd <= t:
            heal += hsp; mana += chs; hscd = t + 10
            if icd <= t: st += 1; icd = t + 6
        else:
            if t + 1.5 > W + 1e-9: break
            heal += fol; mana += cfol
        t += 1.5
    return heal, mana

if __name__ == "__main__":
    for key in ("Druid", "Shaman"):
        print(f"\nAgainst the {key}, 715 healing power, 3 / 5 / 10 min")
        print("| Critical heal | Case | Live | Light's Vigil (C-H7) | C-H7 + Reverence 50% (C-H1) |")
        for b, n in ((1.25, "225%"), (1.0, "200%"), (0.75, "175%")):
            for tank in (False, True):
                print(f"| {n} | {'One tank' if tank else 'Raid'} | {vs(lambda: live(tank=tank, bonus=b), tank, key)} | "
                      f"{vs(lambda: ch7(tank=tank, bonus=b), tank, key)} | {vs(lambda: ch7(tank=tank, bonus=b, rev=0.5), tank, key)} |")
    print("\nParty heal % and cooldown, raid against the Shaman, 225%")
    for icd, x in ((6, 0.25), (6, 0.30), (6, 0.35), (6, 0.40), (8, 0.35), (8, 0.40)):
        print(f"  {icd} sec, {x:.0%}: {vs(lambda: ch7(x=x, icd=icd), False, 'Shaman')}")
    k = ch7(); s = [s for s in k["spells"] if s.name.startswith("Holy Shock")][0]
    base = s.raw/(1 + 5*X)
    print(f"\nEmpowered Holy Shock, raid: {s.raw:.0f} raw ({base:.0f} Holy Shock + 5 x {X*base:.0f}), "
          f"{s.eff/s.cost:.1f} effective healing for each mana point")
    print("Group burst with full stacks (raw / mana):")
    for n in (1, 2, 3, 4):
        print(f"  {n} stacks: 6 sec {burst(n, 6)[0]:.0f}; 10 sec melee {burst(n, 10)[0]:.0f}, ranged {burst(n, 10, False)[0]:.0f} "
              f"({burst(n, 10)[1]:.0f} mana)")
    print(f"Casts in 5 min, raid: {solve(k, 300, False)['casts']}")
