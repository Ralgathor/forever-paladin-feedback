# Threat model for Forever tanks (level 60, one level 63 boss). Analysis, Threat (proposals/analysis/threat.md).
# A steady-state model, not a combat simulation: average threat per second (TPS), source by source.
# The inputs are those of Analysis, Threat, part 6. The first calculation had no script. This file rebuilds it
# from the written inputs. Where the inputs leave a value open, a comment gives the choice.
#
# Paladin threat comes from each damage source: damage x Righteous Fury (x1.9, Holy damage only).
# Warrior and Druid threat comes from their attacks and from rage: each rage point gives 5 threat.
# RAGE_ALL decides which rage gives threat: all rage, or only rage from spells and talents (wowsims Forever).
#
# Warrior and Druid values come from the Forever spellbook and talents (wowforevertalents.com) and player data.
# Spell values and combat rules checked against wowsims Forever (github.com/wowsims/forever, 23 October 2026).
# Rotations checked against the wowsims Forever default rotations (28 October 2026): Revenge 10 casts each min,
# Rend kept up (Warrior), Lacerate as the filler (Druid).
# No value is fitted to the first calculation.

# ---------------------------------------------------------------- fight (part 6)
MISS, DODGE, PARRY = 0.08, 0.065, 0.14   # attacks from the front against a level 63 boss. Each 1% of hit removes 1% miss
CRIT_SUPP = 0.048                        # critical hit decrease against a level 63 boss: 3% + 1.8% (wowsims Forever)
GLANCE, GLANCE_DMG = 0.40, 0.65          # auto attacks only
BOSS_ARMOR = 976                         # 3,731 after 5 Sunder Armor and Faerie Fire
SWING, HIT_FRAC = 2.0, 0.64              # the boss swings each 2 sec; 64% of the swings hit the tank
CRUSADER = 161                           # Judgement of the Crusader: spell power against the boss (Holy damage)
RAGE_THREAT = 5                          # each rage point gives 5 threat (before stance and form)
RAGE_ALL = True                          # True: all rage gives threat. False: only rage from spells and talents
GCD = 1.5

def armor_dr(armor=BOSS_ARMOR, level=60):
    """Classic physical damage reduction."""
    return armor / (armor + 400 + 85 * level)

def table(hit, crit, auto, dodge=DODGE, parry=PARRY, crit_bonus=1.0):
    """Melee attack table. Returns (chance to land, expected damage factor).
    Auto attacks: one roll. Special attacks: the critical hit is a separate roll on the hits that land.
    crit_bonus: the critical damage bonus of special attacks (1.0: critical hit x2)."""
    miss = max(0.0, MISS - hit)
    land = 1 - miss - dodge - parry
    crit = max(0.0, crit - CRIT_SUPP)
    if auto:
        crit = min(crit, land - GLANCE)
        return land, GLANCE * GLANCE_DMG + crit * 2 + (land - GLANCE - crit)
    return land, land * (1 + crit * crit_bonus)

# ---------------------------------------------------------------- gear (parts 1, 2 and 3)
class Gear:
    def __init__(s, name, sp, ap, wdps, wspeed, bv, mana, boss_hit, hit=0.03, crit=0.06, armor=BOSS_ARMOR):
        s.name, s.sp, s.ap, s.wdps, s.wspeed, s.bv, s.mana, s.boss_hit = name, sp, ap, wdps, wspeed, bv, mana, boss_hit
        s.hit, s.crit, s.armor = hit, crit, armor
    def weapon(s, speed=None):
        """Average weapon hit with Attack Power. speed: normalized speed (Holy Strike), else the weapon speed."""
        return s.wdps * s.wspeed + s.ap / 14 * (speed or s.wspeed)
    def but(s, **kw):
        g = Gear(**{k: v for k, v in s.__dict__.items()})
        g.__dict__.update(kw); return g

# Part 1: pre-raid gear, 200 spell power, 60 block value. Part 6: 500 Attack Power, 45 DPS 2.7 sec weapon.
PART1 = Gear("Part 1", sp=200, ap=500, wdps=45, wspeed=2.7, bv=108, mana=3400, boss_hit=4500)

# Part 2: the fresh level 60 tier is a real gear profile. The other tiers are estimates (+15-20% each).
# Block value with Shield Specialization: pre-raid from the gear search of builds/protection.md (Wowhead Forever
# values). Raid tiers: estimates from the Wowhead Forever tank items (Forever has no raid shields yet).
# The Warrior and the Druid have the same Attack Power and weapon as the Paladin.
TIERS = [
    Gear("Fresh level 60",        sp=208, ap=428, wdps=27.5, wspeed=2.2, bv=26,  mana=2897, boss_hit=3000),
    Gear("Pre-raid best in slot", sp=260, ap=520, wdps=42,   wspeed=2.7, bv=108, mana=3400, boss_hit=3500),
    Gear("Molten Core",           sp=310, ap=600, wdps=52,   wspeed=2.7, bv=140, mana=3900, boss_hit=4500),
    Gear("Blackwing Lair",        sp=380, ap=700, wdps=60,   wspeed=2.7, bv=180, mana=4400, boss_hit=6000),
    Gear("Naxxramas",             sp=440, ap=800, wdps=66,   wspeed=2.7, bv=230, mana=4900, boss_hit=8000),
]

# Pre-raid gear of the tank build search (builds/protection.md), wowsims stat sheet with no buffs and no consumables.
# Greenhammer: 47.3 damage per sec, 2.3 sec. Block value from the Wowhead Forever tooltips (wowsims gives epic shields
# about 32% more). Proposed (PT3 gear): 83 x 1.3 (Shield Specialization 3). Beta (BT4b gear): 44, no Shield
# Specialization. Both leave out the Strength part. Hit from gear: 5.0% and 4.3%.
PATH_PROP = TIERS[1].but(name="Pre-raid path gear, proposed", sp=111, ap=616, wdps=47.3, wspeed=2.3, bv=83 * 1.3,
                         mana=2282, hit=0.05)
PATH_BETA = TIERS[1].but(name="Pre-raid path gear, beta", sp=125, ap=476, wdps=47.3, wspeed=2.3, bv=44, mana=2282,
                         hit=0.043)

def flatter(boss_flat):
    """Part 3: from Molten Core, the gear increases at half the rate of part 2.
    boss_flat: the boss hits also increase at half the rate (4,000, 4,750 and 5,750)."""
    pre, out = TIERS[1], TIERS[:2]
    for g in TIERS[2:]:
        half = lambda k: getattr(pre, k) + (getattr(g, k) - getattr(pre, k)) / 2
        kw = {k: half(k) for k in ("sp", "ap", "wdps", "bv", "mana")}
        kw["bv"] = int(kw["bv"])                    # 124, 144, 169
        if boss_flat: kw["boss_hit"] = half("boss_hit")
        out.append(g.but(**kw))
    return out

# ---------------------------------------------------------------- Paladin
RF = 1.9                    # Righteous Fury, Holy damage only
HS_THREAT = 1.2             # Holy Shield: "Damage caused by Holy Shield causes 20% additional threat"
NORM_1H = 2.4               # normalized speed of a one-handed weapon (Holy Strike)
OHWS = (0, 0.03, 0.065, 0.10)
CONS_EVERY = 8              # Consecration on cooldown, as in Analysis, Mana

# Talents. Holy: "is" Improved Seals, "cg" Consecrated Ground, "hp" Holy Power. Protection: "prec" Precision,
# "red" Redoubt, "sj" Swift Judgement, "ohws" One-Handed Weapon Specialization, "reck" Reckoning, "ic" Iron Creed,
# "hsh" Holy Shield. Retribution: "conv" Conviction, "ij" Improved Judgement, "vind" Vindication, "sa" Sacred Arbiter,
# "bz" Burning Zeal (C-R4), "mfm" Measure for Measure (C-R5). Talents with no threat effect are left out.
# TANK_REF: the 8/35/8 tank of Analysis, Threat (Conviction 3, Reverence; first PB1). All threat tables use it.
TANK_REF = {"is": 3, "prec": 3, "red": 5, "sj": 1, "ohws": 3, "reck": 5, "ic": 5, "hsh": 1, "conv": 3}
# Analysis, Builds, part 3: 3/35/13 tanks with Sanctified Judgement (no threat effect) and Improved Judgement.
PB1 = {"is": 3, "prec": 3, "red": 5, "sj": 1, "ohws": 3, "reck": 5, "ic": 5, "hsh": 1, "ij": 2, "conv": 1}
PB2 = dict(PB1, conv=3)     # no Holy Conduit
PB3 = dict(PB1, ic=3)       # PB3 and PB4 differ only in Anticipation and Reach of Law
PB4 = dict(PB3)
# builds/protection.md: the best tanks of the wowsims build search. Talents with no threat effect are left out.
PT3 = {"is": 3, "prec": 3, "red": 5, "sj": 1, "ohws": 3, "reck": 5, "ic": 5, "hsh": 1, "ij": 2, "conv": 5, "vind": 2, "sa": 1}
BT4b = {"is": 3, "prec": 3, "red": 2, "sj": 1, "ohws": 3, "reck": 3, "ic": 5, "hsh": 1, "ij": 2, "conv": 1}
BUILDS = (("PB1", PB1), ("PB2", PB2), ("PB3", PB3), ("PB4", PB4), ("8/35/8 tank of Analysis, Threat", TANK_REF))
# Analysis, Builds, parts 5 and 6: tanks with no Holy Shield
HOLY_SHOCK_TANK = {"is": 3, "cg": 2, "hp": 5, "prec": 3, "red": 5, "sj": 1, "ohws": 3}             # 30/21/0
HEALING_TANK = {"prec": 3, "red": 5, "sj": 1, "ohws": 3, "reck": 1}                                # 29/22/0

def paladin(g, tal=TANK_REF, proposed=True, c14=1.0, crusader=True, consecration=False, c16=False, ic_rank=0.05,
            phys_mult=1.0, holy_shock=False, ret_aura=False, shield_attack=False, casting=0.0, heal=0.0,
            rf_heals=False, detail=False):
    """TPS of a Protection Paladin on one boss.
    proposed: C-P1, C-P6 and C-R1. c14: block value multiplier of C-P9 (0 = no C-P9, the beta).
    consecration: Consecration on cooldown. c16: Holy Strike triggers Seal of Fury (not in the tables).
    ic_rank: Holy Strike threat for each Iron Creed rank. phys_mult: threat of physical damage (withdrawn idea).
    holy_shock: Holy Shock each 10 sec. ret_aura: Retribution Aura. shield_attack: the shield attack of
    Threat, part 5. casting: sec of casts each sec (no auto attacks). heal: healing on yourself per sec."""
    t = lambda k: tal.get(k, 0)
    hit = g.hit + 0.01 * t("prec")
    crit = g.crit + 0.01 * t("conv")
    spell_crit = crit if proposed else g.crit        # spells crit in the beta too. C-R1: Conviction also for spells
    sp = g.sp + (CRUSADER if crusader else 0)
    ap = g.ap * (1 + 0.01 * t("vind"))               # Vindication: +1-5% Attack Power (full uptime)
    w = g.but(ap=ap)
    dr = armor_dr(g.armor)
    ohws = 1 + OHWS[t("ohws")]                       # melee, Seals, Judgements, Holy Strike (beta test)
    seals = 1 + 0.05 * t("is")                       # Seals and Judgements
    cg = 1 + 0.05 * t("cg") if consecration else 1.0 # all Holy damage on targets in Consecration (beta test)
    # Holy Shield blocks each 10 sec: 3 with C-P1 and Redoubt 5/5 (beta: 2.5). Redoubt 5/5 gives about 1 of them.
    hs_blocks = ((2.0 if proposed else 1.5) + t("red") / 5) / 10
    extra = (2.0 if proposed else 1.0) / 10 * t("reck") / 5   # Reckoning extra attacks per sec (C-P6)
    land_a, f_auto = table(hit, crit, auto=True)
    land_s, f_spec = table(hit, crit, auto=False)
    swings = (1 - casting) / g.wspeed                # a cast stops the auto attacks
    bz = 1 + 0.04 * t("bz")                          # Burning Zeal (5 ranks): critical damage bonus of Seals, Judgements, Holy Strike
    src = {}
    if t("hsh"):
        # Holy Shield: 221 + 8% of spell power (+ c14 x block value) for each block. Not OHWS. No critical hits.
        src["Holy Shield, base"] = (221 + 0.08 * sp) * cg * RF * HS_THREAT * hs_blocks
        src["Holy Shield, block value"] = c14 * g.bv * cg * RF * HS_THREAT * hs_blocks
    # Judgement of Fury: 153-167 + 42.9%. Melee hit table with no dodge or parry, critical hit x2. One each 10 sec,
    # Swift Judgement each min. Improved Judgement: -1 sec cooldown for each rank. The damage hits before the taunt
    # (beta test).
    # Measure for Measure: each dodge or parry of the target (auto attacks, Reckoning attacks and Holy Strike) reduces
    # the remaining Judgement cooldown by 1 sec for each rank. Average cooldown: cd / (1 + rank x dodges and parries per sec).
    _, f_jud = table(hit, crit, auto=False, dodge=0.0, parry=0.0, crit_bonus=bz)
    jud = (160 + 0.429 * sp) * seals * ohws * cg * f_jud
    avoided = (swings + extra + 0.1) * (DODGE + PARRY)
    jud_cd = (10 - t("ij")) / (1 + t("mfm") * avoided)
    src["Judgement of Fury"] = jud * RF * (1 / jud_cd + t("sj") / 60)
    # Holy Strike: 50% of (normalized weapon damage + 93 + 42.9%), all Holy damage: no armor. Holy Power: +3% critical
    # hit for each rank. Its threat is x1.9 in full (beta test), and Iron Creed adds ic_rank for each rank.
    _, f_hstr = table(hit, crit + 0.03 * t("hp"), auto=False, crit_bonus=bz)
    hstr = 0.5 * (w.weapon(NORM_1H) + 93 + 0.429 * sp) * cg * ohws * f_hstr
    src["Holy Strike"] = hstr * RF * (1 + ic_rank * t("ic")) * (1 + 0.20 * t("sa")) / 10   # Sacred Arbiter: +20%
    # Auto attacks: physical. Reckoning extra attacks: in the beta, the next swing (glancing blows possible).
    # With C-P6, Holy Strike releases them: no glancing blows.
    src["Auto attacks"] = w.weapon() * (1 - dr) * ohws * f_auto * swings * phys_mult
    src["Reckoning attacks"] = w.weapon() * (1 - dr) * ohws * (f_spec if proposed else f_auto) * extra * phys_mult
    # Seal of Fury (rank 7): 35 + 10% of spell power for each melee hit. Cannot miss. Critical hit x2 with a separate roll.
    hits = land_a * swings + (land_s if proposed else land_a) * extra + (land_s / 10 if c16 else 0)
    src["Seal of Fury"] = (35 + 0.10 * sp) * seals * ohws * cg * (1 + max(0.0, crit - CRIT_SUPP) * bz) * RF * hits
    if consecration:
        # Rank 5: 8 ticks of 12 + 27 Holy damage (312) + 33.6% of spell power. 15% of the ticks miss. Not OHWS.
        # Spell critical hit x1.5 (beta test).
        src["Consecration"] = (312 + 0.336 * sp) * 0.85 * (1 + 0.5 * spell_crit) * cg * RF / CONS_EVERY
    if holy_shock:
        # Rank 4: 334-362 + 42.9%, 10 sec cooldown. Holy Power +3% critical hit for each rank. Spell hit as Consecration.
        c = spell_crit + 0.03 * t("hp")
        src["Holy Shock"] = (348 + 0.429 * sp) * 0.85 * (1 + 0.5 * c) * cg * RF / 10
    if ret_aura:
        # 20 Holy damage + 6% of spell power for each boss hit that hits the tank.
        src["Retribution Aura"] = (20 + 0.06 * sp) * cg * RF * HIT_FRAC / SWING
    if shield_attack:
        # Threat, part 5: 6 sec cooldown, weapon damage + 100 Holy damage, x2 threat.
        dmg = (w.weapon() * (1 - dr) * phys_mult + 100 * cg * RF) * ohws * f_spec
        src["Shield attack"] = dmg * 2 / 6
    if heal:
        # Each point of effective healing gives 0.5 threat (Classic), x1.9 if Righteous Fury applies to heals.
        src["Healing"] = heal * 0.5 * (RF if rf_heals else 1.0)
    total = sum(src.values())
    return (total, src) if detail else total

# ---------------------------------------------------------------- Warrior and Druid
RAGE_TAKEN = 2.5 * 0.6 / 243.6           # rage for each point of boss hit before armor (level 63)
RAGE_SWING = 3.46                        # normalized rage: 3.46 x weapon speed for each hit, x2 for a critical hit

def rage_taken(g, crush=0.0):
    """Rage per sec from boss hits. crush: share of the boss swings that are crushing blows (x1.5 rage)."""
    return RAGE_TAKEN * g.boss_hit * (HIT_FRAC + 0.5 * crush) / SWING

BOSS_MISS = 0.05                         # boss swings that miss the tank (not dodged, parried or blocked)

# Warrior: Forever spellbook and talents (wowforevertalents.com, client 1.60.1.70450). Assumed Protection build:
# Defiance 3/3, Bastion 5/5, Improved Revenge 3/3, Shield Specialization 5/5, Master of Defense 2/2,
# Improved Sunder Armor 3/3, Focused Rage 3/3 and Improved Heroic Strike 3/3.
WAR_STANCE = 1.3 * 1.15                  # Defensive Stance x Defiance 3/3 (+15% with a shield)
WAR = dict(dmg=0.9 * 1.10,               # Defensive Stance -10% damage, Bastion +10% damage with a shield
           revenge=153, revenge_ap=0.28, revenge_mult=1.6,  # rank 6: 138-168, 28% AP (player sheet), Improved Revenge +60%
           revenge_cd=5, revenge_cost=5 - 3,                # Focused Rage
           revenge_rate=10 / 60,         # Revenge needs a block, dodge or parry: 10 casts each min (wowsims Forever)
           rend=21, rend_ap=0.02, rend_ticks=7, rend_dur=21, rend_cost=10 - 3,   # rank 7: 7 ticks of 21 + 2% AP, bleed
           slam=655, slam_cd=6, slam_cost=20 - 3,           # rank 4: 640-670 + block value
           sunder=206, sunder_ap=0.05, sunder_cost=15 - 3 - 3,   # rank 5: 206 + 5% AP (game files)
           hs_bonus=157, hs_threat=152.4, hs_cost=15 - 3 - 3,   # rank 9: +157 damage, +152.4 threat (wowsims, measured)
           bloodrage=20 / 60,            # Bloodrage: 10 rage + 10 over 10 sec, 1 min cooldown
           block_cost=10, block_cd=5,    # Shield Block on cooldown, not on the global cooldown
           event_rage=5,                 # Shield Specialization and Master of Defense: 5 rage for each block, dodge, parry
           blocked=0.86,                 # share of the hits that Shield Block (80% of the swings) and base block stop
           crush=0.03)                   # crushing blows between Shield Blocks (Analysis, Crushing blows)

def warrior(g, slam_mult=1.0, detail=False):
    """Shield Slam and Shield Block on cooldown, Revenge after a block, dodge or parry, Rend kept up, Sunder Armor in the
    other global cooldowns, then Heroic Strike with the spare rage. slam_mult: Shield Slam threat multiplier (not known: "a very high amount of threat")."""
    w = WAR; dr = armor_dr(g.armor)
    land_a, f_auto = table(g.hit, g.crit, auto=True)
    land_s, f_spec = table(g.hit, g.crit, auto=False)
    rate = 1 / g.wspeed
    swing_rage = RAGE_SWING * g.wspeed * (land_a + max(0.0, g.crit - CRIT_SUPP))
    events = (1 - HIT_FRAC - BOSS_MISS) + HIT_FRAC * w["blocked"]       # dodges, parries and blocks for each swing
    talent = w["event_rage"] * events / SWING + w["bloodrage"]        # rage from talents and spells
    taken = rage_taken(g, w["crush"]) + talent
    spare = (taken + rate * swing_rage - w["slam_cost"] / w["slam_cd"] - w["revenge_cost"] * w["revenge_rate"]
             - w["block_cost"] / w["block_cd"] - w["rend_cost"] / w["rend_dur"])
    gcd_left = 1 / GCD - 1 / w["slam_cd"] - w["revenge_rate"] - 1 / w["rend_dur"]
    sunders = max(0.0, min(gcd_left, spare / w["sunder_cost"]))
    spare -= sunders * w["sunder_cost"]
    hs = max(0.0, min(1.0, spare / (rate * (w["hs_cost"] + swing_rage))))   # Heroic Strike hits give no rage
    phys = (1 - dr) * w["dmg"]
    src = {}
    src["Auto attacks"] = g.weapon() * phys * f_auto * rate * (1 - hs)
    src["Heroic Strike"] = ((g.weapon() + w["hs_bonus"]) * phys * f_spec + w["hs_threat"] * land_s) * rate * hs
    src["Shield Slam"] = (w["slam"] + g.bv) * phys * f_spec * slam_mult / w["slam_cd"]
    src["Revenge"] = ((w["revenge"] + w["revenge_ap"] * g.ap) * w["revenge_mult"] * phys * f_spec * 2.25
                      * w["revenge_rate"])
    # Rend: a bleed, no armor. Threat = damage (wowsims Forever).
    src["Rend"] = (w["rend"] + w["rend_ap"] * g.ap) * w["rend_ticks"] * w["dmg"] * land_s / w["rend_dur"]
    src["Sunder Armor"] = (w["sunder"] + w["sunder_ap"] * g.ap) * land_s * sunders
    src["Rage"] = RAGE_THREAT * ((taken + rate * swing_rage * (1 - hs)) if RAGE_ALL else talent)
    src = {k: v * WAR_STANCE for k, v in src.items()}
    total = sum(src.values())
    return (total, src) if detail else total

# Druid: Forever spellbook, talents and player data. Assumed Feral build: Ferocity 5/5, Savage Fury 2/2,
# Feral Instinct 3/3, Sharpened Claws 2/2, Predatory Strikes 3/3, Blood Frenzy 2/2 and Natural Reaction 5/5.
BEAR = 1.5                               # Bear Form threat
DRU = dict(crit=0.12,                    # 6% from gear + Sharpened Claws 6%
           ap=1.5 * 60,                  # Predatory Strikes: +150% of the level as Attack Power
           maul_bonus=128, maul_mult=1.75, maul_cost=15 - 5,          # rank 7, Ferocity
           savage=1.1,                   # Savage Fury: Maul and Swipe damage +10%
           bite=77, bite_mult=3.0, bite_cd=6, bite_cost=20 - 5,      # rank 4: 100% normal damage + 77
           swipe=83, swipe_ap=0.03, swipe_fi=1.3, swipe_mult=1.75, swipe_cost=20 - 5,   # Feral Instinct +30% damage
           ff=2 * 60, ff_cd=6,           # Faerie Fire in Bear Form: 2 x level threat, 6 sec cooldown, no rage (not verified;
                                         # wowsims Forever gives it no threat)
           lac_tick=15, lac_ticks=5, lac_dur=15, lac_hit=0.10, lac_stacks=5, lac_cost=15,
                                         # Lacerate rank 3: 15 bleed damage each 3 sec for each stack, 5 stacks,
                                         # the hit: 10% weapon damage for each stack. Threat = damage (wowsims Forever)
           crit_rage=5,                  # Blood Frenzy: 5 rage for each critical hit
           dodge_rage=5,                 # Natural Reaction: 5 rage for each dodge
           enrage=30 / 60,               # Enrage: 10 rage + 20 over 10 sec, 1 min cooldown (-27% base armor: not in the model)
           crush=0.15)                   # no block: crushing blows at the full rate (Analysis, Crushing blows)

DRU_WOWSIMS = dict(maul_mult=1.0, bite_mult=1.0, swipe_mult=1.0)   # wowsims Forever: Bear Form x1.5 only

def druid(g, detail=False, mults=None):
    """Primal Bite and Faerie Fire on cooldown, Maul with the spare rage, then Lacerate in the other global cooldowns
    (wowsims Forever rotation). Bear Form damage: weapon damage per sec + Attack Power / 14, 2.5 sec swing (player data).
    mults: threat multipliers of Maul, Primal Bite and Swipe (default: player data; DRU_WOWSIMS: wowsims Forever)."""
    d = dict(DRU, **(mults or {})); dr = armor_dr(g.armor); crit = d["crit"]
    speed = 2.5
    ap = g.ap + d["ap"]
    sw = (g.wdps + ap / 14) * speed
    land_a, f_auto = table(g.hit, crit, auto=True)
    land_s, f_spec = table(g.hit, crit, auto=False)
    rate = 1 / speed
    ec = max(0.0, crit - CRIT_SUPP)                                     # critical hits after the decrease
    swing_rage = RAGE_SWING * speed * 1.3 * (land_a + ec)              # x1.3 in Bear Form
    talent = (d["dodge_rage"] * (1 - HIT_FRAC - BOSS_MISS) / SWING
              + d["crit_rage"] * ec * (rate + 1 / d["bite_cd"])       # swings and Primal Bite
              + d["enrage"])
    taken = rage_taken(g, d["crush"]) + talent
    spare = taken + rate * swing_rage - d["bite_cost"] / d["bite_cd"]
    maul = max(0.0, min(1.0, spare / (rate * (d["maul_cost"] + swing_rage))))   # Maul hits give no rage
    spare -= maul * rate * (d["maul_cost"] + swing_rage)
    lacs = max(0.0, min(1 / GCD - 1 / d["bite_cd"] - 1 / d["ff_cd"], spare / d["lac_cost"]))
    stacks = d["lac_stacks"] * min(1.0, lacs * d["lac_dur"])        # 1 cast each 15 sec keeps the 5 stacks
    phys = 1 - dr
    src = {}
    src["Auto attacks"] = sw * phys * f_auto * rate * (1 - maul)
    src["Maul"] = (sw + d["maul_bonus"]) * d["savage"] * phys * f_spec * d["maul_mult"] * rate * maul
    src["Primal Bite"] = (sw + d["bite"]) * phys * f_spec * d["bite_mult"] / d["bite_cd"]
    src["Faerie Fire"] = d["ff"] / d["ff_cd"]
    src["Lacerate"] = (sw * d["lac_hit"] * stacks * phys * f_spec * lacs
                       + d["lac_tick"] * stacks * d["lac_ticks"] / d["lac_dur"] * land_s)
    src["Rage"] = RAGE_THREAT * ((taken + rate * swing_rage * (1 - maul)) if RAGE_ALL else talent)
    src = {k: v * BEAR for k, v in src.items()}
    total = sum(src.values())
    return (total, src) if detail else total
