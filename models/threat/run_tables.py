"""Tables of Analysis, Threat (proposals/analysis/threat.md) and the build values of Analysis, Builds.
Run: python3 run_tables.py
Each line gives the model value and, in brackets, the value in the document."""
from threat_model import PART1, TIERS, BUILDS, PB1, flatter, paladin, warrior, druid

def cmp(model, doc):
    return f"{model:4.0f} ({doc})"

def beta(g, **kw):
    return paladin(g, PB1, proposed=False, c14=False, **kw)

if __name__ == "__main__":
    print("## Part 1: pre-raid gear, 200 spell power, 60 block value")
    print("Boss hit | Warrior | Druid | Paladin, beta | Paladin, all proposals | + Consecration")
    doc = {3000: (525, 520), 4500: (600, 585), 6000: (660, 650)}
    for H, (dw, dd) in doc.items():
        g = PART1.but(boss_hit=H)
        print(f"{H:,} | {cmp(warrior(g), dw)} | {cmp(druid(g), dd)} | {cmp(beta(g), 400)} | "
              f"{cmp(paladin(g), 540)} | {cmp(paladin(g, consecration=True), 625)}")
    g = PART1
    print(f"Beta Paladin without Judgement of the Crusader: {cmp(beta(g, crusader=False), 355)}")
    print(f"Proposed Paladin without C14: {cmp(paladin(g, c14=False), 455)}, "
          f"with Consecration {cmp(paladin(g, c14=False, consecration=True), 545)}")
    na = g.but(armor=3731)
    print(f"No armor debuffs (4,500 hits): Warrior {cmp(warrior(na), 470)}, Druid {cmp(druid(na), 425)}, "
          f"Paladin {cmp(paladin(na), 515)}")
    print(f"Shield Slam x2.25: Warrior {warrior(g, slam_mult=2.25) - warrior(g):+.0f} (+135)")
    print(f"Judgement of the Crusader, proposed Paladin: {paladin(g) - paladin(g, crusader=False):+.0f} (+50)")
    print("Spell power: " + ", ".join(f"{sp} {cmp(paladin(g.but(sp=sp)), d)}"
                                      for sp, d in zip((100, 150, 200, 250, 300, 350), (505, 525, 540, 555, 570, 585))))
    total, src = paladin(g, detail=True)
    print("Threat sources (PB1): " + ", ".join(f"{k} {v:.0f}" for k, v in src.items()) + f". Total {total:.0f} (540)")

    print("\n## Part 2: gear tiers. Paladin columns: % of the Druid")
    doc = ((490, 405, 380, 430, 470, 555), (545, 455, 415, 470, 555, 645), (640, 530, 450, 515, 625, 720),
           (755, 635, 495, 565, 700, 800), (815, 760, 535, 605, 775, 880))
    print("Tier | Warrior | Druid | Paladin, beta | Without C14 | All proposals | + Consecration")
    for g, d in zip(TIERS, doc):
        w, dr = warrior(g), druid(g)
        p = (beta(g), paladin(g, c14=False), paladin(g))
        print(f"{g.name} | {cmp(w, d[0])} | {cmp(dr, d[1])} | "
              + " | ".join(f"{cmp(v, dv)} {v / dr:.0%}" for v, dv in zip(p, d[2:5]))
              + f" | {cmp(paladin(g, consecration=True), d[5])}")

    print("\n## Part 3: Paladin with all proposals, % of the Druid (% of the Warrior)")
    cases = (("Gear as in part 2", TIERS), ("Flatter gear, boss hits as in part 2", flatter(False)),
             ("Flatter gear, flatter boss hits", flatter(True)))
    for name, tiers in cases:
        print(name + ": " + ", ".join(f"{paladin(g) / druid(g):.0%} ({paladin(g) / warrior(g):.0%})" for g in tiers)
              + f"; Naxxramas without C14 {paladin(tiers[-1], c14=False) / druid(tiers[-1]):.0%}")
    print("Document: 116/122/118/111/102% (96/101/97/93/95); 116/122/114/104/94% (96/101/95/88/89); "
          "116/122/120/115/110% (96/101/99/95/91). Without C14: 80%, 76%, 89%")

    print("\n## Analysis, Builds: threat per sec (one target / with Consecration), part 1 gear")
    # The document keeps PB1 and PB2 from the first calculation. The other builds use the model result
    # relative to PB1: the "scaled" values.
    doc = {"PB1": "562 / 650", "PB2": "569 / 657", "PB3": "about 527 / 666", "PB4": "about 527 / 666",
           "PB3 + One-Handed Weapon Specialization": "about 552 / 692"}
    one1, cons1 = paladin(PART1, PB1), paladin(PART1, PB1, consecration=True)
    for name, tal in BUILDS:
        one, cons = paladin(PART1, tal), paladin(PART1, tal, consecration=True)
        print(f"{name}: {one:.0f} / {cons:.0f} ({doc[name]}). Scaled to PB1 = 562 / 650: "
              f"{562 * one / one1:.0f} / {650 * cons / cons1:.0f}")
