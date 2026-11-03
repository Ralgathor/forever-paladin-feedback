"""Retribution on the beta of 30 October 2026 (wowsims Forever, branch paladin/hotfix-113554-port, push 113554).
Uses models/damage/damage_model.py of the repo (gear tiers, hit tables, Vengeance, Fury, Arms, Rogue).
Run: python3 retribution_b2.py

Build (wowsims default Retribution build of 1 November, 050250002-501-05233011201301351, 14/6/31):
- Holy: Divine Strength 5/5 (+10% Strength), Reverence 2/2, Improved Seals 5/5 (+15% Seals and Judgements),
  Holy Conduit 2/2 (-40% Hammer of Wrath and Consecration cost).
- Protection: Divine Intellect 5/5 (+10% Intellect), Precision 1/1 (+1% hit).
- Retribution: Benediction 5/5, Improved Judgement 2/2, Conviction 3/3 (+6% critical chance, all attacks and spells),
  Sanctified Judgement 3/3, Unyielding Faith 1, Pursuit of Justice 2, Seal of Command, Sacred Arbiter (+20% Holy Strike),
  Two-Handed Weapon Specialization 3/3 (+6% Physical damage only), Vengeance 3/3, Champion of the Light 5/5
  (60% of Intellect as spell damage, Hammer of Wrath -1 sec cast time), Unsealed Wrath.

Unsealed Wrath (wowsims talents_retribution.go, spell 1310735): proc flag 0x4, auto attacks only. Each auto attack that
lands stores a copy of the active Seal (15 sec, 3 stacks). An auto attack that lands with a different Seal consumes
all copies: each copy gives the stored Seal its usual chance. Seal of Command copies ignore the 1 sec cooldown of
the Seal of Command proc (wowsims commit 3989a1237): 3 copies give 3 chances. Seal of Righteousness copies all hit.
Seal plan (r, c): r swings with Seal of Righteousness, then c swings with Seal of Command. The wowsims rotation is
(1, 3). The tables of Analysis, Damage use (1, 1), a Seal change after each swing: 2.5% below (1, 3) in the model.

Mana (wowsims spell data): Seal of Righteousness rank 8 200, Seal of Command rank 5 210, Benediction x0.90.
Unsealed Wrath has no cost decrease (W29). Judgement 6% of base mana (91). Sanctified Judgement 3/3 returns 60% of
the base cost of the judged Seal. Holy Strike 20. Hammer of Wrath 425 x0.60.
Income: Reverence 2/2 (30% of Spirit regeneration in casts) 6.2 per sec, Blessing of Wisdom 8 per sec.
"""
import sys
import os; D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, sys.argv[1] if len(sys.argv) > 1 else os.path.join(D, "..", "damage"))
import damage_model as M
# Pure damage classes: wowsims Forever 895cd67f9, same pre-raid item pool for each spec (game start and Dire Maul
# content, models/wowsims-b2/matched_gear), wowsims preset enchants, the same consumables for each spec, Ret raid buffs,
# 2 min, 10,000 iterations. Fury 804.8, Combat Rogue 645.6, Hunter 799.6, Fire Mage 824.0, Demonology Warlock 845.6,
# Retribution 874.4. The values below put them on the scale of RET_SIM (x 906 / 874.4).
PURE_MATCHED = {"Warrior": 804.8, "Rogue": 645.6, "Hunter": 799.6, "Mage": 824.0, "Warlock": 845.6}
RET_MATCHED = 874.4
PURE = {k: v * 906 / RET_MATCHED for k, v in PURE_MATCHED.items()}
RET_SIM = 906                                                                          # wowsims master of 1 November, full buffs, 2 min (the anchor of Analysis, Damage)
from damage_model import (gear, auto_table, spec_table, vengeance, fury, arms, rogue, TIER_NAMES, CRIT_SPEC, DODGE,
                          EXECUTE, FIGHT, KINGS, MOTW, MIGHT, SHOUT, NORM_2H, SPEED_2H, DR, MISS)

B2 = dict(ds=5, is_=5, di=5, prec=1, ben=5, ij=2, conv=3, sanc=3, soc=1, sa=1, thws=3, veng=3, cotl=5)
BEN = 0.90
SOR_COST, SOC_COST, JUD_COST, HS_COST, HOW_COST = 200, 210, 91, 20, 425 * 0.60
REV_INCOME, WISDOM = 10.3 * 30 / 50, 8.0

def stats_b2(g, tal=B2):
    t = lambda k: tal.get(k, 0)
    st = (g["str"] + MOTW) * KINGS * (1 + 0.02 * t("ds"))
    ap = st * 2 + g["ap_items"] + MIGHT + SHOUT
    intel = (g["int"] + MOTW) * KINGS * (1 + 0.02 * t("di"))
    crit = g["crit"] + (MOTW * KINGS) / 20 / 100 + 0.02 * t("conv")
    return dict(ap=ap, sd=g["sd"] + 0.12 * t("cotl") * intel, int=intel, hit=min(g["hit"] + 0.01 * t("prec"), MISS), crit=crit,
                w=g["w2"], speed=SPEED_2H)

def retribution_b2(g, c1=False, bz=0, n=1, tal=B2, fight=FIGHT, detail=False, seal_mult=1.0, crusader=False, plan=(1, 3)):
    """c1: Holy Strike triggers your Seal (C1). bz: Burning Zeal ranks (C-R4, +10% critical damage bonus each).
    plan: (r, c), r swings with Seal of Righteousness, then c swings with Seal of Command. (1, 3) is the wowsims
    default rotation. plan=None: Seal of Command only (no copy is consumed). n is not used (kept for old calls).
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
    if plan is None:                                         # one Seal: Seal of Command, no copy is consumed
        sor_auto, soc_auto, share_sor, seals = 0.0, 1.0, 0.0, 1 / 30
    else:
        # A cycle of r + c swings: r with Seal of Righteousness, c with Seal of Command. The first swing with the
        # other Seal consumes the stored copies (3 at most). Seal of Righteousness: r active hits + min(r, 3) copies.
        # Seal of Command: c chances + min(c, 3) copy chances. The copies ignore the 1 sec ICD (wowsims 3989a1237).
        r, c = plan
        k = r + c
        sor_auto = (r + min(r, 3)) / k
        soc_auto = (c + min(c, 3)) / k
        share_sor = r / k                                    # part of the time with Seal of Righteousness active
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
    if crusader:     # Judgement of the Crusader: +161 Holy damage taken, x the spell coefficient of each hit
        cr = M.CRUSADER
        src["Seal of Command"] += soc_rate * 0.29 * cr * imp * V * (1 + c_seal * m)
        src["Holy Strike"] += hs_rate * 0.5 * 0.429 * cr * sa * V * f_hs
        src["Judgement"] += jud_rate * 0.429 * cr * imp * V * f_jud
        src["Seal of Righteousness"] += sor_rate * 0.12 * cr * imp * V * (1 + c_seal * m)
        src["Hammer of Wrath"] += how_rate * 0.429 * cr * V * f_how
    total = sum(src.values())
    # Mana each sec
    seal_cost = (SOR_COST + SOC_COST) / 2 if plan else SOC_COST
    spend = (seals * seal_cost * BEN * seal_mult + jud_rate * (JUD_COST * BEN - 0.20 * t("sanc") * seal_cost)
             + hs_rate * HS_COST * BEN + how_rate * HOW_COST * BEN)
    mana = dict(pool=1232 + 15 * s["int"], spend=spend, seals=seals)
    return (total, src, V, mana) if detail else total

def time_to_zero(mana, wisdom=True):
    net = mana["spend"] - REV_INCOME - (WISDOM if wisdom else 0)
    return None if net <= 0 else mana["pool"] / net

PLANS = ((1, 3), (1, 2), (1, 1), (2, 2), (3, 3), (3, 1))

def fight_dps(g, fight, wisdom=True, **kw):
    """Best average DPS in the fight: the Seal plan that the mana permits, else Seal of Command only after the mana
    is zero."""
    best = (0, None)
    one = retribution_b2(g, plan=None, fight=fight, **kw)
    for p in PLANS:
        d, _, _, mana = retribution_b2(g, plan=p, fight=fight, detail=True, **kw)
        z = time_to_zero(mana, wisdom)
        avg = d if z is None or z >= fight else (d * z + one * (fight - z)) / fight
        if avg > best[0]:
            best = (avg, p)
    return best

if __name__ == "__main__":
    g = gear(0)
    base, src, V, mana = retribution_b2(g, detail=True)
    print("## Fresh level 60, 2 min, plan (1, 1): a Seal change after each swing")
    print("  " + ", ".join(f"{k} {v:.0f}" for k, v in src.items()) + f". Total {base:.0f}. Vengeance +{V - 1:.1%}")
    print(f"  Mana: pool {mana['pool']:.0f}, spend {mana['spend']:.1f} per sec ({mana['seals']:.2f} Seals each sec), "
          f"income {REV_INCOME:.1f} + Wisdom {WISDOM:.0f}")
    for w in (True, False):
        z = time_to_zero(mana, w)
        print(f"  Mana zero {'with' if w else 'without'} Blessing of Wisdom: "
              f"{'never' if z is None else f'{int(z // 60)}:{int(z % 60):02d}'}")
    print("## Seal plans (r, c): r swings with Seal of Righteousness, then c with Seal of Command (W29)")
    top = retribution_b2(g, plan=(1, 3))
    for p in ((1, 3), (1, 2), (1, 1), (2, 2), (3, 3), (3, 1), None):
        d, _, _, mn = retribution_b2(g, plan=p, detail=True)
        z = time_to_zero(mn)
        print(f"  {p}: {d:.0f} ({d / top - 1:+.1%}), spend {mn['spend']:.1f}, mana zero "
              f"{'never' if z is None else f'{int(z // 60)}:{int(z % 60):02d}'}")
    print("## Proposals against the beta, same Seal plan (1, 1), by tier")
    print("  tier | beta | C1 | C-R4 2/2 | C1 + C-R4")
    for tier, name in enumerate(TIER_NAMES):
        h = gear(tier)
        b = retribution_b2(h)
        c = retribution_b2(h, c1=True); z = retribution_b2(h, bz=2); cz = retribution_b2(h, c1=True, bz=2)
        print(f"  {name} | {b:.0f} | {c / b - 1:+.1%} | {z / b - 1:+.1%} | {cz / b - 1:+.1%}")
    print("## Best plan in the fight with the mana (with Blessing of Wisdom): DPS (plan)")
    for fight in (120, 180, 300):
        row = []
        for tier in range(5):
            h = gear(tier)
            b, nb = fight_dps(h, fight)
            p, npp = fight_dps(h, fight, c1=True)
            row.append(f"{b:.0f} {nb} -> {p:.0f} {npp} ({p / b - 1:+.1%})")
        print(f"  {fight} sec: " + " | ".join(row))
    print("## Seal cost -20% on Unsealed Wrath (option for W29), with Blessing of Wisdom: mana zero, best DPS in the fight")
    for pl in ((1, 3), (1, 1), (3, 3)):
        _, _, _, mn = retribution_b2(g, plan=pl, detail=True, seal_mult=0.80)
        z = time_to_zero(mn)
        print(f"  {pl}: spend {mn['spend']:.1f}, mana zero {'never' if z is None else f'{int(z // 60)}:{int(z % 60):02d}'}")
    for fight in (120, 180, 300):
        a = fight_dps(g, fight)[0]; b = fight_dps(g, fight, seal_mult=0.80)[0]
        print(f"  {fight} sec, fresh level 60: {a:.0f} -> {b:.0f} ({b / a - 1:+.1%})")
    print(f"## Against the pure average (wowsims {RET_SIM} at fresh level 60, the increase of the model; Hunter, Mage and "
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
