# Damage model for Forever melee (level 60, one level 63 boss). Analysis, Damage (proposals/analysis/damage.md).
# A steady-state model, not a combat simulation: average damage per second (DPS), source by source.
# The inputs are those of Analysis, Damage, parts 1 and 2. The first calculation had no script. This file rebuilds
# it from the written inputs and the Forever spellbook and talents (wowforevertalents.com, build 1.60.1.70450).
# Where the inputs leave a value open, a comment gives the choice. No value is fitted to the first calculation.
#
# The other classes are not compared directly: Analysis, Damage, part 5 uses the MythicSim values. Fury, Arms and
# Combat Rogue are in the model only for the check with the same gear (part 5) and the increase with gear (part 6).

# ---------------------------------------------------------------- fight (part 2)
BOSS_ARMOR = 976                 # 3,731 after 5 Sunder Armor and Faerie Fire
DODGE = 0.065                    # from behind: no parry, no block
GLANCE, GLANCE_DMG = 0.40, 0.65  # auto attacks only
CRIT_AUTO, CRIT_SPEC = 0.048, 0.048  # critical hit decrease against a level 63 boss: 3% + 1.8%, all melee attacks (wowsims Forever)
MISS = 0.08                      # before hit; each 1% of hit removes 1% miss (wowsims Forever)
DW_MISS = 0.27                   # auto attacks with two weapons: 8% + 19%
FIGHT = 120.0
EXECUTE = 0.2                    # last 20% of the fight: Hammer of Wrath, Execute
GCD = 1.5
RAGE_SWING = 3.46                # normalized rage: 3.46 x weapon speed for each auto attack that lands, x2 if critical
                                 # (Warrior Compendium, Rage on Crit: rage = L + (m - 1) c, with c the critical hits of all swings)
RAGE_2H = 1.3                    # x1.3 for two-handed weapons (Threat, part 6)
OH_RAGE = 0.5                    # off hand: 1.73 x weapon speed, half of the main hand (Warrior Compendium, Rage on Crit),
                                 # before Dual Wield Specialization (+50%): Forever v2 rage rules (announced fix)
CRUSADER = 161                   # Judgement of the Crusader: Holy damage taken

def armor_dr(armor=BOSS_ARMOR, level=60):
    return armor / (armor + 400 + 85 * level)

DR = armor_dr()

def miss(hit, dw=False):
    return max(0.0, (DW_MISS if dw else MISS) - hit)

def auto_table(hit, crit, dw=False, dodge=DODGE):
    """Auto attacks: (chance to land, chance of a critical hit, expected damage factor)."""
    land = 1 - miss(hit, dw) - dodge
    c = min(max(0.0, crit - CRIT_AUTO), land - GLANCE)
    return land, c, GLANCE * GLANCE_DMG + c * 2 + (land - GLANCE - c)

def spec_table(hit, crit, dodge=DODGE, crit_mult=2.0):
    """Special attacks, Seals and Judgements: (chance to land, chance of a critical hit, damage factor).
    The critical hit is a separate roll on the hits that land (wowsims Forever)."""
    land = 1 - miss(hit) - dodge
    c = max(0.0, crit - CRIT_SPEC) * land
    return land, c, land + c * (crit_mult - 1)

def vengeance(crits_per_sec, per=0.03, stacks=3, dur=30.0, fight=FIGHT, dt=0.25):
    """Average Vengeance bonus over the fight: each critical hit adds a stack (maximum 3) and resets the 30 sec
    duration. A Markov chain in steps of 0.25 sec, from 0 stacks at the pull."""
    p = 1 - 2.718281828 ** (-crits_per_sec * dt)
    n_age = int(dur / dt)
    none = 1.0                                   # no stack
    ages = [[0.0] * n_age for _ in range(stacks)]   # ages[n - 1][a]: n stacks, a steps since the last critical hit
    total, steps = 0.0, int(fight / dt)
    for _ in range(steps):
        hit = [none * p] + [sum(ages[n]) * p for n in range(stacks)]
        expired = sum(ages[n][-1] for n in range(stacks)) * (1 - p)
        for n in range(stacks):
            ages[n] = [0.0] + [x * (1 - p) for x in ages[n][:-1]]
        for n in range(stacks + 1):
            ages[min(stacks, n + 1) - 1][0] += hit[n]
        none = none * (1 - p) + expired
        total += sum((n + 1) * sum(ages[n]) for n in range(stacks))
    return 1 + per * total / steps

# ---------------------------------------------------------------- gear (parts 1 and 6)
# Fresh level 60: a real profile (Analysis, Damage, part 1). Without talents and buffs.
FRESH = dict(str=283, agi=74, ap_items=770 - 2 * 283, crit=0.059, hit=0.05, sd=254, int=87)
GROWTH = 0.175                   # each tier: about 15-20% more Attack Power, critical hit and spell damage from gear
TIER_NAMES = ("Fresh level 60", "Pre-raid best in slot", "Molten Core", "Blackwing Lair", "Naxxramas")
GEAR_HIT = (0.05, 0.06, 0.07, 0.08, 0.09)
TWO_HAND = (53.9, 56, 63, 66, 75)     # damage per sec, Classic steps. Fresh: Stormcarver, 155-233, 3.6 sec
MAIN_HAND = (42, 47, 52, 57, 64)      # one-handed: 42 and 40 at fresh level 60, 64 and 60 in Naxxramas
OFF_HAND = (40, 44, 49, 54, 60)
SPEED_2H, SPEED_1H = 3.6, 2.6

# Raid buffs: Blessing of Kings (+10% stats), Blessing of Might (133), Battle Shout (193), Mark of the Wild (+12).
KINGS, MIGHT, SHOUT, MOTW = 1.10, 133, 193, 12

def gear(tier=0, flat=False, sd_fixed=False):
    """Gear stats of a tier. flat: from Molten Core, the gear increases at half the rate (Threat, part 3).
    sd_fixed: the spell damage on Paladin items stays at the fresh value (254)."""
    if flat and tier >= 2:
        f = (1 + GROWTH) * (1 + GROWTH / 2) ** (tier - 1)
        half = lambda t: t[1] + (t[tier] - t[1]) / 2
        w2, mh, oh = half(TWO_HAND), half(MAIN_HAND), half(OFF_HAND)
    else:
        f = (1 + GROWTH) ** tier
        w2, mh, oh = TWO_HAND[tier], MAIN_HAND[tier], OFF_HAND[tier]
    g = {k: v * f for k, v in FRESH.items()}
    g["hit"] = GEAR_HIT[tier]
    if sd_fixed: g["sd"] = FRESH["sd"]
    g.update(w2=w2, mh=mh, oh=oh)
    return g

# ---------------------------------------------------------------- Retribution (parts 1-4, 7, 8)
# Build 12/8/31 (RB2). Conviction +5% critical hit. Precision +3% hit. Two-Handed Weapon Specialization x1.06.
# Improved Seals x1.15 (Seals and Judgements). Vindication 5/5 (C-P3): +5% Attack Power, full uptime on a boss.
THWS, IMP_SEALS = 1.06, 1.15
NORM_2H = 3.3

# Talents (points) of the Retribution builds of Analysis, Builds, part 4. Only the talents with a raid damage effect.
# "is" Improved Seals, "cg" Consecrated Ground, "di" Divine Intellect, "hsk" Holy Shock, "prec" Precision,
# "sj" Swift Judgement, "conv" Conviction, "ij" Improved Judgement, "vind" Vindication, "soc" Seal of Command,
# "sa" Sacred Arbiter, "thws" Two-Handed Weapon Specialization, "veng" Vengeance, "cotl" Champion of the Light,
# "iol" Instrument of Law, "tol" Twist of Light, "hp" Holy Power, "bz" Burning Zeal (C-R4), "mfm" Measure for Measure (C-R5).
RB2 = dict(is_=3, di=2, prec=3, conv=5, ij=2, vind=5, soc=1, sa=1, thws=3, veng=3, cotl=3, iol=2, tol=1)
RB1 = dict(RB2, di=0)                                                     # Pursuit of Justice
RB3 = dict(RB2, is_=0, di=0, sj=1)                                        # 0/19/32: no Holy points
RB4 = dict(RB2, di=0)                                                     # Repentance, Eye for an Eye
RB5 = dict(RB2, is_=0, di=0, ij=0, vind=0, cotl=0, iol=0, tol=0, sj=1)    # 0/26/25
SHOCK_RET = dict(RB2, prec=0, vind=3, iol=0, tol=0, cotl=0, di=5, hsk=1, hp=5)   # 26/0/25: Holy Power (Holy row 5, M-H3)
RET_BUILDS = (("RB1", RB1), ("RB2", RB2), ("RB3", RB3), ("RB4", RB4), ("RB5", RB5))

def ret_stats(g, cotl=None, ap_pct=None, str_pct=0.0, tal=RB2):
    t = lambda k: tal.get(k, 0)
    cotl = 0.20 * t("cotl") if cotl is None else cotl
    ap_pct = 0.01 * t("vind") if ap_pct is None else ap_pct     # Vindication: +1-5% Attack Power
    st = (g["str"] + MOTW) * KINGS * (1 + str_pct)
    ap = (st * 2 + g["ap_items"] + MIGHT + SHOUT) * (1 + ap_pct)
    intel = (g["int"] + MOTW) * KINGS * (1 + 0.02 * t("di"))
    crit = g["crit"] + (MOTW * KINGS) / 20 / 100 + 0.01 * t("conv")  # gear (with its Agility), Mark of the Wild, Conviction
    return dict(ap=ap, sd=g["sd"] + cotl * intel, hit=min(g["hit"] + 0.01 * t("prec"), MISS), crit=crit, w=g["w2"],
                speed=SPEED_2H)

def retribution(g, version="c16", sa=None, crusader=False, ths=None, fight=FIGHT, detail=False, extra=None,
                 soc_w=0.70, hs_w=0.5, v_stacks=3, tal=RB2, front=False, **kw):
    """version: "c16" (Holy Strike triggers your Seal and Echo, C-R2 keeps both Seals active), "c16_first" (Holy Strike
    always triggers Seal of Command), "c16_soc" (Holy Strike triggers Seal of Command by chance only),
    "beta_swap" (a Seal change before each swing), "beta_soc" (Seal of Command only).
    A build with no Twist of Light has no Echo: "c16" then works as "c16_soc".
    sa: Sacred Arbiter bonus on Holy Strike. extra: "consecration" (Consecration on cooldown) or "exorcism".
    soc_w, hs_w, v_stacks: weapon damage of Seal of Command and Holy Strike, Vengeance stacks (talent tests).
    tal: the talents (RB2 by default). front: attacks from the front (14% parry, as Threat, part 6)."""
    t = lambda k: tal.get(k, 0)
    if version == "c16" and not t("tol"):
        version = "c16_soc"
    if version.startswith("beta"):
        kw = dict(dict(str_pct=0.10, ap_pct=0.0), **kw)                 # beta: Divine Strength 5/5 (+10% Strength), no Vindication
    sa = (1 + 0.20 * t("sa")) if sa is None else sa
    ths = (1 + 0.02 * t("thws")) if ths is None else ths
    imp = 1 + 0.05 * t("is_")
    s = ret_stats(g, tal=tal, **kw)
    sd = s["sd"] + (CRUSADER if crusader else 0)
    sd_soc = 0.233 * s["sd"] + (0.29 * imp * CRUSADER if crusader else 0)   # 29% x Improved Seals for Crusader
    wd = s["w"] * s["speed"] + s["ap"] / 14 * s["speed"]
    wn = s["w"] * s["speed"] + s["ap"] / 14 * NORM_2H
    dodge = DODGE + (0.14 if front else 0.0)
    land_a, crit_a, f_auto = auto_table(s["hit"], s["crit"], dodge=dodge)
    land, crit_s, f_spec = spec_table(s["hit"], s["crit"], dodge=dodge)
    # Holy Power (Holy row 5, M-H3): +3% critical hit for each rank on Holy Strike and Holy Shock, +1% on the other
    # spells (Judgement, Hammer of Wrath, Exorcism, Consecration). Not on Seals.
    hp = t("hp")
    # Burning Zeal (C-R4): +10% critical damage bonus for each rank on Seals, Judgements and Holy Strike.
    bz = 1 + 0.04 * t("bz")   # Burning Zeal: 5 ranks, +4% each
    _, crit_j, f_jud = spec_table(s["hit"], s["crit"] + 0.01 * hp, dodge=0.0, crit_mult=1 + bz)   # Judgement: no dodge
    _, crit_hs, f_hs = spec_table(s["hit"], s["crit"] + 0.03 * hp, dodge=dodge, crit_mult=1 + bz)
    _, crit_how, f_how = spec_table(s["hit"], s["crit"] + 0.01 * hp, dodge=dodge)
    c_seal = max(0.0, s["crit"] - CRIT_SPEC)                             # Seals: a separate roll, cannot miss
    c_spell, c_hsk = c_seal + 0.01 * hp, c_seal + 0.03 * hp              # spell critical hits (x1.5)
    how_rate = EXECUTE / 6
    how_cast = 1.0 - 0.5 * t("iol")                                      # Instrument of Law: -1 sec cast time
    autos = (1 - how_rate * how_cast) / s["speed"]                       # a cast stops the auto attacks
    hs_rate = 1 / 10
    # Measure for Measure (C-R5): each dodge or parry of the target (auto attacks and Holy Strike) reduces the remaining
    # Judgement cooldown by 1 sec for each rank. Average cooldown: cd / (1 + rank x dodges per sec).
    jud_cd = (10 - t("ij")) / (1 + t("mfm") * (autos + hs_rate) * dodge)
    jud_rate = 1 / jud_cd + t("sj") / 60                                 # Improved Judgement 2/2: one each 8 sec
    soc_chance = 7 / 60 * s["speed"] * t("soc")                          # 7 procs each minute
    hs_soc = {"c16": soc_chance, "c16_first": t("soc"), "c16_soc": soc_chance}.get(version, 0.0)
    hs_sor = version == "c16"
    auto_sor = version in ("c16", "c16_first", "c16_soc", "beta_swap")
    soc_rate = (autos * land_a * soc_chance + hs_rate * land * hs_soc) * land     # the proc uses the hit table too
    sor_rate = autos * land_a * auto_sor + hs_rate * land * hs_sor
    if not t("tol") and version != "beta_swap":
        sor_rate = 0.0                                                   # no Echo: only Seal of Command is active
    hsk_rate = t("hsk") / 10                                             # Holy Shock: 10 sec cooldown
    # Vengeance: critical hits of auto attacks, Seals, Holy Strike, Judgement, Hammer of Wrath and Holy Shock.
    cps = (autos * crit_a + hs_rate * crit_hs + how_rate * crit_how + jud_rate * crit_j + (soc_rate + sor_rate) * c_seal
           + hsk_rate * c_hsk)
    V = vengeance(cps, per=0.01 * t("veng"), stacks=v_stacks, fight=fight)
    src = {}
    src["Auto attacks"] = wd * (1 - DR) * ths * V * f_auto * autos
    src["Seal of Command"] = soc_rate * (soc_w * imp * wd + sd_soc) * ths * V * (1 + c_seal * bz)
    # Holy Strike: hs_w x (normalized weapon damage + 93 + 42.9%). Judgement of Righteousness rank 8: 170-187 + 42.9%.
    # Seal of Righteousness rank 8: 67.5 + 12% with a two-handed weapon, critical hit x2 with a separate roll.
    src["Holy Strike"] = hs_rate * hs_w * (wn + 93 + 0.429 * sd) * sa * ths * V * f_hs
    src["Judgement"] = jud_rate * (178.2 + 0.429 * sd) * imp * ths * V * f_jud
    src["Seal of Righteousness"] = sor_rate * (67.5 + 0.12 * sd) * imp * ths * V * (1 + c_seal * bz)
    src["Hammer of Wrath"] = how_rate * (498 + 0.429 * sd) * V * f_how
    if hsk_rate:   # rank 4: 334-362 Holy damage + 42.9%, spell (critical hit x1.5). The build has 18% spell hit: no miss
        src["Holy Shock"] = hsk_rate * (348 + 0.429 * sd) * V * (1 + 0.5 * c_hsk)
    if extra == "exorcism":   # rank 6: 475-529 Holy damage, 15 sec cooldown, spell (critical hit x1.5)
        src["Exorcism"] = (502 + 0.429 * sd) * V * (1 + 0.5 * c_spell) / 15
    if extra == "consecration":   # Consecrated Ground: +5% Holy damage on the target for each point. 15% of the ticks miss.
        # Forever rank 5 (wowsims Forever, spell 1280349): 8 ticks of 12 + 27 Holy damage (the 27 on the first
        # 4 enemies), 4.2% of spell damage for each tick. Ticks can be critical hits (x1.5, beta test). They are
        # periodic: no Vengeance stack.
        cg = 0.05 * t("cg")
        holy = sum(v for k, v in src.items() if k != "Auto attacks")
        src["Consecration"] = (312 + 0.336 * sd) * 0.85 * V * (1 + 0.5 * c_spell) * (1 + cg) / 8
        if cg:
            src["Consecrated Ground"] = holy * cg
    total = sum(src.values())
    return (total, src, V) if detail else total

# ---------------------------------------------------------------- Warriors (parts 5 and 6)
# Forever spellbook: Bloodthirst rank 4 (45% of Attack Power + 48, 30 rage, 6 sec), Mortal Strike rank 4 (weapon
# damage + 160, 30 rage, 6 sec), Whirlwind (weapon damage, both weapons, 25 rage, 10 sec), Heroic Strike rank 9
# (+157 damage, 15 rage), Slam rank 5 (weapon damage + 87, 15 rage, 18 sec), Execute rank 5 (600 + 15 for each
# extra rage, 15 rage), Overpower rank 4 (weapon damage + 35, 5 rage, 5 sec, after a dodge).
# Rage: Forever v2 rules: critical hits +100% rage (beta notes, 2 October), off hand +50% with Dual Wield
# Specialization (hotfix after 2 October). Bloodthirst and Whirlwind use 7.2 rage each sec: 6.5 at fresh level 60, 7.3 in Naxxramas.
# Talents: Cruelty 5/5 (+5% critical hit), Unbridled Wrath 5/5 (60%: +1 rage for each hit), Improved Heroic Strike
# 3/3 (-3 rage), Anger Management (1 rage each 3 sec), Deep Wounds 3/3 (60% of the average weapon damage over 12 sec
# after a critical hit), Impale 2/2 (+20% critical hit damage of abilities).
# Fury: Dual Wield Specialization 5/5 (+25% off-hand damage, +50% off-hand rage, no hit), Furious Precision 3/3 (+10%
# off-hand hit), Raging Blows (Whirlwind -3 rage), Improved Execute 2/2 (-5 rage), Flurry 5/5 (+25% attack speed for 3 swings after a critical hit), Death Wish (+20% physical damage,
# 30 sec, 3 min cooldown: one use in a 2 min fight), Berserker Stance (+3% critical hit).
# Arms: Two-Handed Weapon Specialization 3/3 (+3%), Weaponmaster 5/5 (axe: +5% critical hit), Improved Slam 2/2
# (no swing reset, -3 sec cooldown), Battle Stance. As the wowsims Forever Arms build: Improved Rend 3/3 (+35%),
# Spearing Strike (40% normalized weapon damage, 15 rage, 20 sec), Bloodthrill 5/5 (20% of main-hand swings and
# Heroic Strikes on a target with Rend open Overpower). Rend rank 7: 7 ticks of 21 + 2% of Attack Power, 10 rage,
# 21 sec, a bleed (no armor).
# Not in the model: Recklessness, Sweeping Strikes, Hamstring.

def warrior_stats(g, crit_bonus):
    st = (g["str"] + MOTW) * KINGS
    ap = st * 2 + g["ap_items"] + MIGHT + SHOUT
    return ap, g["crit"] + (MOTW * KINGS) / 20 / 100 + 0.05 + crit_bonus   # Cruelty

def spend(rage, prio):
    """Rage in priority order. prio: (name, rage for each use, maximum uses each sec). Returns uses each sec."""
    out = {}
    for name, cost, cap in prio:
        out[name] = max(0.0, min(cap, rage / cost))
        rage -= out[name] * cost
    return out

def execute_dps(rage, cost=15):
    """Execute phase: all rage to Execute (600 damage + 15 for each extra rage), one each global cooldown."""
    return min(1 / GCD, rage / cost) * 600 + max(0.0, rage - cost / GCD) * 15

BLOODRAGE = 20 / 60              # Bloodrage: 20 rage each minute

def fury(g, detail=False):
    ap, crit = warrior_stats(g, 0.03)                                   # Berserker Stance
    hit = g["hit"]
    mh = g["mh"] * SPEED_1H + ap / 14 * SPEED_1H
    oh = (g["oh"] * SPEED_1H + ap / 14 * SPEED_1H) * 0.5 * 1.25        # off hand: 50% damage, +25%
    norm = lambda w: w * SPEED_1H + ap / 14 * 2.4
    land_m, crit_m, f_m = auto_table(hit, crit, dw=True)
    land_o, crit_o, f_o = auto_table(hit + 0.10, crit, dw=True)        # Furious Precision
    land, crit_s, f_spec = spec_table(hit, crit, crit_mult=2.2)       # Impale
    flurry = 1 - (1 - (crit_m + crit_o) / 2) ** 3
    rate = (1 + 0.25 * flurry) / SPEED_1H
    phys = (1 - DR) * (1 + 0.20 * 30 / FIGHT)                           # Death Wish: one use
    mh_rage = RAGE_SWING * SPEED_1H * (land_m + crit_m) + 0.6 * land_m
    oh_rage = RAGE_SWING * SPEED_1H * OH_RAGE * 1.5 * (land_o + crit_o) + 0.6 * land_o
    rage = rate * (mh_rage + oh_rage) + 1 / 3 + BLOODRAGE
    use = spend(rage, (("Bloodthirst", 30, 1 / 6), ("Whirlwind", 25 - 3, 1 / 10), ("Heroic Strike", 12 + mh_rage, rate)))
    hs = use["Heroic Strike"] / rate
    src = {}
    src["Main hand"] = mh * f_m * rate * (1 - hs) * phys
    src["Off hand"] = oh * f_o * rate * phys
    src["Heroic Strike"] = (mh + 157) * f_spec * use["Heroic Strike"] * phys
    src["Bloodthirst"] = (0.45 * ap + 48) * f_spec * use["Bloodthirst"] * phys
    src["Whirlwind"] = (norm(g["mh"]) + norm(g["oh"]) * 0.5 * 1.25) * f_spec * use["Whirlwind"] * phys
    crits = rate * (land_m * crit_m * (1 - hs) + land_o * crit_o) + sum(use.values()) * crit_s
    src["Deep Wounds"] = 0.6 * mh / 12 * (1 - 2.718281828 ** (-crits * 12)) * phys / (1 - DR)   # a bleed: no armor
    for k in ("Heroic Strike", "Bloodthirst", "Whirlwind"):
        src[k] *= 1 - EXECUTE
    src["Main hand"] += mh * f_m * rate * hs * phys * EXECUTE           # no Heroic Strike in the Execute phase
    src["Execute"] = execute_dps(rage, 15 - 5) * f_spec * phys * EXECUTE
    total = sum(src.values())
    return (total, src) if detail else total

def arms(g, detail=False):
    ap, crit = warrior_stats(g, 0.05)                                   # Weaponmaster (axe)
    hit = g["hit"]
    sp = SPEED_2H
    wd = g["w2"] * sp + ap / 14 * sp
    wn = g["w2"] * sp + ap / 14 * NORM_2H
    land_a, crit_a, f_a = auto_table(hit, crit)
    land, crit_s, f_spec = spec_table(hit, crit, crit_mult=2.2)       # Impale
    _, crit_op, f_op = spec_table(hit, crit + 0.5, crit_mult=2.2)     # Improved Overpower
    phys = (1 - DR) * 1.03                                              # Two-Handed Weapon Specialization 3/3
    rate = 1 / sp
    swing_rage = RAGE_SWING * RAGE_2H * sp * (land_a + crit_a) + 0.6 * land_a
    rage = rate * swing_rage + 1 / 3 + BLOODRAGE
    # Overpower after a dodge, or after a Bloodthrill proc (20% of main-hand swings and Heroic Strikes)
    op_cap = min(1 / 5, (rate + 1 / 6 + 1 / 15 + 1 / 20) * DODGE + rate * land_a * 0.20)
    use = spend(rage, (("Rend", 10, 1 / 21), ("Overpower", 5, op_cap), ("Mortal Strike", 30, 1 / 6),
                       ("Spearing Strike", 15, 1 / 20), ("Slam", 15, 1 / 15), ("Heroic Strike", 12 + swing_rage, rate)))
    hs = use["Heroic Strike"] / rate
    src = {}
    src["Auto attacks"] = wd * f_a * rate * (1 - hs) * phys
    src["Heroic Strike"] = (wd + 157) * f_spec * use["Heroic Strike"] * phys
    src["Mortal Strike"] = (wn + 160) * f_spec * use["Mortal Strike"] * phys
    src["Slam"] = (wd + 87) * f_spec * use["Slam"] * phys
    src["Overpower"] = (wn + 35) * f_op * use["Overpower"] * phys
    src["Spearing Strike"] = 0.40 * wn * f_spec * use["Spearing Strike"] * phys
    src["Rend"] = 7 * (21 + 0.02 * ap) * 1.35 * land * use["Rend"] * 1.03            # a bleed: no armor
    crits = (rate * land_a * crit_a * (1 - hs) + (use["Heroic Strike"] + use["Mortal Strike"] + use["Slam"]
             + use["Spearing Strike"]) * crit_s + use["Overpower"] * crit_op)
    src["Deep Wounds"] = 0.6 * wd / 12 * (1 - 2.718281828 ** (-crits * 12)) * 1.03
    for k in ("Heroic Strike", "Mortal Strike", "Slam", "Overpower", "Spearing Strike", "Rend"):
        src[k] *= 1 - EXECUTE
    src["Auto attacks"] += wd * f_a * rate * hs * phys * EXECUTE
    src["Execute"] = execute_dps(rage) * f_spec * phys * EXECUTE
    total = sum(src.values())
    return (total, src) if detail else total

# ---------------------------------------------------------------- Combat Rogue (part 6)
# Forever spellbook: Sinister Strike rank 8 (weapon damage + 68, 45 energy), Eviscerate rank 8 (5 combo points:
# 803-899, 35 energy, increased by Attack Power), Slice and Dice rank 2 (+30% attack speed, 21 sec with 5 combo
# points, 25 energy). Talents: Malice 5/5 (+5% critical hit), Ruthlessness 3/3 (60%: +1 combo point), Improved Slice
# and Dice 3/3 (+45% duration), Relentless Strikes (20% for each combo point: 25 energy), Lethality 5/5 (Sinister
# Strike critical hit +20%), Improved Sinister Strike 2/2 (-5 energy), Precision 3/3 (+3% hit), Dual Wield
# Specialization 5/5, Blade Flurry (+20% attack speed, 15 sec: one use), Hack and Slash 5/5 (sword: 5% extra
# attack), Weapon Expertise 2/2 (-2% dodge), Aggression 3/3 (+6% Sinister Strike and Eviscerate), Adrenaline Rush
# (+100% energy, 15 sec: one use), Improved Eviscerate 3/3 (+20%), Flawless Execution (Eviscerate -10 energy).
# Not known: the Attack Power part of Eviscerate (15% at 5 combo points, assumed). Poisons are not in the model.

def rogue(g, detail=False):
    st, agi = (g["str"] + MOTW) * KINGS, (g["agi"] + MOTW) * KINGS
    ap = st + agi + g["ap_items"] + MIGHT + SHOUT
    crit = g["crit"] + (MOTW * KINGS) / 20 / 100 + 0.05
    hit = g["hit"] + 0.03
    dodge = DODGE - 0.02
    mh = g["mh"] * SPEED_1H + ap / 14 * SPEED_1H
    oh = (g["oh"] * SPEED_1H + ap / 14 * SPEED_1H) * 0.5 * 1.25
    land_m, crit_m, f_m = auto_table(hit, crit, dw=True, dodge=dodge)
    land, crit_s, f_spec = spec_table(hit, crit, dodge=dodge)
    _, _, f_ss = spec_table(hit, crit, dodge=dodge, crit_mult=2.2)
    haste = 1.30 * (1 + 0.20 * 15 / FIGHT)                               # Slice and Dice, Blade Flurry
    rate = haste / SPEED_1H * 1.05                                       # Hack and Slash: 5% extra attacks
    energy = 10 * (1 + 15 / FIGHT)                                       # Adrenaline Rush
    cp_per_ss = land
    cps_needed = 5 - 0.6                                                 # Ruthlessness
    ss_per_fin = cps_needed / cp_per_ss
    fin_cost = 35 - 10 - 25                                              # Flawless Execution, Relentless Strikes
    cycle = ss_per_fin * 40 + fin_cost * land
    cycles = energy / cycle
    snd_rate = 1 / (21 * 1.45)
    evis_rate = max(0.0, cycles - snd_rate)
    src = {}
    src["Main hand"] = mh * f_m * rate * (1 - DR)
    src["Off hand"] = oh * f_m * rate * (1 - DR)
    src["Sinister Strike"] = (mh + 68) * 1.06 * f_ss * cycles * ss_per_fin * (1 - DR)
    src["Eviscerate"] = (851 + 0.15 * ap) * 1.06 * 1.20 * f_spec * evis_rate * (1 - DR)
    total = sum(src.values())
    return (total, src) if detail else total
