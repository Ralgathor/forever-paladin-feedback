"""Mana of a Protection Paladin while tanking one boss. Analysis, Mana (proposals/analysis/mana.md), part 4,
and Analysis, Builds, part 3. Proposed trees. Run: python3 mana_model.py
A steady-state model: mana per sec (MPS), income minus costs. Spell costs and talent values checked against
wowsims Forever (github.com/wowsims/forever, 25 October 2026)."""

TIERS = (("Fresh level 60", 2897, 3), ("Pre-raid best in slot", 3400, 5), ("Molten Core", 3900, 8),
         ("Blackwing Lair", 4400, 10), ("Naxxramas", 4900, 12))          # maximum mana, mp5

# Costs (Forever spellbook). Judgement: 6% of base mana 1,512. Holy Strike and Holy Shield each 10 sec.
HOLY_SHIELD, HOLY_STRIKE, JUDGEMENT, SEAL_OF_FURY, CONSECRATION = 240, 20, 91, 200, 565
SEAL_TIME, CONS_EVERY = 30, 8
BLOCK, SWING = 0.60, 2.0          # C6 block chance; the boss swings each 2 sec
REVERENCE = 10.3                  # Reverence 3/3 (C1, 50%): half of 41 mana each 2 sec at 130 Spirit
WISDOM = 40 / 5                   # Blessing of Wisdom rank 6: 40 mana each 5 sec
ISOF = 23.3                       # beta Improved Seal of Fury: 87 mana for each shield that a boss hit uses

def mps(mana, mp5, rev=False, sanj=0, ij=0, swift=1, ben=0, hc=0, cons=False, wisdom=False, hit=True, beta=False):
    """rev: Reverence 3/3. sanj: Sanctified Judgement ranks. ij: Improved Judgement ranks (-1 sec cooldown each).
    swift: Swift Judgement (a free Judgement each min). ben: Benediction ranks (-2% instant costs each).
    hc: Holy Conduit ranks (-20% Consecration cost each). hit: the boss hits the Paladin.
    beta: beta Shield Specialization (once each 3 sec, 50% block) and Improved Seal of Fury, not C13."""
    b = 1 - 0.02 * ben
    judgements = 1 / (10 - ij)                                       # paid Judgements per sec
    cost = (HOLY_SHIELD / 10 + HOLY_STRIKE / 10 + JUDGEMENT * judgements + SEAL_OF_FURY / SEAL_TIME) * b
    if cons:
        cost += CONSECRATION * b * (1 - 0.2 * hc) / CONS_EVERY
    income = mp5 / 5 + (REVERENCE if rev else 0) + (WISDOM if wisdom else 0)
    if hit and beta:
        income += mana * 0.04 / 6 + ISOF                             # the 3 sec limit skips the next swing
    elif hit:
        income += mana * 0.04 * BLOCK / SWING                        # Shield Specialization 3/3 (C13)
    # Sanctified Judgement (C26): 20% of the seal base cost for each rank, on each Judgement (also the free one).
    # Beta: only a 33/66/100% chance; the model uses rank 3, where the two are the same.
    # A seal cost decrease goes on top of the return (wowsims Forever, measured in game).
    income += SEAL_OF_FURY * (2 - b) * 0.2 * sanj * (judgements + swift / 60)
    return income - cost

def lasts(mana, v):
    if v >= 0:
        return "all the fight"
    s = int(mana / -v)
    if s >= 3600:
        return "more than 1 hour"
    return f"{s // 60} min {s % 60} sec" if s >= 60 else f"{s} sec"

# Analysis, Builds, part 3. Only the talents that change mana.
BUILDS = (("PB1, PB3, PB4 (3/35/13)", dict(sanj=3, ij=2, hc=2)),
          ("PB2 (3/35/13, no Holy Conduit)", dict(sanj=3, ij=2)),
          ("3/35/13 with Vindication, no Improved Judgement or Holy Conduit", dict(sanj=3)),
          ("8/35/8 tank (Reverence)", dict(rev=True)),
          ("8/35/8 tank, Holy Conduit (Reverence)", dict(rev=True, hc=2)))

if __name__ == "__main__":
    print("## Mana, part 4: income while tanking, Sanctified Judgement 3/3")
    for ij in (0, 2):
        j = 1 / (10 - ij) + 1 / 60
        print(f"Improved Judgement {ij}: {j * 60:.1f} Judgements each min, return {SEAL_OF_FURY * 0.6 * j:.1f} MPS, "
              f"Judgement cost {JUDGEMENT / (10 - ij):.1f} MPS")
    print("\n## Sanctified Judgement by rank (C26), Seal of Fury, Improved Judgement 2/2 and Swift Judgement")
    j = 1 / 8 + 1 / 60
    for r, chance in ((1, 0.33), (2, 0.66), (3, 1.0)):
        beta, c26 = SEAL_OF_FURY * 0.2 * r * chance, SEAL_OF_FURY * 0.2 * r
        print(f"{r}/3: beta {beta:.0f} mana ({beta * j:.1f} MPS), C26 {c26:.0f} mana ({c26 * j:.1f} MPS)")
    print("\n## Mana used (MPS)")
    for name, kw in (("no Consecration", {}), ("Consecration", dict(cons=True)),
                     ("Consecration, Holy Conduit", dict(cons=True, hc=2)),
                     ("Improved Judgement 2/2, no Consecration", dict(ij=2)),
                     ("Improved Judgement 2/2, Consecration", dict(ij=2, cons=True)),
                     ("Improved Judgement 2/2, Consecration, Holy Conduit", dict(ij=2, cons=True, hc=2))):
        print(f"{name}: {-mps(0, 0, hit=False, swift=0, **kw):.1f}")
    for wisdom in (False, True):
        print(f"\n## Tank builds, {'with' if wisdom else 'no'} Blessing of Wisdom: MPS (time until zero)")
        print("Build | " + " | ".join(f"{t[0]}, no Consecration | {t[0]}, Consecration" for t in (TIERS[0], TIERS[-1])))
        for name, kw in BUILDS:
            cols = []
            for _, m, p in (TIERS[0], TIERS[-1]):
                for cons in (False, True):
                    v = mps(m, p, cons=cons, wisdom=wisdom, **kw)
                    cols.append(f"{v:+.1f}" + ("" if v >= 0 else f": {lasts(m, v)}"))
            print(name + " | " + " | ".join(cols))
    pb1 = BUILDS[0][1]
    print("\n## PB1, tanking, no Consecration: beta and proposed MPS")
    for name, m, p in TIERS:
        print(f"{name} ({m:,}): {mps(m, p, beta=True, **pb1):+.1f} | {mps(m, p, **pb1):+.1f}")
    print("\n## PB1, other cases: beta | proposed (time until zero)")
    for name, kw in (("Consecration, no Holy Conduit", dict(cons=True, hc=0)),
                     ("Consecration, Benediction, no Holy Conduit", dict(cons=True, ben=5, hc=0)),
                     ("Consecration, Holy Conduit", dict(cons=True)),
                     ("Consecration, Benediction and Holy Conduit", dict(cons=True, ben=5)),
                     ("Not hit, no Consecration", dict(hit=False)),
                     ("Not hit, Consecration, Holy Conduit", dict(hit=False, cons=True))):
        k = dict(pb1, **kw)
        cols = [f"{v:+.1f}: {lasts(m, v)}" for _, m, p in (TIERS[0], TIERS[-1]) for v in (mps(m, p, beta=True, **k), mps(m, p, **k))]
        print(name + " | " + " | ".join(cols))
    print("\n## Not hit, no Consecration, no Blessing of Wisdom")
    for name, kw in BUILDS[:1] + BUILDS[3:4]:
        print(name + ": " + ", ".join(f"{t[0]} {mps(t[1], t[2], hit=False, **kw):+.1f} ({lasts(t[1], mps(t[1], t[2], hit=False, **kw))})"
                                      for t in (TIERS[0], TIERS[-1])))
    print("\n## Check against part 4 (8/35/8 tank, no Consecration): " +
          ", ".join(f"{mps(m, p, rev=True):+.1f}" for _, m, p in TIERS))
