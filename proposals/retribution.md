# Retribution

These proposals connect the melee attacks of Retribution to its Holy spells. They also decrease the work of Seal swaps.

## Retribution layout

| Row (points necessary) | Talents | Points in the row |
| --- | --- | --- |
| 1 (0) | Deflection, Conviction (C15, M8) | 10 |
| 2 (5) | Improved Judgement, Holy Conduit, Benediction (M8, C21) | 7 |
| 3 (10) | Vindication, Sanctified Judgement, Seal of Command, Pursuit of Justice | 9 |
| 4 (15) | Eye for an Eye, Sacred Arbiter, Two-Handed Weapon Specialization (M6) | 6 |
| 5 (20) | Vengeance, Repentance | 4 |
| 6 (25) | Champion of the Light, Instrument of Law | 5 |
| 7 (30) | Twist of Light (C17) | 1 |

Retribution has 42 points (beta: 44).

## C15. Conviction: attacks and spells

- **Proposed text.** "Improves your chance to get a critical strike with attacks and spells by 1/2/3/4/5%."
- **Model.** Thundering Strikes (Shaman) has the same change.
- **Real change.** In the beta, Conviction already applies to damage Seals and Hammer of Wrath. The change adds only Holy Shock, Exorcism, Consecration and heals.
- **Cost for healers.** With M8, Conviction is in row 1. Thus, a Holy Paladin needs only 5 Retribution points.

## C16. Holy Strike triggers your Seal and Echo (spell change)

- **Proposed Holy Strike text (spell, all specs).** "An instant strike that causes 50% weapon damage plus an additional 81 to 105 as Holy damage. Triggers your active Seal and Echo the same as a melee attack."
- **Change.** In the beta, Holy Strike triggers Seal of Light, Justice and Wisdom. It does not trigger Seal of Command, Righteousness or Fury. With C16, Holy Strike triggers all Seals, as all melee attacks do. Seal of Command keeps its usual chance: 7 procs each minute (42% with a 3.6 sec weapon). Holy Strike also triggers a Twist of Light Echo, because the Echo applies to melee attacks.
- **Sacred Arbiter does not change.** It keeps the beta text (+20% Holy Strike damage and the Judgement refresh) and the beta row (row 4, 15 points).
- **Why the trigger is in the spell.** A talent that gives only a chance to trigger is weak design: the player does not see its effect each time. In the spell, the chance is the usual Seal rule. Thus, one rule is true for all melee attacks, with no exceptions.
- **Value.** Retribution gets +10% DPS against the beta (see Analysis, Damage). The first version of C16 (Sacred Arbiter: Holy Strike always triggers Seal of Command) gave +13% and put Retribution above Fury Warrior.
- **Model.** Stormstrike (Shaman) makes the weapon strike the core of Enhancement. Holy Strike with your Seals does the same for Retribution.
- **Protection.** Seal of Fury on each Holy Strike gives about +10 TPS. The Threat tables do not include it.
- **Seal of Justice.** In the beta, Holy Strike already triggers Seal of Justice and its stun chance. C16 does not change this.
- **Tuning.** If Retribution does more damage than the pure damage classes in raids, decrease the Sacred Arbiter bonus first: +20% → +10% (see Watch list, W15).

## C17. Twist of Light: the Echo lasts 10 sec

- **Problem.** Each Echo lasts for one melee attack. For full value, you must change Seals before almost each swing. With a 3.5 sec two-handed weapon, the global cooldown is active about 80% of the time. Players on the beta forums give a developer statement: rotations must stay at about four buttons.
- **Proposed text.** "Reduces the Mana cost of your Seal spells by 20%. When you replace your Seal of Command, Seal of Righteousness, Seal of Fury, or Seal of Justice with a different Seal, you gain an Echo of that Seal for 10 sec. While the Echo lasts, your melee attacks also apply the replaced Seal's effects."
- **Same action, slower rhythm.** You still change Seals, but one time each 10 sec, together with Holy Strike and Judgement.

| Each 10 sec, 3.5 sec weapon | Beta | With C17 |
| --- | --- | --- |
| Seal casts | About 3 | 1 |
| Holy Strike | 1 | 1 |
| Judgement (8 sec cooldown with Improved Judgement 2/2) | 1.25 | 1.25 |
| Time in global cooldown (1.5 sec each, Judgement included) | About 79% | About 49% |
| Mana used, one target | About 41.6 per sec | About 11.4 per sec |

- **Mana.** With one Seal change each 10 sec, the Sanctified Judgement refund pays for most of the cost. Thus, C17 is also the main mana fix for Retribution (see Analysis, Mana).

## M6. Two-Handed Weapon Specialization: row 5 → row 4 (20 → 15 points)

- **Model.** The Warrior version opens at 15 points.
- **Values.** 2/4/6%, the same as the beta.
- **Space.** Row 4 has a free column.

## M8. Conviction and Benediction change rows (Conviction row 2 → row 1)

- **Move.** Conviction goes to row 1, column 3. Benediction goes to row 2, column 3. The text of the two talents does not change. Conviction keeps the C15 text.
- **Parity.** All other +5% critical hit talents are in row 1: Cruelty (Warrior), Malice (Rogue), Lethal Attacks (Hunter) and Thundering Strikes (Shaman).
- **Holy.** A Holy Paladin gets +5% critical heal chance for 5 Retribution points, not 10. A Restoration Shaman also pays 5 points for Thundering Strikes. A Holy PvP build can then also take the Protection dip: 35/7/9, or 36/7/8 with C21 (see Analysis, Tree balance).
- **Protection and Retribution.** Benediction stays in reach in row 2. Retribution gets critical hit earlier when it levels.
- **Risk.** All specs get +5% critical hit for 5 points. The other classes have the same.

## C21. Benediction: 3 ranks, 3/6/9%

- **Proposed text.** "Reduces the Mana cost of all instant cast spells and abilities by 3/6/9%."
- **Change.** 3 ranks, not 5 ranks (2/4/6/8/10%). The maximum decreases from 10% to 9%.
- **Precedent.** Cataclysm (Warlock) gives −10% for 3 points in Forever. Forever uses fewer ranks for cost talents.
- **Why.** With M8, Benediction is in row 2. Rows 1 and 2 must give the other specs a reason to put points in the tree (design rule 2). With 3 ranks, the dips into Retribution cost 2 points less.

| Dip | Beta ranks | C21 |
| --- | --- | --- |
| Holy PvP build (Conviction, Benediction, Redoubt, Guardian's Favor) | 35/7/9: Benediction 4/5 (8%) | 36/7/8: Benediction 3/3 (9%), 1 more point for Holy |
| Protection Consecration dip (Deflection 5, Holy Conduit 2, Benediction) | 12 points (10%) | 10 points (9%) |
| Retribution with 3 points in Benediction | 6% | 9% |

- **Mana.** Retribution spends about 1 mana per sec less (see Analysis, Damage). For a full investment, Holy Shock costs about 3 mana more than with 10%. The Protection mana tables change by less than 1 mana per sec.
- **Points.** Retribution has 42 points (beta: 44). Rows 1 and 2 have 17 points. Row 3 still opens at 10 points.
