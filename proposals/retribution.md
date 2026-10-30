# Retribution

These proposals connect the melee attacks of Retribution to its Holy spells. They also decrease the work of Seal swaps.

## Retribution layout

| Row (points necessary) | Talents | Points in the row |
| --- | --- | --- |
| 1 (0) | Deflection, Conviction (C-R1, M-R2) | 10 |
| 2 (5) | Improved Judgement, Holy Conduit, Vindication (C-P3) | 9 |
| 3 (10) | Pursuit of Justice, Sanctified Judgement (C-R3), Seal of Command | 6 |
| 4 (15) | Eye for an Eye, Sacred Arbiter, Two-Handed Weapon Specialization (M-R1) | 6 |
| 5 (20) | Burning Zeal (C-R4), Vengeance, Repentance, Measure for Measure (C-R5) | 9 |
| 6 (25) | Champion of the Light, Instrument of Law | 5 |
| 7 (30) | Twist of Light (C-R2) | 1 |

Retribution has 46 points (beta: 44). Benediction (M-P1) moves to Protection row 1. Vindication goes to row 2, column 3, with 5 ranks (see Protection, C-P3).

## C1. Holy Strike triggers your Seal and Echo (spell change)

- **Proposed Holy Strike text (spell, all specs).** "An instant strike that causes 50% weapon damage plus an additional 81 to 105 as Holy damage. Triggers your active Seal and Echo the same as a melee attack."
- **Change.** In the beta, Holy Strike triggers Seal of Light, Justice and Wisdom. It does not trigger Seal of Command, Righteousness or Fury. With Holy Strike Seal trigger (C1), Holy Strike triggers all Seals, as all melee attacks do. Seal of Command keeps its usual chance: 7 procs each minute (42% with a 3.6 sec weapon). Holy Strike also triggers a Twist of Light Echo, because the Echo applies to melee attacks.
- **Why the trigger is in the spell.** Holy Strike uses the usual Seal rule. Thus, one rule is true for all melee attacks, with no exceptions.
- **Value.** Retribution has +11% DPS against the beta (see Analysis, Damage).
- **Protection.** Seal of Fury on each Holy Strike gives about +14 TPS. The Threat tables do not include it.
- **Seal of Justice.** In the beta, Holy Strike already triggers Seal of Justice and its stun chance. Holy Strike Seal trigger (C1) does not change this.
- **Balance.** If Retribution does more damage than the pure damage classes in raids, decrease the Sacred Arbiter bonus first: +20% → +10% (see Watch list, W15).

## C-R1. Conviction: attacks and spells

- **Proposed text.** "Improves your chance to get a critical strike with attacks and spells by 1/2/3/4/5%."
- **Model.** Thundering Strikes (Shaman) has the same change.
- **Real change.** In the beta, Conviction already applies to damage Seals and Hammer of Wrath. The change adds only Holy Shock, Exorcism, Consecration and heals.
- **Cost for healers.** Conviction (M-R2) is in row 1. Thus, a Holy Paladin needs only 5 Retribution points.

## C-R2. Twist of Light: the Echo lasts 10 sec

- **Problem.** Each Echo lasts for one melee attack. For full value, you must change Seals before almost each swing. With a 3.5 sec two-handed weapon, the global cooldown is active about 79% of the time. Players on the beta forums give a developer statement: rotations must stay at about four buttons.
- **Proposed text.** "Reduces the Mana cost of your Seal spells by 20%. When you replace your Seal of Command, Seal of Righteousness, Seal of Fury, or Seal of Justice with a different Seal, you gain an Echo of that Seal for 10 sec. While the Echo lasts, your melee attacks also apply the replaced Seal's effects."
- **Same action, slower rhythm.** You still change Seals, but one time each 10 sec, together with Holy Strike and Judgement.

| Each 10 sec, 3.5 sec weapon | Beta | With Twist of Light (C-R2) |
| --- | --- | --- |
| Seal casts | About 3 | 1 |
| Holy Strike | 1 | 1 |
| Judgement (8 sec cooldown with Improved Judgement 2/2) | 1.25 | 1.25 |
| Time in global cooldown (1.5 sec each, Judgement included) | About 79% | About 49% |
| Mana used, one target | About 41.6 per sec | About 11.4 per sec |

- **Mana.** With one Seal change each 10 sec, the Sanctified Judgement refund pays for most of the cost. Thus, Twist of Light (C-R2) is also the main mana fix for Retribution (see Analysis, Mana).

## C-R3. Sanctified Judgement: the return always occurs

- **Problem.** In the beta, each rank increases two values: the chance (33/66/100%) and the return (20/40/60% of the Seal cost). The average return for each Judgement is 7/26/60%. Thus, the first two ranks give almost no mana. The talent has value only at 3/3.
- **Proposed text.** "Your Judgement ability returns 20/40/60% of the Mana cost of the judged seal."
- **Change.** The return occurs on each Judgement at all ranks. Only the % of the Seal cost increases with each rank.
- **Model.** Master of Elements (Mage) returns 10/20/30% of the base mana cost of a spell. Only the % increases with each rank.
- **Total return.** At 3/3, the return does not change: 60% of the base Seal cost. This is 120 mana for Seal of Fury and 126 mana for Seal of Command. The tank and Retribution builds use 3/3. Thus, their mana values do not change (see Analysis, Mana).

| Rank | Beta: average return, Seal of Fury | Sanctified Judgement (C-R3): return, Seal of Fury | Beta MPS | Sanctified Judgement (C-R3) MPS |
| --- | --- | --- | --- | --- |
| 1/3 | 13 mana (33% × 20%) | 40 mana | 1.9 | 5.7 |
| 2/3 | 53 mana (66% × 40%) | 80 mana | 7.5 | 11.3 |
| 3/3 | 120 mana | 120 mana | 17.0 | 17.0 |

- **MPS.** Mana per sec with 8.5 Judgements each min: Improved Judgement 2/2 and Swift Judgement.
- **Each point has the same value.** Each rank adds 40 mana for each Judgement. In the beta, rank 1 adds 13 and rank 3 adds 67.
- **Risk.** Row 3 needs 10 Retribution points. A 10-point dip with 1 point in Sanctified Judgement gives 5.7 MPS (beta: 1.9). Reverence gives 10.3 MPS for 3 points. Thus, the 1-point rank is not too strong.

## M-R1. Two-Handed Weapon Specialization: row 5 → row 4 (20 → 15 points)

- **Model.** The Warrior version opens at 15 points.
- **Values.** 2/4/6%, the same as the beta.
- **Space.** Row 4 has a free column.

## M-R2. Conviction: row 2 → row 1

- **Move.** Conviction goes to row 1, column 3. Benediction (M-P1) moves from this place to Protection row 1. The text of Conviction does not change. It keeps the Conviction (C-R1) text.
- **Parity.** All other +5% critical hit talents are in row 1: Cruelty (Warrior), Malice (Rogue), Lethal Attacks (Hunter) and Thundering Strikes (Shaman).
- **Holy.** A Holy Paladin receives +5% critical heal chance for 5 Retribution points, not 10. A Restoration Shaman also pays 5 points for Thundering Strikes. A Holy build can then also take the Protection dip: 34/12/5 (see Analysis, Tree balance).
- **Retribution.** Retribution has the critical hit at a lower level.
- **Risk.** All specs can take +5% critical hit for 5 points. The other classes have the same.

## C-R4. Burning Zeal (new talent): row 5, column 1, 2 ranks

- **Proposed text.** "Increases the critical strike damage bonus of your Seals, Judgements and Holy Strike by 10/20%."
- **Model.** Impale (Warrior) and Ruin (Warlock) increase the critical damage bonus. Both are Classic talents. Burning Zeal has the ranks and values of Impale (10/20%).
- **Problem.** Retribution damage increases less with gear than Fury damage (×1.58 against ×1.73 from fresh level 60 to Naxxramas). Fixed base values cause this (see Analysis, Damage, part 6). Row 5 also had only 4 points.
- **Why critical damage.** The critical hit chance of Retribution increases with gear: 11.6% at fresh level 60, 16.9% in Naxxramas. Thus, the talent gives more in late raids.
- **Value (RB2 with Burning Zeal 2/2, see Analysis, Damage, part 11).**

| Gear | Fresh level 60 | Pre-raid | Molten Core | Blackwing Lair | Naxxramas |
| --- | --- | --- | --- | --- | --- |
| Damage | +0.8% | +0.9% | +1.0% | +1.2% | +1.3% |
| Against the pure average | 104% | 101% | 99% | 97% | 96% |
| Now (RB2) | 103% | 101% | 98% | 96% | 95% |

- **wowsims.** In a raid with consumables, Burning Zeal 2/2 gives +2.0%: two times the model value. The wowsims gear and buffs give more critical hits.

- **Risk.** In PvP, a critical Holy Strike or Judgement does 2.2 times the damage (now 2 times). See PvP burst check and Watch list, W6.

## C-R5. Measure for Measure (new talent): row 5, column 4, 3 ranks

- **Proposed text.** "When your target dodges or parries your attack, the remaining cooldown of your Judgement is reduced by 1/2/3 sec."
- **Model.** Overpower (Warrior) answers a dodge of the target. The name is an old proverb: justice paid back in kind. Eye for an Eye has the same theme in the same tree.
- **Problem.** From behind, a boss dodges 6.5% of the attacks. Hit chance does not remove dodges. The talent gives a small return for each dodge.
- **Value (RB2 with Measure for Measure 3/3, see Analysis, Damage, part 11).**
  - Raid, from behind (dodge only): about +7% Judgements, +1.0% to +1.1% damage at all gear levels.
  - From the front (dodge and parry: PvP, Retribution tanks): about +23% Judgements, about +4% damage.
- **Mana.** A Judgement costs about 82 mana. Sanctified Judgement 3/3 returns 126. Thus, each extra Judgement gives mana.
- **Risk.** In PvP, Evasion (Rogue) gives many dodges. Judgement then comes back fast while Evasion lasts. A Retribution tank with a two-handed weapon receives about +7% threat. A tank with Holy Shield cannot take the talent: row 5 needs 21 Retribution points (see Watch list, W23).

## Retribution with Burning Zeal (C-R4) and Measure for Measure (C-R5)

- **Points.** A deep build with both talents needs 5 more Retribution points. RB6 (5/8/38) takes them from the Holy dip: it keeps Improved Seals 3, adds Divine Intellect 2 and loses Reverence, Infusion of Light and Unyielding Faith.
- **Damage.** RB6 has +1.9% at fresh level 60 and +2.4% in Naxxramas against RB2. It is 105% of the pure average at fresh level 60 and 97% in Naxxramas (see Analysis, Damage, part 11). In wowsims, it is 108% of the pure average in a raid.
- **Balance.** The hybrid target is 95% of the pure average. If Retribution is above the pure average at the raid release, decrease Sacred Arbiter first (+20% → +10%, see Watch list, W15).
