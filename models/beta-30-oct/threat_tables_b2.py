"""Analysis, Threat, on the beta of 30 October 2026: all tables of the tab.
Run: python3 threat_tables_b2.py ..   (the models folder of the repository)

Beta tank: B2T 0/38/13 (threat_b2.py). Proposed tank: the same talents with the kept proposals:
Personal Judgement of the Crusader (C2), Redoubt (C-P1). The Holy Strike Seal trigger (C1) and Reckoning (C-P12) were withdrawn on 2 November 2026: part 4 still shows their values.
Toughness removal (C-P13) does not change threat. The Warrior and the Druid come from models/threat/threat_model.py.
Several targets: the rules of models/threat/multi_target.py, with the Holy Shield of the beta of 30 October.
"""
import sys
base = sys.argv[1] if len(sys.argv) > 1 else ".."
sys.argv = [sys.argv[0], base]
sys.path.insert(0, base + "/threat"); sys.path.insert(0, base + "/beta-30-oct")
import threat_model as T
import multi_target as MT
from threat_b2 import paladin_b2, B2T

PROP = ("CP1",)  # withdrawn on 2 November 2026: Reckoning (C-P12) and the Holy Strike Seal trigger (C1)
pct = lambda a, b: f"{a / b:.0%}"

def beta(g, **kw): return paladin_b2(g, **kw)
def prop(g, **kw): return paladin_b2(g, prop=PROP, **kw)

def pal_multi(g, n, proposed=True, cons=True):
    """(threat per sec on all targets, on one extra target). Holy Shield: blocks use 4 charges each 10 sec with
    2 or more attackers, shared between the attackers. The Shieldsworn trigger of Holy Strike hits the main target."""
    gg = g.but(armor=MT.TRASH_ARMOR)
    p = PROP if proposed else ()
    tot, src = paladin_b2(gg, consecration=cons, detail=True, prop=p)
    if n == 1:
        return tot, 0.0
    _, s0 = paladin_b2(gg, consecration=cons, detail=True, prop=p, crusader=False)
    hit = gg.hit + 0.03
    land_s, _ = T.table(hit, gg.crit + 0.06, auto=False)
    blocks1 = (1.5 + 1) / 10
    if proposed:
        blocks1 = min(0.4, blocks1 * 61.6 / 42.3)
    rate1 = blocks1 + land_s / 6
    one_main = src["Holy Shield"] / rate1                  # threat of one Holy Shield hit on the main target
    one_extra = s0["Holy Shield"] / rate1                  # extra target: no Judgement of the Crusader
    single = tot - src["Holy Shield"]
    hs_total = one_main * (land_s / 6 + MT.HS_CHARGES / n) + one_extra * MT.HS_CHARGES * (n - 1) / n
    cons_near = s0.get("Consecration", 0.0)
    cons_far = cons_near * 96 / (312 + 0.336 * gg.sp)
    cons_extra = cons_near * min(n - 1, MT.CONS_TARGETS - 1) + cons_far * max(0, n - MT.CONS_TARGETS)
    return single + hs_total + cons_extra, one_extra * MT.HS_CHARGES / n + cons_extra / (n - 1)

if __name__ == "__main__":
    print("## Part 1: same gear (PART1), boss hit 3,000 | 4,500 | 6,000")
    rows = (("Warrior", T.warrior), ("Druid", T.druid), ("Druid, wowsims multipliers", lambda g: T.druid(g, mults=T.DRU_WOWSIMS)),
            ("Paladin, beta", beta), ("Paladin, beta, no Crusader", lambda g: beta(g, crusader=False)),
            ("Paladin, proposed", prop), ("Paladin, proposed + Consecration", lambda g: prop(g, consecration=True)))
    for name, f in rows:
        print(f"  {name:34s} " + " | ".join(f"{f(T.PART1.but(boss_hit=H)):.0f}" for H in (3000, 4500, 6000)))
    g = T.PART1
    for name, f in (("beta", beta), ("proposed", prop)):
        tot, s = f(g, detail=True)
        print(f"  sources {name}: " + ", ".join(f"{k} {v:.0f}" for k, v in s.items()) + f"; total {tot:.0f}")
    b = beta(g)
    for lab, p in (("C1", ("C1",)), ("CP1", ("CP1",)), ("CP12 (with CP1)", ("CP1", "CP12"))):
        base_p = ("CP1",) if lab.startswith("CP12") else ()
        print(f"  {lab}: {paladin_b2(g, prop=p) - paladin_b2(g, prop=base_p):+.0f}")
    print(f"  C2 (raid needs the tank Judgement): beta {beta(g, crusader=False):.0f}, proposed keeps {prop(g):.0f}")
    print(f"  no armor debuffs (4,500): Warrior {T.warrior(g.but(armor=3731)):.0f}, Druid {T.druid(g.but(armor=3731)):.0f}, "
          f"beta {beta(g.but(armor=3731)):.0f}, proposed {prop(g.but(armor=3731)):.0f}")
    print("  spell power 100..350, beta | proposed: " + ", ".join(
        f"{sp}: {beta(g.but(sp=sp)):.0f}/{prop(g.but(sp=sp)):.0f}" for sp in (100, 150, 200, 250, 300, 350)))

    print("\n## Part 2: tiers. Warrior | Druid | Druid wowsims | beta | beta no Crusader | proposed | proposed + Consecration")
    for t in T.TIERS + [T.PATH_BETA]:
        w, d, dw = T.warrior(t), T.druid(t), T.druid(t, mults=T.DRU_WOWSIMS)
        vals = (beta(t), beta(t, crusader=False), prop(t), prop(t, consecration=True))
        print(f"  {t.name} | {w:.0f} | {d:.0f} | {dw:.0f} | " + " | ".join(f"{v:.0f} ({pct(v, w)} W, {pct(v, d)} D)" for v in vals))

    print("\n## Part 3: flatter gear, proposed % of the Warrior (of the Druid)")
    for name, ts in (("Gear as in part 2", T.TIERS), ("Flatter, boss as part 2", T.flatter(False)), ("Flatter, flatter boss", T.flatter(True))):
        print(f"  {name}: " + " | ".join(f"{t.name}: {pct(prop(t), T.warrior(t))} ({pct(prop(t), T.druid(t))}); beta {pct(beta(t), T.warrior(t))} ({pct(beta(t), T.druid(t))})" for t in ts))

    print("\n## Part 8: several targets, Paladin with Consecration. all (one extra)")
    for n in (1, 3, 5):
        print(f" {n} target(s): Tier | Warrior | Druid | Druid wowsims | beta | proposed | proposed % of best (extra)")
        for t in T.TIERS:
            w, we = MT.war(t, n); d, de = MT.dru(t, n); dw, dwe = MT.dru(t, n, T.DRU_WOWSIMS)
            bb, be = pal_multi(t, n, proposed=False); p, pe = pal_multi(t, n)
            best = max(w, d)
            ex = f" ({pe / max(we, de):.0%})" if n > 1 else ""
            print(f"  {t.name} | {w:.0f} ({we:.0f}) | {d:.0f} ({de:.0f}) | {dw:.0f} ({dwe:.0f}) | {bb:.0f} ({be:.0f}) | {p:.0f} ({pe:.0f}) | {p / best:.0%}{ex}")
    for n in (3, 5):
        r = [pal_multi(t, n, cons=False)[0] / max(MT.war(t, n)[0], MT.dru(t, n)[0]) for t in T.TIERS]
        e = [pal_multi(t, n, cons=False)[1] / max(MT.war(t, n)[1], MT.dru(t, n)[1]) for t in T.TIERS]
        print(f"  no Consecration, {n} targets: all {min(r):.0%}-{max(r):.0%}, extra {min(e):.0%}-{max(e):.0%}")
