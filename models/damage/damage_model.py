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
CRIT_AUTO, CRIT_SPEC = 0.048, 0.03   # critical hit decrease against a level 63 boss (Classic 1.12 rule)
MISS = 0.09                      # before hit; the first 1% of hit has no effect, thus 8% hit gives 1% miss
DW_MISS = 0.28                   # auto attacks with two weapons
FIGHT = 120.0
EXECUTE = 0.2                    # last 20% of the fight: Hammer of Wrath, Execute
GCD = 1.5
RAGE_SWING = 3.46                # normalized rage: 3.46 x weapon speed for each auto attack that lands, x2 if critical
RAGE_2H = 1.3                    # x1.3 for two-handed weapons (Threat, part 6)
OH_RAGE = 0.5                    # off-hand rage (not known in Forever: half, as in Classic)
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
    """Special attacks, Seals and Judgements: (chance to land, chance of a critical hit, damage factor)."""
    land = 1 - miss(hit) - dodge
    c = min(max(0.0, crit - CRIT_SPEC), land)
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
# Build 12/7/32 (RB2) of version 1: Divine Strength 5/5 (+10% Strength), no Vindication. Conviction +5% critical hit.
# Precision +3% hit. Two-Handed Weapon Specialization x1.06. Improved Seals x1.15 (Seals and Judgements).
THWS, IMP_SEALS = 1.06, 1.15
NORM_2H = 3.3

def ret_stats(g, cotl=0.60, ap_pct=0.0, str_pct=0.10):
    st = (g["str"] + MOTW) * KINGS * (1 + str_pct)
    ap = (st * 2 + g["ap_items"] + MIGHT + SHOUT) * (1 + ap_pct)
    intel = (g["int"] + MOTW) * KINGS
    agi = (g["agi"] + MOTW) * KINGS
    crit = g["crit"] + (MOTW * KINGS) / 20 / 100 + 0.05          # gear (with its Agility), Mark of the Wild, Conviction
    return dict(ap=ap, sd=g["sd"] + cotl * intel, hit=min(g["hit"] + 0.03, MISS), crit=crit, w=g["w2"],
                speed=SPEED_2H)

def retribution(g, version="c16", sa=1.20, crusader=False, ths=THWS, fight=FIGHT, detail=False, extra=None,
                 soc_w=0.70, hs_w=0.5, v_stacks=3, **kw):
    """version: "c16" (Holy Strike triggers your Seal and Echo, C17 keeps both Seals active), "c16_first" (Holy Strike
    always triggers Seal of Command), "c16_soc" (Holy Strike triggers Seal of Command by chance only),
    "beta_swap" (a Seal change before each swing), "beta_soc" (Seal of Command only).
    sa: Sacred Arbiter bonus on Holy Strike. extra: "consecration" (Consecrated Ground) or "exorcism".
    soc_w, hs_w, v_stacks: weapon damage of Seal of Command and Holy Strike, Vengeance stacks (talent tests)."""
    s = ret_stats(g, **kw)
    sd = s["sd"] + (CRUSADER if crusader else 0)
    sd_soc = 0.233 * s["sd"] + (0.29 * IMP_SEALS * CRUSADER if crusader else 0)   # 29% x Improved Seals for Crusader
    wd = s["w"] * s["speed"] + s["ap"] / 14 * s["speed"]
    wn = s["w"] * s["speed"] + s["ap"] / 14 * NORM_2H
    land_a, crit_a, f_auto = auto_table(s["hit"], s["crit"])
    land, crit_s, f_spec = spec_table(s["hit"], s["crit"])
    autos, hs_rate, jud_rate = 1 / s["speed"], 1 / 10, 1 / 8           # Improved Judgement 2/2: one each 8 sec
    how_rate = EXECUTE / 6
    soc_chance = 7 / 60 * s["speed"]                                     # 7 procs each minute
    hs_soc = {"c16": soc_chance, "c16_first": 1.0, "c16_soc": soc_chance}.get(version, 0.0)
    hs_sor = version == "c16"
    auto_sor = version in ("c16", "c16_first", "c16_soc", "beta_swap")
    soc_rate = (autos * land_a * soc_chance + hs_rate * land * hs_soc) * land     # the proc uses the hit table too
    sor_rate = autos * land_a * auto_sor + hs_rate * land * hs_sor
    # Vengeance: critical hits of auto attacks, Seal of Command, Holy Strike, Judgement and Hammer of Wrath.
    # Seal of Righteousness cannot be a critical hit.
    cps = autos * crit_a + (hs_rate + jud_rate + how_rate) * crit_s + soc_rate * max(0, s["crit"] - CRIT_SPEC)
    V = vengeance(cps, stacks=v_stacks, fight=fight)
    src = {}
    src["Auto attacks"] = wd * (1 - DR) * ths * V * f_auto * autos
    src["Seal of Command"] = soc_rate * (soc_w * IMP_SEALS * wd + sd_soc) * ths * V * (1 + crit_s)
    src["Holy Strike"] = hs_rate * (hs_w * wn + 93 + 0.2145 * sd) * sa * ths * V * f_spec
    src["Judgement"] = jud_rate * (186.5 + 0.429 * sd) * IMP_SEALS * ths * V * f_spec
    src["Seal of Righteousness"] = sor_rate * (67.5 + 0.12 * sd) * IMP_SEALS * ths * V
    src["Hammer of Wrath"] = how_rate * (498 + 0.429 * sd) * V * f_spec
    if extra == "exorcism":   # rank 6: 475-529 Holy damage, 15 sec cooldown, spell (critical hit x1.5)
        src["Exorcism"] = (502 + 0.429 * sd) * V * (1 + 0.5 * crit_s) / 15
    if extra == "consecration":   # Consecrated Ground: +10% Holy damage on the target. 15% of the ticks miss.
        holy = sum(v for k, v in src.items() if k != "Auto attacks")
        src["Consecration"] = (384 + 0.336 * sd) * 0.85 * V * 1.1 / 8
        src["Consecrated Ground"] = holy * 0.10
    total = sum(src.values())
    return (total, src, V) if detail else total

# ---------------------------------------------------------------- Warriors (parts 5 and 6)
# Forever spellbook: Bloodthirst rank 4 (45% of Attack Power + 48, 30 rage, 6 sec), Mortal Strike rank 4 (weapon
# damage + 160, 30 rage, 6 sec), Whirlwind (weapon damage, both weapons, 25 rage, 10 sec), Heroic Strike rank 9
# (+157 damage, 15 rage), Slam rank 5 (weapon damage + 87, 15 rage, 18 sec), Execute rank 5 (600 + 15 for each
# extra rage, 15 rage), Overpower rank 4 (weapon damage + 35, 5 rage, 5 sec, after a dodge).
# Talents: Cruelty 5/5 (+5% critical hit), Unbridled Wrath 5/5 (60%: +1 rage for each hit), Improved Heroic Strike
# 3/3 (-3 rage), Anger Management (1 rage each 3 sec), Deep Wounds 3/3 (60% of the average weapon damage over 12 sec
# after a critical hit), Impale 2/2 (+20% critical hit damage of abilities).
# Fury: Dual Wield Specialization 5/5 (+25% off-hand damage, +50% off-hand rage), Furious Precision 3/3 (+10%
# off-hand hit), Flurry 5/5 (+25% attack speed for 3 swings after a critical hit), Death Wish (+20% physical damage,
# 30 sec, 3 min cooldown: one use in a 2 min fight), Berserker Stance (+3% critical hit).
# Arms: Two-Handed Weapon Specialization 3/3 (+3%), Weaponmaster 5/5 (axe: +5% critical hit), Improved Slam 2/2
# (no swing reset, -3 sec cooldown), Battle Stance.
# Not in the model: Recklessness, Bloodrage, Rend, Sweeping Strikes, Bloodthrill.

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

def execute_dps(rage):
    """Execute phase: all rage to Execute (15 rage: 600 damage + 15 for each extra rage), one each global cooldown."""
    return min(1 / GCD, rage / 15) * 600 + max(0.0, rage - 15 / GCD) * 15

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
    mh_rage = land_m * (RAGE_SWING * SPEED_1H * (1 + crit_m) + 0.6)
    rage = rate * mh_rage + rate * land_o * (RAGE_SWING * SPEED_1H * (1 + crit_o) * OH_RAGE * 1.5 + 0.6) + 1 / 3 + BLOODRAGE
    use = spend(rage, (("Bloodthirst", 30, 1 / 6), ("Whirlwind", 25, 1 / 10), ("Heroic Strike", 12 + mh_rage, rate)))
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
    src["Execute"] = execute_dps(rage) * f_spec * phys * EXECUTE
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
    swing_rage = land_a * (RAGE_SWING * RAGE_2H * sp * (1 + crit_a) + 0.6)
    rage = rate * swing_rage + 1 / 3 + BLOODRAGE
    op_cap = min(1 / 5, (rate + 1 / 6 + 1 / 15) * DODGE)               # Overpower after a dodge
    use = spend(rage, (("Mortal Strike", 30, 1 / 6), ("Overpower", 5, op_cap), ("Slam", 15, 1 / 15),
                       ("Heroic Strike", 12 + swing_rage, rate)))
    hs = use["Heroic Strike"] / rate
    src = {}
    src["Auto attacks"] = wd * f_a * rate * (1 - hs) * phys
    src["Heroic Strike"] = (wd + 157) * f_spec * use["Heroic Strike"] * phys
    src["Mortal Strike"] = (wn + 160) * f_spec * use["Mortal Strike"] * phys
    src["Slam"] = (wd + 87) * f_spec * use["Slam"] * phys
    src["Overpower"] = (wn + 35) * f_op * use["Overpower"] * phys
    crits = (rate * land_a * crit_a * (1 - hs) + (use["Heroic Strike"] + use["Mortal Strike"] + use["Slam"]) * crit_s
             + use["Overpower"] * crit_op)
    src["Deep Wounds"] = 0.6 * wd / 12 * (1 - 2.718281828 ** (-crits * 12)) * 1.03
    for k in ("Heroic Strike", "Mortal Strike", "Slam", "Overpower"):
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
