# Threat model for Forever tanks (level 60, one level 63 boss). Analysis, Threat (proposals/analysis/threat.md).
# A steady-state model, not a combat simulation: average threat per second (TPS), source by source.
# The inputs are those of Analysis, Threat, part 6. The first calculation had no script. This file rebuilds it
# from the written inputs. Where the inputs leave a value open, a comment gives the choice.
#
# Paladin threat comes from each damage source: damage x Righteous Fury (x1.9, Holy damage only).
# Warrior and Druid threat comes from their attacks and from rage: each rage point gives 5 threat.
# Their rage comes partly from damage taken. Thus, their threat increases when the boss hits harder.
#
# Two values are calibrated to the part 1 table, because Forever data for them is not known:
# the Revenge base damage (Warrior) and the Primal Bite damage (Druid). See WAR and DRU.

# ---------------------------------------------------------------- fight (part 6)
MISS, DODGE, PARRY = 0.06, 0.065, 0.14   # attacks from the front against a level 63 boss
GLANCE, GLANCE_DMG = 0.40, 0.65          # auto attacks only
BOSS_ARMOR = 976                         # 3,731 after 5 Sunder Armor and Faerie Fire
SWING, HIT_FRAC = 2.0, 0.64              # the boss swings each 2 sec; 64% of the swings hit the tank
CRUSADER = 161                           # Judgement of the Crusader: spell power against the boss (Holy damage)
RAGE_THREAT = 5                          # each rage point gives 5 threat (before stance and form)
GCD = 1.5

def armor_dr(armor=BOSS_ARMOR, level=60):
    """Classic physical damage reduction."""
    return armor / (armor + 400 + 85 * level)

def table(hit, crit, auto):
    """Melee attack table. Returns (chance to land, expected damage factor)."""
    miss = max(0.0, MISS - hit)
    land = 1 - miss - DODGE - PARRY
    glance = GLANCE if auto else 0.0
    normal = land - glance - crit
    return land, glance * GLANCE_DMG + crit * 2 + normal

# ---------------------------------------------------------------- gear (parts 1, 2 and 3)
class Gear:
    """druid: (damage for each swing, speed) in Bear Form. None: the Druid uses the weapon of the Paladin (part 2)."""
    def __init__(s, name, sp, ap, wdps, wspeed, bv, mana, boss_hit, hit=0.03, crit=0.06, druid=None, armor=BOSS_ARMOR):
        s.name, s.sp, s.ap, s.wdps, s.wspeed, s.bv, s.mana, s.boss_hit = name, sp, ap, wdps, wspeed, bv, mana, boss_hit
        s.hit, s.crit, s.druid, s.armor = hit, crit, druid, armor
    def weapon(s, speed=None):
        """Average weapon hit with Attack Power. speed: normalized speed (Holy Strike), else the weapon speed."""
        return s.wdps * s.wspeed + s.ap / 14 * (speed or s.wspeed)
    def but(s, **kw):
        g = Gear(**{k: v for k, v in s.__dict__.items()})
        g.__dict__.update(kw); return g

# Part 1: pre-raid gear, 200 spell power, 60 block value. Part 6: 500 Attack Power, 45 DPS 2.7 sec weapon.
PART1 = Gear("Part 1", sp=200, ap=500, wdps=45, wspeed=2.7, bv=60, mana=3400, boss_hit=4500, druid=(260, 2.5))

# Part 2: the fresh level 60 tier is a real gear profile. The other tiers are estimates (+15-20% each).
# The Warrior and the Druid have the same Attack Power and weapon as the Paladin.
TIERS = [
    Gear("Fresh level 60",        sp=208, ap=428, wdps=27.5, wspeed=2.2, bv=26,  mana=2897, boss_hit=3000),
    Gear("Pre-raid best in slot", sp=260, ap=520, wdps=42,   wspeed=2.7, bv=60,  mana=3400, boss_hit=3500),
    Gear("Molten Core",           sp=310, ap=600, wdps=52,   wspeed=2.7, bv=80,  mana=3900, boss_hit=4500),
    Gear("Blackwing Lair",        sp=380, ap=700, wdps=60,   wspeed=2.7, bv=100, mana=4400, boss_hit=6000),
    Gear("Naxxramas",             sp=440, ap=800, wdps=66,   wspeed=2.7, bv=125, mana=4900, boss_hit=8000),
]

def flatter(boss_flat):
    """Part 3: from Molten Core, the gear increases at half the rate of part 2.
    boss_flat: the boss hits also increase at half the rate (4,000, 4,750 and 5,750)."""
    pre, out = TIERS[1], TIERS[:2]
    for g in TIERS[2:]:
        half = lambda k: getattr(pre, k) + (getattr(g, k) - getattr(pre, k)) / 2
        kw = {k: half(k) for k in ("sp", "ap", "wdps", "bv", "mana")}
        kw["bv"] = int(kw["bv"])                    # 70, 80, 92
        if boss_flat: kw["boss_hit"] = half("boss_hit")
        out.append(g.but(**kw))
    return out

# ---------------------------------------------------------------- Paladin
RF = 1.9                    # Righteous Fury, Holy damage only
HS_THREAT = 1.2             # Holy Shield: "Damage caused by Holy Shield causes 20% additional threat"
NORM_1H = 2.4               # normalized speed of a one-handed weapon (Holy Strike)
OHWS = (0, 0.03, 0.065, 0.10)
CONS_EVERY = 8              # Consecration on cooldown, as in Analysis, Mana

# Talents. Holy: "is" Improved Seals, "cg" Consecrated Ground. Protection: "prec" Precision, "red" Redoubt,
# "sj" Swift Judgement, "ohws" One-Handed Weapon Specialization, "reck" Reckoning, "ic" Iron Creed.
# Retribution: "conv" Conviction. Holy Shield is always taken. Talents with no threat effect are left out.
PB1 = {"is": 3, "prec": 3, "red": 5, "sj": 1, "ohws": 3, "reck": 5, "ic": 5, "conv": 3}
PB2 = dict(PB1, conv=5)
PB3 = {"is": 3, "cg": 2, "prec": 3, "red": 5, "sj": 1, "reck": 5, "ic": 5}
PB4 = dict(PB3)             # PB4 differs from PB3 only in Anticipation and Fury's Reach
PB_BOTH = dict(PB3, ohws=3) # "One build can have both" (Analysis, Builds, part 3)
BUILDS = (("PB1", PB1), ("PB2", PB2), ("PB3", PB3), ("PB4", PB4), ("PB3 + One-Handed Weapon Specialization", PB_BOTH))

def paladin(g, tal=PB1, proposed=True, c14=True, crusader=True, consecration=False, c16=False, detail=False):
    """TPS of a Protection Paladin. proposed: C6, C11 and C15 (C14 has its own switch).
    consecration: Consecration on cooldown. c16: Holy Strike triggers Seal of Fury (not in the tables)."""
    t = lambda k: tal.get(k, 0)
    hit = g.hit + 0.01 * t("prec")
    crit = g.crit + 0.01 * t("conv")
    spell_crit = crit if proposed else 0.0           # C15: Conviction also for spells (Consecration)
    sp = g.sp + (CRUSADER if crusader else 0)
    dr = armor_dr(g.armor)
    ohws = 1 + OHWS[t("ohws")]                       # melee, Seals, Judgements, Holy Strike (beta test)
    seals = 1 + 0.05 * t("is")                       # Seals and Judgements
    cg = 1 + 0.05 * t("cg") if consecration else 1.0 # all Holy damage on targets in Consecration (beta test)
    if t("red") < 5: raise ValueError("the Holy Shield block rate assumes Redoubt 5/5")
    hs_blocks = (3.0 if proposed else 2.5) / 10      # Holy Shield blocks per sec (C6)
    extra = (2.0 if proposed else 1.0) / 10 * t("reck") / 5   # Reckoning extra attacks per sec (C11)
    land_a, f_auto = table(hit, crit, auto=True)
    land_s, f_spec = table(hit, crit, auto=False)
    src = {}
    # Holy Shield: 221 + 10.7% of spell power (+ 200% of block value, C14) for each block. Not OHWS. No critical hits.
    src["Holy Shield, base"] = (221 + 0.107 * sp) * cg * RF * HS_THREAT * hs_blocks
    src["Holy Shield, block value"] = 2 * g.bv * cg * RF * HS_THREAT * hs_blocks if c14 else 0.0
    # Judgement of Fury: 153-167 + 42.9%. Melee hit table, critical hit x2. One each 10 sec, Swift Judgement each min.
    jud = (160 + 0.429 * sp) * seals * ohws * cg * f_spec
    src["Judgement of Fury"] = jud * RF * (1 / 10 + t("sj") / 60)
    # Holy Strike: 50% normalized weapon damage (armor) + 81-105 Holy + 21.45%. Its threat is x1.9 in full
    # (beta test), x1.05 for each Iron Creed rank.
    hstr = (0.5 * g.weapon(NORM_1H) * (1 - dr) + (93 + 0.2145 * sp) * cg) * ohws * f_spec
    src["Holy Strike"] = hstr * RF * (1 + 0.05 * t("ic")) / 10
    # Auto attacks: physical, x1.0. Reckoning extra attacks: Holy Strike releases them (C11), thus no glancing blows.
    src["Auto attacks"] = g.weapon() * (1 - dr) * ohws * f_auto / g.wspeed
    src["Reckoning attacks"] = g.weapon() * (1 - dr) * ohws * f_spec * extra
    # Seal of Fury: 10% of spell power for each melee hit. Cannot miss. Critical hit x2 with a separate roll.
    hits = land_a / g.wspeed + land_s * extra + (land_s / 10 if c16 else 0)
    src["Seal of Fury"] = 0.10 * sp * seals * ohws * cg * (1 + crit) * RF * hits
    if consecration:
        # Rank 5: 384 over 8 sec + 33.6% of spell power. 15% of the ticks miss. Not OHWS. Spell critical hit x1.5.
        src["Consecration"] = (384 + 0.336 * sp) * 0.85 * (1 + 0.5 * spell_crit) * cg * RF / CONS_EVERY
    total = sum(src.values())
    return (total, src) if detail else total

# ---------------------------------------------------------------- Warrior and Druid
RAGE_TAKEN = 2.5 * 0.6 / 243.6           # rage for each point of boss hit before armor (level 63)
RAGE_SWING = 3.46                        # normalized rage: 3.46 x weapon speed for each hit, x2 for a critical hit

def rage_taken(g):
    return RAGE_TAKEN * g.boss_hit * HIT_FRAC / SWING

WAR_STANCE = 1.3 * 1.15                  # Defensive Stance x Defiance 3/3
WAR = dict(dmg=0.9 * 1.10,               # Defensive Stance -10% damage, One-Handed Weapon Specialization +10%
           revenge_base=255,             # calibrated to part 1 (Classic rank 6: 81-99). With 28% of Attack Power
           revenge_ap=0.28, revenge_cd=5, revenge_cost=5,
           slam=655 + 50, slam_cd=6, slam_cost=20,       # 640-670 + 50 block value; not OHWS
           sunder=225, sunder_cost=15, hs_bonus=138, hs_threat=145, hs_cost=15, avoid_rage=5)

def warrior(g, slam_mult=1.0, detail=False):
    """Shield Slam and Revenge on cooldown, Sunder Armor in the other global cooldowns, then Heroic Strike
    with the spare rage. slam_mult: Shield Slam threat multiplier (2.25 is not tested)."""
    w = WAR; dr = armor_dr(g.armor)
    land_a, f_auto = table(g.hit, g.crit, auto=True)
    land_s, f_spec = table(g.hit, g.crit, auto=False)
    rate = 1 / g.wspeed
    swing_rage = RAGE_SWING * g.wspeed * (land_a + g.crit)
    taken = rage_taken(g) + w["avoid_rage"] * (1 - HIT_FRAC) / SWING   # 5 rage for each block, dodge and parry
    spare = taken + rate * swing_rage - w["slam_cost"] / w["slam_cd"] - w["revenge_cost"] / w["revenge_cd"]
    gcd_left = 1 / GCD - 1 / w["slam_cd"] - 1 / w["revenge_cd"]
    sunders = max(0.0, min(gcd_left, spare / w["sunder_cost"]))
    spare -= sunders * w["sunder_cost"]
    hs = max(0.0, min(1.0, spare / (rate * (w["hs_cost"] + swing_rage))))   # Heroic Strike hits give no rage
    phys = (1 - dr) * w["dmg"]
    src = {}
    src["Auto attacks"] = g.weapon() * phys * f_auto * rate * (1 - hs)
    src["Heroic Strike"] = ((g.weapon() + w["hs_bonus"]) * phys * f_spec + w["hs_threat"] * land_s) * rate * hs
    src["Shield Slam"] = w["slam"] * (1 - dr) * 0.9 * f_spec * slam_mult / w["slam_cd"]
    src["Revenge"] = (w["revenge_base"] + w["revenge_ap"] * g.ap) * phys * f_spec * 2.25 / w["revenge_cd"]
    src["Sunder Armor"] = w["sunder"] * land_s * sunders
    src["Rage"] = RAGE_THREAT * (taken + rate * swing_rage * (1 - hs))
    src = {k: v * WAR_STANCE for k, v in src.items()}
    total = sum(src.values())
    return (total, src) if detail else total

BEAR = 1.5                               # Bear Form with Feral Instinct 3/3
DRU = dict(crit=0.12,                    # Sharpened Claws
           maul_bonus=128 * 1.2, maul_mult=1.75, maul_cost=10,   # Savage Fury 2/2, Ferocity 5/5
           bite=259,                     # Primal Bite damage: calibrated to part 1
           bite_mult=3.0, bite_cd=6, bite_cost=10,
           swipe=83 * 1.2, swipe_mult=1.75, swipe_cost=15)

def druid(g, detail=False):
    """Primal Bite on cooldown, Maul with the spare rage, then Swipe in the other global cooldowns."""
    d = DRU; dr = armor_dr(g.armor); crit = d["crit"]
    sw, speed = g.druid or (g.weapon(), g.wspeed)
    land_a, f_auto = table(g.hit, crit, auto=True)
    land_s, f_spec = table(g.hit, crit, auto=False)
    rate = 1 / speed
    swing_rage = RAGE_SWING * speed * 1.3 * (land_a + crit)            # x1.3 in Bear Form
    taken = rage_taken(g)
    spare = taken + rate * swing_rage - d["bite_cost"] / d["bite_cd"]
    maul = max(0.0, min(1.0, spare / (rate * (d["maul_cost"] + swing_rage))))   # Maul hits give no rage
    spare -= maul * rate * (d["maul_cost"] + swing_rage)
    swipes = max(0.0, min(1 / GCD - 1 / d["bite_cd"], spare / d["swipe_cost"]))
    phys = 1 - dr
    src = {}
    src["Auto attacks"] = sw * phys * f_auto * rate * (1 - maul)
    src["Maul"] = (sw + d["maul_bonus"]) * phys * f_spec * d["maul_mult"] * rate * maul
    src["Primal Bite"] = d["bite"] * phys * f_spec * d["bite_mult"] / d["bite_cd"]
    src["Swipe"] = d["swipe"] * phys * f_spec * d["swipe_mult"] * swipes
    src["Rage"] = RAGE_THREAT * (taken + rate * swing_rage * (1 - maul))
    src = {k: v * BEAR for k, v in src.items()}
    total = sum(src.values())
    return (total, src) if detail else total
