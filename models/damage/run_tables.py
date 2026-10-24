"""All values of Analysis, Damage (proposals/analysis/damage.md). Run: python3 run_tables.py"""
import damage_model as M
from damage_model import gear, retribution, fury, arms, rogue, TIER_NAMES

# MythicSim (part 5): wowsims Forever, beta client 1.60.1.70425. Best spec of each pure damage class.
PURE = {"Warrior": 929, "Rogue": 702, "Hunter": 1175, "Mage": 860, "Warlock": 879}
RET_BETA_SIM = 847

def pct(a, b):
    return f"{a / b:.0%}"

# Mana of Retribution, build RB2 (Analysis, Mana, parts 3 and 5). Costs from wowsims Forever.
# Mana pool: 1,232 + 15 x Intellect (Classic formula: base 1,512, the first 20 Intellect give 1 mana each), with Mark
# of the Wild and Kings, from the Retribution gear of each tier (fresh level 60: 87 Intellect, 2,931 mana with buffs and Divine Intellect 2).
# Retribution gear has no mp5. Benediction 3/3 (C21): instant spells x0.90. Twist of Light: Seals x0.80.
# Holy Conduit (C8): Consecration (565) x0.60. Sanctified Judgement returns 60% of the base Seal cost x (2 - the cost
# multiplier): 210 x (2 - 0.72) x 0.6 = 161 (wowsims Forever). Judgement: 6% of base mana (91). Holy Strike: 20.
# Hammer of Wrath rank 3: 425 x0.60, in the execute phase. Income: Reverence 50% (C1) at 130 Spirit (10.3) and
# Blessing of Wisdom (8).
BEN, TOL = 0.90, 0.80

def ret_mana(tier, wisdom=True):
    """(mana pool, income, rotation cost, Hammer of Wrath cost, Consecration cost), all per sec except the pool."""
    intel = (gear(tier)["int"] + M.MOTW) * M.KINGS * (1 + 0.02 * M.RB2.get("di", 0))   # Divine Intellect
    pool = 1232 + 15 * intel
    income = 10.3 + (8 if wisdom else 0)
    seal = 210 * BEN * TOL
    rotation = seal / 10 + 91 * BEN / 8 - 210 * (2 - BEN * TOL) * 0.6 / 8 + 20 * BEN / 10
    return pool, income, rotation, 425 * 0.60 * BEN / 6, 565 * 0.60 * BEN / 8

def consecration_mana(tier, fight, dt=0.1):
    """Consecration on cooldown until the mana is zero, then only when the mana returns.
    Returns (time of zero mana or None, average DPS)."""
    g = gear(tier)
    base, full = retribution(g), retribution(g, extra="consecration")
    mana, income, rotation, how, cons = ret_mana(tier)
    t, dmg, zero = 0.0, 0.0, None
    while t < fight:
        rest = income - rotation - (how if t >= fight * (1 - M.EXECUTE) else 0)
        c = min(cons, max(0.0, mana / dt + rest))       # at zero mana: Consecration only from the mana that returns
        mana += (rest - c) * dt
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
    pool, inc, rot, how, _ = ret_mana(0)
    print(f"Mana: pool {pool:.0f}. Rotation {rot:.1f} per sec (Hammer of Wrath +{how:.1f} in the execute phase), income "
          f"{inc:.1f} with Blessing of Wisdom, {inc - 8:.1f} without")

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
    print(f"Consecration on cooldown: {cons:.0f} ({cons / P - 1:+.0%}). Exorcism: {exo:.0f} ({exo / P - 1:+.0%})")
    sh, shc = retribution(g, tal=M.SHOCK_RET), retribution(g, tal=M.SHOCK_RET, extra="consecration")
    _, sc8, _ = retribution(g, tal=M.SHOCK_RET, extra="consecration", detail=True)
    print(f"Shock-Retribution (Consecrated Ground, Holy row 5) with Consecration: {sh:.0f} -> {shc:.0f} "
          f"({shc / sh - 1:+.0%}). Consecrated Ground part of the increase: {sc8['Consecrated Ground'] / (shc - sh):.0%}")
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

    print("\n## Analysis, Builds, parts 4 and 5: Retribution builds (fresh level 60, 2 min)")
    for name, tal in M.RET_BUILDS:
        x, xc = retribution(g, tal=tal), retribution(g, tal=tal, extra="consecration")
        print(f"{name} | {x:.0f} ({xc:.0f} with Consecration) | {pct(x, P)} of RB2")
    sh, sh0 = retribution(g, tal=M.SHOCK_RET), retribution(g, tal=dict(M.SHOCK_RET, hsk=0))
    print(f"Shock-Retribution: {sh:.0f} ({pct(sh, P)} of RB2). No mana for Holy Shock: {sh0:.0f} ({pct(sh0, P)})")

    def ret_tank(front=True, dungeon=True, cons=False):
        """RB2 with Righteous Fury (x1.9 on Holy damage), pre-raid gear (Threat, part 1). dungeon: Blessing of Might only."""
        save = (M.KINGS, M.SHOUT, M.MOTW)
        if dungeon:
            M.KINGS, M.SHOUT, M.MOTW = 1.0, 0, 0
        tot, src_t, _ = retribution(gear(1), detail=True, front=front, extra="consecration" if cons else None)
        M.KINGS, M.SHOUT, M.MOTW = save
        return src_t["Auto attacks"] + 1.9 * (tot - src_t["Auto attacks"])
    PB2_TPS, PB2_CONS = 560, 652          # Analysis, Builds, part 3 (threat model)
    a, c = ret_tank(), ret_tank(cons=True)
    print(f"Retribution tank (front, dungeon buffs): {a:.0f} TPS ({pct(a, PB2_TPS)} of PB2), with Consecration "
          f"{c:.0f} ({pct(c, PB2_CONS)} of PB2 with Consecration). From behind with raid buffs: "
          f"{pct(ret_tank(False, False), PB2_TPS)}")
