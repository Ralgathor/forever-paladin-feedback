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
- **Unsealed Wrath.** Holy Strike is a melee attack. Thus, it also stores a copy of the Seal and can consume the stored copies.
- **Why the trigger is in the spell.** Holy Strike uses the usual Seal rule. Thus, one rule is true for all melee attacks, with no exceptions.
- **Protection.** With Shieldsworn, Holy Strike has a 6 sec cooldown. Seal of Fury on each Holy Strike gives more threat. The Threat tables do not include it.
- **Values to model again.** With the beta of 18 October, Holy Strike Seal trigger (C1) gave Retribution +11% damage. The damage model has no Unsealed Wrath yet.
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
- **Problem.** Retribution damage increases less with gear than Fury damage. Fixed base values of the Seals, Judgement and Holy Strike cause this (see Analysis, Damage, part 6). The beta of 30 October does not change these values. With pre-raid gear, Retribution has about 96% of the pure average. In Naxxramas, it has about 88–89% (estimate).
- **Why critical damage.** The critical hit chance of Retribution increases with gear. Conviction now gives 6%. Thus, the talent gives more in late raids.
- **Value (beta of 18 October, see Analysis, Damage, part 11).**

| Gear | Fresh level 60 | Pre-raid | Molten Core | Blackwing Lair | Naxxramas |
| --- | --- | --- | --- | --- | --- |
| Damage | +0.8% | +0.9% | +1.0% | +1.2% | +1.3% |

- **Values to model again.** The values use the damage model of 18 October. The model has no Unsealed Wrath yet.
- **Position.** Row 5, column 4, a free place.
- **Risk.** In PvP, a critical Holy Strike or Judgement does 2.2 times the damage (now 2 times). See PvP burst check and Watch list, W6.
