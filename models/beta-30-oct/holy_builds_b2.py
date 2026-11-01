"""builds/holy.md on the beta of 30 October 2026: the value of each healing talent and the stat weights (model).
Run: python3 holy_builds_b2.py ../healing

Build HB1/HB2 (Analysis, Builds): all healing talents of the tree, as in healing_b2.py. The proposed trees have no
Holy talent change, thus HB1 (beta) and HB2 (proposed, with Devoted Sacrifice) heal the same.
Stat weights: each stat + a small amount, healing per sec after overhealing, divided by the gain of 1 healing power.
Intellect: +15 mana and +1/60% critical chance for each point (healing_model: 438 Intellect = 7.3%).
Critical chance: 14 rating = 1%. Spirit: Classic regeneration, 30% during casts (Reverence 2/2). The model has no haste.
"""
import sys
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else "../healing"]
sys.path.insert(0, sys.argv[1]); sys.path.insert(0, ".")
import healing_model as H
import healing_b2 as B
from healing_model import solve, regen_full

HP = 715

def hps(T, tank, hp=HP, dint=0.0, dspi=0.0, dmp5=0.0, dcrit=0.0, **kw):
    old_c, old_m = B.CRIT_BASE, H.MP5
    B.CRIT_BASE = old_c + dint / 60 / 100 + dcrit
    H.MP5 = old_m + dmp5
    try:
        k = B.paladin_b2(hp, tank, **kw)
        k["pool"] += 15 * dint
        k["regen"] = regen_full("pal", 336 + dspi)
        return solve(k, T, tank)["eff"]
    finally:
        B.CRIT_BASE, H.MP5 = old_c, old_m

TALENTS = (
    ("Healing Light 3/3", dict(light=1.0)),
    ("Holy Power 5/5", dict(bonus=0.5)),
    ("Illumination 5/5", dict(illum=0.0)),
    ("Reverence 2/2 (and Illumination: it needs Reverence)", dict(rev=0.0, illum=0.0)),
    ("Conviction 3/3", dict(conv=0.0)),
    ("Divine Favor", dict(df_cd=10 ** 6)),
    ("Benediction 5/5", dict(bened=0.0)),
    ("Boundless Light 2/2", dict(boundless=0.0)),
    ("Light's Vigil", dict(lv=False)),
)

if __name__ == "__main__":
    print("## HB1/HB2, healing power 715: raid | one tank, healing each sec after overhealing")
    for T in (180, 300, 600):
        print(f"  {T // 60} min: {hps(T, False):.0f} | {hps(T, True):.0f}")
    print("\n## Value of each talent (5 min): raid | one tank")
    base = {t: hps(300, t) for t in (False, True)}
    # Divine Intellect 5/5: +10% Intellect (438 -> 398 without it)
    di = {t: hps(300, t, dint=-40) / base[t] - 1 for t in (False, True)}
    print(f"  Divine Intellect 5/5: {di[False]:+.1%} | {di[True]:+.1%}")
    for name, kw in TALENTS:
        print(f"  {name}: " + " | ".join(f"{hps(300, t, **kw) / base[t] - 1:+.1%}" for t in (False, True)))
    print("\n## Stat weights (healing power = 1.00): 3 min | 5 min | 10 min, raid; 5 min one tank")
    steps = (("Healing power", dict(hp=HP + 40), 40), ("Intellect", dict(dint=40), 40), ("Spirit", dict(dspi=40), 40),
             ("MP5", dict(dmp5=10), 10), ("Crit rating (14 = 1%)", dict(dcrit=0.01), 14))
    cases = ((180, False), (300, False), (600, False), (300, True))
    hp1 = {c: (hps(c[0], c[1], hp=HP + 40) - hps(c[0], c[1])) / 40 for c in cases}
    print("  healing each sec for 1 healing power: " + " | ".join(f"{hp1[c]:.3f}" for c in cases))
    for name, kw, n in steps:
        row = []
        for c in cases:
            g = (hps(c[0], c[1], **kw) - hps(c[0], c[1])) / n
            row.append(f"{g / hp1[c]:.2f}")
        print(f"  {name}: " + " | ".join(row))
