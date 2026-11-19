# Threat

**Question.** Does the Paladin tank hold a boss and a group as well as the Warrior and the Druid?

All values are threat each sec (TPS). The tanks are level 60 and the boss is level 63. The values come from a model and from wowsims. The proposed values include Righteous Fury +90% (C25). Part 9 compares C25 alone with the alternative C25a (+80%). Part 10 gives the inputs.

The Warrior and Druid values use the development notes of 2 November 2026. Defensive Stance gives +80% threat (was +30%) and Defiance 7/13/20% (was 5/10/15%). Bear Form and Dire Bear Form give +115% (was +50%). The hotfix pushes of 4 November 2026 (113600 and 113605) have these values, and wowsims Forever master 9a8624af9 reads them from the game data. Thus the wowsims Warrior and Druid values are now native values, with no scaling. A test on the live realms must confirm them.

All tanks in wowsims have the full threat consumables of 17 November (part 6). Since 18 November, the wowsims values come from master ad6b13af8, with new tank sets (part 6). Since 18 November evening, all tanks also have enchants, and the same enchant rules apply to the three tanks (part 6). Since 19 November, the Paladin tank sets have Crusader in place of Revelation and Libram of Invocation in place of Libram of Holy Alacrity (part 6). The same rules apply to the three tanks: one flask, one food, one potion, one weapon oil or stone, all elixirs that stack, Juju Power, Juju Might, R.O.I.D.S. and Dragonbreath Chili. Each tank takes the items that give it the most threat. In the survival sets, all tanks have Greater Stoneshield Potion. For the Paladin, these are spell power items, for example Flask of Supreme Power and Elixir of Holy Power.

## Short answer

- **No. After the development notes of 2 November 2026, the Paladin tank has less threat than the Warrior and the Druid.** The notes give the Warrior ×1.44 and the Druid ×1.43 more threat. This replaces Blessing of Salvation (1 ÷ 0.7 = ×1.43). The Paladin received ×1.33 from Righteous Fury in the beta of 30 October, and no more on 2 November.
- **With the same gear, the live Paladin has 70% of the Warrior threat** in the model. In wowsims, with item pool tank sets and the full threat consumables, it has 75% of the Warrior and 54% of the Druid. Before the notes, it had 101% and 108% of the Warrior.
- **The Druid has 138% of the Warrior threat on one boss in wowsims.** Master 52471a100 (12 November) gives Lacerate 10/3 threat for each point of damage: Druid +43%. Master 129fcd89e (12 November evening) decreases the Hand of Justice and Ironfoe procs: Warrior −3%, Druid −1%. On 13 November, the new Warrior set had 5% less threat and took 9% less damage. On 15 November, new rage rules give the Warrior +3% and the Druid +7%, and the new Warrior set has 7% more threat. On 16 November, an open item search gives the Warrior set 10% more threat. On 17 November, the full threat consumables give the Druid 6% and the Warrior 3% more threat (part 6). On 18 November, the Warrior gains 1% from a new rage rule, and the new Druid set has 1% less threat. On 18 November evening, the same enchant rules give the Druid 4% and the Warrior 1% more threat. wowsims measured this rule in the game only on rank 2, at levels 38 to 50. Its own note says that the later ranks fit it only in part (part 6). On 11 November, the Druid had 99% of the Warrior.
- **From fresh 60 to Naxxramas, the live Paladin has 71–82% of the Warrior threat.** With Consecration on cooldown, it has 83–98%, but the mana does not last (see Mana).
- **With the proposals, the Paladin passes the Warrior.** Righteous Fury (C25) gives +90% to all threat (live: +33%). In wowsims, the proposed Paladin has 110% of the Warrior threat and 79% of the Druid (C25 alone: 106% and 77%). In the model, it has 114–135% of the Warrior from Naxxramas to fresh 60.
- **With +80% (C25a), the live Paladin has 101% of the Warrior in wowsims** and 96–111% in the model. With Redoubt (C-P1), it has 104% of the Warrior and 75% of the Druid in wowsims.
- **Righteous Fury (C25) closes the gap.** Redoubt (C-P1) gives more blocks, thus more Holy Shield damage: +3% in wowsims (77% of the Warrior). C25 multiplies all Paladin threat by 1.43.
- **Two threat proposals were withdrawn on 2 November 2026.** The Holy Strike Seal trigger (C1) and Reckoning (C-P12) each added +3% in wowsims of 1 November. They do not close the gap.
- **Judgement of the Crusader is important.** It gives the tank about 72 TPS. In the live version, the raid can need the tank Judgement for Light or Wisdom. The tank then has about 70% of the Warrior threat. With Personal Judgement of the Crusader (C2), the tank keeps Crusader.
- **At the pull, the proposed Paladin has the best burst threat, but only with a Fury opener** (part 8). The Paladin casts Seal of Fury and Holy Shield before the pull. Two Judgements of Fury and Holy Strike then hit at 0 sec. The live Paladin then has 183% of the Warrior threat after 1.5 sec, 99% after 3 sec and 79% after 10 sec. The proposed Paladin has 145% after 3 sec and 117% after 10 sec. With the wowsims default opener, the live Paladin has 50% after 3 sec.
- **In its best short windows, the live Paladin has 62–70% of the Warrior** (part 8). The proposed Paladin has 89–102%. The Druid has 116–129%. The Warrior has large spikes from Shield Slam, Revenge and Heroic Strike critical hits.
- **Against 3 or more enemies, the Paladin holds the extra enemies better than the Warrior** (part 7). On the enemy with the least threat, the live Paladin has 1.9–2.1 times the Warrior threat. The proposed Paladin has 2.7–3.1 times. On 3 targets, the Druid holds this enemy better (live Paladin: 69% of the Druid). With the proposals, the Paladin total threat is 119–122% of the Warrior and 112–119% of the Druid.
- **Threat sets and survival sets give the same threat order** (part 6). With the survival sets, the live Paladin has 81% of the Warrior and the proposed Paladin 119%.
- **The Paladin takes less damage than the Warrior** (part 6). With the threat sets, the live Paladin takes 5% less damage than the Warrior. With Redoubt (C-P1), it takes 15% less damage, but its TMI is a little higher (31.3 against 30). With the survival sets, the Paladin with Redoubt takes 13% less damage than the Warrior. Before 18 November evening, only the Druid had a Greater Stoneshield Potion in the survival sets, and the Paladin with Redoubt took 2% more damage than the Warrior. Before 4 November evening, the Paladin test had no consumables, and the gap was 28%.
- **The wowsims tank sets obey the item pool rules** (part 6): no raid drops, no Zul'Gurub or Ahn'Qiraj items, no PvP items, no Revered or Exalted reputation items, item level 63 or lower. The wowsims default sets had these items. Since 18 November evening, the enchants obey the same rules: no raid source, no Revered or Exalted reputation source and phase 1 only. Before, the Paladin sets had no enchants.
- **The model Druid uses the same multipliers as wowsims of 11 November:** Bear Form ×2.15, Maul ×1.75, Swipe ×1.75 and Primal Bite ×3. The Maul, Swipe and Primal Bite values come from player data. A test in the game must confirm them (part 2). The model does not have the Lacerate threat of 12 November.

## 1. One boss, same gear

All tanks have pre-raid gear: 200 spell power, 500 Attack Power and a 45 DPS weapon (2.7 sec). The boss has 5 Sunder Armor and Faerie Fire. The proposed Paladin has C2, C-P1 and C25.

| Boss hit before armor | Warrior | Druid | Paladin, live | Paladin, live, no Crusader | Paladin, proposed | Paladin, proposed, with Consecration |
| --- | --- | --- | --- | --- | --- | --- |
| 3,000 | 832 | 790 | 661 | 589 | 1,081 | 1,257 |
| 4,500 | 943 | 861 | 661 | 589 | 1,081 | 1,257 |
| 6,000 | 976 | 897 | 661 | 589 | 1,081 | 1,257 |

- **Warrior and Druid threat increases with the boss damage.** They receive rage when the boss hits them. Paladin threat does not change.
- **At 4,500,** the live Paladin has 70% of the Warrior threat. The proposed Paladin has 115% (Redoubt alone: 80%).
- **"No Crusader"** is the live tank when the raid takes its Judgement for Light or Wisdom.
- **Boss armor does not change Paladin threat much.** With no armor debuffs, the Warrior has 763 TPS, the Druid 665, the live Paladin 637 and the proposed Paladin 1,044. Most Paladin threat is Holy damage, and armor does not decrease Holy damage.

**Where the Paladin threat comes from (200 spell power)**

| Source | Live | Proposed | Cause of the change |
| --- | --- | --- | --- |
| Holy Shield (blocks and Shieldsworn) | 287 | 374 | Redoubt (C-P1): more blocks |
| Judgement of Fury | 118 | 118 | — |
| Seal of Fury | 70 | 74 | More Reckoning attacks |
| Holy Strike with Iron Creed 3/3 | 104 | 104 | — |
| Auto attacks | 64 | 64 | — |
| Reckoning extra attacks | 17 | 22 | Redoubt (C-P1): more blocks |
| Righteous Fury (C25), ×1.43 on all rows | — | +324 | C25 |
| **Total** | **661** | **1,081** | |

In the model, Redoubt (C-P1) gives +96 TPS, and Righteous Fury (C25) +324 more. The withdrawn ideas gave more: the Holy Strike Seal trigger (C1) +25 and the Reckoning change (C-P12) +20. Personal Judgement of the Crusader (C2) gives +72 when the raid needs the tank Judgement.

**Where the Warrior and Druid threat comes from (4,500 hits)**

| Warrior | TPS | Druid | TPS |
| --- | --- | --- | --- |
| Heroic Strike | 281 | Maul | 388 |
| Revenge (about 10 each min) | 241 | Primal Bite | 215 |
| Shield Slam | 174 | Rage | 122 |
| Rage | 125 | Lacerate | 92 |
| Sunder Armor | 106 | Faerie Fire (not verified) | 43 |
| Rend | 16 | | |
| **Total** | **943** | **Total** | **861** |

The Druid multipliers are Bear Form ×2.15, Maul ×1.75 and Primal Bite ×3 (player data). wowsims master 9a8624af9 uses the same multipliers. Master 52471a100 also gives Faerie Fire threat (2 × level, thus 120) and Lacerate 10/3 threat for each point of damage.

**Spell power.** Each +100 spell power gives about +45 TPS to the live Paladin and +69 TPS to the proposed Paladin.

| Spell power | 100 | 150 | 200 | 250 | 300 | 350 |
| --- | --- | --- | --- | --- | --- | --- |
| Paladin, live | 616 | 639 | 661 | 684 | 706 | 729 |
| Paladin, proposed | 1,013 | 1,047 | 1,081 | 1,116 | 1,150 | 1,184 |

Judgement of the Crusader adds 161 spell power against the boss. This is more than the step from 150 to 300 spell power.

## 2. One boss, from fresh 60 to Naxxramas

In raids, the gear and the boss damage increase together. The model uses five gear levels. The fresh 60 level uses real gear (crafted and dungeon items). The other levels are estimates, each with about 15–20% more stats. All tanks have the same Attack Power and weapon.

| Gear level | Spell power | Attack Power | Weapon DPS | Maximum mana | Boss hit before armor |
| --- | --- | --- | --- | --- | --- |
| Fresh 60 | 208 | 428 | 27.5 (2.2 sec) | 2,897 | 3,000 |
| Pre-raid best | 260 | 520 | 42 | 3,400 | 3,500 |
| Molten Core | 310 | 600 | 52 | 3,900 | 4,500 |
| Blackwing Lair | 380 | 700 | 60 | 4,400 | 6,000 |
| Naxxramas | 440 | 800 | 66 | 4,900 | 8,000 |

TPS on one boss. The two percentages compare the Paladin with the Warrior and with the Druid.

| Gear level | Warrior | Druid | Paladin, live | Paladin, live, no Crusader | **Paladin, proposed** | Proposed, with Consecration |
| --- | --- | --- | --- | --- | --- | --- |
| Fresh 60 | 775 | 681 | 636 (82%, 93%) | 560 (72%, 82%) | **1,043 (135%, 153%)** | 1,220 (157%, 179%) |
| Pre-raid best | 874 | 806 | 686 (78%, 85%) | 613 (70%, 76%) | **1,119 (128%, 139%)** | 1,303 (149%, 162%) |
| Molten Core | 996 | 934 | 733 (74%, 78%) | 661 (66%, 71%) | **1,191 (120%, 128%)** | 1,381 (139%, 148%) |
| Blackwing Lair | 1,085 | 1,051 | 789 (73%, 75%) | 717 (66%, 68%) | **1,274 (117%, 121%)** | 1,476 (136%, 140%) |
| Naxxramas | 1,185 | 1,167 | 837 (71%, 72%) | 764 (65%, 66%) | **1,347 (114%, 115%)** | 1,556 (131%, 133%) |

- **The live Paladin is below the Warrior at all gear levels,** and the gap increases: 82% at fresh 60, 71% in Naxxramas. The Warrior and the Druid receive more Attack Power and rage from gear. The Paladin receives only spell power.
- **Without Crusader,** the live Paladin has 65–72% of the Warrior threat.
- **The proposed Paladin has 114–135%** of the Warrior threat in the model. Without C25, it has 80–94%. wowsims gives a smaller gain from Redoubt (part 6): the proposed Paladin has 110% there, with the full threat consumables and the enchants.
- **Consecration does not close the gap.** The live Paladin with Consecration on cooldown has 83–98% of the Warrior threat. It costs 565 mana each 8 sec. At fresh 60, the mana lasts only about 1 min with Consecration on cooldown. In Naxxramas, it lasts about 3 min (see Mana).
- **The Druid multipliers** come from player data. wowsims master 9a8624af9 uses the same values. A test in the game must confirm them (see Open items).

## 3. If the gear increases more slowly

Blizzard said that it wants flatter gear progression. This is an intention, not a promise. In this part, the gear from Molten Core increases at half the rate of part 2. There are two cases for boss damage: as in part 2, or at half the rate (4,000, 4,750 and 5,750 before armor).

Each cell gives the Paladin TPS as a percentage of the Warrior TPS, then of the Druid TPS in brackets.

| Gear level | Gear as in part 2 | Flatter gear, boss hits as in part 2 | Flatter gear, flatter boss hits |
| --- | --- | --- | --- |
| Live, Naxxramas | 71% (72%) | 69% (72%) | 72% (76%) |
| Proposed, fresh 60 | 134% (153%) | 134% (153%) | 134% (153%) |
| Proposed, pre-raid best | 129% (139%) | 129% (139%) | 129% (139%) |
| Proposed, Molten Core | 120% (127%) | 119% (129%) | 123% (133%) |
| Proposed, Blackwing Lair | 117% (121%) | 116% (123%) | 119% (127%) |
| Proposed, Naxxramas | 114% (116%) | 111% (117%) | 117% (123%) |

- **Flatter gear changes the result by 3 points or less.**
- **The weakest case** is flatter gear with boss hits that increase as in part 2. The live Paladin then has 69% of the Warrior threat in Naxxramas.
- **Crusader is more important with flatter gear.** Its 161 spell power is a larger part of the total.

## 4. Why the Paladin is different

- **Righteous Fury.** It gives ×1.33 to all threat, and ×1.9 more to Holy damage: ×2.527 in total. The Warrior has ×2.16 on all threat (Defensive Stance ×1.8 and Defiance ×1.2). The Druid has ×2.15 (Bear Form). Before 2 November, the Warrior had ×1.495 and the Druid ×1.5.
- **Most Paladin threat is Holy damage.** Holy Shield, Judgement of Fury, Holy Strike and Seal of Fury are Holy damage. Boss armor does not change it, and the Paladin needs no rage.
- **Shieldsworn.** Holy Strike has a 6 sec cooldown. Each Holy Strike that lands also does the Holy Shield damage, with no charge used.

| Attack | Total threat multiplier | Cooldown |
| --- | --- | --- |
| Primal Bite (Druid) | ×6.45 | 6 sec |
| Revenge (Warrior) | ×4.9 | 5 sec. About 10 casts each min, because it needs a block, dodge or parry |
| Maul (Druid) | ×3.8 | Each swing |
| Holy Strike with Iron Creed 3/3 (Paladin) | ×3.3 | 6 sec |
| Holy Shield (Paladin) | ×3.0 | Each block, and each Holy Strike that lands |
| Paladin auto attacks and Reckoning attacks | ×1.33 | — |

**Groups.** Consecration hits all enemies near the Paladin. Its full damage hits only 4 of them. Holy Shield hits only the attacker that the Paladin blocks, with 4 charges each 10 sec. Thus, the Paladin spreads threat well on 2 to 4 enemies.

## 5. Is the threat too low?

The design goal is a Paladin tank with the threat of the Warrior. The beta of 30 October reached it (101%). The development notes of 2 November give the Warrior and the Druid about ×1.44, and the Paladin no change. Thus, the live Paladin has 70% of the Warrior threat in the model, and 75% in wowsims with the full threat consumables and the enchants.

- **Why the gap.** Blessing of Salvation decreased the threat of the damage dealers by 30%. Blizzard removed it and gave the tanks about ×1.43 (1 ÷ 0.7). The Paladin received ×1.33 from Righteous Fury in the beta of 30 October. But the Paladin needed this ×1.33 to reach the Warrior before the notes.
- **Redoubt (C-P1) adds 3% in wowsims.** With Redoubt only, the tank has 77% of the Warrior threat. The live tank blocks 42% of the swings, and 54% with Redoubt (part 6).
- **The Holy Strike Seal trigger (C1) and Reckoning (C-P12) were withdrawn.** Each added only +3% in wowsims of 1 November. They do not close the gap.
- **The fix: Righteous Fury (C25).** The Paladin needs about ×1.44 on all threat. C25 changes the first part of Righteous Fury from +33% to +90% to all threat: ×1.43. The model needs +62% at fresh 60 and +88% in Naxxramas. wowsims needs +78% to reach the Warrior with the item pool tank sets, the full threat consumables and the enchants, and +73% with Redoubt (C-P1). With Revelation (18 November evening), it needed +75% and +69%. Without the enchants, it needed +84% and +77%. With the consumables of 16 November, it needed +107% and +99%. With Redoubt (C-P1), C25 gives 110%. To reach the Druid, it needs +147%. This is a baseline spell, thus the talent rule (a % only) is not necessary.
- **With C25, the model gives 101–117% of the Warrior threat** from Naxxramas to fresh 60. Before the notes, the live Paladin had 101–118%. With all proposals, wowsims gives 110% of the Warrior and 79% of the Druid.
- **The gear is not the same.** wowsims gives each class a tank set from the same item pool (part 6), but the items are different for each class. A Warrior with better gear can make the gap larger. Since 18 November evening, the three tanks have enchants with the same rules (part 6).
- **Consumables are important.** The Paladin test of wowsims has only a Demonic Rune. With the full threat consumables, the live Paladin had +36% threat and −23% damage taken on 17 November (part 6). Most Paladin threat is Holy damage, thus spell power consumables give the most. Flask of Supreme Power alone gives +10%.
- **Live tests give the real answer.** First, confirm the new Defensive Stance and Bear Form values on the live realms. Then compare the tanks with the same gear in real fights.

## 6. Check with wowsims

wowsims Forever plays the fight with the full rules of the game. Full buffs, one level 63 boss from the front, 3 min fight. The Paladin has the wowsims default tank build (12/32/7) with Redoubt 5/5.

**Tank sets.** Each class has two tank sets from the item pool of Analysis, Damage, part 7: a threat set and a survival set. Threat sets: [Protection Paladin](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-pool-protection-paladin.html), [Protection Warrior](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-pool-protection-warrior.html) and [Bear Druid](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-pool-bear-druid.html). Survival sets: [Protection Paladin](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-surv-protection-paladin.html), [Protection Warrior](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-surv-protection-warrior.html) and [Bear Druid](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-surv-bear-druid.html).

- **Item pool rules.** No raid drops. No items of the Zul'Gurub and Ahn'Qiraj patches (item ids 19000 to 23999). No PvP items. No Revered or Exalted reputation items. Item level 63 or lower.
- **Search.** The first search starts from the wowsims default tank set of each class. It replaces each item that is not in the pool. For each slot, it runs the 12 best pool items for the tank stats in wowsims, 1,000 iterations each. Since 11 November, it also runs all pool items with an effect that wowsims implements, in all slots. Examples are the proc weapons Ironfoe and Flurry Axe. It keeps the item with the best tank score.

  Since 16 November, an open search follows. It runs the same candidates in all 17 slots, also in the slots with a pool item of the default set. For the Paladin, it also runs all pool items with spell damage and Defense. It makes up to 3 passes over the slots. It keeps a new item only if the score increases by more than 0.2%.

  Threat set: 40% threat, 20% damage, 20% damage taken and 20% TMI. Survival set: 40% threat, 30% damage taken and 30% TMI. The final set runs with 3,000 iterations. The item search keeps the enchants of the default set. Since 18 November evening, an enchant search follows (below). Scripts: `models/wowsims-b2/tank_gear`.
- **Replaced items.** Paladin: 10 items, for example Arena Grand Master, Force Reactive Disk and Dark Iron Destroyer. Warrior: 8 items, for example Annihilator, Hyperion Legplates and Ring of Awareness. Druid: 11 items, for example the PvP bracers, the Stormpike Insignia, Timbermaw Brawlers and the Premier Grand Marshal's Battle Hammer.
- **The default sets** of wowsims have raid, PvP and reputation items. The [default sets](https://ralgathor.github.io/forever-paladin-feedback/sets/) page keeps their links. The Builds tab uses the two item pool Protection Paladin sets.

- **Consumables (17 November).** All tanks have the full threat consumables. The same rules apply to the three tanks: one flask, one food, one potion, one weapon oil or stone, all elixirs that stack, Juju Power, Juju Might, R.O.I.D.S., Dragonbreath Chili, an explosive, Rumsey Rum and a Major Healthstone. Each tank takes the item of each kind that gives it the most threat in wowsims (1,000 iterations, one item at a time, master 6084403a9). World buffs are not in the runs.

  | Kind | Paladin | Warrior | Druid |
  | --- | --- | --- | --- |
  | Flask | Flask of Supreme Power (+150 spell damage) | Flask of the Titans | Flask of the Titans |
  | Food | Lobster Stew (+28 spell damage) | Smoked Desert Dumplings | Smoked Desert Dumplings |
  | Potion | Major Spellblasting Potion | Major Frenzy Potion | Major Frenzy Potion |
  | Weapon | Brilliant Wizard Oil | Elemental Sharpening Stone | — (no effect in Bear Form) |
  | Elixirs | Ferocity, the Mongoose, Greater Defense, the Phalanx, Greater Arcane Elixir, Holy Power (+40 Holy damage), Gift of Arthas | Ferocity, the Mongoose, Greater Defense, the Phalanx, Gift of Arthas | Ferocity, the Mongoose, Greater Defense, the Phalanx, Gift of Arthas |
  | Other | Juju Power, Juju Might, R.O.I.D.S., Dragonbreath Chili, Rumsey Rum, the Scrolls of Agility, Strength and Protection IV, Goblin Sapper Charge, EZ-Thro Dark Bomb | The same, with SAF-T Clever Dynamite | The same, no bomb |

  **Survival sets:** all three tanks have Greater Stoneshield Potion (+2,000 armor) in place of the threat potion. Before 18 November evening, only the Druid had it, also in its threat set.

  **Same items for all (18 November evening).** The Paladin and the Warrior now also have Gift of Arthas and the three Scrolls, as the Druid. Gift of Arthas gives the Paladin +0.4% threat and the Warrior +0.8%. The Scrolls do not change their threat.

  The tests of 4 to 16 November gave the Paladin no flask, no spell power food, no Elixir of Holy Power and no Juju or R.O.I.D.S. The Warrior and the Druid had the consumables of their wowsims tests. Juju Might replaces Winterfall Firewater: the two do not stack.

  | Tank | Consumables of 16 November | Full threat consumables | Change |
  | --- | --- | --- | --- |
  | Warrior | 1,838 | 1,899 | +3.3% |
  | Druid | 2,454 | 2,611 | +6.4% |
  | Paladin, live | 1,180 (64%) | 1,396 (74%) | +18.3% |
  | Paladin, all kept proposals | 1,747 (95%) | 2,066 (109%) | +18.3% |

  - **The Paladin gains the most,** because most of its threat is Holy damage, and spell power increases Holy damage. Righteous Fury multiplies Holy threat by 2.53. Each item alone, against the Paladin set of 16 November: Flask of Supreme Power +10.4%, Elixir of Holy Power +2.8%, Lobster Stew in place of Smoked Desert Dumplings +1.3%, Dragonbreath Chili +1.0%, Major Spellblasting Potion in place of Major Frenzy Potion +1.1%, R.O.I.D.S. +0.7%, Juju Might +0.5%.
  - **The Warrior gains from R.O.I.D.S. (+1.7%) and the Elemental Sharpening Stone (+1.3%).** The Druid gains from R.O.I.D.S. (+2.0%), Juju Power and Juju Might (+1.5%), Smoked Desert Dumplings (+1.4%) and Winterfall Firewater or Juju Might (+1.3%).
  - **With Flask of the Titans,** as the other tanks, the live Paladin had 1,267 TPS (67% of the Warrior), and 1,878 with all kept proposals (99%). On master ad6b13af8, it has 1,254 TPS (66%). Flask of Supreme Power gives more threat, but less health (no +1,200 health).
  - **The Flasks of Natural Aggression, Accuracy, Precision and Swiftness are not in the runs.** Their bonus applies only in Mount Hyjal, Hyjal Summit and the Barrow Deeps. wowsims applies it in all fights.
- **Enchants (18 November evening).** Before, the Paladin pool sets had no enchants. The Warrior and the Druid had the enchants of the wowsims default sets. Now the same rules apply to the three tanks:

  - An enchant must have a source in the game data.
  - No source in a raid, and no reputation source at Revered or Exalted.
  - Phase 1 only.

  A search sets the enchant of each slot, one slot at a time, with the score of the set (threat set or survival set). Each enchant runs with 1,000 iterations. A new enchant must increase the score by more than 0.2%. The search makes two passes. Script: `models/wowsims-b2/tank_gear/search_enchants.py`. Results: `tank_gear/enchants_*.json`.

  | Tank | Threat set | Survival set |
  | --- | --- | --- |
  | Paladin | Lesser Arcane Amalgamation, +spell power on the neck, Superior Defense, Greater Spellpower, Holy Power gloves, Crusader, Greater Stamina shield, armor kits on chest, legs and feet | Arcanum of Protection, Agility, Superior Deflection, Lesser Block shield, Crusader, armor kits |
  | Warrior | The wowsims pre-raid enchants that obey the rules, with +Agility on the neck | The same, with Arcanum of Protection |
  | Druid | Lesser Arcane Amalgamation, Superior Defense, Superior Deflection, Crusader, armor kits | Arcanum of Protection, Agility, two-hand weapon Agility, armor kits |

  | Tank | No enchants (threat each sec) | Enchants | Change | Damage taken each sec |
  | --- | --- | --- | --- | --- |
  | Warrior | 1,914 | 1,932 | +0.9% | 293 → 291 |
  | Druid | 2,573 | 2,674 | +3.9% | 316 → 328 |
  | Paladin, live | 1,384 | 1,439 | +4.0% | 291 → 278 |
  | Paladin, all kept proposals | 2,045 | 2,119 | +3.6% | 264 → 253 |

  The Paladin gains the most, because it had no enchants. The Druid takes more damage, because its threat set lost Greater Stoneshield Potion. The no enchants runs: `logs/checks_ad6b13af8_pool_full_no_enchants.log` and `logs/checks_ad6b13af8_pool_surv_full_no_enchants.log`.

  **Weapon enchant and libram of the Paladin (19 November).** The first search gave the Paladin Revelation on the weapon. In wowsims, no Protection ability procs it: only the heal of Judgement of Light procs it, and the next Judgement of Fury then crits. In the game, Revelation does not proc from the Protection abilities. Thus, the Paladin tank sets now have Crusader, the second enchant of the search. Revelation gave the live Paladin +2.2% threat (1,472 against 1,439).

  The sets also had Libram of Holy Alacrity. This libram changes only Holy Shock and Holy Light, thus it does nothing for the tank. Libram of Invocation (the Seals cost 5% less mana) replaces it, with no change in threat. Libram of Law (+4% Judgement damage) and Steadfast Libram (+30% block value with Holy Shield) help the tank. But they have item level 65, and the item pool rules stop at 63. The runs with Revelation: `logs/checks_ad6b13af8_pool_full_revelation.log` and `logs/checks_ad6b13af8_pool_surv_full_revelation.log`.

wowsims Forever master commit 9a8624af9 (4 November 2026) has the game data of client 1.60.1.70755 and the hotfixes of 4 November. This data has Holy Shield rank 4 (221 damage, 4 charges), Defensive Stance +80%, Defiance 7/13/20% and Bear Form +115%. The Warrior and Druid values are native wowsims values. The Paladin spells did not change since commit 8298ab833.

Master commit 9f254e8d8 (9 November 2026, hotfix push 113823) adds 262 items. It also changes the Windfury Totem rule and the Warrior and Druid threat rules. With the sets of 8 November, the Warrior gains 1.5% (1,489 → 1,512). The Druid loses 10% (1,756 → 1,582), and the live Paladin 2.8% (1,229 → 1,195). The search ran again for all tank sets. The Paladin threat set takes Warder's Gloves, Scalding Flamehoof (new) and Volunteer's Lucky Seal.

This set loses Justicar's Gloves and Enriched Seal: −0.6% threat and −3.9% damage taken. The Druid survival set takes Warden's Leather Bracers, Thrall's Resolve (new) and Scalding Flamehoof. The other sets do not change. On 8 November (commit ae9b8c23a), the Paladin threat set took Lightforge Belt, Hand of Edward the Odd and Argent Defender. On 6 November (commit df57e2571), Scarlet Kris replaced Greatflank Flayer in the Warrior set (1,448 → 1,503).

Master commit 3633d376a (11 November 2026, client 1.60.1.70888, hotfixes of 10 and 11 November) adds 464 items, for example Ironfoe. It also gives Shield Slam ranks 2 to 4 flat threat. It fixes an error: until this commit, wowsims applied the proc buff of Argent Defender (+18% block for 10 sec) all the time. Now wowsims lists this proc as not implemented, and the shield gives only its stats.

With the sets of 9 November, the live Paladin loses 4.5% (1,187 → 1,133) and takes 6% more damage. The Warrior gains 5.3% (1,512 → 1,592), and the Druid 0.7% (1,582 → 1,593). The search ran again for all tank sets, also with the proc items that wowsims implements. The Warrior threat set takes Ironfoe (a proc weapon), Grimy Metal Boots, Myrmidon's Signet, Royal Seal of Eldre'Thalas, Eaglehorn Long Bow and Hand of Justice. The Druid threat set takes Ouroboros Ring and Hand of Justice.

The Paladin survival set takes Intricately Runed Shield in place of Argent Defender, and five other items. The Paladin threat set does not change: Argent Defender still has the best stats. In the Paladin main hand, Flurry Axe and Ironfoe come second and third, after Hand of Edward the Odd. The Warrior survival set takes Skullflame Shield, Force Imbued Gauntlets, Hand of Justice and two other items.

Master commit 52471a100 (12 November 2026, hotfixes of 11 and 12 November) adds 69 items, for example Darrowshire Strongguard and Warmaster Legguards. Weapon procs no longer trigger from Shield Slam, Shield Bash, Thunder Clap and abilities with magic DefenseType. Lacerate now gives 10/3 threat for each point of damage, from the hit and from the ticks. Faerie Fire in Bear Form gives 2 × level threat. With the sets of 11 November, the Warrior loses 0.5% (1,632 → 1,624). The Druid gains 43% (1,614 → 2,302).

The Paladin values do not change. The search ran again for all tank sets. The Warrior threat set takes Skullflame Shield and Deep Jungle Rifle (+1.0% score). The Warrior survival set takes Ironfoe, Warmaster Legguards, Royal Seal of Eldre'Thalas, Mark of Tyranny and five other items (+0.7%). The other sets do not change.

Master commit 129fcd89e (12 November 2026 evening, hotfixes of 12 November and push 114027) changes two proc items. Hand of Justice now has its full proc chance (3%) only against Dwarves, and 1% against other targets. Ironfoe has 6% against Orcs and 3% against other targets. Weapon procs no longer trigger from melee abilities with no DefenseType.

wowsims now gives the set bonuses of 113 item sets, and adds Blackhand's Breadth. With the sets of 12 November, the Warrior loses 3.0% (1,650 → 1,601) and the Druid 1.1% (2,302 → 2,277). The Paladin values do not change: its sets have no Hand of Justice and no Ironfoe.

The search ran again for all tank sets. The Warrior survival set takes Hammer of the Vesper in place of Ironfoe, Naglering and Sentinel's Gloves (+0.7% score). The other sets stay. The threat set searches gave −0.3% to +0.06%. The Paladin survival set search gave +0.4% (Cloudkeeper Legplates), less than the 0.5% run noise.

Master commit 8c7b5a5f5 (13 November 2026, client 1.60.1.70938, hotfixes of 13 November) changes Redoubt and Shieldsworn. Each melee swing or ability against the Paladin rolls the 10% Redoubt chance, avoided attacks included. The hotfixes of 11 November make the judgements ranged attacks. The late hotfix of 13 November makes Judgement of Command a melee attack again. The tank uses Judgement of Fury, thus the tank values do not change. Since 13 November, our runs use this rule (`patches/judgement-ranged.patch`): Judgement of Righteousness and Judgement of Fury no longer trigger melee weapon procs.

The commit also adds 46 items, for example The Lion Horn of Stormwind. When the tank is struck, it has a 10% chance to give 725 armor for 30 sec. With the sets of 12 November, evening, the live Paladin gains 0.7% threat (1,133 → 1,141) and takes 2.4% less damage (336 → 328). Redoubt (C-P1) loses 0.5% (1,208 → 1,202). The Warrior and the Druid do not change. The search ran again for all tank sets.

Four sets change, all with The Lion Horn of Stormwind. The Paladin threat set takes Draconian Deflector in place of Argent Defender, Storm Gauntlets, Bolt's Charged Eyeball and four other items (+0.6% score). It has 0.2% less threat and takes 3.9% less damage. The Warrior threat set takes Scaleguard Scimitar in place of Ironfoe, Sabatons of Heroism and three other items (+2.0% score). It has 4.7% less threat and takes 8.8% less damage. The Paladin survival set (+2.3%) and the Druid survival set (+1.5%) also change.

Master commit 6084403a9 (15 November 2026, hotfixes of 15 November) changes these rules. wowsims now makes Judgement of Righteousness and Judgement of Fury ranged attacks itself. Thus, our `patches/judgement-ranged.patch` is no longer necessary. The commit also changes the rage rules. Spell damage, periodic damage and special attacks give a Warrior or a Druid two times the rage of a melee swing. The Warrior receives new flat threat values for Shield Slam and Cleave. The wowsims presets also have new default Warrior and Druid sets.

With the sets of 13 November on this commit, the live Paladin gains 1.0% threat (1,139 → 1,151). The Warrior gains 2.9% (1,525 → 1,569), and the Druid 6.7% (2,277 → 2,428). The damage taken and the crushing blows of the Paladin do not change (Analysis, Crushing blows). The commit also adds 98 items, for example the dungeon set 0.5 Soulforge and Heroism items. The search ran again for all tank sets.

Three sets change. The Warrior threat set takes Chestguard of Heroism, Force Imbued Gauntlets, Scarlet Kris and ten other items (+4.0% score). It has 6.9% more threat (1,569 → 1,678) and takes 3.0% more damage. The Warrior survival set (+6.7%) and the Druid threat set (+1.2%) also change. The Paladin sets, the Druid survival set and the Shockadin set stay: their searches gave less than 0.5%.

On 16 November, the open search ran for all six tank sets on the same commit (`tank_gear/search_open.py`). The first search changed only the slots with an item outside the pool. Thus, it did not try good pool items in the other slots. Examples are Soulforge Chestguards for the Paladin and the Heroism items for the Warrior. All six sets change:

- **Paladin threat set:** Soulforge Chestguards, Warder's Wristguards, Warder's Waistguard, Shifting Cloak, Initiate's Signet of Vigilance, Myrmidon's Signet and Flamebreak Talisman. It has 2.5% more threat (1,151 → 1,180) and takes 5% less damage (317 → 300).
- **Warrior threat set:** Lightforge Spaulders, Stoneskin Gargoyle Cape, Breastplate and Handguards of Heroism, Legplates of Valor, Valiant's Waistguard, Ironfoe, Royal Seal of Eldre'Thalas and three other items. It has 9.6% more threat (1,678 → 1,838).
- **Druid threat set:** Horn of Ve'han, Death's Clutch and Cloak of Warding. It has 0.6% more threat (2,439 → 2,454).
- **Survival sets:** the Paladin set takes Enriched Thorium Helm, Enriched Thorium Leggings, Soulforge Chestguards and three other items. The Warrior set takes Faceguard and Handguards of Heroism, Spaulders of Valor, Krol Blade and seven other items. Damage taken each sec: Paladin 302 → 294, Warrior 282 → 255, Druid 337 → 331.

Thus, the open search gives the Warrior more threat than the Paladin. With all kept proposals and the consumables of 16 November, the Paladin had 95% of the Warrior threat (first sets of 15 November: 103%). The full threat consumables of 17 November gave 109%. The values in this list use the consumables of 16 November. The epic items and the proc items of item level 31 to 44 do not improve a set. An example is Gloves of Holy Might (Paladin: −1% threat).

The values below come from master commit ad6b13af8 (18 November 2026, hotfixes of 16 and 17 November). The commit changes the proc rates of many items. Unbridled Wrath now also procs from melee abilities, thus the Warrior receives more rage. Some Paladin spell rules also change, for example the Seal of Fury coefficients. The live Paladin threat does not change with them.

With the sets of 16 November and the full threat consumables on this commit, the live Paladin has 1,396 threat each sec (no change). The Warrior gains 0.8% (1,899 → 1,914), and the Druid does not change (2,611). Thus, the live Paladin has 73% of the Warrior (was 74%), and 108% with all kept proposals (was 109%). Logs: `logs/checks_ad6b13af8_pool_full_old_sets.log` and `logs/checks_ad6b13af8_pool_surv_full_old_sets.log`.

The open search then ran again for all tank sets, with the full threat consumables. A new set replaces the old set only if its score is more than 0.5% better. Four sets change:

- **Paladin threat set:** Vigorsteel Vambraces, Warder's Gloves and Frozen Heart of the Mountain (+0.9% score). It has 0.9% less threat (1,396 → 1,384) and takes 2% less damage (296 → 291).
- **Paladin survival set:** Warder's Wristguards, Soulforge Sabatons and Initiate's Signet of Vigilance (+1.4% score). It has 0.8% more threat (1,282 → 1,292).
- **Druid threat set:** Feralheart Faceguard, Feralheart Armor, Truestrike Shoulders and Cloudrunner Girdle (+2.3% score). It has 1.4% less threat (2,611 → 2,573) and takes 4% less damage (330 → 316).
- **Druid survival set:** Feralheart Faceguard, Feralheart Armor and Horn of Ve'han (+4.0% score). It takes 5% less damage (316 → 300).

The Warrior sets (+0.2% score) and the Shockadin set (+0.05%) stay.

The tables below use the runs of 19 November: the same sets with the enchants, Gift of Arthas and the Scrolls, and the Paladin sets with Crusader and Libram of Invocation (above). Without them, the live Paladin had 1,384 threat each sec (72% of the Warrior), and 2,045 with all kept proposals (107%).


| Tank | TPS (% of the Warrior, % of the Druid) | Damage taken each sec | TMI | Crushing blows |
| --- | --- | --- | --- | --- |
| Warrior | 1,932 (100%, 72%) | 291 | 30 | 1.0% |
| Druid | 2,674 (138%, 100%) | 328 | 25.3 | 14.9% |
| Paladin, live | 1,439 (75%, 54%) | 278 | 38.5 | 10.3% |
| Paladin, Redoubt (C-P1) | 1,488 (77%, 56%) | 248 | 31.3 | 1.1% |
| Paladin, Righteous Fury (C25) | 2,050 (106%, 77%) | 278 | 38.5 | 10.3% |
| **Paladin, all kept proposals (C-P1, C-P13, C25)** | **2,119 (110%, 79%)** | **253** | **32.0** | **1.1%** |

- **The live Paladin has 75% of the Warrior threat in wowsims.** The model gives 70%. The model has no consumables. Before the notes of 2 November, they gave 101% and 108%. With the consumables of 16 November, wowsims gave 64%. On 13 November, it gave 75%, and with the first sets of 15 November 69%. The full threat consumables give the Paladin +18% and the Warrior +3% (17 November: 74%). The enchants of 18 November evening give the Paladin +4% and the Warrior +1% (no enchants: 72%). With Revelation on the weapon (18 November evening), the Paladin had 76%.
- **The Argent Defender error.** From 8 to 10 November, wowsims gave the live Paladin 55% block in place of 41%, and 5% more threat. It had 5.6% crushing blows in place of 12.0%. Now the live Paladin blocks 42% of the swings and takes 10.3% crushing blows (Analysis, Crushing blows). Since 13 November, its threat set has Draconian Deflector in place of Argent Defender. Hand of Edward the Odd gives 90 spell damage.
- **The Druid has 138% of the Warrior threat.** Master 52471a100 gives Lacerate 10/3 threat for each point of damage, and the Druid gains 43% (99% → 140% of the Warrior). On master 129fcd89e, the Warrior loses more threat than the Druid from the Hand of Justice change (142%). On master 8c7b5a5f5, the new Warrior set has less threat (149%). On master 6084403a9, both classes gain threat (145%). The open search of 16 November gives the Warrior more threat (134%). The full threat consumables of 17 November give the Druid more threat than the Warrior (137%). On master ad6b13af8, the Warrior gains rage, and the new Druid set has less threat (134%). The enchants of 18 November evening give the Druid more threat than the Warrior (138%). wowsims measured this rule in the game only on rank 2 in Bear Form, at levels 38 to 50. Its note says that the later ranks in Dire Bear Form fit 10/3 only in part. A test at level 60 must confirm it (Open items).
- **Where the Druid gain comes from.** On both commits, the Druid has the same set and rotation: 80 Lacerate casts in 3 min. The Lacerate hit goes from 175 to 585 threat each sec (×10/3). The Lacerate ticks go from 65 to 349 threat each sec. Since 12 November, a Lacerate dose keeps the tick timer of the bleed, thus the ticks do 62% more damage.

  Maul, Primal Bite and the melee hits do not change. Lacerate now gives 41% of the Druid threat (was 15%). Log: `logs/druid_threat_by_ability_52471a100.log`.
- **wowsims applies its rules correctly.** Each ability has the threat for each point of damage that its rule gives: melee hits 2.15 (Bear Form +115%), Maul 3.76 (×1.75), Primal Bite 6.45 (×3), Lacerate hit and ticks 7.17 (×10/3). Our runs give the same values as the wowsims runs. The only open point is the Lacerate rule at level 60.
- **Bonus threat of the abilities (16 November).** Each tank has a base multiplier: Warrior ×2.16, Druid ×2.15, Paladin ×1.33 (Holy damage ×2.53). Some abilities add threat above damage × this multiplier. The stance or form multiplier also applies to this bonus threat. Log: `logs/threat_sources_6084403a9.log` (consumables of 16 November).

  | Tank | Threat each sec | Damage × multiplier | Bonus threat | Largest bonus |
  | --- | --- | --- | --- | --- |
  | Warrior | 1,838 | about 1,250 | about 535 (29%) | Revenge 367, Heroic Strike 97, Shield Slam 71 |
  | Druid | 2,454 | about 1,050 | about 1,300 (53%) | Lacerate ticks 424, Primal Bite 322, Maul 309, Lacerate hit 243 |
  | Paladin, live | 1,180 | about 1,050 | about 76 (6%) | Holy Shield 40 (×1.2), Holy Strike 36 (Iron Creed) |

  Without the bonus threat, the live Paladin has about 91% of the Warrior and 103% of the Druid. Thus, the bonus threat of the abilities causes most of the gap, and the raise of 2 November multiplies it. Most Druid bonus values come from player data or from the wowsims Lacerate rule. A test at level 60 must confirm them. The game files give Judgement of Fury a third effect (1,691 + 18% of spell power) that wowsims does not use (Open items). If it is bonus threat, it adds about 200 TPS to the Paladin.
- **If the Lacerate rule is different at level 60 (commit 52471a100).** wowsims notes that rank 5 in Dire Bear Form fits 10/3 only in part. With ×2 in place of ×10/3, the Druid has 1,929 threat each sec (117% of the Warrior). With no Lacerate bonus, it has 1,649 (100%). The live Paladin then has 59% and 69% of the Druid. With C25 and C-P1, it has 89% and 104%.
- **The Druid values before 12 November.** wowsims master 9a8624af9 gives Bear Form +115% and Maul ×1.75, Swipe ×1.75 and Primal Bite ×3. Master 9f254e8d8 decreases the Druid threat by 10% (118% → 105% of the Warrior). Master 3633d376a gives the Warrior Shield Slam flat threat (105% → 101%). Hand of Justice in the Warrior set gives 99%. The earlier runs gave Bear Form only, and the Druid had 77% of the Warrior.
- **The consumables give the Paladin +36% threat and −23% damage taken.** Without them (Demonic Rune only), the live Paladin had 1,029 TPS and 384 damage taken each sec (set of 4 November). With the consumables of 4 to 16 November, it had +10% threat.
- **With Redoubt (C-P1), the Paladin takes 15% less damage than the Warrior** (248 against 291 each sec). Its TMI is a little higher (31.3 against 30): the Warrior TMI decreases with the full consumables (37 → 31) and on master ad6b13af8 (30). The live Paladin takes 5% less damage than the Warrior. With all kept proposals, it takes 13% less damage than the Warrior (253 against 291). Without the enchants, these values were 11%, 1% and 10%. The open search sets of 16 November give the Paladin 5% less damage taken (317 → 300) and the Warrior 1% less (296 → 294).
- **Redoubt adds less in wowsims:** +49 TPS (+3%) against +96 TPS (+15%) in the model. The model gives too many Holy Shield blocks. The live Paladin blocks 42% of the swings (Redoubt: 54%). Since 13 November, the live Redoubt rolls on more attacks, thus C-P1 adds less (+7% before).
- **Righteous Fury (C25) multiplies all Paladin threat by 1.43.** With all kept proposals, the Paladin has 110% of the Warrior threat and 79% of the Druid. The model gives 115% of the Warrior (part 1).
- **Holy Shield rank 4 adds 6% in wowsims.** With the default set and rank 3 (wowsims of 1 November), the live Paladin had 928 TPS. With rank 4, it had 980 TPS.
- **C1 (withdrawn) agrees:** +26 in wowsims of 1 November, +25 in the model. The C1 flag does not run on commit d97252f2a.
- **Reckoning (C-P12), withdrawn.** With C1, it gave +27 more in wowsims of 1 November and +20 in the model.
- **Toughness removal (C-P13)** does not change threat. Damage taken increases by 2%.

**Survival sets.** The same runs with the survival set of each class. All three tanks have Greater Stoneshield Potion.

| Tank | TPS (% of the Warrior, % of the Druid) | Damage taken each sec | TMI | Crushing blows |
| --- | --- | --- | --- | --- |
| Warrior | 1,601 (100%, 67%) | 237 | 23 | 0.9% |
| Druid | 2,406 (150%, 100%) | 276 | 20.1 | 15.1% |
| Paladin, live | 1,302 (81%, 54%) | 227 | 26.5 | 8.6% |
| Paladin, Redoubt (C-P1) | 1,335 (83%, 55%) | 206 | 22.6 | 0.9% |
| Paladin, Righteous Fury (C25) | 1,854 (116%, 77%) | 227 | 26.5 | 8.6% |
| **Paladin, all kept proposals (C-P1, C-P13, C25)** | **1,900 (119%, 79%)** | **209** | **23.1** | **0.9%** |

- **The threat order does not change.** The Paladin loses 10% threat with its survival set (1,439 → 1,302), the Warrior 17% (1,932 → 1,601) and the Druid 10% (2,674 → 2,406). Thus, with the survival sets the Paladin has 81% (live) and 119% (all kept proposals) of the Warrior.
- **The TMI decreases for all three tanks:** Paladin 38.5 → 26.5 (live) and 32.0 → 23.1 (all kept proposals), Druid 25.3 → 20.1, Warrior 30 → 23.
- **With Redoubt (C-P1), the Paladin takes 13% less damage than the Warrior** (206 against 237 each sec), and its TMI is a little lower (22.6 against 23). The live Paladin takes 4% less damage. Before 18 November evening, only the Druid had Greater Stoneshield Potion, and the Paladin with Redoubt took 2% more damage than the Warrior. With the first survival sets of 15 November, Redoubt gave 4% less damage than the Warrior.
- **C25a (+80%)** gives 110% of the Warrior (live) and 113% with C-P1 (threat sets: 101% and 104%).

**Other fights (wowsims, 3 min, item pool threat sets, full threat consumables, enchants).** TPS, % of the Warrior in brackets. "Fast" is a swing each 1.2 sec with 60% damage, thus the same damage each sec. "Two weapons" is a boss with a second weapon. The 5 min row has C-P1 only: Toughness removal (C-P13) does not change threat.

| Boss | Warrior | Paladin, live | Paladin, C-P1 and C-P13 | Paladin, all kept proposals (×1.43) |
| --- | --- | --- | --- | --- |
| Normal, 5 min | 1,906 | 1,438 (75%) | 1,485 (78%) | 2,121 (111%) |
| Fast | 2,019 | 1,578 (78%) | 1,613 (80%) | 2,305 (114%) |
| Two weapons | 2,041 | 1,631 (80%) | 1,655 (81%) | 2,364 (116%) |
| Fast, two weapons | 2,162 | 1,740 (80%) | 1,744 (81%) | 2,491 (115%) |

- **Faster boss attacks help the Warrior and the Paladin.** The Warrior receives more rage. The Paladin blocks more, thus Holy Shield hits more.
- **Against a boss with two weapons, Redoubt adds little threat** (+0.2% to +1.5%). The Holy Shield charges are empty too soon (Crushing blows, part 3).

**Other Seals (wowsims, 3 min, item pool threat set of the first search of 15 November, consumables of 16 November).** Threat each sec, damage taken each sec and TMI. Seal of Command needs a build with 13 Retribution points: [`b201005-05302102213301531-50223001`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b201005-05302102213301531-50223001). It takes Conviction 2, Sanctified Judgement 3 and Seal of Command in place of Divine Strength 4 and Holy Conduit 2.

| Build and Seal | Live: threat | Live: damage taken | Live: TMI | C25 and C-P1: threat |
| --- | --- | --- | --- | --- |
| Live build, Seal of Fury | 1,151 | 317 | 50.5 | 1,721 |
| Live build, Seal of Righteousness | 1,136 (−1.3%) | 328 | 52.6 | 1,698 (−1.4%) |
| Seal of Command build, Seal of Fury | 1,173 | 316 | 50.4 | 1,753 |
| Seal of Command build, Seal of Righteousness | 1,158 (−1.3%) | 329 | 52.7 | 1,729 (−1.4%) |
| Seal of Command build, Seal of Command | 1,085 (−7.5%) | 333 | 53.4 | 1,622 (−7.5%) |

- **Seal of Fury stays the best tank Seal.** Seal of Righteousness gives 1.3% less threat, and Seal of Command 7.5% less. The proposals do not change this order.
- **The other Seals also cost survival.** Without the Seal of Fury absorb shield, the Paladin takes 4–5% more damage, and the TMI increases by 2–3 points.
- **Seal of Command procs only on a part of the swings.** Seal of Fury and Seal of Righteousness hit on each swing. Judgement of Command is a melee attack, and Judgement of Righteousness is a ranged attack. Since 15 November, the Windfury Totem strike also triggers the Seals in wowsims, thus Seal of Command gains 1.9% (other Seals: 1.0–1.2%).
- **The Seal of Command build has more threat with Seal of Fury** (+1.9% against the live build, 1,173 against 1,151). It has almost the same values as BS1 with the same set (Builds, first sets of 15 November: 1,171 threat, 319 damage taken). Against BS2 (1,165), it has +0.7% threat, but 2.3% more damage taken (316 against 309). Thus, BS2 stays the tank build.
- **Files.** `models/wowsims-b2/apl/sor.apl.siml` and `soc.apl.siml` (flag `FEEDBACK_APL`), log `logs/seals_6084403a9.log` (13 November: `logs/seals_8c7b5a5f5.log`).

**Seals and weapon speed (same settings, first threat set of 15 November, consumables of 16 November, main hand replaced).** Threat each sec. The percent is the difference against Seal of Fury with the same weapon and build.

| Main hand | Speed | Live: Fury | Live: Righteousness | SoC build: Fury | SoC build: Righteousness | SoC build: Command |
| --- | --- | --- | --- | --- | --- | --- |
| Flurry Axe | 1.5 | 1,132 | 1,108 (−2.1%) | 1,153 | 1,129 (−2.1%) | 1,052 (−8.8%) |
| Hand of Edward the Odd (set, +90 spell damage) | 1.6 | 1,151 | 1,136 (−1.3%) | 1,173 | 1,158 (−1.3%) | 1,085 (−7.5%) |
| Masterwork Stormhammer | 1.6 | 1,102 | 1,086 (−1.5%) | 1,123 | 1,107 (−1.5%) | 1,055 (−6.0%) |
| Phase Blade | 2.1 | 1,062 | 1,070 (+0.7%) | 1,081 | 1,088 (+0.7%) | 1,069 (−1.1%) |
| Ironfoe | 2.4 | 1,080 | 1,099 (+1.8%) | 1,098 | 1,117 (+1.7%) | 1,121 (+2.1%) |
| Mastersmith's Hammer (+68 spell damage) | 2.4 | 1,080 | 1,095 (+1.5%) | 1,096 | 1,112 (+1.4%) | 1,098 (+0.1%) |
| Elderwild Construction Hammer (+68 spell damage) | 2.4 | 1,073 | 1,091 (+1.6%) | 1,091 | 1,110 (+1.7%) | 1,091 (−0.1%) |
| Masterwork Crimson Hammer | 2.4 | 1,054 | 1,072 (+1.7%) | 1,070 | 1,089 (+1.8%) | 1,073 (+0.3%) |
| Hammer of the Vesper | 2.5 | 1,052 | 1,073 (+2.0%) | 1,068 | 1,090 (+2.0%) | 1,097 (+2.7%) |
| Frostguard | 2.8 | 1,046 | 1,073 (+2.6%) | 1,061 | 1,089 (+2.6%) | 1,114 (+5.0%) |
| Sword of Zeal | 2.8 | 1,051 | 1,078 (+2.6%) | 1,065 | 1,094 (+2.7%) | 1,119 (+5.1%) |

- **Seal of Righteousness and Seal of Command increase with a slow weapon.** With a 2.8 sec weapon, Seal of Righteousness gives +2.6% and Seal of Command +5.0% against Seal of Fury. With a 1.5–1.6 sec weapon, Seal of Righteousness gives −1.3 to −2.1%, and Seal of Command −6 to −9%.
- **The change point is at approximately 2 sec for Seal of Righteousness and 2.4 sec for Seal of Command.** Above this speed, the Seal is better than Seal of Fury with the same weapon.
- **The weapon is more important than the Seal.** Hand of Edward the Odd with Seal of Fury stays the best (1,173 in the Seal of Command build). The best slow weapon with its best Seal (Sword of Zeal, Seal of Command) gives 1,119, 5% less. Hand of Edward the Odd has +90 spell damage, and the Holy spells give most of the tank threat.
- **A fast weapon increases the damage taken.** With Hand of Edward the Odd, the boss swings 81.4 times in 3 min, against 79 with a 2.4–2.8 sec weapon. The damage taken is 3% more (317 against 307–309).
- **Log.** `logs/seals_weapons_6084403a9.log` (13 November: `logs/seals_weapons_8c7b5a5f5.log`).

## 7. Groups of enemies

This part compares the tanks against 3 and 5 enemies.

- **Main target:** the enemy that the tank attacks.
- **Lowest target:** the enemy with the least threat. A healer or a damage dealer pulls this enemy first. Thus, it shows how well a tank holds a group.

**Area spells**

| Class | Spell | What it does |
| --- | --- | --- |
| Warrior | Thunder Clap rank 6 | 103 + 7% of Attack Power to 4 targets, 6 sec cooldown, 20 rage. Armor decreases it |
| Warrior | Cleave rank 5 | Weapon damage + 50 to 2 targets, 20 rage |
| Druid | Swipe rank 5 | 83 + 3% of Attack Power to 3 targets, 15 rage, ×1.75 threat (player data) |
| Paladin | Consecration rank 5 | 96 Holy damage to all enemies. The first 4 enemies also take 216 + 33.6% of spell power. 565 mana each 8 sec |
| Paladin | Holy Shield rank 4 | Damage to the attacker on each block. 4 charges each 10 sec. The Shieldsworn trigger hits the Holy Strike target |

**wowsims result.** Item pool tank sets, the full threat consumables and the enchants (part 6). Each enemy is level 63 and hits for 1/3 of a boss hit. The Paladin uses its default rotation with Consecration. The values are TPS on each target, with the main target first. All values come from commit ad6b13af8 (part 6).

| Tank | 1 target | 3 targets | 5 targets |
| --- | --- | --- | --- |
| Paladin, live | 1,439 | 1,398 / 370 / 370 | 1,381 / 326 / 326 / 325 / 180 |
| Paladin, proposed | 2,119 | 1,996 / 530 / 530 | 1,967 / 464 / 465 / 465 / 256 |
| Warrior | 1,838 | 1,823 / 571 / 173 | 1,866 / 686 / 163 / 163 / 94 |
| Druid | 2,215 | 1,641 / 547 / 536 | 2,084 / 398 / 391 / 80 / 80 |

- **On the lowest target, the Paladin still leads the Warrior.** On 3 targets, the live Paladin has 2.1 times the Warrior threat, but only 69% of the Druid. On 5 targets, it has 1.9 times the Warrior threat and 2.3 times the Druid threat.
- **The proposed Paladin leads by more.** On the lowest target, it has 3.1 times the Warrior threat on 3 targets and 2.7 times on 5 targets. It has 99% of the Druid on 3 targets and 3.2 times on 5 targets.
- **In total, the live Paladin is last.** On 3 targets: live Paladin 2,139, Warrior 2,568, Druid 2,725. On 5 targets: live Paladin 2,538, Warrior 2,973, Druid 3,033.
- **The proposed Paladin has more than the Warrior and the Druid totals.** On 3 targets: 3,055 (119% of the Warrior, 112% of the Druid). On 5 targets: 3,616 (122% of the Warrior, 119% of the Druid). The open search sets of 16 November give the Warrior 18% more total threat on 3 targets (2,034 → 2,391), mostly on the second target.
- **Redoubt changes almost nothing on groups:** less than 1%. On extra targets, all Holy Shield charges are already used in the live version. The gain comes from Righteous Fury (C25).
- **The fifth enemy has less Paladin threat** because Consecration gives its full damage to 4 enemies only.
- **The Warrior** holds only 2 targets well: Cleave hits 2 targets. **The Druid** holds only 3: Swipe hits 3 targets. Since 15 November, the Druid puts more threat on the second and third targets, and less on the main target. On 3 targets, the other targets went from 277–280 to 477–486 (511–519 with the full threat consumables on master ad6b13af8, 536–547 with the enchants).

**Model result.** The model gives a larger Paladin lead. The live Paladin has 115–149% of the stronger of the two other tanks on all targets. The proposed Paladin has 165–214%. The model lead is too large. In the model, trash hits for only 1/3 of a boss hit, thus the Warrior and the Druid receive little rage.

| Gear level | 3 targets: Warrior | Druid | Paladin, live | Paladin, proposed | 5 targets: Warrior | Druid | Paladin, live | Paladin, proposed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fresh 60 | 705 | 716 | 1,064 | 1,529 | 883 | 813 | 1,198 | 1,720 |
| Pre-raid best | 799 | 820 | 1,123 | 1,617 | 956 | 908 | 1,262 | 1,814 |
| Molten Core | 906 | 917 | 1,183 | 1,703 | 1,046 | 1,004 | 1,326 | 1,907 |
| Blackwing Lair | 996 | 1,009 | 1,256 | 1,809 | 1,160 | 1,120 | 1,407 | 2,024 |
| Naxxramas | 1,095 | 1,107 | 1,320 | 1,901 | 1,290 | 1,250 | 1,476 | 2,124 |

Values are TPS on all targets. Without Consecration, the proposed Paladin has 119–146% of the stronger tank on 3 targets, and 101–117% on 5 targets.

**Conclusion.** Against 3 or more enemies, the Paladin holds the extra enemies better than the Warrior. On 5 targets, it holds them better than the Druid too. The live total threat is the lowest of the three tanks. The problem is the main target (parts 1 and 6). With Righteous Fury (C25), the Paladin has more than the Warrior total (119–122%) and the Druid total (112–119%). On the main target, it has 109% of the Warrior on 3 targets and 105% on 5 targets.

## 8. Burst threat

This part compares the threat in the first seconds of a pull and in the best short windows of a fight. A damage dealer pulls the boss when it has more threat than the tank. At the start of a pull, and after a large threat spike, this can occur before the sustained values of part 6 apply.

**Setup.** wowsims, as in part 6: item pool tank sets, the full threat consumables, the enchants, full buffs, one level 63 boss from the front, 3 min fight, 3,000 iterations. A recorder adds the threat on the boss in steps of 0.1 sec. All values come from commit ad6b13af8 with the tank sets and enchants of 18 November, except the Warrior variants of commit 6ee3c30f35 (default sets).

- **Warrior.** Default rotation, 0 rage at the pull. Bloodrage at −1.5 sec.
- **Druid.** Default rotation, 25 rage at the pull.
- **Goblin Sapper Charge.** All three tanks have it in their consumables, and the sim uses it at the pull. The Warrior and the Paladin also have the EZ-Thro Dark Bomb.
- **Boss armor.** The boss has no armor debuff at the pull. Only a Warrior (Sunder Armor) or a Rogue (Expose Armor) can apply it. wowsims adds 1 Sunder Armor stack each 1.5 sec, thus 5 stacks at 6 sec.

**The Paladin openers**

| Opener | Before the pull | First casts |
| --- | --- | --- |
| wowsims default | Seal of the Crusader at −1.5 sec | 0 sec: Judgement of the Crusader, then Seal of Fury. 1.5 sec: Swift Judgement (Judgement of Fury), Consecration. 3 sec: Holy Shield. 4.5 sec: Holy Strike |
| Fury opener | Seal of Fury at −3 sec, Holy Shield at −1.5 sec | 0 sec: Judgement of Fury, Swift Judgement, Holy Strike (with the Shieldsworn Holy Shield hit). 1.5 sec: Consecration. Then the default order |

Judgement and Swift Judgement are not on the global cooldown, thus both hit at 0 sec. The Fury opener does not use Judgement of the Crusader. The raid debuffs of the sim already have it. With the item pool set, the 3 min threat of the Fury opener is 2% higher.

**Threat in the first seconds** (threat on the boss, % of the Warrior)

| Tank | First 1.5 sec | First 3 sec | First 6 sec | First 10 sec | First 20 sec | 3 min (TPS) |
| --- | --- | --- | --- | --- | --- | --- |
| Warrior | 4,141 (100%) | 9,043 (100%) | 14,087 (100%) | 24,464 (100%) | 45,047 (100%) | 1,927 (100%) |
| Druid | 5,725 (138%) | 8,833 (98%) | 13,734 (97%) | 23,234 (95%) | 52,018 (115%) | 2,665 (138%) |
| Paladin, live, wowsims opener | 1,640 (40%) | 4,489 (50%) | 9,333 (66%) | 14,892 (61%) | 29,863 (66%) | 1,439 (75%) |
| Paladin, live, Fury opener | 7,573 (183%) | 8,974 (99%) | 11,663 (83%) | 19,342 (79%) | 33,997 (75%) | 1,463 (76%) |
| Paladin, proposed, wowsims opener | 2,335 (56%) | 6,386 (71%) | 13,575 (96%) | 21,846 (89%) | 43,887 (97%) | 2,120 (110%) |
| Paladin, proposed, Fury opener | 10,952 (264%) | 13,150 (145%) | 17,303 (123%) | 28,608 (117%) | 49,940 (111%) | 2,158 (112%) |

- **With the wowsims default opener, the Paladin starts slowly.** The first global cooldown goes to Judgement of the Crusader. Holy Shield starts at 3 sec, and Holy Strike at 4.5 sec.
- **With the Fury opener, the Paladin has the best start of the three tanks in the first 1.5 sec.** Two Judgements of Fury, Holy Strike, the Shieldsworn Holy Shield hit and the explosives hit the boss at the pull.
- **The live lead does not last.** After 3 sec, the live Fury opener has 99% of the Warrior, and after 10 sec 79%. After 20 sec, it has 75%, near the sustained gap of part 6.
- **The proposed Paladin keeps the lead.** With the Fury opener, it has 145% of the Warrior after 3 sec, 117% after 10 sec and 111% after 20 sec. In the first 3 sec, all of the gain comes from Righteous Fury (C25). Redoubt starts after the first blocks.
- **The Druid starts fast, and it is first after 20 sec.** It uses its 25 rage at once: it has 138% of the Warrior in the first 1.5 sec, then 95–98% from 3 to 10 sec. After 20 sec, it has 115% of the Warrior, and the proposed Paladin with the Fury opener 111%. Without the enchants, the Druid had 99% in the first 1.5 sec. The Lacerate threat of 12 November gives the Druid this gain (part 6).
- **The Warrior set of 16 November starts faster.** After 3 sec, the Warrior has 9,043 threat (no enchants: 8,981; 17 November: 8,936; consumables of 16 November: 8,640; first set of 15 November: 6,677). Ironfoe and the new set give more hits and more rage at the pull.
- **The Warrior needs rage first.** It starts with 0 rage. Its threat increases fast from 2 sec, when the boss hits give rage.
- **Boss armor helps the Paladin.** In the first 6 sec, the boss has less than 5 Sunder Armor stacks. This decreases Warrior and Druid physical damage. Most Paladin threat is Holy damage, thus boss armor does not decrease it.
- **With one Judgement at 0 sec,** Swift Judgement hits at 1.5 sec. Only the first 1.5 sec change: 5,812 threat (140%) in place of 7,573. From 3 sec, the two openers have the same threat.

**Bad pulls** (threat on the 10% worst fights, % of the Warrior on its 10% worst fights)

| Tank | First 3 sec | First 6 sec | First 10 sec |
| --- | --- | --- | --- |
| Warrior | 4,727 (100%) | 9,209 (100%) | 17,348 (100%) |
| Druid | 4,916 (104%) | 8,946 (97%) | 16,105 (93%) |
| Paladin, live, wowsims opener | 3,286 (70%) | 7,016 (76%) | 12,096 (70%) |
| Paladin, live, Fury opener | 6,811 (144%) | 9,166 (100%) | 16,003 (92%) |
| Paladin, proposed, Fury opener | 10,020 (212%) | 13,666 (148%) | 23,802 (137%) |

- **A bad pull costs the Warrior and the Druid the most.** When their first attacks miss or the boss attacks miss them, they have no rage. The Warrior threat after 3 sec decreases to 52% of its mean. The Druid keeps 56%, and the live Paladin 73–76%.
- **A bad pull costs the Paladin less.** Judgement of Fury cannot be dodged or parried. Holy Shield and Seal of Fury cannot miss.

**Best short windows** (the highest threat in a window at any time in the 3 min fight, % of the Warrior)

| Tank | Best 3 sec | Best 6 sec | Best 10 sec | Best 3 sec ÷ mean 3 sec |
| --- | --- | --- | --- | --- |
| Warrior | 16,651 (100%) | 23,275 (100%) | 32,456 (100%) | ×2.9 |
| Druid | 19,264 (116%) | 28,982 (125%) | 42,029 (129%) | ×2.4 |
| Paladin, live, wowsims opener | 10,275 (62%) | 14,663 (63%) | 22,212 (68%) | ×2.4 |
| Paladin, live, Fury opener | 10,927 (66%) | 14,770 (63%) | 22,655 (70%) | ×2.5 |
| Paladin, proposed, wowsims opener | 14,896 (89%) | 21,384 (92%) | 32,398 (100%) | ×2.3 |
| Paladin, proposed, Fury opener | 15,920 (96%) | 21,588 (93%) | 33,147 (102%) | ×2.5 |

- **The Paladin has no threat cooldown.** Its best windows come from Holy Strike, Judgement and Holy Shield in the same 3 sec, with critical hits. The Warrior adds Shield Slam, Revenge and Heroic Strike critical hits to the rage from boss hits. The Druid has larger windows than the Warrior (116–129%), from Maul, Primal Bite and Lacerate.
- **The best-window gap is larger than the sustained gap.** Live: 62–70% against 75%. Proposed: 89–102% against 110%. Thus the Paladin has a smaller margin against a large threat spike from a damage dealer.

**Warrior variants**

| Warrior | First 1.5 sec | First 3 sec | First 6 sec | First 10 sec |
| --- | --- | --- | --- | --- |
| Default, with Goblin Sapper Charge (above) | 4,141 | 9,043 | 14,087 | 24,464 |
| No Engineering items | 4,603 (+11%) | 8,532 (−6%) | 13,019 (−8%) | 23,067 (−6%) |
| Default set, no engineering items, commit 6ee3c30f35 | 1,968 | 4,609 | 6,962 | 12,881 |
| Default set, Charge at −0.5 sec, 20 yards (Vanguard), commit 6ee3c30f35 | 1,711 (−13%) | 4,213 (−9%) | 7,223 (+4%) | 13,354 (+4%) |

- **Charge does not increase the Warrior burst.** Charge gives 15 rage, but this rage gives no threat. The Charge stun also delays the first boss swings, thus the Warrior receives less rage from boss hits. The Charge rotation does not run on commits 8298ab833, 9a8624af9, ae9b8c23a, 9f254e8d8, 3633d376a, 52471a100, 129fcd89e, 8c7b5a5f5, 6084403a9 and ad6b13af8: the Warrior does almost no attacks. Thus, the Charge row comes from commit 6ee3c30f35 with the default Warrior set, and its % compare it with the default rotation of that commit. The two rows of commit 6ee3c30f35 are wowsims values × 1.445 (the Warrior multipliers of the notes of 2 November).
- **Charge in combat.** With Vanguard, the Warrior can charge in Defensive Stance. The Vanguard Charge row in the game files still has the "not in combat" attribute. Thus the Warrior can charge only at the pull. A test in the game must confirm this.

**Tank swaps.** Shoulder the Burden (C-P5) moves 50% of the threat of an ally to the Paladin. After 30 sec, the Warrior has about 50,000 threat. Shoulder the Burden on the Warrior then gives the Paladin about 25,000 threat at once. This is 2.4 times the best 3 sec live Paladin window. It does not help at the pull, because no ally has threat yet.

**Conclusion.** With a Fury opener, the proposed Paladin holds the boss at the pull better than the Warrior and the Druid. The live Paladin leads only in the first 1.5 sec. The default opener of wowsims gives it 50% of the Warrior threat in the first 3 sec. After 10 sec, the sustained gap of part 6 returns.

In short windows later in the fight, the live Paladin has 62–70% of the Warrior. The proposed Paladin keeps the lead on the Warrior over the pull, and has 89–102% of the Warrior in short windows. The Druid passes the Warrior after 10 to 20 sec, and its short windows are larger than the Warrior windows.

## 9. Righteous Fury alone: +90% (C25) and +80% (C25a)

This part gives parts 1 to 8 again with Righteous Fury (C25) alone, and with the live trees: all threat +90% in place of +33%. The alternative C25a gives +80%, the value of Defensive Stance.

- **Righteous Fury multiplies all Paladin threat.** Thus, C25 multiplies each Paladin value of the model by 1.43 (1.9 ÷ 1.33), and C25a by 1.35 (1.8 ÷ 1.33).
- **The wowsims values come from new runs.** C25 multiplies the wowsims threat by 1.43, and C25a by 1.35.
- **The Warrior and Druid values do not change.** They use the notes of 2 November, as in parts 1 to 8. The wowsims values are native values of commit ad6b13af8.

**One boss, same gear (model, part 1).** Boss hit of 4,500 before armor. The cells give TPS, then % of the Warrior and of the Druid. The last column gives % of the Warrior at 3,000 and 6,000 hits.

| Paladin | Live (+33%) | C25 (+90%) | C25a (+80%) | C25 / C25a at 3,000 and 6,000 hits |
| --- | --- | --- | --- | --- |
| Live | 661 (70%, 77%) | 944 (100%, 110%) | 895 (95%, 104%) | 113%, 97% / 108%, 92% |
| Live, no Crusader | 589 (62%, 68%) | 841 (89%, 98%) | 797 (85%, 93%) | 101%, 86% / 96%, 82% |
| Proposed (C2, C-P1) | 757 (80%, 88%) | 1,081 (115%, 126%) | 1,025 (109%, 119%) | 130%, 111% / 123%, 105% |
| Proposed, with Consecration | 880 (93%, 102%) | 1,257 (133%, 146%) | 1,191 (126%, 138%) | 151%, 129% / 143%, 122% |

- **With C25, the live Paladin has the Warrior threat at 4,500 hits** (100%). Against faster boss hits (6,000), it has 97%. With C25a, it has 95% and 92%.
- **Without Crusader,** C25 gives 89% and C25a 85%. Personal Judgement of the Crusader (C2) is still important.

**From fresh 60 to Naxxramas (model, part 2), C25 (+90%).** TPS, then % of the Warrior and of the Druid.

| Gear level | Warrior | Druid | Paladin, live | Paladin, live, no Crusader | Paladin, proposed | Paladin, proposed, with Consecration |
| --- | --- | --- | --- | --- | --- | --- |
| Fresh 60 | 775 | 681 | 909 (117%, 133%) | 800 (103%, 117%) | 1,043 (135%, 153%) | 1,220 (157%, 179%) |
| Pre-raid best | 874 | 806 | 980 (112%, 122%) | 876 (100%, 109%) | 1,119 (128%, 139%) | 1,303 (149%, 162%) |
| Molten Core | 996 | 934 | 1,047 (105%, 112%) | 944 (95%, 101%) | 1,191 (120%, 128%) | 1,381 (139%, 148%) |
| Blackwing Lair | 1,085 | 1,051 | 1,127 (104%, 107%) | 1,024 (94%, 97%) | 1,274 (117%, 121%) | 1,476 (136%, 140%) |
| Naxxramas | 1,185 | 1,167 | 1,196 (101%, 102%) | 1,091 (92%, 94%) | 1,347 (114%, 115%) | 1,556 (131%, 133%) |

**From fresh 60 to Naxxramas (model, part 2), C25a (+80%).** TPS, then % of the Warrior and of the Druid.

| Gear level | Warrior | Druid | Paladin, live | Paladin, live, no Crusader | Paladin, proposed | Paladin, proposed, with Consecration |
| --- | --- | --- | --- | --- | --- | --- |
| Fresh 60 | 775 | 681 | 861 (111%, 126%) | 758 (98%, 111%) | 988 (127%, 145%) | 1,156 (149%, 170%) |
| Pre-raid best | 874 | 806 | 928 (106%, 115%) | 830 (95%, 103%) | 1,060 (121%, 131%) | 1,234 (141%, 153%) |
| Molten Core | 996 | 934 | 992 (100%, 106%) | 895 (90%, 96%) | 1,129 (113%, 121%) | 1,309 (131%, 140%) |
| Blackwing Lair | 1,085 | 1,051 | 1,068 (98%, 102%) | 970 (89%, 92%) | 1,207 (111%, 115%) | 1,398 (129%, 133%) |
| Naxxramas | 1,185 | 1,167 | 1,133 (96%, 97%) | 1,034 (87%, 89%) | 1,276 (108%, 109%) | 1,474 (124%, 126%) |

- **C25 gives the live Paladin 101–117% of the Warrior threat,** from Naxxramas to fresh 60. Before the notes of 2 November, it had 101–118%. Thus, C25 gives the same positions again.
- **C25a gives 96–111%.** The live Paladin is below the Warrior from Blackwing Lair. With Redoubt (C-P1), it has 108–127%.
- **The proposed Paladin with C25 has 114–135%.** The model gives too many Holy Shield blocks (part 6). In wowsims, Redoubt adds 5%, not 15%.

**Flatter gear (model, part 3).** % of the Warrior, then % of the Druid in brackets. Columns as in part 3: gear as in part 2 / flatter gear, boss hits as in part 2 / flatter gear, flatter boss hits.

| Gear level | C25 (+90%) | C25a (+80%) |
| --- | --- | --- |
| Live, Naxxramas | 101% (103%) / 99% (103%) / 103% (109%) | 96% (97%) / 93% (97%) / 97% (103%) |
| Proposed, fresh 60 | 134% (153%) / 134% (153%) / 134% (153%) | 127% (145%) / 127% (145%) / 127% (145%) |
| Proposed, pre-raid best | 129% (139%) / 129% (139%) / 129% (139%) | 122% (131%) / 122% (131%) / 122% (131%) |
| Proposed, Molten Core | 120% (127%) / 119% (129%) / 123% (133%) | 114% (120%) / 112% (122%) / 116% (126%) |
| Proposed, Blackwing Lair | 117% (121%) / 116% (123%) / 119% (127%) | 111% (115%) / 110% (116%) / 112% (120%) |
| Proposed, Naxxramas | 114% (116%) / 111% (117%) / 117% (123%) | 108% (110%) / 106% (111%) / 111% (116%) |

- **Flatter gear changes the result by 3 points or less,** as in part 3. With C25, the weakest live case has 99% of the Warrior. With C25a, it has 93%.

**wowsims, one boss (part 6).** New runs, item pool tank sets, the full threat consumables, the enchants, 3 min, 3,000 iterations. Damage taken and TMI do not change with Righteous Fury. The cells give TPS, then % of the Warrior and of the Druid.

| Paladin | Live (+33%) | C25 (+90%) | C25a (+80%) |
| --- | --- | --- | --- |
| Live | 1,439 (75%, 54%) | 2,050 (106%, 77%) | 1,943 (101%, 73%) |
| Redoubt (C-P1) | 1,488 (77%, 56%) | 2,119 (110%, 79%) | 2,009 (104%, 75%) |
| All kept proposals (with C-P13) | 1,488 (77%, 56%) | 2,119 (110%, 79%) | 2,009 (104%, 75%) |

The Warrior has 1,932 and the Druid 2,674 (commit ad6b13af8, tank sets of 18 November, full threat consumables, enchants of 18 November evening, Paladin weapon enchant and libram of 19 November).

- **C25: the live Paladin has 106% of the Warrior threat** in wowsims, and 110% with Redoubt (C-P1). The model gives 100%. Against the Druid, it has 77% and 79% (part 6). With the consumables of 16 November, wowsims gave 91% and 95%. The full threat consumables give the Paladin 18% more threat and the Warrior 3% more. Without the enchants, wowsims gave 103% and 107%. With Revelation on the weapon (18 November evening), it gave 108% and 112%.
- **C25a: the live Paladin has 101%,** and 104% with Redoubt (C-P1). The model gives 95%. The Paladin has 73% and 75% of the Druid. With the consumables of 16 November, C25a gave 87% and 90%. Without the enchants, it gave 98% and 101%. With Revelation, it gave 103% and 106%.
- **Toughness removal (C-P13)** still does not change threat.

**wowsims, groups (part 7).** TPS on each target, main target first, and the total.

| Tank | 1 target | 3 targets | 5 targets |
| --- | --- | --- | --- |
| Paladin, live, C25 (+90%) | 2,049 | 1,995 / 527 / 527 (total 3,049) | 1,972 / 464 / 464 / 463 / 256 (total 3,619) |
| Paladin, Redoubt (C-P1), C25 (+90%) | 2,119 | 1,996 / 530 / 530 (total 3,055) | 1,967 / 464 / 465 / 465 / 256 (total 3,616) |
| Paladin, live, C25a (+80%) | 1,942 | 1,891 / 499 / 499 (total 2,889) | 1,868 / 440 / 440 / 439 / 243 (total 3,429) |
| Paladin, Redoubt (C-P1), C25a (+80%) | 2,008 | 1,891 / 502 / 502 (total 2,895) | 1,863 / 440 / 440 / 440 / 242 (total 3,426) |
| Warrior | 1,838 | 1,823 / 571 / 173 (total 2,568) | 1,866 / 686 / 163 / 163 / 94 (total 2,973) |
| Druid | 2,215 | 1,641 / 547 / 536 (total 2,725) | 2,084 / 398 / 391 / 80 / 80 (total 3,033) |

- **On 1 target, the Paladin with C25 holds the enemy better than the Warrior.** With C25, it has 111% of the Warrior and 93% of the Druid. With C25a, it has 106% and 88%. On 3 targets, the Paladin with C25 has the most threat on the main target. On 5 targets, the Druid has the most.
- **In total, the Paladin with C25 has more threat than the Warrior and the Druid.** With C25: 119% and 122% of the Warrior on 3 and 5 targets (Druid: 112% and 119%). With C25a: 113% and 115% of the Warrior.
- **On the lowest target, the lead on the Warrior becomes larger.** With C25, the Paladin has 3.0 times the Warrior threat on 3 targets and 2.7 times on 5 targets. On 3 targets, it has 98% of the Druid.
- **The model gives a larger lead** (part 7). With C25, the proposed Paladin has 172–213% of the stronger tank on 3 targets, and 165–195% on 5 targets.

**Burst threat (part 8).** Threat on the boss after the first seconds, % of the Warrior.

| Tank | First 1.5 sec | First 3 sec | First 6 sec | First 10 sec | First 20 sec | First 30 sec |
| --- | --- | --- | --- | --- | --- | --- |
| Warrior | 4,141 | 9,043 | 14,087 | 24,464 | 45,047 | 64,431 |
| Druid | 5,725 (138%) | 8,833 (98%) | 13,734 (97%) | 23,234 (95%) | 52,018 (115%) | 78,089 (121%) |
| Paladin, live, wowsims opener, C25 (+90%) | 2,335 (56%) | 6,386 (71%) | 13,287 (94%) | 21,195 (87%) | 42,516 (94%) | 61,490 (95%) |
| Paladin, Redoubt (C-P1), wowsims opener, C25 (+90%) | 2,335 (56%) | 6,386 (71%) | 13,575 (96%) | 21,846 (89%) | 43,887 (97%) | 63,539 (99%) |
| Paladin, live, Fury opener, C25 (+90%) | 10,794 (261%) | 12,781 (141%) | 16,609 (118%) | 27,548 (113%) | 48,427 (108%) | 66,589 (103%) |
| Paladin, Redoubt (C-P1), Fury opener, C25 (+90%) | 10,952 (264%) | 13,150 (145%) | 17,303 (123%) | 28,608 (117%) | 49,940 (111%) | 68,821 (107%) |
| Paladin, live, wowsims opener, C25a (+80%) | 2,213 (53%) | 6,053 (67%) | 12,593 (89%) | 20,090 (82%) | 40,296 (89%) | 58,279 (90%) |
| Paladin, Redoubt (C-P1), wowsims opener, C25a (+80%) | 2,213 (53%) | 6,053 (67%) | 12,866 (91%) | 20,706 (85%) | 41,595 (92%) | 60,221 (93%) |
| Paladin, live, Fury opener, C25a (+80%) | 10,228 (247%) | 12,113 (134%) | 15,741 (112%) | 26,108 (107%) | 45,896 (102%) | 63,110 (98%) |
| Paladin, Redoubt (C-P1), Fury opener, C25a (+80%) | 10,379 (251%) | 12,463 (138%) | 16,399 (116%) | 27,113 (111%) | 47,328 (105%) | 65,224 (101%) |

- **With the Fury opener, the Paladin has the best start.** With C25, it has 141% of the Warrior after 3 sec and 113% after 10 sec. With C25a, it has 134% and 107%.
- **With the Fury opener, the Paladin with C25 stays above the Warrior for 30 sec.** After 30 sec, the live Paladin with C25 has 103% of the Warrior, and C25a 98%. With Redoubt (C-P1), C25 gives 107%. After 30 sec, the Druid has 121% of the Warrior.
- **With the wowsims default opener, the start is still slow:** 71% after 3 sec with C25, 67% with C25a. After 6 sec, the Paladin has 89–96%.

**Bad pulls (part 8).** Threat on the 10% worst fights, % of the Warrior on its 10% worst fights.

| Tank | First 3 sec | First 6 sec | First 10 sec |
| --- | --- | --- | --- |
| Warrior | 4,727 | 9,209 | 17,348 |
| Paladin, live, Fury opener, C25 (+90%) | 9,701 (205%) | 13,046 (142%) | 22,790 (131%) |
| Paladin, Redoubt (C-P1), Fury opener, C25 (+90%) | 10,020 (212%) | 13,666 (148%) | 23,802 (137%) |
| Paladin, live, Fury opener, C25a (+80%) | 9,192 (194%) | 12,364 (134%) | 21,599 (125%) |
| Paladin, Redoubt (C-P1), Fury opener, C25a (+80%) | 9,500 (201%) | 12,951 (141%) | 22,557 (130%) |

- **A bad pull costs the Paladin less than the Warrior,** as in part 8. With C25, the Paladin has 2.1 times the Warrior threat after 3 sec.

**Best short windows (part 8).** The highest threat in any window of the 3 min fight, % of the Warrior.

| Tank | Best 3 sec | Best 6 sec | Best 10 sec |
| --- | --- | --- | --- |
| Warrior | 16,651 | 23,275 | 32,456 |
| Druid | 19,264 (116%) | 28,982 (125%) | 42,029 (129%) |
| Paladin, live, Fury opener, C25 (+90%) | 15,572 (94%) | 21,045 (90%) | 32,277 (99%) |
| Paladin, Redoubt (C-P1), Fury opener, C25 (+90%) | 15,920 (96%) | 21,588 (93%) | 33,147 (102%) |
| Paladin, live, Fury opener, C25a (+80%) | 14,757 (89%) | 19,944 (86%) | 30,589 (94%) |
| Paladin, Redoubt (C-P1), Fury opener, C25a (+80%) | 15,087 (91%) | 20,459 (88%) | 31,413 (97%) |

- **The best windows stay near the Warrior level.** With C25, the live Paladin has 90–99% of the Warrior. The Druid has 116–129%. With C25a, the Paladin has 86–94%.
- **The Paladin still has no threat cooldown.** The Warrior and the Druid keep the largest spikes.

**Conclusion.** C25 (+90%) gives the live Paladin the Warrior threat again in the model (100%). In wowsims of 18 November (master ad6b13af8) with the full threat consumables and the enchants, it gives 106%, and 110% with Redoubt (C-P1). Thus, C25 closes the gap. To reach the Warrior in wowsims with Redoubt (C-P1), Righteous Fury needs about +73%. The Paladin with C25 has 77% of the Druid threat, and 79% with Redoubt (C-P1). This Druid value comes from a Lacerate rule that has no level 60 test yet (part 6).

C25a (+80%) gives 96–98% of the Warrior on one boss in the late raids in the model, and 101% in wowsims (104% with Redoubt). The recommendation stays C25. The C25 value stays +90% until the next review of the numbers.

## 10. Inputs of the model

**All tanks**

- Level 60, 500 Attack Power, 3% hit. One-hand weapon: 45 DPS, 2.7 sec.
- Critical hit chance 6%. Druid: 12% (Sharpened Claws).
- Against a level 63 boss from the front: 8% miss, 6.5% dodge, 14% parry. 40% of auto attacks are glancing blows (−35% damage). Critical hit chance −4.8%.
- Boss: 3,731 armor, 976 after 5 Sunder Armor and Faerie Fire. One swing each 2 sec. 64% of the swings hit the tank.
- Each rage point gives 5 threat (player data).

**Rage (normalized in Forever)**

- Auto attack: 3.46 rage × weapon speed. ×1.3 for two-hand weapons and Bear Form. ×2 for a critical hit. No rage for a miss, dodge or parry.
- Damage taken: 2.5 × 0.6 × boss hit before armor ÷ 243.6. ×1.5 for a crushing blow.
- Heroic Strike and Maul hits give no rage (as in Classic).

**Warrior**

- Talents: Defiance 3/3, Bastion 5/5, Improved Revenge 3/3, Shield Specialization 5/5, Master of Defense 2/2, Improved Sunder Armor 3/3, Focused Rage 3/3, Improved Heroic Strike 3/3.
- Defensive Stance ×1.8 threat and −10% damage. Defiance ×1.2 threat with a shield. Bastion +10% damage with a shield. (Notes of 2 November 2026. Client 1.60.1.70755: ×1.3 and ×1.15.)
- Revenge rank 6: 138–168 + 28% of Attack Power, +60%. Threat = damage × 2.25.
- Shield Slam rank 4: 640–670 + block value. Threat = damage (the real multiplier is not known).
- Heroic Strike rank 9: +157 damage. Threat = damage + 152.4 (wowsims).
- Sunder Armor: 206 threat + 5% of Attack Power. Rend rank 7: 7 ticks of 21 + 2% of Attack Power.
- 5 rage for each block, dodge and parry. Bloodrage: 20 rage each min.
- Shield Block on cooldown: it covers about 80% of the swings. 3% of the swings are crushing blows.
- Order: Shield Slam and Shield Block on cooldown, Revenge after each block, dodge or parry, Rend on the boss, Sunder Armor in the free global cooldowns. Heroic Strike uses the extra rage.

**Druid**

- Talents: Ferocity 5/5, Savage Fury 2/2, Feral Instinct 3/3, Sharpened Claws 2/2, Predatory Strikes 3/3, Blood Frenzy 2/2, Natural Reaction 5/5.
- Threat: Bear Form ×2.15 (notes of 2 November 2026; client 1.60.1.70755: ×1.5), Maul ×1.75, Primal Bite ×3, Swipe ×1.75 (player data). wowsims master 9a8624af9 uses the same values. The ability multipliers are not verified in the game. wowsims master 52471a100 also gives Lacerate 10/3 threat for each point of damage (measured on rank 2 at levels 38 to 50). The model does not have it.
- Primal Bite is now the Feral talent in row 7 (31 points). The model keeps it in the rotation.
- Each swing: weapon DPS + Attack Power ÷ 14, with a 2.5 sec swing. Predatory Strikes +90 Attack Power.
- Maul rank 7: +128 damage, +10%, 10 rage. Primal Bite rank 4: weapon damage + 77, 15 rage, 6 sec cooldown. Lacerate rank 3: 15 rage, a stack bleed.
- Faerie Fire in Bear Form: 120 threat, 6 sec cooldown (player data, not verified). Since master 52471a100, wowsims gives it 2 × level threat (120 at level 60), × the form multiplier.
- Blood Frenzy: 5 rage for each critical hit. Natural Reaction: 5 rage for each dodge. Enrage: 30 rage each min.
- No shield: 15% of the swings are crushing blows.

**Paladin (live version)**

- Tank build 0/38/13: Divine Intellect 2, Redoubt 5, Precision 3, Sacred Duty 1, Templar's Bulwark, Shield Specialization 2, Toughness 5, Swift Judgement, Improved Righteous Fury 3, Anticipation 5, Holy Shield, Reckoning 5, Iron Creed 3, Shieldsworn. Retribution: Benediction 5, Improved Judgement 2, Conviction 3, Sanctified Judgement 3.
- Hit +3% (Precision). Critical hit chance +6% (Conviction 3/3).
- Holy Shield rank 4: 221 Holy damage + 8% of spell power on each block, threat ×1.2. 2.5 blocks each 10 sec in the live version.
- Holy Strike: 50% of (weapon damage + 93 + 42.9% of spell power), all Holy damage. Iron Creed 3/3: +30% threat.
- Judgement of Fury: 160 + 42.9% of spell power. One each 8 sec, plus one Swift Judgement each min.
- Seal of Fury rank 7: 35 + 10% of spell power for each hit. It cannot miss.
- Reckoning 5/5: 1 extra attack each 10 sec.
- Consecration rank 5: 312 damage in 8 sec + 33.6% of spell power. 15% of ticks miss.

**Kept proposals (values from wowsims)**

- Redoubt (C-P1): block 44.0% → 58.7% (item pool set of 13 November, commit 6084403a9). Earlier values: commit 8c7b5a5f5 44.0% → 58.8%; set of 11 November, commit 3633d376a 41.2% → 60.7%. On commit 9f254e8d8, with the Argent Defender error: 55.0% → 61.9%. Set of 4 November: 42.3% → 61.6%. The model multiplies the Holy Shield blocks by 1.46 and the Reckoning attacks by 1.29.
- Reckoning (C-P12), withdrawn: extra attacks ×1.48.
- Holy Strike Seal trigger (C1), withdrawn: each Holy Strike that lands also triggers Seal of Fury.

## 11. Method and limits

- **Scripts.** `models/beta-30-oct/threat_tables_b2.py` for the model. `models/wowsims-b2` for wowsims Forever (master commit ad6b13af8 of 18 November 2026), 3,000 iterations. `models/wowsims-b2/tank_gear/run_pool.sh` with `FEEDBACK_CONSUMES=full` gives the runs with the item pool threat sets, the full threat consumables and the enchants of `tank_gear/enchants_*.json` (`logs/checks_ad6b13af8_pool_full.log`), and with the argument `surv` the runs with the survival sets (`logs/checks_ad6b13af8_pool_surv_full.log`). `FEEDBACK_ENCHANTS=default` gives the runs without the enchant search (`logs/checks_ad6b13af8_pool_full_no_enchants.log`, `logs/checks_ad6b13af8_pool_surv_full_no_enchants.log`). Without `FEEDBACK_CONSUMES`, it gives the runs with the consumables of 16 November (`logs/checks_ad6b13af8_pool.log`, `logs/checks_ad6b13af8_pool_surv.log`). These runs use the tank sets of 18 November (`tank_gear/search_open.py`). The runs of 17 November (master 6084403a9) are in `logs/checks_6084403a9_pool_full.log` and `logs/checks_6084403a9_pool_surv_full.log`. `logs/consumables_6084403a9.log` has the consumable tests of part 6, and `logs/consumables_ad6b13af8.log` the checks on master ad6b13af8. The runs with the first sets of 15 November are in `logs/checks_6084403a9_pool_6084403a9_first.log` and `logs/checks_6084403a9_pool_surv_6084403a9_first.log`. The runs of 4, 6, 8, 9, 11, 12 and 13 November are in `logs/checks_9a8624af9_pool.log`, `logs/checks_df57e2571_pool.log`, `logs/checks_ae9b8c23a_pool.log`, `logs/checks_9f254e8d8_pool.log`, `logs/checks_3633d376a_pool.log`, `logs/checks_52471a100_pool.log`, `logs/checks_129fcd89e_pool.log` and `logs/checks_8c7b5a5f5_pool.log`.

  The earlier sets on the new commits: `logs/checks_52471a100_pool_old_sets.log`, `logs/checks_129fcd89e_pool_old_sets.log`, `logs/checks_8c7b5a5f5_pool_old_sets.log`, `logs/checks_6084403a9_pool_old_sets.log` and `logs/checks_ad6b13af8_pool_full_old_sets.log`. The withdrawn ideas C1 and C-P12 use the runs of master commit 895cd67f9 (1 November). The Warrior and Druid wowsims values are native values. The tanks have the full threat consumables of part 6 (`feedbackFullConsumes` in the three tank tests of `models/wowsims-b2/go`). `FEEDBACK_CONSUMES=default` gives the consumables of the wowsims tests (Paladin: the Demonic Rune only, as in the runs before 4 November evening).
- **Holy Shield blocks.** The model gives Redoubt (C-P1) too many blocks. Use the wowsims value.
- **Druid multipliers.** The Maul, Swipe and Primal Bite values come from player data. wowsims uses the same values. A test in the game must confirm them (see Open items). The same applies to the Lacerate threat of wowsims master 52471a100 at level 60.
- **Gear.** The model gives all tanks the same gear. wowsims gives each class a threat set and a survival set from the item pool of Analysis, Damage, part 7 (part 6). Parts 7 to 9 use the threat sets. `models/wowsims-b2/tank_gear` has the search and the sets.
- **Righteous Fury.** The values use the wowsims rule: the two multipliers multiply (×2.527). If they add, Holy threat is ×2.23, and the Paladin has about 10% less threat.
- **Holy Shield rank 4** is a level 60 spell since build 70755. The model uses its 221 damage.
- **Righteous Fury (C25).** The `C25` flag of `proposals_sim.go` multiplies all Paladin threat by 1.9 ÷ 1.33. `RF_ALL` sets the value. The sim tank always has Righteous Fury, thus a fixed multiplier gives the same result.
- **Burst threat (part 8).** `models/wowsims-b2/patches/burst-threat.patch` adds the threat recorder. `run.sh` gives the runs. The openers are sim rotations. A player can use a different opener.
- **Groups model.** Trash has no Sunder Armor or Faerie Fire. Demoralizing Shout, Demoralizing Roar and tab targets are not in the model.
- The earlier version of this tab (trees of 18 October) is in the history of the repository.
