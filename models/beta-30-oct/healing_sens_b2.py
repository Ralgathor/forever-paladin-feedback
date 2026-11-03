"""Analysis, Healing: parts 5, 6 and 9 (cost values, Holy Power cases and limits) on the beta of 30 October 2026.
Run: python3 healing_sens_b2.py ..   (the models folder of the repository)
NOTES_OFF=1 runs the model without the development notes of 2 November 2026."""
import os, sys
base = sys.argv[1] if len(sys.argv) > 1 else ".."
sys.path.insert(0, base + "/healing"); sys.path.insert(0, base + "/beta-30-oct"); sys.argv = [sys.argv[0], base + "/healing"]
import healing_model as H
if os.environ.get("NOTES_OFF"): H.NOTES_NOV2 = False
from healing_b2 import paladin_b2

hp, T = 715, 180
e = lambda k, tank=False, t=T: H.solve(k, t, tank)["eff"]
pct = lambda a, b: f"{a / b - 1:+.0%}"
TS = (180, 300, 600)

print("## Holy Power cases against the Druid, 3 | 5 | 10 min: raid ; one tank")
for name, b in (("225%", 1.25), ("200%", 1.0), ("175%", 0.75)):
    r = [pct(e(paladin_b2(hp, False, bonus=b), False, t), e(H.druid(hp), False, t)) for t in TS]
    k = [pct(e(paladin_b2(hp, True, bonus=b), True, t), e(H.druid(hp, tank=True), True, t)) for t in TS]
    print(f"  {name}: " + " / ".join(r) + " ; " + " / ".join(k))

print("## Limits (raid 3 min unless noted)")
pri = H.priest(hp)
for s in pri["spells"]:
    if s.name.startswith("Prayer of Mending"):
        s.raw *= 3 / 5; s.eff *= 3 / 5
print(f"  Priest, Prayer of Mending on 3 targets: {e(pri):.0f} (5 targets: {e(H.priest(hp)):.0f})")
print(f"  Druid, 2 free Wild Growth each min: {e(H.druid(hp, ooc_wg=2)):.0f} (base {e(H.druid(hp)):.0f})")
sha = H.shaman(hp, T=T); sha["extra"] = lambda t: H.uses(t, 300, 12) * H.TIDE
print(f"  Shaman, two Mana Tide Totems: {e(sha):.0f} (base {e(H.shaman(hp, T=T)):.0f})")
print(f"  Druid, Swiftmend removes the heal over time: raid {e(H.druid(hp, sm_consumes=True)):.0f}, "
      f"tank {e(H.druid(hp, tank=True, sm_consumes=True), True):.0f}")
print(f"  Druid, no Nature's Splendor: raid {e(H.druid(hp, splendor=False)):.0f}, "
      f"tank {e(H.druid(hp, tank=True, splendor=False), True):.0f}")
H.HOT_CRIT = False
r = [(e(paladin_b2(hp, False), False, t), e(H.shaman(hp, T=t), False, t), e(H.druid(hp), False, t)) for t in TS]
k = [(e(paladin_b2(hp, True), True, t), e(H.druid(hp, tank=True), True, t)) for t in TS]
print("  Classic tick rule: raid against Shaman " + " / ".join(pct(a, b) for a, b, _ in r)
      + ", against Druid " + " / ".join(pct(a, c) for a, _, c in r) + "; tank against Druid " + " / ".join(pct(a, b) for a, b in k))
H.HOT_CRIT = True

print("## Healing for each mana point (raw / after overhealing), raid, 715")
for k in (H.priest(hp), H.druid(hp), H.shaman(hp, T=T)):
    print(f"  {k['cls']}: " + ", ".join(f"{s.name} {s.raw / s.cost:.1f} / {s.eff / s.cost:.1f}" for s in k["spells"] if s.cost > 0))

print("## Share of cooldown heals, raid, 3 min")
for k, cds in ((H.priest(hp), ("Prayer of Mending",)), (H.druid(hp), ("Swiftmend", "Tranquility")), (H.shaman(hp, T=T), ("Riptide",))):
    r = H.solve(k, T)
    sp = {s.name: s for s in k["spells"]}
    tot = sum(sp[n].eff * x for n, x in r["casts"].items())
    cd = sum(sp[n].eff * x for n, x in r["casts"].items() if n.startswith(cds))
    print(f"  {k['cls']}: {cd / tot:.0%} ({', '.join(f'{n} {x:.0f}' for n, x in r['casts'].items())})")
