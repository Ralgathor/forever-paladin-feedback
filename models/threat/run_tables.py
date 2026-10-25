"""All threat values of the document: Analysis, Threat (proposals/analysis/threat.md), Analysis, Builds (parts 3,
5 and 6), Protection (C7, C11, C14), Judgements and Blessings (C18), Retribution (C16) and Withdrawn ideas.
Run: python3 run_tables.py"""
from threat_model import (PART1, TIERS, BUILDS, TANK_REF, PB1, PB2, HOLY_SHOCK_TANK, HEALING_TANK, flatter, paladin,
                          warrior, druid, armor_dr, table, OHWS)

def beta(g, **kw):
    return paladin(g, TANK_REF, proposed=False, c14=0, **kw)

def pct(a, b):
    return f"{a / b:.0%}"

def diff(f, base, **kw):
    """f(**kw) - base as a signed integer."""
    return f"{f(**kw) - base:+.0f}"

if __name__ == "__main__":
    g = PART1
    P = paladin(g)
    print("## Threat, part 1: pre-raid gear, 200 spell power, 60 block value (8/35/8 tank talents)")
    print("Boss hit | Warrior | Druid | Paladin, beta | Paladin, all proposals | + Consecration")
    for H in (3000, 4500, 6000):
        h = g.but(boss_hit=H)
        print(f"{H:,} | {warrior(h):.0f} | {druid(h):.0f} | {beta(h):.0f} | {paladin(h):.0f} | "
              f"{paladin(h, consecration=True):.0f}")
    print(f"Beta Paladin without Judgement of the Crusader: {beta(g, crusader=False):.0f}"
          f" (Crusader {beta(g) - beta(g, crusader=False):+.0f})")
    print(f"Judgement of the Crusader, proposed Paladin: {P - paladin(g, crusader=False):+.0f}")
    print(f"Proposed Paladin without C14: {paladin(g, c14=0):.0f}, with Consecration "
          f"{paladin(g, c14=0, consecration=True):.0f}")
    na = g.but(armor=3731)
    print(f"No armor debuffs (4,500 hits): Warrior {warrior(na):.0f}, Druid {druid(na):.0f}, Paladin {paladin(na):.0f}")
    print(f"Shield Slam x2.25: Warrior {warrior(g, slam_mult=2.25) - warrior(g):+.0f}")
    print(f"Retribution Aura: {paladin(g, ret_aura=True) - P:+.0f}")
    print(f"C16 (Holy Strike triggers Seal of Fury): {paladin(g, c16=True) - P:+.0f}")
    total, src = paladin(g, detail=True)
    print("Threat sources: " + ", ".join(f"{k} {v:.0f}" for k, v in src.items()) + f". Total {total:.0f}")
    print(f"Proposals against the beta: {P - beta(g):+.0f}. C14 {P - paladin(g, c14=0):+.0f}. "
          f"C6 and C11 {paladin(g, c14=0) - beta(g):+.0f}")
    sps = (100, 150, 200, 250, 300, 350)
    v = [paladin(g.but(sp=sp)) for sp in sps]
    print("Spell power: " + ", ".join(f"{sp} {x:.0f}" for sp, x in zip(sps, v))
          + f". Each +100: {(v[-1] - v[0]) / 2.5:+.0f}")

    print("\n## Threat, part 2: gear tiers. Paladin columns: % of the Druid")
    print("Tier | Warrior | Druid | Paladin, beta | Without C14 | All proposals | + Consecration")
    for t in TIERS:
        w, d = warrior(t), druid(t)
        cols = (beta(t), paladin(t, c14=0), paladin(t))
        print(f"{t.name} | {w:.0f} | {d:.0f} | " + " | ".join(f"{x:.0f} ({pct(x, d)})" for x in cols)
              + f" | {paladin(t, consecration=True):.0f}")
    print("Judgement of the Crusader, beta: " + ", ".join(f"{beta(t) - beta(t, crusader=False):+.0f}" for t in TIERS))

    print("\n## Threat, part 3: % of the Druid (% of the Warrior)")
    cases = (("Gear as in part 2", TIERS), ("Flatter gear, boss hits as in part 2", flatter(False)),
             ("Flatter gear, flatter boss hits", flatter(True)))
    for name, tiers in cases:
        n = tiers[-1]
        print(name + ": " + ", ".join(f"{pct(paladin(t), druid(t))} ({pct(paladin(t), warrior(t))})" for t in tiers)
              + f". Naxxramas without C14 {pct(paladin(n, c14=0), druid(n))}"
              + f", C14 at 100% {pct(paladin(n, c14=1), druid(n))}, 150% {pct(paladin(n, c14=1.5), druid(n))}"
              + f", 300% {pct(paladin(n, c14=3), druid(n))} ({pct(paladin(n, c14=3), warrior(n))} of the Warrior)")
    print("C14 at 300%, % of the Warrior: " + ", ".join(pct(paladin(t, c14=3), warrior(t)) for t in TIERS))

    print("\n## Threat, part 5: next steps (TPS added at each tier)")
    print("Iron Creed +100%: " + ", ".join(f"{paladin(t, ic_rank=0.20) - paladin(t):+.0f}" for t in TIERS))
    print("Shield attack: " + ", ".join(f"{paladin(t, shield_attack=True) - paladin(t):+.0f}" for t in TIERS))

    print("\n## Builds, part 3 (part 1 gear)")
    for name, tal in BUILDS:
        print(f"{name}: {paladin(g, tal):.0f} / {paladin(g, tal, consecration=True):.0f}")
    p1 = paladin(g, PB1)
    print(f"PB2 against PB1: {paladin(g, PB2) / p1 - 1:+.1%}. PB1 against the 8/35/8 tank: {p1 / P - 1:+.1%}")
    print(f"Improved Judgement in PB1, per point: {(p1 - paladin(g, dict(PB1, ij=0))) / 2:.1f}")
    per = {"Holy Shield": ("hsh", 1), "Redoubt": ("red", 5), "Reckoning": ("reck", 5), "Swift Judgement": ("sj", 1),
           "One-Handed Weapon Specialization": ("ohws", 3), "Improved Seals": ("is", 3), "Precision": ("prec", 3),
           "Conviction": ("conv", 3), "Iron Creed": ("ic", 5)}
    print("Per point (8/35/8 tank): " + ", ".join(f"{n} {(P - paladin(g, dict(TANK_REF, **{k: 0}))) / r:.1f}" for n, (k, r) in per.items())
          + f", Vindication {(paladin(g, dict(TANK_REF, vind=5)) - P) / 5:.1f}")

    print("\n## Builds, part 5")
    p2 = paladin(g, PB2)
    jud_casts = 1 / 10 + 1 / 60
    _, src = paladin(g, detail=True)
    hs = (src["Holy Shield, base"] + src["Holy Shield, block value"]) * 10 / 240
    jud = src["Judgement of Fury"] / jud_casts / 91
    _, s2 = paladin(g, HOLY_SHOCK_TANK, holy_shock=True, consecration=True, detail=True)
    _, s3 = paladin(g, HOLY_SHOCK_TANK, holy_shock=True, detail=True)
    print(f"Threat for each mana point: Holy Shield {hs:.1f}, Judgement {jud:.1f}, "
          f"Holy Shock {s3['Holy Shock'] * 10 / 325:.1f}, Consecration {s2['Consecration'] * 8 / 565:.1f}")
    hst = paladin(g, HOLY_SHOCK_TANK, holy_shock=True)
    hstc = paladin(g, HOLY_SHOCK_TANK, holy_shock=True, consecration=True)
    print(f"Holy Shock tank: {hst:.0f} ({pct(hst, p2)} of PB2), with Consecration {hstc:.0f} ({pct(hstc, p2)})")
    print(f"Retribution tank, 75-95% of PB2: {0.75 * p2:.0f}-{0.95 * p2:.0f}")

    print("\n## Builds, part 6: healing threat (Righteous Fury x1 / x1.9 on heals)")
    v1 = dict(TANK_REF, conv=5)    # dungeon tank of version 1: the threat talents of the 8/35/8 tank, Conviction 5
    p2 = paladin(g, v1)
    rows = (("Dungeon tank (version 1), no heals", v1, 0, 0.0),
            ("Dungeon tank, 1 Flash of Light each 10 sec", v1, 42, 0.15),
            ("Dungeon tank, 1 Holy Light each 10 sec", v1, 183, 0.25),
            ("Healing tank, 1 Holy Light and 1 Flash of Light each 10 sec", HEALING_TANK, 293, 0.30),
            ("Healing tank, 2 Holy Light and 2 Flash of Light each 10 sec", HEALING_TANK, 586, 0.70))
    for name, tal, hps, cast in rows:
        a = paladin(g, tal, heal=hps, casting=cast)
        b = paladin(g, tal, heal=hps, casting=cast, rf_heals=True)
        print(f"{name}: {a:.0f} / {b:.0f} ({pct(a, p2)} / {pct(b, p2)} of no heals)")

    print("\n## Protection")
    print(f"C7 Iron Creed 5/5 Holy Strike threat: {P - paladin(g, dict(TANK_REF, ic=0)):+.0f}")
    dr = armor_dr()
    for name, prop, attacks in (("Beta, 1 boss", False, 1.0), ("Beta, 3 enemies", False, 2.2),
                                ("Proposed, 1 boss", True, 2.0), ("Proposed, 3 enemies", True, 2.0)):
        land, f = table(g.hit + 0.03, g.crit + 0.03, auto=not prop)
        dmg = g.weapon() * (1 - dr) * (1 + OHWS[3]) * f
        sof = 0.10 * (g.sp + 161) * 1.15 * 1.10 * 1.09 * 1.9 * land
        print(f"C11 {name}: {attacks} attacks each 10 sec, {dmg:.0f} damage and {dmg + sof:.0f} threat each, "
              f"{dmg * attacks / 10:+.0f} damage per sec, {(dmg + sof) * attacks / 10:+.0f} TPS")

    print("\n## Withdrawn ideas")
    n = TIERS[-1]
    print(f"Righteous Fury x1.5 on physical damage, no C14, Naxxramas: {pct(paladin(n, c14=0, phys_mult=1.5), druid(n))}"
          " of the Druid")
