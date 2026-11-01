"""Retribution on the beta of 30 October 2026 (wowsims Forever, branch paladin/hotfix-113554-port, push 113554).
Uses models/damage/damage_model.py of the repo (gear tiers, hit tables, Vengeance, Fury, Arms, Rogue).
Run from the repo: python3 retribution_b2.py <repo>/models/damage

Build (wowsims UnsealedWrathTalents 050250002-5-05233301101301351, 14/5/32):
- Holy: Divine Strength 5/5 (+10% Strength), Reverence 2/2, Improved Seals 5/5 (+15% Seals and Judgements),
  Holy Conduit 2/2 (-40% Hammer of Wrath and Consecration cost).
- Protection: Divine Intellect 5/5 (+10% Intellect). No Precision.
- Retribution: Benediction 5/5, Improved Judgement 2/2, Conviction 3/3 (+6% critical chance, all attacks and spells),
  Sanctified Judgement 3/3, Vindication 3/3 (no Attack Power now), Seal of Command, Sacred Arbiter (+20% Holy Strike),
  Two-Handed Weapon Specialization 3/3 (+6% Physical damage only), Vengeance 3/3, Champion of the Light 5/5
  (60% of Intellect as spell damage, Hammer of Wrath -1 sec cast time), Unsealed Wrath.

Unsealed Wrath (wowsims talents_retribution.go, spell 1310735): proc flag 0x4, auto attacks only. Each auto attack that
lands stores a copy of the active Seal (15 sec, 3 stacks). An auto attack that lands with a different Seal consumes
all copies: each copy gives the stored Seal its usual chance. Seal of Command copies share the 1 sec cooldown of the
Seal of Command proc: only one of the copies can proc at a time. Seal of Righteousness copies all hit.
The wowsims rotation casts the other Seal after each swing (n = 1): each swing gives Seal of Righteousness and a
Seal of Command chance. n swings with Seal of Righteousness, then 1 swing with Seal of Command: fewer Seal casts.

Mana (wowsims spell data): Seal of Righteousness rank 8 200, Seal of Command rank 5 210, Benediction x0.90.
Unsealed Wrath has no cost decrease (W29). Judgement 6% of base mana (91). Sanctified Judgement 3/3 returns 60% of
the base cost of the judged Seal. Holy Strike 20. Hammer of Wrath 425 x0.60.
Income: Reverence 2/2 (30% of Spirit regeneration in casts) 6.2 per sec, Blessing of Wisdom 8 per sec.
"""
import sys
sys.path.insert(0, sys.argv[1] if len(sys.argv) > 1 else ".")
import damage_model as M
PURE = {"Warrior": 929, "Rogue": 702, "Hunter": 1175, "Mage": 860, "Warlock": 879}   # run_tables.py (MythicSim)
RET_SIM = 848                                                                          # wowsims test runs, 30 October
from damage_model import (gear, auto_table, spec_table, vengeance, fury, arms, rogue, TIER_NAMES, CRIT_SPEC, DODGE,
                          EXECUTE, FIGHT, KINGS, MOTW, MIGHT, SHOUT, NORM_2H, SPEED_2H, DR, MISS)

B2 = dict(ds=5, is_=5, di=5, ben=5, ij=2, conv=3, sanc=3, soc=1, sa=1, thws=3, veng=3, cotl=5)
BEN = 0.90
SOR_COST, SOC_COST, JUD_COST, HS_COST, HOW_COST = 200, 210, 91, 20, 425 * 0.60
REV_INCOME, WISDOM = 10.3 * 30 / 50, 8.0

def stats_b2(g, tal=B2):
    t = lambda k: tal.get(k, 0)
    st = (g["str"] + MOTW) * KINGS * (1 + 0.02 * t("ds"))
    ap = st * 2 + g["ap_items"] + MIGHT + SHOUT
    intel = (g["int"] + MOTW) * KINGS * (1 + 0.02 * t("di"))
    crit = g["crit"] + (MOTW * KINGS) / 20 / 100 + 0.02 * t("conv")
    return dict(ap=ap, sd=g["sd"] + 0.12 * t("cotl") * intel, int=intel, hit=min(g["hit"], MISS), crit=crit,
                w=g["w2"], speed=SPEED_2H)

def retribution_b2(g, c1=False, bz=0, n=1, tal=B2, fight=FIGHT, detail=False, seal_mult=1.0):
    """c1: Holy Strike triggers your Seal (C1). bz: Burning Zeal ranks (C-R4, +10% critical damage bonus each).
    n: swings with Seal of Righteousness before one swing with Seal of Command. n=None: Seal of Command only.
    seal_mult: Seal cost factor (0.80: a -20% Seal cost on Unsealed Wrath, as Twist of Light)."""
    t = lambda k: tal.get(k, 0)
    s = stats_b2(g, tal)
    sd, imp, ths = s["sd"], 1 + 0.03 * t("is_"), 1 + 0.02 * t("thws")
    sa = 1 + 0.20 * t("sa")
    wd = s["w"] * s["speed"] + s["ap"] / 14 * s["speed"]
    wn = s["w"] * s["speed"] + s["ap"] / 14 * NORM_2H
    land_a, crit_a, f_auto = auto_table(s["hit"], s["crit"])
    land, _, _ = spec_table(s["hit"], s["crit"])
    m = 1 + 0.10 * bz
    _, crit_j, f_jud = spec_table(s["hit"], s["crit"], dodge=0.0, crit_mult=1 + m)
    _, crit_hs, f_hs = spec_table(s["hit"], s["crit"], crit_mult=1 + m)
    _, crit_how, f_how = spec_table(s["hit"], s["crit"])
    c_seal = max(0.0, s["crit"] - CRIT_SPEC)
    how_rate = EXECUTE / 6
    autos = 1 / s["speed"]                                   # Champion of the Light 5/5: Hammer of Wrath is instant
    hs_rate = 1 / 10
    jud_rate = 1 / (10 - t("ij"))
    p_soc = 7 / 60 * s["speed"]                              # 7 procs each minute
    landed = autos * land_a
    if n is None:                                            # one Seal: Seal of Command, no copy is consumed
        sor_auto, soc_auto, share_sor, seals = 0.0, 1.0, 0.0, 1 / 30
    else:
        # A cycle of n + 1 swings: n with Seal of Righteousness (n copies), 1 with Seal of Command (1 copy).
        # Seal of Righteousness: n active hits + min(n, 3) copies. Seal of Command: 1 chance + 1 copy chance.
        k = n + 1
        sor_auto = (n + min(n, 3)) / k
        soc_auto = 2 / k
        share_sor = n / k                                    # part of the time with Seal of Righteousness active
        seals = 2 / k * landed                               # Seal casts each sec
    sor_rate = landed * sor_auto
    soc_rate = landed * soc_auto * p_soc * land
    if c1:                                                   # Holy Strike triggers the active Seal (no copy)
        sor_rate += hs_rate * land * share_sor
        soc_rate += hs_rate * land * (1 - share_sor) * p_soc * land
    cps = (autos * crit_a + hs_rate * crit_hs + how_rate * crit_how + jud_rate * crit_j + (soc_rate + sor_rate) * c_seal)
    V = vengeance(cps, per=0.01 * t("veng"), stacks=3, fight=fight)
    src = {}
    src["Auto attacks"] = wd * (1 - DR) * ths * V * f_auto * autos
    src["Seal of Command"] = soc_rate * (0.70 * imp * wd + 0.233 * sd) * V * (1 + c_seal * m)
    src["Holy Strike"] = hs_rate * 0.5 * (wn + 93 + 0.429 * sd) * sa * V * f_hs
    # Judgement of Righteousness (Seal of Righteousness active) or Judgement of Command (Seal of Command): the model
    # uses Judgement of Righteousness for both.
    src["Judgement"] = jud_rate * (178.2 + 0.429 * sd) * imp * V * f_jud
    src["Seal of Righteousness"] = sor_rate * (67.5 + 0.12 * sd) * imp * V * (1 + c_seal * m)
    src["Hammer of Wrath"] = how_rate * (498 + 0.429 * sd) * V * f_how
    total = sum(src.values())
    # Mana each sec
    seal_cost = (SOR_COST + SOC_COST) / 2 if n else SOC_COST
    spend = (seals * seal_cost * BEN * seal_mult + jud_rate * (JUD_COST * BEN - 0.20 * t("sanc") * seal_cost)
             + hs_rate * HS_COST * BEN + how_rate * HOW_COST * BEN)
    mana = dict(pool=1232 + 15 * s["int"], spend=spend, seals=seals)
    return (total, src, V, mana) if detail else total

def time_to_zero(mana, wisdom=True):
    net = mana["spend"] - REV_INCOME - (WISDOM if wisdom else 0)
    return None if net <= 0 else mana["pool"] / net

def fight_dps(g, fight, wisdom=True, **kw):
    """Best average DPS in the fight: the twist with the n that the mana permits (n = 1..6), else Seal of Command only
    after the mana is zero."""
    best = (0, None)
    one = retribution_b2(g, n=None, fight=fight, **kw)
    for n in range(1, 7):
        d, _, _, mana = retribution_b2(g, n=n, fight=fight, detail=True, **kw)
        z = time_to_zero(mana, wisdom)
        avg = d if z is None or z >= fight else (d * z + one * (fight - z)) / fight
        if avg > best[0]:
            best = (avg, n)
    return best

if __name__ == "__main__":
    g = gear(0)
    base, src, V, mana = retribution_b2(g, detail=True)
    print("## Fresh level 60, 2 min, wowsims rotation (a Seal change after each swing)")
    print("  " + ", ".join(f"{k} {v:.0f}" for k, v in src.items()) + f". Total {base:.0f}. Vengeance +{V - 1:.1%}")
    print(f"  Mana: pool {mana['pool']:.0f}, spend {mana['spend']:.1f} per sec ({mana['seals']:.2f} Seals each sec), "
          f"income {REV_INCOME:.1f} + Wisdom {WISDOM:.0f}")
    for w in (True, False):
        z = time_to_zero(mana, w)
        print(f"  Mana zero {'with' if w else 'without'} Blessing of Wisdom: "
              f"{'never' if z is None else f'{int(z // 60)}:{int(z % 60):02d}'}")
    print("## Seal plans: n swings with Seal of Righteousness, 1 with Seal of Command")
    one = retribution_b2(g, n=None)
    print(f"  Seal of Command only: {one:.0f} ({one / base - 1:+.0%})")
    for n in (1, 2, 3, 4, 6):
        d, _, _, mn = retribution_b2(g, n=n, detail=True)
        z = time_to_zero(mn)
        print(f"  n={n}: {d:.0f} ({d / base - 1:+.1%}), spend {mn['spend']:.1f}, mana zero "
              f"{'never' if z is None else f'{int(z // 60)}:{int(z % 60):02d}'}")
    print("## Proposals against the beta, same Seal plan (n=1), by tier")
    print("  tier | beta | C1 | C-R4 2/2 | C1 + C-R4")
    for tier, name in enumerate(TIER_NAMES):
        h = gear(tier)
        b = retribution_b2(h)
        c = retribution_b2(h, c1=True); z = retribution_b2(h, bz=2); cz = retribution_b2(h, c1=True, bz=2)
        print(f"  {name} | {b:.0f} | {c / b - 1:+.1%} | {z / b - 1:+.1%} | {cz / b - 1:+.1%}")
    print("## Best plan in the fight with the mana (with Blessing of Wisdom): DPS (n)")
    for fight in (120, 180, 300):
        row = []
        for tier in range(5):
            h = gear(tier)
            b, nb = fight_dps(h, fight)
            p, npp = fight_dps(h, fight, c1=True, bz=2)
            row.append(f"{b:.0f} (n={nb}) -> {p:.0f} (n={npp}, {p / b - 1:+.1%})")
        print(f"  {fight} sec: " + " | ".join(row))
    print("## Seal cost -20% on Unsealed Wrath (option for W29), with Blessing of Wisdom: mana zero, best DPS in the fight")
    for n in (1, 2, 3):
        _, _, _, mn = retribution_b2(g, n=n, detail=True, seal_mult=0.80)
        z = time_to_zero(mn)
        print(f"  n={n}: spend {mn['spend']:.1f}, mana zero {'never' if z is None else f'{int(z // 60)}:{int(z % 60):02d}'}")
    for fight in (120, 180, 300):
        a = fight_dps(g, fight)[0]; b = fight_dps(g, fight, seal_mult=0.80)[0]
        print(f"  {fight} sec, fresh level 60: {a:.0f} -> {b:.0f} ({b / a - 1:+.1%})")
    print("## Against the pure average (wowsims 848 at fresh level 60, the increase of the model; Hunter, Mage and "
          "Warlock with the shape of Arms, x1.60 | x1.75 | x1.90 in Naxxramas)")
    gr = lambda f: [f(gear(t)) / f(gear(0)) for t in range(5)]
    Rb, F, A, C = gr(retribution_b2), gr(fury), gr(arms), gr(rogue)
    print("  Increase to Naxxramas: Retribution x%.2f, Fury x%.2f, Arms x%.2f, Combat Rogue x%.2f" % (Rb[4], F[4], A[4], C[4]))
    shape = [(a - 1) / (A[4] - 1) for a in A]
    casters = PURE["Hunter"] + PURE["Mage"] + PURE["Warlock"]
    for o in (1.60, 1.75, 1.90):
        for name, kw in (("beta", {}), ("C1", dict(c1=True)), ("C1 + C-R4", dict(c1=True, bz=2))):
            row = []
            for t in range(5):
                pure = (PURE["Warrior"] * F[t] + PURE["Rogue"] * C[t] + casters * (1 + (o - 1) * shape[t])) / 5
                r = RET_SIM * Rb[t] * retribution_b2(gear(t), **kw) / retribution_b2(gear(t))
                row.append(f"{r / pure:.0%}")
            print(f"  x{o:.2f} {name:10s} " + " | ".join(row))
