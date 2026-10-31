# Retribution

The beta of 30 October 2026 changes most of the Retribution tree. Unsealed Wrath replaces Twist of Light. Conviction now applies to all spells and attacks. Two-Handed Weapon Specialization is now in row 4. In wowsims, Retribution has +3% damage against the beta of 18 October (see Beta test results). These proposals connect Holy Strike to the Seals, make Sanctified Judgement useful at each rank, and help Retribution in late raids.

## Retribution layout

| Row (points necessary) | Talents | Points in the row |
| --- | --- | --- |
| 1 (0) | Deflection, Benediction | 10 |
| 2 (5) | Improved Judgement, Conviction, Sanctified Judgement (C-R3) | 8 |
| 3 (10) | Vindication, Unyielding Faith, Seal of Command, Pursuit of Justice | 8 |
| 4 (15) | Eye for an Eye, Sacred Arbiter, Two-Handed Weapon Specialization | 6 |
| 5 (20) | Turn Evil, Repentance, Vengeance, Burning Zeal (C-R4) | 8 |
| 6 (25) | Champion of the Light | 5 |
| 7 (30) | Unsealed Wrath | 1 |

- Retribution has 46 points (beta: 44).
- All talents keep their beta places. Burning Zeal (C-R4) uses the free place in row 5, column 4.
- Row 4, column 3 is not free. The arrow from Seal of Command to Vengeance passes through it.

## C1. Holy Strike triggers your Seal (spell change)

- **Proposed Holy Strike text (spell, all specs).** "An instant strike that causes 50% weapon damage plus an additional 97 to 121 as Holy damage. Triggers your active Seal the same as a melee attack."
- **Change.** In the beta, Holy Strike triggers Seal of Light, Justice and Wisdom. It does not trigger Seal of Command, Righteousness or Fury. With Holy Strike Seal trigger (C1), Holy Strike triggers all Seals, as all melee attacks do. Seal of Command keeps its usual chance: 7 procs each minute.
- **Unsealed Wrath.** Unsealed Wrath triggers only on auto attacks (wowsims spell data, spell 1310735). Thus, Holy Strike does not store a Seal copy and does not consume the stored copies. With C1, Holy Strike triggers only the active Seal.
- **Why the trigger is in the spell.** Holy Strike uses the usual Seal rule. Thus, one rule is true for all melee attacks, with no exceptions.
- **Protection.** With Shieldsworn, Holy Strike has a 6 sec cooldown. Seal of Fury on each Holy Strike gives more threat. The Threat tables do not include it.
- **Value (beta of 30 October).** Holy Strike Seal trigger (C1) gives Retribution +5.2% damage at all gear tiers. With the beta of 18 October, it gave +11%. Unsealed Wrath already gives both Seals to each auto attack. Thus, Holy Strike adds less now.
- **Balance.** If Retribution does more damage than the pure damage classes in raids, decrease the Sacred Arbiter bonus first: +20% → +10% (see Watch list, W15).

## C-R3. Sanctified Judgement: the return always occurs

- **Problem.** In the beta, each rank increases two values: the chance (33/66/100%) and the return (20/40/60% of the Seal cost). The average return for each Judgement is 7/26/60%. Thus, the first two ranks give almost no mana. The talent has value only at 3/3.
- **Proposed text.** "Your Judgement ability returns 20/40/60% of the Mana cost of the judged seal."
- **Change.** The return occurs on each Judgement at all ranks. Only the % of the Seal cost increases with each rank.
- **Model.** Master of Elements (Mage) returns 10/20/30% of the base mana cost of a spell. Only the % increases with each rank.
- **Total return.** At 3/3, the return does not change: 60% of the base Seal cost. This is 120 mana for Seal of Fury and 126 mana for Seal of Command. Tank and Retribution builds use 3/3. Thus, their mana values do not change.
- **Beta.** The beta of 30 October moves Sanctified Judgement to row 2 (5 points). Its text does not change.

| Rank | Beta: average return, Seal of Fury | Sanctified Judgement (C-R3): return, Seal of Fury | Beta MPS | Sanctified Judgement (C-R3) MPS |
| --- | --- | --- | --- | --- |
| 1/3 | 13 mana (33% × 20%) | 40 mana | 1.9 | 5.7 |
| 2/3 | 53 mana (66% × 40%) | 80 mana | 7.5 | 11.3 |
| 3/3 | 120 mana | 120 mana | 17.0 | 17.0 |

- **MPS.** Mana per sec with 8.5 Judgements each min: Improved Judgement 2/2 and Swift Judgement.
- **Each point has the same value.** Each rank adds 40 mana for each Judgement. In the beta, rank 1 adds 13 and rank 3 adds 67.
- **Risk.** Row 2 needs only 5 Retribution points. A 6-point dip (Benediction 5, Sanctified Judgement 1) gives 5.7 MPS (beta: 1.9). Reverence gives 10.3 MPS for 2 points. Thus, the 1-point rank is not too strong.

## C-R4. Burning Zeal (new talent): row 5, column 4, 2 ranks

- **Proposed text.** "Increases the critical strike damage bonus of your Seals, Judgements and Holy Strike by 10/20%."
- **Model.** Impale (Warrior) and Ruin (Warlock) increase the critical damage bonus. Both are Classic talents. Burning Zeal has the ranks and values of Impale (10/20%).
- **Problem.** Retribution damage increases less with gear than Fury damage: ×1.65 against ×1.73 from fresh level 60 to Naxxramas. Fixed base values of the Seals, Judgement and Holy Strike cause this (see Analysis, Damage, part 6). The beta of 30 October does not change these values. At fresh level 60, Retribution has about 93% of the pure average. In Naxxramas, it has about 89% (see the table below).
- **Why critical damage.** The critical hit chance of Retribution increases with gear. Conviction now gives 6%. Thus, the talent gives more in late raids.
- **Value (beta of 30 October).**

| Gear | Fresh level 60 | Pre-raid | Molten Core | Blackwing Lair | Naxxramas |
| --- | --- | --- | --- | --- | --- |
| Damage | +0.8% | +0.9% | +1.0% | +1.2% | +1.3% |

- **Position.** Row 5, column 4, a free place.
- **Risk.** In PvP, a critical Holy Strike or Judgement does 2.2 times the damage (now 2 times). See PvP burst check and Watch list, W6.

## Retribution against the pure average

- **Model.** models/beta-30-oct/retribution_b2.py. It uses the wowsims build with Unsealed Wrath (14/5/32) and the wowsims rotation: a Seal change after each swing.
- **Start value.** The wowsims test runs give 848 DPS at fresh level 60. The model gives the increase with gear.
- **Pure average.** Fury and Combat Rogue use the increase of the model. Hunter, Mage and Warlock increase ×1.75 to Naxxramas (the middle case of Analysis, Damage, part 6).

| Build | Fresh level 60 | Pre-raid | Molten Core | Blackwing Lair | Naxxramas |
| --- | --- | --- | --- | --- | --- |
| Beta | 93% | 92% | 91% | 90% | 89% |
| With C1 | 98% | 97% | 96% | 95% | 94% |
| With C1 and C-R4 | 99% | 98% | 97% | 96% | 95% |

- **Result.** With Holy Strike Seal trigger (C1) and Burning Zeal (C-R4), Retribution is at the hybrid target (95%) or above it at all tiers. The beta is 2–6 points below the target.
- **Other cases.** Hunter, Mage and Warlock ×1.60: 99–101%. ×1.90: 90–99%.

## Mana with Unsealed Wrath (W29)

- **Rotation.** The wowsims rotation casts the other Seal after each swing. Each auto attack then triggers Seal of Righteousness and has a Seal of Command chance. This is one Seal cast for each swing.
- **Cost.** Unsealed Wrath has no Seal cost decrease. Twist of Light had −20%. With fresh level 60 gear, the rotation uses 50.7 mana each sec. The income is 14.2 mana each sec (Reverence 2/2 and Blessing of Wisdom). The mana pool (3,029) is empty after 1 min 22 sec.
- **Fewer Seal changes.** The plans below use n swings with Seal of Righteousness, then 1 swing with Seal of Command (fresh level 60, Blessing of Wisdom).

| Seal plan | Damage | Mana each sec | Mana empty after |
| --- | --- | --- | --- |
| A Seal change after each swing (n = 1) | 100% | 50.7 | 1 min 22 sec |
| n = 2 | 98.3% | 35.2 | 2 min 23 sec |
| n = 3 | 97.4% | 27.5 | 3 min 47 sec |
| n = 4 | 94.6% | 22.9 | 5 min 48 sec |
| Seal of Command only | 88% | 10.2 | No limit |

- **Result.** At fresh level 60, the mana decreases the damage by 2% in a 2 min fight and by 4% in a 5 min fight. With better gear, the mana pool is larger. From Molten Core, a Seal change after each swing is possible for 2 min.
- **The pure average table above uses no mana limit.** In long fights, Retribution is 2–4 points lower.
- **Spell data.** Unsealed Wrath has a Seal cost effect at 0% (wowsims spell data, spell 1310735). A −20% value, as Twist of Light had, gives +0.8% damage in a 2 min fight and +2.4% in a 5 min fight.

## wowsims check

- **Sim.** wowsims Forever, branch paladin/hotfix-113554-port, with the proposals as flags (models/wowsims-b2). Default gear, rotation and consumables of the Unsealed Wrath set, 3,000 iterations.
- **Full buffs** have Mana Spring Totem, Mana Tide Totem and Atiesh. **Lean buffs** have only Gift of the Wild, Battle Shout, Kings, Might and Wisdom.

| Fight | Beta | C1 | C-R4 | C1 and C-R4 | Seal cost −20% |
| --- | --- | --- | --- | --- | --- |
| 2 min, full buffs | 830 DPS | +4.2% | +2.4% | +6.7% | 0% |
| 5 min, full buffs | 839 DPS | +4.0% | +2.4% | +6.6% | +0.3% |
| 2 min, lean buffs | 609 DPS | +5.0% | +1.9% | +7.0% | +0.1% |
| 5 min, lean buffs | 583 DPS | +5.3% | +2.0% | +7.5% | +5.2% |

- **C1.** The sim gives +4.0–5.3%. The model gives +5.2%.
- **C-R4.** The sim gives +1.9–2.4%. The model gives +0.8–1.3%. The sim has more critical hit chance from buffs and consumables.
- **Mana.** With full buffs, the mana is empty after 5 min 28 sec. With lean buffs, it is empty after about 4 min: in a 5 min fight, Retribution has no mana for 38 sec and loses 5% damage. The model is lower (1 min 22 sec) because it has no Demonic Rune and no consumables.
- **Seal cost −20%.** It has an effect only in long fights with lean buffs (+5.2% in 5 min).

