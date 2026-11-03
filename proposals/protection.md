# Protection

The live version changes most of the Protection tree. Righteous Fury now increases all threat by 33%. Shieldsworn gives a Holy Strike each 6 sec that triggers Holy Shield and Shield Specialization. Thus, mana is no longer a main problem (see Beta test results). But the development notes of 2 November give the Warrior and the Druid about 44% more threat, and the Paladin no change. The Protection proposals now give:

- The Warrior threat again, with a larger Righteous Fury bonus (C25, a baseline spell).
- A fix for crushing blows (Redoubt, C-P1). This is the largest difference between the Paladin and the Warrior.
- A threat transfer for tank swaps and groups (Shoulder the Burden, C-P5, a baseline spell).
- A ranged pull for dungeons: a longer Judgement range with Seal of Fury (Reach of Law, C-P7).
- A Lay on Hands that does not drain all the mana, and a Hand of Sacrifice that costs less health (Devoted Sacrifice, C-P11).
- No talent that gives only armor (Toughness removal, C-P13). Devoted Sacrifice takes its place.
- No prerequisite for Swift Judgement (C-P14). Templar's Bulwark and Swift Judgement have different uses.

## Protection layout

| Row (points necessary) | Talents | Points in the row |
| --- | --- | --- |
| 1 (0) | Divine Intellect, Redoubt (C-P1) | 10 |
| 2 (5) | Precision, Guardian's Favor, Sacred Duty | 7 |
| 3 (10) | Templar's Bulwark, Improved Hammer of Justice, Shield Specialization, Devoted Sacrifice (C-P11) | 8 |
| 4 (15) | Swift Judgement (C-P14), Improved Righteous Fury, Anticipation, Stoicism (M-P2) | 11 |
| 5 (20) | Reach of Law (C-P7), Holy Shield, Reckoning | 8 |
| 6 (25) | Iron Creed | 3 |
| 7 (30) | Shieldsworn | 1 |

- Protection has 48 points (live: 49). The Warrior Protection tree has 50.
- Toughness removal (C-P13) deletes Toughness (row 3, column 4). Devoted Sacrifice (C-P11) takes its place. All other talents, except Stoicism (M-P2), keep their places in the live trees. Row 5, column 4 stays free.
- Row 2, column 3 is not free. The arrow from Redoubt to Shield Specialization passes through it.

## C-P1. Redoubt: Holy Shield also starts it

- **Proposed text.** "Damaging melee attacks against you have a 10% chance to increase your chance to block by 6/12/18/24/30%. Lasts 10 sec or 5 blocks. Casting Holy Shield also triggers this effect."
- **Change.** Only the Holy Shield trigger is new. If Redoubt is active, a new trigger sets it again to 10 sec and 5 blocks.
- **Why.** It removes most crushing blows (see Analysis, Crushing blows).
- **Live.** The live version gives Redoubt 6–30% again (beta of 18 October: 4–20%). Holy Shield is now in row 5.
- **Value (wowsims, live version).** With Holy Shield (30%) and Redoubt 5/5 (30%), block from talents can be 60%. This removes almost all crushing blows: 11.9% → 1.0% of the boss attacks. The Warrior has 1.0%. Thus, 60% is not too much. Keep 6–30% (see Protection, wowsims check).
- **Other specs.** Holy and Retribution can take Holy Shield with 20 Protection points. Then their Redoubt also starts with each Holy Shield.

## C-P5. Shoulder the Burden (baseline spell)

- **Proposed text.** "You shoulder the burden of a friendly party or raid member, transferring 50% of their threat against all enemies to you." Instant, 30 yards, 5 min cooldown, 45 mana (3% of base mana). All Paladins can learn it.
- **Problem.** The Paladin tank has no area taunt and no threat transfer. Judgement of Fury taunts only one enemy, at 10 yards. Thus, tank swaps and threat on a group of enemies are difficult. The live version gives more threat, but no new tool for a swap.
- **Change.** Shoulder the Burden moves half of the threat of the ally to the Paladin, on each enemy. The ally keeps the other half. Thus, the ally must still control their threat.
- **Model.** Fade (Priest) and Feint (Rogue) decrease the threat of a player. Shoulder the Burden also moves that threat to the tank.
- **Raw threat.** The threat that moves does not change. Righteous Fury does not multiply it.
- **Tank swaps.** First use Judgement of Fury to take the boss. Then use Shoulder the Burden on the other tank. You then have 1.5 times their threat, and they keep 0.5 times. Do not use it before the taunt: the threat of the other tank decreases, and a damage dealer can then pull the boss.
- **PvP.** Players do not use threat. Thus, the spell has no effect in PvP.
- **Why a baseline spell.** The live version gives the Protection tree its ability talents: Templar's Bulwark, Swift Judgement, Holy Shield and Shieldsworn. There is no place for one more ability talent.
- **Why 5 min.** It works on all enemies that the ally has threat on, at any range, and the threat stays moved. Thus, it is near an area taunt. Challenging Shout (Warrior) and Challenging Roar (Druid) have 10 min, but they taunt all enemies. Mocking Blow (Warrior) has 2 min, but it works on one target for 6 sec. Most boss fights last 3–6 min. At 5 min, a raid tank uses it one time for each tank swap.
- **Sacred Duty.** Sacred Duty does not decrease the cooldown of Shoulder the Burden. The 5 min cooldown is the final value.
- **Other specs.** Holy and Retribution also have the spell. The threat goes to the caster, not to a tank. Thus, a Holy or Retribution Paladin only takes the boss with it. The risk is low.
- **No change.** Righteous Fury, Seal of Fury and its absorb shield stay baseline spells. Righteous Fury (C25) changes only the threat value.

## C-P7. Reach of Law (new talent): row 5, column 1

- **Proposed text.** "Increases the range of your Judgement and Swift Judgement by 5/10 yards while Seal of Fury is active." 2 ranks. Requires Swift Judgement.
- **Position.** Row 5, column 1, below Swift Judgement. Stoicism moves to row 4, column 4 (Stoicism move, M-P2).
- **Problem.** In dungeons, the tank must pull enemies from a distance. Judgement of Fury taunts one enemy, but only at 10 yards. The Warrior has Charge in Defensive Stance, and the Druid has Feral Charge. The Paladin has no ranged pull.
- **Change.** With Reach of Law 2/2, the range is 20 yards (15 yards at 1/2). Swift Judgement gives a second Judgement each min. Thus, the tank has two ranged pulls.
- **Seal of Fury only.** Seal of Fury is the tank Seal. Retribution PvP builds also take Swift Judgement, but with Seal of Command or Seal of Justice. Thus, the range of their Judgements does not change.
- **Model.** Arctic Reach (Mage) and Nature's Reach (Druid) give +10/20% range in 2 ranks. Hawk Eye (Hunter) gives +2/4/6 yards. Reach of Law gives yards: the range of Judgement is short (10 yards), thus a % gives an unclear value.
- **Cost.** A dungeon tank takes it for 2 Benediction points: [`v6p-353011021350153102-52233`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p-353011021350153102-52233). In wowsims, the threat does not change against PT1 (1,056 each sec), because the raid buffs fill the mana. A raid tank can skip it.
- **Not in the sim.** wowsims does not model the pull. The value is the range, not damage or threat.

## M-P2. Stoicism move: row 4, column 4

- **Change.** Stoicism moves from row 5, column 1 to row 4, column 4. The ranks and the text do not change.
- **Why.** Reach of Law (C-P7) takes the place below Swift Judgement, for the prerequisite arrow. Row 4, column 4 is free.
- **Effect.** Stoicism opens at 15 Protection points (was 20). A PvP build receives the stun resistance for 5 fewer points.

## C-P11. Devoted Sacrifice (new talent): row 3, column 4

- **Proposed text.** "Your Lay on Hands drains only 75/50% of your remaining Mana, and reduces the damage you take from your Hand of Sacrifice by 20/40%." 2 ranks.
- **Position.** Row 3, column 4, the place of Toughness (Toughness removal, C-P13).
- **Theme.** The Paladin gives its own resources to save others. Lay on Hands costs mana, and Hand of Sacrifice costs health. Devoted Sacrifice makes the two spells cost less.
- **Lay on Hands.** The spell keeps its heal, its 20 min cooldown and its mana for the target.
- **Problem.** Lay on Hands drains all the mana of the Paladin (Forever spellbook, all ranks). Forever decreases the cooldown from 1 hour to 20 min. Thus, the Paladin can use it about one time for each boss. But the drain is largest when the mana is full, early in a fight. Thus, Paladins use it only when their mana is already low.
- **Keep mana for the role.** With Devoted Sacrifice (C-P11), the Paladin can use Lay on Hands at any time and always keeps half of the mana. The healer continues to heal, the tank keeps its threat, and Retribution keeps its damage. The time until the mana is back is also half (see the table).
- **Other saves.** At 0 mana, the Paladin cannot cast Divine Shield (110 mana), Hand of Protection (7% of base mana) or Hammer of Justice (100 mana). With Devoted Sacrifice (C-P11), these saves stay available.
- **Hand of Sacrifice.** The pool does not change. The target is still protected from up to 825 damage (Hand of Sacrifice, C4). Only the damage that the Paladin takes decreases: about 660 at 1/2 and 495 at 2/2. A tank takes the damage of an ally in addition to the boss damage. Thus, without Devoted Sacrifice (C-P11), a tank uses Hand of Sacrifice only when its health is high.
- **Why 20/40%.** At rank 1, the drain is 75%. Lay on Hands is then more efficient than the usual heals only below 21% mana. Thus, the Hand of Sacrifice part gives the value of rank 1. At 40%, the Paladin still takes more than half of the damage. With Hand of Sacrifice each 15 sec (C4), 2/2 removes about 22 damage per sec from the raid.
- **Model.** Improved Health Funnel (Warlock) and Improved Mend Pet (Hunter) are 2-rank talents for save spells. Sacred Duty also gives two effects in one talent.
- **Cost for Holy.** Holy takes it with 12 Protection points, for example Divine Intellect 5, Guardian's Favor 2, Sacred Duty 2, Precision 1 and Devoted Sacrifice 2. Holy keeps 39 points. Holy then removes only damage talents: Improved Seals and Consecrated Ground. In row 4, the cost was 17 points.
- **PvP.** Divine Shield already stops all the damage that moves (W20). Thus, the Hand of Sacrifice part does not change the Divine Shield risk.
- **Design rule 1.** Lay on Hands and Hand of Sacrifice are not buffs (Hands, C5). Thus, Devoted Sacrifice (C-P11) does not break the rule.

**Cast at full mana**

| Spec (maximum mana, mana income) | Heal (maximum health, estimate) | Live: time until the mana is back | Devoted Sacrifice (C-P11) 2/2: drain, time until the mana is back |
| --- | --- | --- | --- |
| Holy (4,416, +22.6 per sec) | About 4,000 | 3 min 15 sec | 2,208: 1 min 38 sec |
| Protection, fresh level 60 (2,897, +14.5 per sec while it tanks) | About 5,500 | 3 min 19 sec | 1,449: 1 min 39 sec |
| Protection, Naxxramas (4,900, +36.9 per sec while it tanks) | About 8,500 | 2 min 12 sec | 2,450: 1 min 6 sec |

- The Holy values use a fresh level 60 Holy profile with no raid buffs and no consumables: 4,416 mana and 22.6 mana per sec.
- The Protection values use the tank of the live version with Blessing of Wisdom and no Consecration (see Beta test results).

**Why 50%**

At 900 healing power and 19% critical heals, Flash of Light and Holy Light give about 5.75 healing for each mana point. This value has no Blessing of Light. Thus, 4,000 healing costs about 695 mana. If the drain is less than 695 mana, Lay on Hands is more efficient than the usual heals.

| Drain (% of the current mana) | Drain at full mana (Holy) | More efficient than the usual heals below | Mana that stays after a cast at 30% mana |
| --- | --- | --- | --- |
| 25% | 1,104 | 63% mana | 994 |
| 40% | 1,766 | 39% mana | 795 |
| 50% (Devoted Sacrifice, C-P11, rank 2) | 2,208 | 31% mana | 662 |
| 75% (Devoted Sacrifice, C-P11, rank 1) | 3,312 | 21% mana | 331 |
| 100% (live) | 4,416 | 16% mana | 0 |

- Below 50%, a healer can use Lay on Hands for mana at half mana. Then it is not an emergency heal.
- Above 60%, the drain is almost the same as the live version.
- With better gear, the healing for each mana point increases more than the health. Thus, 50% becomes safer in late raids.

**Mana for the target**

- Rank 3 restores 550 mana to the target. The drain occurs first.
- If the Paladin casts it on itself, the Paladin receives more mana than it loses below 1,100 mana (live: below 550). The maximum is +550 in the two cases, at 0 mana.
- This is about one time for each boss: about 5% of the mana of a Holy Paladin in a 5 min fight. A Major Mana Potion gives 1,350–2,250 each 2 min. See W18.

**Alternative to the Lay on Hands part**

| ID | Option | How it works | Precedent | Tradeoff |
| --- | --- | --- | --- | --- |
| C-P11a | Change the base spell (use this if Blizzard does not want the talent) | Lay on Hands drains 50% of the current mana for all Paladins. Devoted Sacrifice keeps only the Hand of Sacrifice part | Forever moves the cooldown of Improved Lay on Hands into the spell | All specs receive it with no points. There is no talent choice. Retribution raid builds also receive it |

## C-P13. Toughness removal

- **Change.** Remove Toughness (row 3, column 4, 5 ranks: +2–10% armor from items). Devoted Sacrifice (C-P11) takes its place.
- **Why.** Toughness gives only a stat. The Protection Warrior of Forever has no armor talent.
- **Balance with Redoubt (C-P1).** With Redoubt (C-P1), the Paladin takes almost the same damage as the Warrior and has a better TMI. Without Toughness, the Paladin is near the Warrior again (see the table).
- **Druid.** Thick Hide (Druid) gives armor. But the Druid tank cannot block, and armor is its main defense.
- **Holy and Retribution.** These specs do not take Toughness. Thus, they lose nothing. Holy can now take Devoted Sacrifice (C-P11) with 12 Protection points.
- **Tank points.** Toughness removal frees 5 points. The tank uses them in the other trees, for example Retribution.

**wowsims, 3 min, 3,000 iterations, TMI with a 6 sec window (a lower TMI is better)**

| Case | Damage taken each sec | TMI |
| --- | --- | --- |
| Paladin, live | 338 | 57.5 |
| Paladin, live, no Toughness | 345 (+2%) | 59.0 (+2.7%) |
| Paladin, Redoubt (C-P1) | 292 | 44.4 |
| Paladin, C-P1 and C-P13 | 299 (+2%) | 45.6 (+2.7%) |
| Warrior, pre-raid | 285 | 48 |

- Threat does not change: 1,054 each sec with C-P1, with and without Toughness.

## C-P14. Swift Judgement: no prerequisite

- **Change.** Swift Judgement (row 4, column 1) no longer requires Templar's Bulwark (row 3, column 1). The text and the place do not change.
- **Why.** The two talents have different uses. Templar's Bulwark is a defensive cooldown. Swift Judgement is a second Judgement for pulls and for the PvP stun burst. The arrow makes a build put a point in a talent that it does not use.
- **Who gains.** Retribution PvP builds take Swift Judgement for the burst, and now keep 1 point. A build with Reach of Law (C-P7) needs only Swift Judgement.
- **Tanks.** The tank builds keep Templar's Bulwark for the absorb shield. Thus, they do not change.

## C25. Righteous Fury: +90% to all threat (baseline spell)

- **Proposed text.** "Increases all threat generated by 90%, and all threat generated by your Holy attacks by an additional 90%. Lasts 30 min." Live: 33%, and an additional 90%.
- **Change.** Only the first part changes: all threat ×1.33 → ×1.9. Holy threat is then ×3.61 (live: ×2.527). The damage reduction and Improved Righteous Fury do not change.
- **Problem.** The development notes of 2 November give Defensive Stance +80% threat (was +30%) and Bear Form +115% (was +50%). The Paladin has no change. Thus, the live Paladin tank has 75% of the Warrior threat in wowsims, with Holy Shield rank 4 of build 70755 (see Analysis, Threat).
- **Why +90%.** It gives the Paladin ×1.43 (1.9 ÷ 1.33). The notes give the Warrior ×1.445 and the Druid ×1.433. Thus, the three tanks have the same positions again as in the beta of 30 October.
- **Model.** On 2 November, Defensive Stance (Warrior) and Bear Form (Druid) received a larger flat threat bonus. Righteous Fury is the tank state of the Paladin. C25 gives it the same type of change.
- **Why a baseline spell.** The notes changed the stance and the form, not talents. Thus, the design rules for talents do not apply.

**wowsims, 3 min, default tank gear, full buffs, one level 63 boss** (as Analysis, Threat, part 6)

| Case | Threat each sec | % of the Warrior | % of the Druid |
| --- | --- | --- | --- |
| Warrior | 1,311 | 100% | 112% |
| Druid | 1,175 | 90% | 100% |
| Paladin, live | 980 | 75% | 83% |
| **Paladin, Righteous Fury (C25)** | **1,394** | **106%** | **119%** |
| Paladin, C25 and Redoubt (C-P1) | 1,500 | 114% | 128% |
| Paladin, C25a (+80%) | 1,321 | 101% | 112% |
| Paladin, C25a and Redoubt (C-P1) | 1,422 | 108% | 121% |

- **Gear levels (model).** With C25, the live Paladin has 117% of the Warrior threat at fresh level 60 and 101% in Naxxramas. Before the notes, it had 118% and 101%. With C25a, it has 111% and 96%.
- **All threat cases.** Analysis, Threat, part 9 gives parts 1 to 8 again with C25 and C25a.
- **Pull.** With a Fury opener, the Paladin has 168% of the Warrior threat after 3 sec and 132% after 10 sec. In its best short windows, it has 87–93% of the Warrior (live: 61–66%).
- **Groups.** On 3 enemies, the Paladin total is 2,126 threat each sec. The Warrior has 1,647 and the Druid 1,536. On the enemy with the least threat, the Paladin has 3.5 times the Warrior threat.
- **Other specs.** Holy and Retribution use Righteous Fury only to tank. In PvP, threat has no effect.
- **Alternative C25a.** +80% to all threat, the value of Defensive Stance. The live tank then has 101% of the Warrior threat in wowsims, and 108% with Redoubt (C-P1). The model gives 95% (Analysis, Threat, part 9).
- **First, a live test.** The Warrior and Druid values come from the notes, not from the game files. The live realms must confirm them before this change (W28).

## wowsims check

- **Sim.** wowsims Forever, master commit d97252f2a (game files of client 1.60.1.70755, Holy Shield rank 4), with the proposals as flags (models/wowsims-b2). The default Protection set: default tank gear, rotation and consumables, talents 12/32/7 with Redoubt 5/5. A level 63 boss attacks the Paladin from the front. Full buffs, 3,000 iterations, 3 min, as in Analysis, Crushing blows.
- **Warrior.** The Protection Warrior of wowsims with its pre-raid set, for comparison. The gear is not the same.

| Case | Block | Crushing blows | Damage taken each sec | Threat each sec |
| --- | --- | --- | --- | --- |
| Paladin, live | 42.6% | 11.9% | 338 | 980 |
| Paladin, Redoubt (C-P1) | 62.2% | 1.0% | 292 (−14%) | 1,054 (+8%) |
| Paladin, C-P1 with 4–20% | 55.3% | 5.5% | 319 (−6%) | 1,033 (+5%) |
| Warrior, pre-raid | 49.9% | 1.0% | 285 | 907 |

- **Result.** With Redoubt (C-P1), the Paladin takes almost the same damage as the Warrior (+2%). The live Paladin takes 18% more. With 4–20%, 5.5% of the attacks are still crushing blows. Thus, keep Redoubt at 6–30% with the trigger.
- **Threat.** More blocks give more Holy Shield damage. Thus, threat increases by 8%. The Warrior value has the threat multipliers of the game files (Defensive Stance +30%).
- **Fast bosses and bosses with two weapons.** Both tanks take more crushing blows. With C-P1, the Paladin stays 0–1.6 points above the Warrior. With 4–20%, it is 3–4.5 points above (Crushing blows, part 3).
- **5 min fights.** The results are the same: crushing blows 11.9% → 1.1%, damage taken −13%.
- **Toughness removal (C-P13).** Without Toughness, damage taken increases by 2% (see Toughness removal, C-P13).
- **Not in the sim.** The sim does not have a threat transfer between tanks or Lay on Hands. Thus, it does not include Shoulder the Burden (C-P5) and Devoted Sacrifice (C-P11). Their values stay as in Analysis.

