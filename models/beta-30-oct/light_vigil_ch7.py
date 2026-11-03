"""Light's Vigil redesign (C-H7) on the beta of 30 October, with the development notes of 2 November.
Run: python3 light_vigil_ch7.py

Proposed text:
  Your Holy Shock, Judgement and Holy Strike grant Light's Vigil for 30 sec, stacking up to 3 times. May only occur
  once every 6 sec. Casting Holy Shock consumes one stack, causing that Holy Shock to incur no cooldown and, when cast
  on an ally, to heal the target's party for 60% of the amount healed.

Model:
- A Holy Shock with the buff also triggers the buff again when the 6 sec cooldown is over. Thus the Paladin can use
  one empowered Holy Shock each 6 sec with no other trigger (melee and ranged are the same). Limit: T/6 + 1.
- While the buff is active, each Holy Shock is empowered: the plain Holy Shock is not in the cast plan.
- Party heal: X (60%) of the Holy Shock heal on each of the 5 party members (the target included). It uses the
  Holy Shock crit chance (Boundless Light on a target with no Oath of Light). Overhealing 50%, as Wild Growth. No Illumination on
  the party part.
- On an enemy, the buff only removes the Holy Shock cooldown. This has no healing value.
- Stacks do not change the fight values (still one stack each 6 sec). burst() gives the group burst with full
  stacks: Flash of Light or a plain Holy Shock fills the other global cooldowns.
- Divine Favor: the model keeps it on Holy Light (more effective healing: the party heal has 50% overhealing).
  burst(df=True) gives the opening burst with Divine Favor on the first empowered Holy Shock.
- Live: Light's Vigil rank 3 + Holy Shock, as in healing_b2.py.
"""
import sys
import os; D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(D, "..", "healing")); sys.path.insert(0, D)
import healing_model as H
from healing_model import Spell, solve
import healing_b2 as B

TS = (180, 300, 600)
X = 0.60   # party heal, % of the Holy Shock heal

def ch7(hp=715, tank=False, x=None, icd=6, oh=0.50, bonus=0.75, rev=0.30):
    x = X if x is None else x
    k = B.paladin_b2(hp, tank, bonus=bonus, rev=rev, lv=False)
    hs = [s for s in k["spells"] if s.name == "Holy Shock"][0]
    k["spells"] = [s for s in k["spells"] if s.name != "Holy Shock"]
    one = x*hs.raw                                   # party heal on one member: x of the Holy Shock heal (crit included)
    k["spells"].append(Spell("Holy Shock + Light's Vigil", hs.raw + 5*one, hs.eff + 5*one*(1-oh), hs.cost, 1.5,
                             maxn=lambda T, i=icd: T/i + 1, tank=(hs.raw + one)/(hs.raw + 5*one)))
    return k

def live(hp=715, tank=False, bonus=0.75, rev=0.30):
    return B.paladin_b2(hp, tank, bonus=bonus, rev=rev, lv=True)

def vs(f, tank, key):
    out = []
    for T in TS:
        o = B.others(715, T, tank)[key]
        out.append(solve(f(), T, tank)["eff"]/o - 1)
    return " / ".join(f"{v:+.0%}".replace("-", "−") for v in out)

def burst(stacks=3, W=10, melee=True, bonus=0.75, cj=0.06*1512, df=False, hp=715):
    """Healing (raw) and mana in W sec, with full stacks at the start. Judgement has no global cooldown.
    df: Divine Favor (no global cooldown) on the first empowered Holy Shock: a sure critical heal, also on the party heal."""
    k = ch7(bonus=bonus); sp = {s.name: s for s in k["spells"]}
    e, f = sp["Holy Shock + Light's Vigil"], sp["Flash of Light"]
    hse, chs, hsp, fol, cfol = e.raw, e.cost, e.raw/(1 + 5*X), f.raw, f.cost
    t, st, icd, hscd, jcd, heal, mana = 0.0, stacks, 0.0, 0.0, 0.0, 0, 0
    while t < W - 1e-9:
        if melee and st == 0 and icd <= t and jcd <= t:
            st += 1; icd = t + 6; jcd = t + 10; mana += cj
        if st > 0:
            st -= 1; mana += chs
            if df: heal += (320 + 1.5/3.5*hp)*1.12*(1 + bonus)*(1 + 5*X); mana += 0.04*1512; df = False
            else: heal += hse
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
        for b, n in ((0.75, "175%"), (1.0, "200%"), (1.25, "225%")):
            for tank in (False, True):
                print(f"| {n} | {'One tank' if tank else 'Raid'} | {vs(lambda: live(tank=tank, bonus=b), tank, key)} | "
                      f"{vs(lambda: ch7(tank=tank, bonus=b), tank, key)} | {vs(lambda: ch7(tank=tank, bonus=b, rev=0.5), tank, key)} |")
    print("\nParty heal % and cooldown, raid with Reverence 50%, against the Druid | the Shaman, 175%")
    for icd, x in ((6, 0.35), (6, 0.50), (6, 0.60), (6, 0.70), (8, 0.60), (8, 0.70)):
        print(f"  {icd} sec, {x:.0%}: {vs(lambda: ch7(x=x, icd=icd, rev=0.5), False, 'Druid')} | {vs(lambda: ch7(x=x, icd=icd, rev=0.5), False, 'Shaman')}")
    k = ch7(); s = [s for s in k["spells"] if s.name.startswith("Holy Shock")][0]
    base = s.raw/(1 + 5*X)
    print(f"\nEmpowered Holy Shock, raid: {s.raw:.0f} raw ({base:.0f} Holy Shock + 5 x {X*base:.0f}), "
          f"{s.eff/s.cost:.1f} effective healing for each mana point")
    print("Group burst with full stacks (raw / mana):")
    for n in (1, 2, 3, 4):
        print(f"  {n} stacks: 6 sec {burst(n, 6)[0]:.0f}; 10 sec melee {burst(n, 10)[0]:.0f}, ranged {burst(n, 10, False)[0]:.0f} "
              f"({burst(n, 10)[1]:.0f} mana)")
    print("Divine Favor on the first empowered Holy Shock, 3 stacks:")
    for b, n in ((0.75, "175%"), (1.25, "225%")):
        a, d = burst(3, 6, bonus=b)[0], burst(3, 6, bonus=b, df=True)[0]
        print(f"  {n}: 6 sec {a:.0f} -> {d:.0f} ({d/a-1:+.0%}); 10 sec {burst(3, 10, bonus=b)[0]:.0f} -> {burst(3, 10, bonus=b, df=True)[0]:.0f}")
    print(f"Casts in 5 min, raid: {solve(k, 300, False)['casts']}")
