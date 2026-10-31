# Protection

The beta of 30 October 2026 changes most of the Protection tree. Righteous Fury now increases all threat by 33%. Shieldsworn gives a Holy Strike each 6 sec that triggers Holy Shield and Shield Specialization. Thus, threat and mana are no longer the main problems (see Beta test results). The Protection proposals now give:

- A fix for crushing blows (Redoubt, C-P1). This is the largest difference between the Paladin and the Warrior.
- A threat transfer for tank swaps and groups (Shoulder the Burden, C-P5, a baseline spell).
- A Lay on Hands that does not drain all the mana, and a Hand of Sacrifice that costs less health (Devoted Sacrifice, C-P11).
- A Reckoning that works in raids: more extra attacks from blocks (Reckoning, C-P12).

## Protection layout

| Row (points necessary) | Talents | Points in the row |
| --- | --- | --- |
| 1 (0) | Divine Intellect, Redoubt (C-P1) | 10 |
| 2 (5) | Precision, Guardian's Favor, Sacred Duty | 7 |
| 3 (10) | Templar's Bulwark, Improved Hammer of Justice, Shield Specialization, Toughness | 11 |
| 4 (15) | Swift Judgement, Improved Righteous Fury, Anticipation, Devoted Sacrifice (C-P11) | 11 |
| 5 (20) | Stoicism, Holy Shield, Reckoning (C-P12) | 8 |
| 6 (25) | Iron Creed | 3 |
| 7 (30) | Shieldsworn | 1 |

- Protection has 51 points (beta: 49). The Warrior Protection tree has 50.
- All talents keep their beta places. Devoted Sacrifice (C-P11) uses the free place in row 4, column 4.
- Row 2, column 3 is not free. The arrow from Redoubt to Shield Specialization passes through it.

## C-P1. Redoubt: Holy Shield also starts it

- **Proposed text.** "Damaging melee attacks against you have a 10% chance to increase your chance to block by 6/12/18/24/30%. Lasts 10 sec or 5 blocks. Casting Holy Shield also triggers this effect."
- **Change.** Only the Holy Shield trigger is new. If Redoubt is active, a new trigger sets it again to 10 sec and 5 blocks.
- **Why.** It removes most crushing blows (see Analysis, Crushing blows).
- **Beta.** The beta of 30 October gives Redoubt 6–30% again (18 October: 4–20%). Holy Shield is now in row 5.
- **Value (wowsims, beta of 30 October).** With Holy Shield (30%) and Redoubt 5/5 (30%), block from talents can be 60%. This removes almost all crushing blows: 12.0% → 0.9% of the boss attacks. The Warrior has 1.1%. Thus, 60% is not too much. Keep 6–30% (see Protection, wowsims check).
- **Other specs.** Holy and Retribution can take Holy Shield with 20 Protection points. Then their Redoubt also starts with each Holy Shield.

## C-P5. Shoulder the Burden (baseline spell)

- **Proposed text.** "You shoulder the burden of a friendly party or raid member, transferring 50% of their threat against all enemies to you." Instant, 30 yards, 5 min cooldown, 45 mana (3% of base mana). All Paladins can learn it.
- **Problem.** The Paladin tank has no area taunt and no threat transfer. Judgement of Fury taunts only one enemy, at 10 yards. Thus, tank swaps and threat on a group of enemies are difficult. The beta of 30 October gives more threat, but no new tool for a swap.
- **Change.** Shoulder the Burden moves half of the threat of the ally to the Paladin, on each enemy. The ally keeps the other half. Thus, the ally must still control their threat.
- **Model.** Fade (Priest) and Feint (Rogue) decrease the threat of a player. Shoulder the Burden also moves that threat to the tank.
- **Raw threat.** The threat that moves does not change. Righteous Fury does not multiply it.
- **Tank swaps.** First use Judgement of Fury to take the boss. Then use Shoulder the Burden on the other tank. You then have 1.5 times their threat, and they keep 0.5 times. Do not use it before the taunt: the threat of the other tank decreases, and a damage dealer can then pull the boss.
- **PvP.** Players do not use threat. Thus, the spell has no effect in PvP.
- **Why a baseline spell.** The beta of 30 October gives the Protection tree its ability talents: Templar's Bulwark, Swift Judgement, Holy Shield and Shieldsworn. There is no place for one more ability talent.
- **Why 5 min.** It works on all enemies that the ally has threat on, at any range, and the threat stays moved. Thus, it is near an area taunt. Challenging Shout (Warrior) and Challenging Roar (Druid) have 10 min, but they taunt all enemies. Mocking Blow (Warrior) has 2 min, but it works on one target for 6 sec. Most boss fights last 3–6 min. At 5 min, a raid tank uses it one time for each tank swap.
- **Sacred Duty.** Sacred Duty does not decrease the cooldown of Shoulder the Burden. The 5 min cooldown is the final value.
- **Other specs.** Holy and Retribution also have the spell. The threat goes to the caster, not to a tank. Thus, a Holy or Retribution Paladin only takes the boss with it. The risk is low.
- **No change.** Righteous Fury, Seal of Fury and its absorb shield stay baseline spells.

## C-P11. Devoted Sacrifice (new talent): row 4, column 4

- **Proposed text.** "Your Lay on Hands drains only 75/50% of your remaining Mana, and reduces the damage you take from your Hand of Sacrifice by 20/40%." 2 ranks.
- **Position.** Row 4, column 4, a free place.
- **Theme.** The Paladin gives its own resources to save others. Lay on Hands costs mana, and Hand of Sacrifice costs health. Devoted Sacrifice makes the two spells cost less.
- **Lay on Hands.** The spell keeps its heal, its 20 min cooldown and its mana for the target.
- **Problem.** Lay on Hands drains all the mana of the Paladin (Forever spellbook, all ranks). Forever decreases the cooldown from 1 hour to 20 min. Thus, the Paladin can use it about one time for each boss. But the drain is largest when the mana is full, early in a fight. Thus, Paladins use it only when their mana is already low.
- **Keep mana for the role.** With Devoted Sacrifice (C-P11), the Paladin can use Lay on Hands at any time and always keeps half of the mana. The healer continues to heal, the tank keeps its threat, and Retribution keeps its damage. The time until the mana is back is also half (see the table).
- **Other saves.** At 0 mana, the Paladin cannot cast Divine Shield (110 mana), Hand of Protection (7% of base mana) or Hammer of Justice (100 mana). With Devoted Sacrifice (C-P11), these saves stay available.
- **Hand of Sacrifice.** The pool does not change. The target is still protected from up to 825 damage (Hand of Sacrifice, C4). Only the damage that the Paladin takes decreases: about 660 at 1/2 and 495 at 2/2. A tank takes the damage of an ally in addition to the boss damage. Thus, without Devoted Sacrifice (C-P11), a tank uses Hand of Sacrifice only when its health is high.
- **Why 20/40%.** At rank 1, the drain is 75%. Lay on Hands is then more efficient than the usual heals only below 21% mana. Thus, the Hand of Sacrifice part gives the value of rank 1. At 40%, the Paladin still takes more than half of the damage. With Hand of Sacrifice each 15 sec (C4), 2/2 removes about 22 damage per sec from the raid.
- **Model.** Improved Health Funnel (Warlock) and Improved Mend Pet (Hunter) are 2-rank talents for save spells. Sacred Duty also gives two effects in one talent.
- **Cost for Holy.** Holy takes it with 17 Protection points, for example Divine Intellect 5, Redoubt 3, Guardian's Favor 2, Sacred Duty 2, Improved Hammer of Justice 3 and Devoted Sacrifice 2. In the beta of 18 October, it cost 12 points.
- **PvP.** Divine Shield already stops all the damage that moves (W20). Thus, the Hand of Sacrifice part does not change the Divine Shield risk.
- **Design rule 1.** Lay on Hands and Hand of Sacrifice are not buffs (Hands, C5). Thus, Devoted Sacrifice (C-P11) does not break the rule.

**Cast at full mana**

| Spec (maximum mana, mana income) | Heal (maximum health, estimate) | Beta: time until the mana is back | Devoted Sacrifice (C-P11) 2/2: drain, time until the mana is back |
| --- | --- | --- | --- |
| Holy (4,416, +22.6 per sec) | About 4,000 | 3 min 15 sec | 2,208: 1 min 38 sec |
| Protection, fresh level 60 (2,897, +26.1 per sec while it tanks) | About 5,500 | 1 min 51 sec | 1,449: 56 sec |
| Protection, Naxxramas (4,900, +55.2 per sec while it tanks) | About 8,500 | 1 min 29 sec | 2,450: 44 sec |

- The Holy values use a fresh level 60 Holy profile with no raid buffs and no consumables: 4,416 mana and 22.6 mana per sec.
- The Protection values use the tank of the beta of 30 October with Blessing of Wisdom and no Consecration (see Beta test results).

**Why 50%**

At 900 healing power and 19% critical heals, Flash of Light and Holy Light give about 5.75 healing for each mana point with no Blessing of Light. Thus, 4,000 healing costs about 695 mana. If the drain is less than 695 mana, Lay on Hands is more efficient than the usual heals.

| Drain (% of the current mana) | Drain at full mana (Holy) | More efficient than the usual heals below | Mana that stays after a cast at 30% mana |
| --- | --- | --- | --- |
| 25% | 1,104 | 63% mana | 994 |
| 40% | 1,766 | 39% mana | 795 |
| 50% (Devoted Sacrifice, C-P11, rank 2) | 2,208 | 31% mana | 662 |
| 75% (Devoted Sacrifice, C-P11, rank 1) | 3,312 | 21% mana | 331 |
| 100% (beta) | 4,416 | 16% mana | 0 |

- Below 50%, a healer can use Lay on Hands for mana at half mana. Then it is not an emergency heal.
- Above 60%, the drain is almost the same as the beta.
- With better gear, the healing for each mana point increases more than the health. Thus, 50% becomes safer in late raids.

**Mana for the target**

- Rank 3 restores 550 mana to the target. The drain occurs first.
- If the Paladin casts it on itself, the Paladin receives more mana than it loses below 1,100 mana (beta: below 550). The maximum is +550 in the two cases, at 0 mana.
- This is about one time for each boss: about 5% of the mana of a Holy Paladin in a 5 min fight. A Major Mana Potion gives 1,350–2,250 each 2 min. See W18.

**Alternative to the Lay on Hands part**

| ID | Option | How it works | Precedent | Tradeoff |
| --- | --- | --- | --- | --- |
| C-P11a | Change the base spell (use this if Blizzard does not want the talent) | Lay on Hands drains 50% of the current mana for all Paladins. Devoted Sacrifice keeps only the Hand of Sacrifice part | Forever moves the cooldown of Improved Lay on Hands into the spell | All specs receive it with no points. There is no talent choice. Retribution raid builds also receive it |

## C-P12. Reckoning: 20–100% after a block, 4 sec limit

- **Proposed text.** "Gives you a 20/40/60/80/100% chance after Blocking or after receiving a non-periodic critical strike to gain an extra attack. Stores up to 4 extra attacks. Cannot occur from Blocks more than once every 4 sec."
- **Beta text.** "Gives you a 8/16/24/32/40% chance after Blocking and a 20/40/60/80/100% chance after receiving a non-periodic critical strike to gain an extra attack. Stores up to 4 extra attacks. Cannot occur from Blocks more than once every 1.5 sec."
- **Change.** The block chance is now the same as the critical hit chance: 20–100%. The block limit is 4 sec (beta: 1.5 sec). The critical hit trigger does not change. The stored attacks hit with your next melee swing, as in the beta.
- **Problem.** At the Defense cap, a raid boss cannot make critical hits on the tank. Thus, only the block trigger works in raids. At 40%, it gives about 5 extra attacks each min.
- **Why a 4 sec limit.** With 100% and the 1.5 sec limit, Redoubt (C-P1) gives 15 extra attacks each min. The threat is then 15% above the Warrior. With the 4 sec limit, the value stays almost the same with and without Redoubt.
- **Why the next swing.** Holy Strike already triggers Shieldsworn, Iron Creed, Sacred Arbiter and your Seal (C1). A release with Holy Strike puts too many effects on one ability.
- **Ranks.** Each rank increases the chance. The limit does not change with the rank, as with other proc talents.

**Value (wowsims, beta of 30 October, 2 min, see Protection, wowsims check)**

| Case | Extra attacks each min | Threat each sec |
| --- | --- | --- |
| Beta | 4.9 | 918 |
| Reckoning (C-P12) | 7.8 | 940 (+2%) |
| Beta with Redoubt (C-P1) | 6.3 | 975 |
| Reckoning (C-P12) with Redoubt (C-P1) | 9.3 | 1,002 (+3%) |

- Damage taken does not change. The 5 min values are the same (±0.5%).
- **Other tests.** Block, dodge and parry at 40% with a 1.5 sec limit: 7.4 extra attacks each min, +2% threat. Block at 100% with a 1.5 sec limit: 11.1 each min, +6% threat (+8% with Redoubt).
- **PvP.** The critical hit trigger and the storage do not change. Thus, the Classic Reckoning bomb stays as in the beta. Blocks give a maximum of 1 charge each 4 sec (see Watch list, W6).

## wowsims check

- **Sim.** wowsims Forever, branch paladin/hotfix-113554-port, with the proposals as flags (models/wowsims-b2). The default Protection set: default tank gear, rotation and consumables, talents 14/32/5 with Redoubt 5/5. A level 63 boss attacks the Paladin from the front. Full buffs, 3,000 iterations, 2 min.
- **Warrior.** The Protection Warrior of wowsims with its pre-raid set, for comparison. The gear is not the same.

| Case | Block | Crushing blows | Damage taken each sec | Threat each sec |
| --- | --- | --- | --- | --- |
| Paladin, beta | 42.7% | 12.0% | 326 | 918 |
| Paladin, Redoubt (C-P1) | 62.0% | 0.9% | 281 (−14%) | 975 (+6%) |
| Paladin, C-P1 with 4–20% | 55.7% | 4.8% | 306 (−6%) | 961 (+5%) |
| Warrior, pre-raid | 49.1% | 1.1% | 277 | 917 |

- **Result.** With Redoubt (C-P1), the Paladin takes almost the same damage as the Warrior (+2%). The beta Paladin takes 18% more. With 4–20%, 4.8% of the attacks are still crushing blows. Thus, keep Redoubt at 6–30% with the trigger.
- **Threat.** More blocks give more Holy Shield damage. Thus, threat increases by 6%.
- **5 min fights.** The results are the same: crushing blows 11.9% → 1.1%, damage taken −13%.
- **Not in the sim.** Shoulder the Burden (C-P5) and Devoted Sacrifice (C-P11) act in raid situations that the sim does not have: a threat transfer between tanks, and Lay on Hands. Their values stay as in Analysis.

