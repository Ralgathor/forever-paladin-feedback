# Retribution

The live version changes most of the Retribution tree. Unsealed Wrath replaces Twist of Light. Conviction now applies to all spells and attacks. Two-Handed Weapon Specialization is now in row 4. In wowsims, Retribution has +3% damage against the beta of 18 October (see Beta test results). These proposals connect Holy Strike to the Seals and make Sanctified Judgement useful at each rank.

## Retribution layout

| Row (points necessary) | Talents | Points in the row |
| --- | --- | --- |
| 1 (0) | Deflection, Benediction | 10 |
| 2 (5) | Improved Judgement, Conviction, Sanctified Judgement (C-R3) | 8 |
| 3 (10) | Vindication, Unyielding Faith, Seal of Command, Pursuit of Justice | 8 |
| 4 (15) | Eye for an Eye, Sacred Arbiter, Two-Handed Weapon Specialization | 6 |
| 5 (20) | Turn Evil, Repentance, Vengeance | 6 |
| 6 (25) | Champion of the Light | 5 |
| 7 (30) | Unsealed Wrath | 1 |

- Retribution has 44 points, as in the live version.
- All talents keep their places in the live trees.
- Row 4, column 3 is not free. The arrow from Seal of Command to Vengeance passes through it.

## C1. Holy Strike triggers your Seal (spell change)

- **Proposed Holy Strike text (spell, all specs).** "An instant strike that causes 50% weapon damage plus an additional 97 to 121 as Holy damage. Triggers your active Seal the same as a melee attack."
- **Change.** In the live version, Holy Strike triggers Seal of Light, Justice and Wisdom. It does not trigger Seal of Command, Righteousness or Fury. With Holy Strike Seal trigger (C1), Holy Strike triggers all Seals, as all melee attacks do. Seal of Command keeps its usual chance: 7 procs each minute.
- **Unsealed Wrath.** Unsealed Wrath triggers only on auto attacks (wowsims spell data, spell 1310735). Thus, Holy Strike does not store a Seal copy and does not consume the stored copies. With C1, Holy Strike triggers only the active Seal.
- **Why the trigger is in the spell.** Holy Strike uses the usual Seal rule. Thus, one rule is true for all melee attacks, with no exceptions.
- **Protection.** With Shieldsworn, Holy Strike has a 6 sec cooldown. Seal of Fury on each Holy Strike gives more threat. The Threat tables do not include it.
- **Value (live trees).** Holy Strike Seal trigger (C1) gives Retribution +5.6–5.7% damage at all gear tiers (model) and +5.3–5.6% in wowsims. With the beta of 18 October, it gave +11%. Unsealed Wrath already gives both Seals to each auto attack. Thus, Holy Strike adds less now.
- **Balance.** If Retribution does more damage than the pure damage classes in raids, decrease the Sacred Arbiter bonus first: +20% → +10% (see Watch list, W15).

## C-R3. Sanctified Judgement: the return always occurs

- **Problem.** In the live version, each rank increases two values: the chance (33/66/100%) and the return (20/40/60% of the Seal cost). The average return for each Judgement is 7/26/60%. Thus, the first two ranks give almost no mana. The talent has value only at 3/3.
- **Proposed text.** "Your Judgement ability returns 20/40/60% of the Mana cost of the judged seal."
- **Change.** The return occurs on each Judgement at all ranks. Only the % of the Seal cost increases with each rank.
- **Model.** Master of Elements (Mage) returns 10/20/30% of the base mana cost of a spell. Only the % increases with each rank.
- **Total return.** At 3/3, the return does not change: 60% of the base Seal cost. This is 120 mana for Seal of Fury and 126 mana for Seal of Command. Tank and Retribution builds use 3/3. Thus, their mana values do not change.
- **Live.** The live version moves Sanctified Judgement to row 2 (5 points). Its text does not change.

| Rank | Live: average return, Seal of Fury | Sanctified Judgement (C-R3): return, Seal of Fury | Live MPS | Sanctified Judgement (C-R3) MPS |
| --- | --- | --- | --- | --- |
| 1/3 | 13 mana (33% × 20%) | 40 mana | 1.9 | 5.7 |
| 2/3 | 53 mana (66% × 40%) | 80 mana | 7.5 | 11.3 |
| 3/3 | 120 mana | 120 mana | 17.0 | 17.0 |

- **MPS.** Mana per sec with 8.5 Judgements each min: Improved Judgement 2/2 and Swift Judgement.
- **Each point has the same value.** Each rank adds 40 mana for each Judgement. In the live version, rank 1 adds 13 and rank 3 adds 67.
- **Risk.** Row 2 needs only 5 Retribution points. A 6-point dip (Benediction 5, Sanctified Judgement 1) gives 5.7 MPS (live: 1.9). Reverence 2/2 gives 6.1 MPS for 7 Holy points. Thus, the 1-point rank is not too strong.

## Retribution against the pure average

- **Model.** models/beta-30-oct/retribution_b2.py. It uses the wowsims default Retribution build of 1 November (14/6/31) and the wowsims rotation: plan 1 + 3 (see Mana with Unsealed Wrath).
- **Start value.** wowsims Forever of 1 November gives 906 DPS at fresh level 60 (848 before the wowsims update). The model gives the increase with gear.
- **Increase with gear.** Retribution damage increases less with gear than Fury damage: ×1.65 against ×1.73 from fresh level 60 to Naxxramas. Fixed base values of the Seals, Judgement and Holy Strike cause this (see Analysis, Damage, part 3).
- **Pure average.** Fury and Combat Rogue use the increase of the model. Hunter, Mage and Warlock increase ×1.75 to Naxxramas (the main case of Analysis, Damage, part 1).

| Build | Fresh level 60 | Pre-raid | Molten Core | Blackwing Lair | Naxxramas |
| --- | --- | --- | --- | --- | --- |
| Live | 100% | 99% | 98% | 96% | 96% |
| With C1 | 105% | 104% | 104% | 102% | 101% |

- **Result.** The live version is at the hybrid target (95%) or above it at all gear levels. With Holy Strike Seal trigger (C1), Retribution is 6–10 points above the target.
- **Keep C1.** It gives one Seal rule for all melee attacks and the tank threat. If raid logs confirm the wowsims level, decrease Sacred Arbiter to +10% first: C1 then gives 104% → 100% (W15).
- **Other cases.** Hunter, Mage and Warlock ×1.60: live 100–101%, C1 105–107%. ×1.90: live 91–100%, C1 96–105%.

## Mana with Unsealed Wrath (W29)

- **Rotation.** The wowsims rotation casts Seal of Command after 1 swing with Seal of Righteousness. After 3 swings with Seal of Command, it casts Seal of Righteousness again. The first swing with the new Seal releases the stored copies.
- **Copies of Seal of Command.** Each copy rolls the usual Seal of Command chance. The copies ignore the 1 sec cooldown of the Seal of Command proc (wowsims commit 3989a1237). Thus, 3 copies give 3 chances on one swing.
- **Seal plans.** "1 + 3" is 1 swing with Seal of Righteousness, then 3 swings with Seal of Command. The wowsims rotation is 1 + 3.
- **Cost.** Unsealed Wrath has no Seal cost decrease. Twist of Light had −20%. With fresh level 60 gear, plan 1 + 3 uses 27.8 mana each sec. The income is 14.2 mana each sec (Reverence 2/2 and Blessing of Wisdom). The mana pool (3,029) is empty after 3 min 43 sec.

| Seal plan | wowsims: C1, full buffs, 2 min | Model: damage | Model: mana each sec | Model: mana empty after |
| --- | --- | --- | --- | --- |
| 1 + 3 (wowsims rotation) | 956 DPS | 100% | 27.8 | 3 min 43 sec |
| 1 + 2 | 949 (−0.7%) | 99.2% | 35.6 | 2 min 21 sec |
| 2 + 2 | 934 (−2.4%) | 97.5% | 27.8 | 3 min 43 sec |
| 1 + 1 (a Seal change after each swing) | 924 (−3.4%) | 97.5% | 51.2 | 1 min 21 sec |
| 3 + 3 | 923 (−3.4%) | 97.5% | 19.9 | 8 min 45 sec |
| 3 + 1 | 895 (−6.4%) | 94.9% | 27.8 | 3 min 43 sec |
| Seal of Command only | — | 85.7% | 10.2 | No limit |

- **Model columns.** Fresh level 60, Blessing of Wisdom, no consumables.
- **Result.** Plan 1 + 3 gives the most damage, with half the Seal casts of plan 1 + 1. A copy of Seal of Command has more value than a copy of Seal of Righteousness. Thus, plan 3 + 1 is the weakest plan with copies.
- **Mana.** At fresh level 60, plan 1 + 3 lasts for a 3 min fight. In a 5 min fight, plan 3 + 3 is the best: −2.5% (model). From Molten Core, plan 1 + 3 is the best in a 5 min fight. The mana costs 2.0% in Molten Core, 0.7% in Blackwing Lair and 0% in Naxxramas. With Reverence 50% (C-H1), plan 1 + 3 lasts 5 min 20 sec at fresh level 60, and it is the best plan at all gear levels.
- **The pure average table above uses plan 1 + 3 and no mana limit.** The start value (906) comes from wowsims with the same plan.
- **Spell data.** Unsealed Wrath has a Seal cost effect at 0% (wowsims spell data, spell 1310735). A −20% value, as Twist of Light had, gives 0% in a 2 min fight and +2.6% in a 5 min fight (model). Plan 1 + 3 then lasts 5 min 40 sec.

**Other Seal pairs (wowsims, C1, plan 1 + 3).** Seal of Command with a second Seal in place of Seal of Righteousness.

| Second Seal | Full buffs, 2 min | No buffs and no consumables, 5 min |
| --- | --- | --- |
| Righteousness | 956 DPS | 307 DPS (mana empty after 1 min 29 sec) |
| Fury | 924 (−3.4%) | 284 (−7.6%) |
| Light | 830 (−13%) | 240 (−22%) |
| Wisdom | 828 (−13%) | 350 (+14%, the mana lasts) |
| Justice | 827 (−14%) | 239 (−22%) |

- **With buffs, Seal of Righteousness is the best second Seal.** Lean buffs, 5 min: Righteousness 696, Fury 677 (−2.8%), Wisdom 621 (−11%).
- **Without buffs, Seal of Wisdom is the best second Seal in long fights.** Its copies return mana, thus the Seal changes continue for all of the fight. In a 2 min fight, Wisdom and Righteousness are equal (348 and 345).

**Plans without Seal of Command (wowsims, C1).** "Fury 1 + Righteousness 3" is 1 swing with Seal of Fury, then 3 swings with Seal of Righteousness.

| Plan | Full buffs, 2 min | No buffs and no consumables, 5 min |
| --- | --- | --- |
| Righteousness 1 + Command 3 (wowsims rotation) | 956 DPS | 307 DPS |
| Command only | 809 (−15%) | 292 (−5%) |
| Fury 1 + Righteousness 3 | 818 (−14%) | 269 (−12%) |
| Righteousness 1 + Fury 1 | 788 (−18%) | 253 (−18%) |
| Righteousness 1 + Fury 3 | 775 (−19%) | 259 (−16%) |
| Righteousness only | 749 (−22%) | 272 (−11%) |
| Wisdom 1 + Righteousness 3 | 736 (−23%) | 311 (+1%) |
| Fury only | 691 (−28%) | 239 (−22%) |

- **Each plan without Seal of Command is 14% or more below the wowsims rotation with buffs.** Seal of Command copies are the main value of Unsealed Wrath.
- **Two Seals give more than one Seal.** Fury 1 + Righteousness 3 is 9% above Righteousness only, because each Fury swing releases 3 Righteousness copies.

## wowsims check

- **Sim.** wowsims Forever, master of 1 November, with the proposals as flags (models/wowsims-b2). Default gear, rotation, consumables and build (14/6/31), 3,000 iterations.
- **Full buffs** have Mana Spring Totem, Mana Tide Totem and Atiesh. **Lean buffs** have only Gift of the Wild, Battle Shout, Kings, Might and Wisdom.

| Fight | Live | C1 | Seal cost −20% |
| --- | --- | --- | --- |
| 2 min, full buffs | 906 DPS | +5.6% | 0% |
| 5 min, full buffs | 914 DPS | +5.3% | 0% |
| 2 min, lean buffs | 653 DPS | +5.6% | 0% |
| 5 min, lean buffs | 660 DPS | +5.5% | 0% |

- **C1.** The sim gives +5.3–5.6%. The model gives +5.6–5.7%.
- **Mana.** No run has zero mana. The wowsims consumables now include Major Mana Potion. In the model, plan 1 + 3 has zero mana after 3 min 43 sec, because the model has no consumables.
- **Seal cost −20%.** It has no effect in wowsims, because the mana lasts. The model gives 0–2.6%.

