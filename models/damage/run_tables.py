"""All values of Analysis, Damage (proposals/analysis/damage.md). Run: python3 run_tables.py"""
import damage_model as M
from damage_model import gear, retribution, fury, arms, rogue, TIER_NAMES

# MythicSim (part 5): wowsims Forever, beta client 1.60.1.70425. Best spec of each pure damage class.
PURE = {"Warrior": 929, "Rogue": 702, "Hunter": 1175, "Mage": 860, "Warlock": 879}
RET_BETA_SIM = 847

def pct(a, b):
    return f"{a / b:.0%}"

# Mana of Retribution with Consecration on cooldown (Analysis, Mana, parts 3 and 5). Holy Conduit (C8): Consecration
# x0.60. Twist of Light: Seals x0.80. Sanctified Judgement returns 126 mana. Hammer of Wrath rank 3: 295 mana (Classic
# value), x0.60, in the execute phase. Income: Reverence 50% at 130 Spirit (10.3), Blessing of Wisdom (8), mp5.
MANA = (2897, 3400, 3900, 4400, 4900)
MP5 = (3, 5, 7, 9, 12)

def consecration_mana(tier, fight, dt=0.1):
    """Consecration on cooldown until the mana is zero, then only when the mana returns.
    Returns (time of zero mana or None, average DPS)."""
    g = gear(tier)
    base, full = retribution(g), retribution(g, extra="consecration")
    cons = 565 * 0.60 / 8
    other = 210 * 0.80 / 10 + 91 / 8 - 126 / 8 + 20 / 10
    how = 295 * 0.60 / 6
    income = 10.3 + 8 + MP5[tier] / 5
    mana, t, dmg, zero = MANA[tier], 0.0, 0.0, None
    while t < fight:
        c = cons if mana > 0 else 0.0
        mana += (income - other - (how if t >= fight * (1 - M.EXECUTE) else 0) - c) * dt
        if mana <= 0 and zero is None:
            zero = t
        mana = max(mana, 0.0)
        dmg += (base + (full - base) * c / cons) * dt
        t += dt
    return zero, dmg / fight

def growth(f, **kw):
    v = [f(gear(t, **kw)) for t in range(5)]
    return [x / v[0] for x in v]

if __name__ == "__main__":
    g = gear(0)
    P = retribution(g)
    print("## Part 1: stats with talents and raid buffs")
    s = M.ret_stats(g)
    print(f"Attack Power {s['ap']:.0f}, spell damage {s['sd']:.0f} (Champion of the Light {s['sd'] - g['sd']:.0f}), "
          f"hit {s['hit']:.0%}, critical hit {s['crit']:.1%}")

    print("\n## Part 3: damage sources (all proposals, 2 min)")
    total, src, V = retribution(g, detail=True)
    for k, v in src.items():
        print(f"{k} | {v:.0f} | {v / total:.0%}")
    holy = (total - src["Auto attacks"]) / total
    print(f"Total {total:.0f}. Holy damage {holy:.0%}. Vengeance average +{V - 1:.1%}")
    gcd = (1 / 10 + 1 / 8 + 1 / 10) * M.GCD + M.EXECUTE / 6 * 1.0
    print(f"Global cooldown active: {gcd:.0%} (Holy Strike, Judgement, one Seal each 10 sec, Hammer of Wrath)")
    print(f"5 min fight: {retribution(g, fight=300) / P - 1:+.1%}")

    print("\n## Part 4: proposals against the beta")
    swap = retribution(g, "beta_swap")
    rows = (("Beta: a Seal change before each swing", "beta_swap", 1.2),
            ("Beta: Seal of Command only", "beta_soc", 1.2),
            ("C16, first version", "c16_first", 1.0),
            ("C16: your Seal and Echo, Sacred Arbiter +20%", "c16", 1.2),
            ("C16: your Seal and Echo, Sacred Arbiter +10%", "c16", 1.1),
            ("C16: your Seal and Echo, Sacred Arbiter +0%", "c16", 1.0),
            ("C16: only Seal of Command by chance, Sacred Arbiter +0%", "c16_soc", 1.0))
    for name, v, sa in rows:
        x = retribution(g, v, sa)
        print(f"{name} | {x:.0f} | {x / swap - 1:+.0%}")
    _, sb, _ = retribution(g, "beta_swap", detail=True)
    print(f"Holy Strike with C16 against the beta (Holy Strike, Seal of Command and Seal of Righteousness from it): "
          f"{(src['Seal of Command'] - sb['Seal of Command']) + (src['Seal of Righteousness'] - sb['Seal of Righteousness']):+.0f}")

    print("\n## Part 5: against MythicSim")
    gain = P / swap
    avg = sum(PURE.values()) / len(PURE)
    r = RET_BETA_SIM * gain
    first = RET_BETA_SIM * retribution(g, "c16_first", 1.0) / swap
    print(f"Retribution, all proposals: {r:.0f} ({pct(r, avg)} of the pure average {avg:.0f}, {pct(r, PURE['Warrior'])} "
          f"of Fury). C16 first version {first:.0f} ({pct(first, avg)}). Beta {pct(RET_BETA_SIM, avg)}")
    no_rogue = (avg * 5 - PURE["Rogue"]) / 4
    print(f"Without Combat Rogue: pure average {no_rogue:.0f}, Retribution {pct(r, no_rogue)}")
    print(f"Same gear: beta Retribution {swap:.0f}, Arms {arms(g):.0f}, Fury {fury(g):.0f}, Combat Rogue {rogue(g):.0f}. "
          f"Beta Retribution against Arms {swap / arms(g) - 1:+.0%} (MythicSim {847 / 800 - 1:+.0%})")

    print("\n## Part 6: increase from fresh level 60")
    R, R254 = growth(retribution), growth(retribution, sd_fixed=True)
    F, A, C = growth(fury), growth(arms), growth(rogue)
    RF, R254F, FF = growth(retribution, flat=True), growth(retribution, flat=True, sd_fixed=True), growth(fury, flat=True)
    start = r / PURE["Warrior"]
    for t, n in enumerate(TIER_NAMES):
        print(f"{n} | ×{R[t]:.2f} | ×{R254[t]:.2f} | ×{F[t]:.2f} | ×{A[t]:.2f} | ×{C[t]:.2f}")
    print("Retribution as a % of Fury (Classic steps, spell damage 254, flatter, flatter and 254):")
    for t, n in enumerate(TIER_NAMES):
        print(f"{n} | {start * R[t] / F[t]:.0%} | {start * R254[t] / F[t]:.0%} | {start * RF[t] / FF[t]:.0%} | "
              f"{start * R254F[t] / FF[t]:.0%}")
    sd = s["sd"]; wn = g["w2"] * 3.6 + s["ap"] / 14 * 3.3
    fixed = (src["Judgement"] * 186.5 / (186.5 + 0.429 * sd) + src["Seal of Righteousness"] * 67.5 / (67.5 + 0.12 * sd)
             + src["Hammer of Wrath"] * 498 / (498 + 0.429 * sd) + src["Holy Strike"] * 93 / (0.5 * wn + 93 + 0.2145 * sd))
    spell = (src["Judgement"] + src["Seal of Righteousness"] + src["Hammer of Wrath"]) - (fixed - src["Holy Strike"]
             * 93 / (0.5 * wn + 93 + 0.2145 * sd)) + src["Holy Strike"] * 0.2145 * sd / (0.5 * wn + 93 + 0.2145 * sd)
    wd = s["w"] * 3.6 + s["ap"] / 14 * 3.6
    spell += src["Seal of Command"] * 0.233 * sd / (0.805 * wd + 0.233 * sd)
    print(f"Shares: fixed base values {fixed / total:.0%}, spell damage {spell / total:.0%}, "
          f"weapon and Attack Power {1 - (fixed + spell) / total:.0%}")
    t4 = {k: retribution(gear(4), detail=True)[1][k] / src[k] for k in src}
    print("Increase of each source: " + ", ".join(f"{k} ×{v:.2f}" for k, v in t4.items()) + f". Fury ×{F[4]:.2f}")
    best = max(t4.values())
    print(f"A Retribution with only the best source: {best / F[4]:.0%} of the Fury increase")
    tests = (("Seal of Command 85% of weapon damage", dict(soc_w=0.85)), ("Holy Strike 100% of weapon damage",
             dict(hs_w=1.0)), ("Vengeance 5 stacks", dict(v_stacks=5)), ("Vindication +10% Attack Power", dict(ap_pct=0.10)))
    print("Talent tests (points against Fury in Naxxramas, same DPS at fresh level 60): " + ", ".join(
        f"{n} {100 * start * (growth(lambda h, d=d: retribution(h, **d))[4] - R[4]) / F[4]:+.1f}" for n, d in tests))
    print(f"In Naxxramas: Retribution {r * R[4] / (800 * A[4]):.0%} of Arms, {r * R[4] / (PURE['Rogue'] * C[4]):.0%} "
          f"of Combat Rogue (MythicSim values at fresh level 60)")
    shape = [(a - 1) / (A[4] - 1) for a in A]          # Hunter, Mage and Warlock: the shape of the Arms increase
    casters = PURE["Hunter"] + PURE["Mage"] + PURE["Warlock"]
    for o, RR in ((1.60, R), (1.75, R), (1.90, R), (1.75, R254)):
        row = []
        for t in range(5):
            pure = (PURE["Warrior"] * F[t] + PURE["Rogue"] * C[t] + casters * (1 + (o - 1) * shape[t])) / 5
            row.append(pct(r * RR[t], pure))
        print(f"Hunter, Mage and Warlock ×{o:.2f}{', spell damage 254' if RR is R254 else ''}: " + " | ".join(row))

    print("\n## Part 7: Judgement of the Crusader")
    c = retribution(g, crusader=True)
    print(f"+{c - P:.0f} ({c / P - 1:+.0%}). Naxxramas: {retribution(gear(4), crusader=True) / retribution(gear(4)) - 1:+.0%}")
    _, sc, _ = retribution(g, crusader=True, detail=True)
    print("By source: " + ", ".join(f"{k} {sc[k] - src[k]:+.1f}" for k in src))
    for name, coef, mult in (("Seal of Command", 0.29, 1.15 * 1.06), ("Seal of Righteousness", 0.12, 1.15 * 1.06),
                             ("Judgement", 0.429, 1.15 * 1.06), ("Holy Strike", 0.2145, 1.2 * 1.06),
                             ("Hammer of Wrath", 0.429, 1.0)):
        print(f"  {name}: {161 * coef * mult:.0f} for each hit")

    print("\n## Part 8: other results")
    g5 = dict(fight=300)
    base5 = retribution(g, **g5)
    def stat(**d):
        h = dict(g); h.update({k: g[k] + v for k, v in d.items()}); return retribution(h, **g5) - base5
    print(f"Stat values (5 min): spell damage {stat(sd=10) / 10:.2f}, Attack Power {stat(ap_items=10) / 10:.2f}, "
          f"Strength {stat(str=10) / 10:.2f}, 1% critical hit {stat(crit=0.01):.1f}, "
          f"1% hit {(retribution(dict(g, hit=0.04), **g5) - retribution(dict(g, hit=0.03), **g5)):.1f}")
    cons = retribution(g, extra="consecration")
    exo = retribution(g, extra="exorcism")
    print(f"Consecrated Ground with Consecration on cooldown: {cons:.0f} ({cons / P - 1:+.0%}). "
          f"Exorcism: {exo:.0f} ({exo / P - 1:+.0%})")
    _, sc8, _ = retribution(g, extra="consecration", detail=True)
    print(f"Consecration part of the increase: {sc8['Consecration'] / (cons - P):.0%}, "
          f"Consecrated Ground {sc8['Consecrated Ground'] / (cons - P):.0%}")
    for fight in (120, 180, 300):
        row = []
        for t in range(5):
            zero, avg = consecration_mana(t, fight)
            pure = (PURE["Warrior"] * F[t] + PURE["Rogue"] * C[t] + casters * (1 + 0.75 * shape[t])) / 5
            z = "none" if zero is None else f"{int(zero // 60)}:{int(zero % 60):02d}"
            row.append(f"zero {z}, {avg / retribution(gear(t)) - 1:+.0%}, {pct(r * avg / P, pure)}")
        print(f"Consecration on cooldown until the mana is zero, {fight} sec (mana zero, DPS increase, % of the pure "
              f"average with Hunter, Mage and Warlock x1.75): " + " | ".join(row))
    t3 = retribution(g, ths=1.03)
    print(f"Two-Handed Weapon Specialization: each 1% {(P - t3) / 3:.1f} DPS. At 3%: "
          f"{start * t3 / P:.0%} of Fury at fresh level 60, {start * t3 / P * growth(lambda h: retribution(h, ths=1.03))[4] / F[4]:.0%} in Naxxramas")
    print(f"Champion of the Light at 30%: {retribution(g, cotl=0.30) - P:+.0f}")
