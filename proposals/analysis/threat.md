# Threat

**Question.** Does the Paladin tank hold a boss and a group as well as the Warrior and the Druid?

All values are threat each sec (TPS). The tanks are level 60 and the boss is level 63. The values come from a model and from wowsims. The proposed values include Righteous Fury +90% (C25). Part 9 compares C25 alone with the alternative C25a (+80%). Part 10 gives the inputs.

The Warrior and Druid values use the development notes of 2 November 2026. Defensive Stance gives +80% threat (was +30%) and Defiance 7/13/20% (was 5/10/15%). Bear Form and Dire Bear Form give +115% (was +50%). The hotfix pushes of 4 November 2026 (113600 and 113605) have these values, and wowsims Forever master 9a8624af9 reads them from the game data. Thus the wowsims Warrior and Druid values are now native values, with no scaling. A test on the live realms must confirm them.

All tanks in wowsims have tank consumables. The Paladin has the same consumables as the Warrior, with two Paladin choices: Greater Arcane Elixir (spell power) and Brilliant Wizard Oil on the weapon (part 6).

## Short answer

- **No. After the development notes of 2 November 2026, the Paladin tank has less threat than the Warrior and the Druid.** The notes give the Warrior ×1.44 and the Druid ×1.43 more threat. This replaces Blessing of Salvation (1 ÷ 0.7 = ×1.43). The Paladin received ×1.33 from Righteous Fury in the beta of 30 October, and no more on 2 November.
- **With the same gear, the live Paladin has 70% of the Warrior threat** in the model. In wowsims, with item pool tank sets and tank consumables, it has 79% of the Warrior and 65% of the Druid. Before the notes, it had 101% and 108% of the Warrior.
- **The Druid now has the most threat on one boss in wowsims: 121% of the Warrior.** wowsims master 9a8624af9 gives Bear Form +115% and the Maul, Swipe and Primal Bite threat of the player data.
- **From fresh 60 to Naxxramas, the live Paladin has 71–82% of the Warrior threat.** With Consecration on cooldown, it has 83–98%, but the mana does not last (see Mana).
- **With the proposals, the Paladin is between the Warrior and the Druid.** Righteous Fury (C25) gives +90% to all threat (live: +33%). In wowsims, the proposed Paladin has 119% of the Warrior threat and 98% of the Druid (C25 alone: 112% and 92%). In the model, it has 114–135% of the Warrior from Naxxramas to fresh 60.
- **With +80% (C25a), the live Paladin has 106% of the Warrior in wowsims** and 96–111% in the model. With Redoubt (C-P1), it has 113% of the Warrior and 93% of the Druid in wowsims.
- **Righteous Fury (C25) closes the gap.** Redoubt (C-P1) gives more blocks, thus more Holy Shield damage: +6% in wowsims (84% of the Warrior). C25 multiplies all Paladin threat by 1.43.
- **Two threat proposals were withdrawn on 2 November 2026.** The Holy Strike Seal trigger (C1) and Reckoning (C-P12) each added +3% in wowsims of 1 November. They do not close the gap.
- **Judgement of the Crusader is important.** It gives the tank about 72 TPS. In the live version, the raid can need the tank Judgement for Light or Wisdom. The tank then has 62% of the Warrior threat. With Personal Judgement of the Crusader (C2), the tank keeps Crusader.
- **At the pull, the proposed Paladin has the best burst threat, but only with a Fury opener** (part 8). The Paladin casts Seal of Fury and Holy Shield before the pull. Two Judgements of Fury and Holy Strike then hit at 0 sec. The live Paladin then has 154% of the Warrior threat after 1.5 sec, 96% after 3 sec and 82% after 10 sec. The proposed Paladin has 143% after 3 sec and 126% after 10 sec. With the wowsims default opener, the live Paladin has 48% after 3 sec.
- **In its best short windows, the live Paladin has 62–72% of the Warrior** (part 8). The proposed Paladin has 92–107%. The Druid has 116–123%. The Warrior has large spikes from Shield Slam, Revenge and Heroic Strike critical hits.
- **Against 3 or more enemies, the Paladin still holds the extra enemies well.** On the enemy with the least threat, the live Paladin has 2.2 times the Warrior threat. The proposed Paladin has 3.2 times. With the proposals, its total threat is 122–128% of the Warrior and 98–100% of the Druid.
- **Threat sets and survival sets give the same threat order** (part 6). With the survival sets, the live Paladin has 78% of the Warrior and the proposed Paladin 119%.
- **With the same consumables, Redoubt (C-P1) gives the Paladin the damage taken of the Warrior** (part 6). The live Paladin takes 14% more damage than the Warrior. With Redoubt, it takes the same damage (threat sets) or 1% less (survival sets), and its TMI is lower than the Warrior TMI. Before 4 November evening, the Paladin test had no consumables, and the gap was 28%.
- **The wowsims tank sets obey the item pool rules** (part 6): no raid drops, no Zul'Gurub or Ahn'Qiraj items, no PvP items, no Revered or Exalted reputation items, item level 63 or lower. The wowsims default sets had these items.
- **The model Druid uses the same multipliers as wowsims now:** Bear Form ×2.15, Maul ×1.75, Swipe ×1.75 and Primal Bite ×3. The Maul, Swipe and Primal Bite values come from player data. A test in the game must confirm them (part 2).

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

The Druid multipliers are Bear Form ×2.15, Maul ×1.75 and Primal Bite ×3 (player data). wowsims master 9a8624af9 uses the same multipliers, but it gives Faerie Fire no threat.

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
- **The proposed Paladin has 114–135%** of the Warrior threat in the model. Without C25, it has 80–94%. wowsims gives a smaller gain from Redoubt (part 6): the proposed Paladin has 119% there.
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

The design goal is a Paladin tank with the threat of the Warrior. The beta of 30 October reached it (101%). The development notes of 2 November give the Warrior and the Druid about ×1.44, and the Paladin no change. Thus, the live Paladin has 70% of the Warrior threat in the model, and 79% in wowsims.

- **Why the gap.** Blessing of Salvation decreased the threat of the damage dealers by 30%. Blizzard removed it and gave the tanks about ×1.43 (1 ÷ 0.7). The Paladin received ×1.33 from Righteous Fury in the beta of 30 October. But the Paladin needed this ×1.33 to reach the Warrior before the notes.
- **Redoubt (C-P1) adds 6% in wowsims.** With Redoubt only, the tank has 84% of the Warrior threat.
- **The Holy Strike Seal trigger (C1) and Reckoning (C-P12) were withdrawn.** Each added only +3% in wowsims of 1 November. They do not close the gap.
- **The fix: Righteous Fury (C25).** The Paladin needs about ×1.44 on all threat. C25 changes the first part of Righteous Fury from +33% to +90% to all threat: ×1.43. The model needs +62% at fresh 60 and +88% in Naxxramas. wowsims needs +69% to reach the Warrior and +105% to reach the Druid, with the item pool tank sets and tank consumables. This is a baseline spell, thus the talent rule (a % only) is not necessary.
- **With C25, the model gives 101–117% of the Warrior threat** from Naxxramas to fresh 60. Before the notes, the live Paladin had 101–118%. With all proposals, wowsims gives 119% of the Warrior and 98% of the Druid.
- **The gear is not the same.** wowsims gives each class a tank set from the same item pool (part 6), but the items are different for each class. A Warrior with better gear can make the gap larger.
- **Consumables are important.** The Paladin test of wowsims has only a Demonic Rune. With the tank consumables of the Warrior test and two Paladin choices, the live Paladin has +10% threat and −11% damage taken (part 6).
- **Live tests give the real answer.** First, confirm the new Defensive Stance and Bear Form values on the live realms. Then compare the tanks with the same gear in real fights.

## 6. Check with wowsims

wowsims Forever plays the fight with the full rules of the game. Full buffs, one level 63 boss from the front, 3 min fight. The Paladin has the wowsims default tank build (12/32/7) with Redoubt 5/5.

**Tank sets.** Each class has two tank sets from the item pool of Analysis, Damage, part 7: a threat set and a survival set. Threat sets: [Protection Paladin](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-pool-protection-paladin.html), [Protection Warrior](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-pool-protection-warrior.html) and [Bear Druid](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-pool-bear-druid.html). Survival sets: [Protection Paladin](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-surv-protection-paladin.html), [Protection Warrior](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-surv-protection-warrior.html) and [Bear Druid](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-surv-bear-druid.html).

- **Item pool rules.** No raid drops. No items of the Zul'Gurub and Ahn'Qiraj patches (item ids 19000 to 23999). No PvP items. No Revered or Exalted reputation items. Item level 63 or lower.
- **Search.** The search starts from the wowsims default tank set of each class. It replaces each item that is not in the pool. For each slot, it runs the 12 best pool items for the tank stats in wowsims, 1,000 iterations each. It keeps the item with the best tank score. Threat set: 40% threat, 20% damage, 20% damage taken and 20% TMI. Survival set: 40% threat, 30% damage taken and 30% TMI. The final set runs with 3,000 iterations. The enchants do not change. Scripts: `models/wowsims-b2/tank_gear`.
- **Replaced items.** Paladin: 10 items, for example Arena Grand Master, Force Reactive Disk and Dark Iron Destroyer. Warrior: 8 items, for example Annihilator, Hyperion Legplates and Ring of Awareness. Druid: 11 items, for example the PvP bracers, the Stormpike Insignia, Timbermaw Brawlers and the Premier Grand Marshal's Battle Hammer.
- **The default sets** of wowsims have raid, PvP and reputation items. The [default sets](https://ralgathor.github.io/forever-paladin-feedback/sets/) page keeps their links. The Builds tab uses the two item pool Protection Paladin sets.

- **Consumables.** All tanks have tank consumables. The Warrior and the Druid use the consumables of their wowsims tests. wowsims has no Protection Paladin consumables (only a Demonic Rune). Thus the Paladin has the consumables of the Warrior test, with two Paladin choices: Greater Arcane Elixir in place of Winterfall Firewater, and Brilliant Wizard Oil in place of the Dense Sharpening Stone. The other items are Major Frenzy Potion, Smoked Desert Dumplings, EZ-Thro Dark Bomb, Goblin Sapper Charge, Major Healthstone, Rumsey Rum and the Elixirs of Ferocity, the Mongoose, Greater Defense and the Phalanx. A test of seven mixes on the survival set with Redoubt (C-P1) gave the most threat with this mix.

wowsims Forever master commit 9a8624af9 (4 November 2026) has the game data of client 1.60.1.70755 and the hotfixes of 4 November. This data has Holy Shield rank 4 (221 damage, 4 charges), Defensive Stance +80%, Defiance 7/13/20% and Bear Form +115%. The Warrior and Druid values are native wowsims values. The Paladin spells did not change since commit 8298ab833.

| Tank | TPS (% of the Warrior, % of the Druid) | Damage taken each sec | TMI | Crushing blows |
| --- | --- | --- | --- | --- |
| Warrior | 1,448 (100%, 83%) | 300 | 41 | 1.0% |
| Druid | 1,755 (121%, 100%) | 393 | 43.9 | 15.1% |
| Paladin, live | 1,137 (79%, 65%) | 343 | 54.0 | 11.9% |
| Paladin, Redoubt (C-P1) | 1,210 (84%, 69%) | 300 | 42.8 | 1.2% |
| Paladin, Righteous Fury (C25) | 1,617 (112%, 92%) | 343 | 54.0 | 11.9% |
| **Paladin, all kept proposals (C-P1, C-P13, C25)** | **1,722 (119%, 98%)** | **305** | **43.8** | **1.2%** |

- **The live Paladin has 79% of the Warrior threat in wowsims.** The model gives 70%. The model has no consumables. Before the notes of 2 November, they gave 101% and 108%.
- **The Druid has the most threat: 121% of the Warrior.** wowsims master 9a8624af9 gives Bear Form +115% and Maul ×1.75, Swipe ×1.75 and Primal Bite ×3. The earlier runs gave Bear Form only, and the Druid had 77% of the Warrior.
- **The consumables give the Paladin +10% threat and −11% damage taken.** Without them (Demonic Rune only), the live Paladin had 1,029 TPS and 384 damage taken each sec.
- **With Redoubt (C-P1), the Paladin takes the same damage as the Warrior** (300 each sec), and its TMI is near the Warrior TMI (42.8 against 41). The live Paladin takes 14% more damage than the Warrior. With all kept proposals, it takes 2% more.
- **Redoubt adds less in wowsims:** +73 TPS (+6%) against +96 TPS (+15%) in the model. The model gives too many Holy Shield blocks.
- **Righteous Fury (C25) multiplies all Paladin threat by 1.43.** With all kept proposals, the Paladin has 119% of the Warrior threat and 98% of the Druid. The model gives 115% of the Warrior (part 1).
- **Holy Shield rank 4 adds 6% in wowsims.** With the default set and rank 3 (wowsims of 1 November), the live Paladin had 928 TPS. With rank 4, it had 980 TPS.
- **C1 (withdrawn) agrees:** +26 in wowsims of 1 November, +25 in the model. The C1 flag does not run on commit d97252f2a.
- **Reckoning (C-P12), withdrawn.** With C1, it gave +27 more in wowsims of 1 November and +20 in the model.
- **Toughness removal (C-P13)** does not change threat. Damage taken increases by 2%.

**Survival sets.** The same runs with the survival set of each class.

| Tank | TPS (% of the Warrior, % of the Druid) | Damage taken each sec | TMI | Crushing blows |
| --- | --- | --- | --- | --- |
| Warrior | 1,382 (100%, 80%) | 292 | 41 | 0.9% |
| Druid | 1,718 (124%, 100%) | 393 | 42.7 | 15.1% |
| Paladin, live | 1,081 (78%, 63%) | 333 | 45.8 | 11.8% |
| Paladin, Redoubt (C-P1) | 1,157 (84%, 67%) | 289 | 36.0 | 1.1% |
| Paladin, Righteous Fury (C25) | 1,538 (111%, 90%) | 333 | 45.8 | 11.8% |
| **Paladin, all kept proposals (C-P1, C-P13, C25)** | **1,647 (119%, 96%)** | **295** | **36.9** | **1.1%** |

- **The threat order does not change.** The Paladin loses 5% threat with its survival set (1,137 → 1,081), the Warrior 5% and the Druid 2%. The Paladin keeps 78% (live) and 119% (all kept proposals) of the Warrior.
- **The Paladin TMI decreases the most:** 54.0 → 45.8 (live) and 43.8 → 36.9 (all kept proposals). The Warrior TMI stays at 41.
- **With Redoubt (C-P1), the Paladin takes 1% less damage than the Warrior,** and its TMI is lower (36.0 against 41). The live Paladin takes 14% more damage. The Warrior dodges more (22.5% against 13.9%), and the boss has 2.6% critical hits on the live Paladin (Warrior: 0.1%).
- **C25a (+80%)** gives 105% of the Warrior (live) and 113% with C-P1 (threat sets: 106% and 113%).

**Other fights (wowsims, 3 min, item pool threat sets).** TPS, % of the Warrior in brackets. "Fast" is a swing each 1.2 sec with 60% damage, thus the same damage each sec. "Two weapons" is a boss with a second weapon. The 5 min row has C-P1 only: Toughness removal (C-P13) does not change threat.

| Boss | Warrior | Paladin, live | Paladin, C-P1 and C-P13 | Paladin, all kept proposals (×1.43) |
| --- | --- | --- | --- | --- |
| Normal, 5 min | 1,431 | 1,135 (79%) | 1,209 (84%) | 1,727 (121%) |
| Fast | 1,538 | 1,255 (82%) | 1,305 (85%) | 1,864 (121%) |
| Two weapons | 1,583 | 1,298 (82%) | 1,333 (84%) | 1,904 (120%) |
| Fast, two weapons | 1,687 | 1,396 (83%) | 1,395 (83%) | 1,993 (118%) |

- **Faster boss attacks help the Warrior and the Paladin.** The Warrior receives more rage. The Paladin blocks more, thus Holy Shield hits more.
- **Against a fast boss with two weapons, Redoubt adds no threat.** The Holy Shield charges are empty too soon (Crushing blows, part 3).

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

**wowsims result.** Item pool tank sets and tank consumables (part 6). Each enemy is level 63 and hits for 1/3 of a boss hit. The Paladin uses its default rotation with Consecration. The values are TPS on each target, with the main target first. The Warrior and Druid values are native values of commit 9a8624af9 (part 6).

| Tank | 1 target | 3 targets | 5 targets |
| --- | --- | --- | --- |
| Paladin, live | 1,137 | 1,079 / 299 / 299 | 1,052 / 258 / 258 / 258 / 144 |
| Paladin, proposed | 1,722 | 1,534 / 430 / 431 | 1,491 / 367 / 367 / 367 / 205 |
| Warrior | 1,363 | 1,345 / 388 / 133 | 1,419 / 549 / 126 / 126 / 64 |
| Druid | 1,422 | 1,694 / 378 / 366 | 1,877 / 402 / 387 / 63 / 63 |

- **On the lowest target, the Paladin still leads the Warrior.** On 3 targets, the live Paladin has 2.2 times the Warrior threat, but 82% of the Druid. On 5 targets, it has 2.2 times the Warrior threat and 2.3 times the Druid threat.
- **The proposed Paladin leads by more.** On the lowest target, it has 3.2 times the Warrior threat on 3 and on 5 targets. It has 117% of the Druid on 3 targets and 3.3 times on 5 targets.
- **In total, the live Paladin is last.** On 3 targets: live Paladin 1,678, Warrior 1,866, Druid 2,439. On 5 targets: live Paladin 1,970, Warrior 2,284, Druid 2,792.
- **The proposed Paladin has the Druid total.** On 3 targets: 2,396 (128% of the Warrior, 98% of the Druid). On 5 targets: 2,798 (122% of the Warrior, 100% of the Druid).
- **Redoubt changes almost nothing on groups:** less than 1%. On extra targets, all Holy Shield charges are already used in the live version. The gain comes from Righteous Fury (C25).
- **The fifth enemy has less Paladin threat** because Consecration gives its full damage to 4 enemies only.
- **The Warrior** holds only 2 targets well: Cleave hits 2 targets. **The Druid** holds only 3: Swipe hits 3 targets.

**Model result.** The model gives a larger Paladin lead. The live Paladin has 115–149% of the stronger of the two other tanks on all targets. The proposed Paladin has 165–214%. The model lead is too large. In the model, trash hits for only 1/3 of a boss hit, thus the Warrior and the Druid receive little rage.

| Gear level | 3 targets: Warrior | Druid | Paladin, live | Paladin, proposed | 5 targets: Warrior | Druid | Paladin, live | Paladin, proposed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fresh 60 | 705 | 716 | 1,064 | 1,529 | 883 | 813 | 1,198 | 1,720 |
| Pre-raid best | 799 | 820 | 1,123 | 1,617 | 956 | 908 | 1,262 | 1,814 |
| Molten Core | 906 | 917 | 1,183 | 1,703 | 1,046 | 1,004 | 1,326 | 1,907 |
| Blackwing Lair | 996 | 1,009 | 1,256 | 1,809 | 1,160 | 1,120 | 1,407 | 2,024 |
| Naxxramas | 1,095 | 1,107 | 1,320 | 1,901 | 1,290 | 1,250 | 1,476 | 2,124 |

Values are TPS on all targets. Without Consecration, the proposed Paladin has 119–146% of the stronger tank on 3 targets, and 101–117% on 5 targets.

**Conclusion.** Against 3 or more enemies, the Paladin holds the extra enemies better than the Warrior. On 5 targets, it holds them better than the Druid too. The live total threat is the lowest of the three tanks. The problem is the main target (parts 1 and 6). With Righteous Fury (C25), the Paladin is above the Warrior on the main target and in total, and it has the Druid total.

## 8. Burst threat

This part compares the threat in the first seconds of a pull and in the best short windows of a fight. A damage dealer pulls the boss when it has more threat than the tank. At the start of a pull, and after a large threat spike, this can occur before the sustained values of part 6 apply.

**Setup.** wowsims, as in part 6: item pool tank sets, tank consumables, full buffs, one level 63 boss from the front, 3 min fight, 3,000 iterations. A recorder adds the threat on the boss in steps of 0.1 sec. All values come from commit 9a8624af9, except the Warrior variants of commit 6ee3c30f35 (default sets).

- **Warrior.** Default rotation, 0 rage at the pull. Bloodrage and a rage potion at −1.5 sec.
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
| Warrior | 3,823 (100%) | 7,269 (100%) | 10,879 (100%) | 17,940 (100%) | 34,228 (100%) | 1,450 (100%) |
| Druid | 4,081 (107%) | 7,018 (97%) | 10,499 (97%) | 17,880 (100%) | 38,190 (112%) | 1,751 (121%) |
| Paladin, live, wowsims opener | 1,407 (37%) | 3,515 (48%) | 7,207 (66%) | 11,335 (63%) | 22,843 (67%) | 1,134 (78%) |
| Paladin, live, Fury opener | 5,907 (154%) | 6,960 (96%) | 8,962 (82%) | 14,756 (82%) | 25,950 (76%) | 1,154 (80%) |
| Paladin, proposed, wowsims opener | 2,001 (52%) | 4,992 (69%) | 10,742 (99%) | 17,226 (96%) | 34,797 (102%) | 1,721 (119%) |
| Paladin, proposed, Fury opener | 8,641 (226%) | 10,399 (143%) | 13,740 (126%) | 22,602 (126%) | 39,479 (115%) | 1,751 (121%) |

- **With the wowsims default opener, the Paladin starts slowly.** The first global cooldown goes to Judgement of the Crusader. Holy Shield starts at 3 sec, and Holy Strike at 4.5 sec.
- **With the Fury opener, the Paladin has the best start of the three tanks in the first 1.5 sec.** Two Judgements of Fury, Holy Strike, the Shieldsworn Holy Shield hit and the explosives hit the boss at the pull.
- **The live lead does not last.** After 3 sec, the live Fury opener has 96% of the Warrior, and after 10 sec 82%. After 20 sec, it has 76%, near the sustained gap of part 6.
- **The proposed Paladin keeps the lead.** With the Fury opener, it has 126% of the Warrior after 10 sec and 115% after 20 sec. In the first 3 sec, all of the gain comes from Righteous Fury (C25). Redoubt starts after the first blocks.
- **The Druid starts as fast as the Warrior.** It uses its 25 rage at once. After 20 sec, it has 112% of the Warrior, and the proposed Paladin with the Fury opener 115%.
- **The Warrior needs rage first.** It starts with 0 rage. Its threat increases fast from 2 sec, when the boss hits give rage.
- **Boss armor helps the Paladin.** In the first 6 sec, the boss has less than 5 Sunder Armor stacks. This decreases Warrior and Druid physical damage. Most Paladin threat is Holy damage, thus boss armor does not decrease it.
- **With one Judgement at 0 sec,** Swift Judgement hits at 1.5 sec. Only the first 1.5 sec change: 4,608 threat (121%) in place of 5,907. From 3 sec, the two openers have the same threat.

**Bad pulls** (threat on the 10% worst fights, % of the Warrior on its 10% worst fights)

| Tank | First 3 sec | First 6 sec | First 10 sec |
| --- | --- | --- | --- |
| Warrior | 3,414 (100%) | 6,676 (100%) | 12,443 (100%) |
| Druid | 3,341 (98%) | 5,948 (89%) | 11,693 (94%) |
| Paladin, live, wowsims opener | 2,598 (76%) | 5,396 (81%) | 9,136 (73%) |
| Paladin, live, Fury opener | 5,237 (153%) | 7,027 (105%) | 12,123 (97%) |
| Paladin, proposed, Fury opener | 7,938 (233%) | 10,928 (164%) | 18,786 (151%) |

- **A bad pull costs the Warrior and the Druid the most.** When their first attacks miss or the boss attacks miss them, they have no rage. The Warrior threat after 3 sec decreases to 47% of its mean. The Druid keeps 48%, and the live Paladin 74%.
- **A bad pull costs the Paladin less.** Judgement of Fury cannot be dodged or parried. Holy Shield and Seal of Fury cannot miss.

**Best short windows** (the highest threat in a window at any time in the 3 min fight, % of the Warrior)

| Tank | Best 3 sec | Best 6 sec | Best 10 sec | Best 3 sec ÷ mean 3 sec |
| --- | --- | --- | --- | --- |
| Warrior | 12,939 (100%) | 18,711 (100%) | 24,964 (100%) | ×3.0 |
| Druid | 15,773 (122%) | 21,728 (116%) | 30,608 (123%) | ×3.0 |
| Paladin, live, wowsims opener | 8,146 (63%) | 11,632 (62%) | 17,577 (70%) | ×2.4 |
| Paladin, live, Fury opener | 8,780 (68%) | 11,734 (63%) | 17,979 (72%) | ×2.6 |
| Paladin, proposed, wowsims opener | 12,018 (93%) | 17,234 (92%) | 26,026 (104%) | ×2.3 |
| Paladin, proposed, Fury opener | 12,819 (99%) | 17,296 (92%) | 26,624 (107%) | ×2.5 |

- **The Paladin has no threat cooldown.** Its best windows come from Holy Strike, Judgement and Holy Shield in the same 3 sec, with critical hits. The Warrior adds Shield Slam, Revenge and Heroic Strike critical hits to the rage from boss hits. The Druid has the largest windows, from Maul and Primal Bite.
- **The best-window gap is larger than the sustained gap.** Live: 62–72% against 78%. Proposed: 92–107% against 119%. Thus the Paladin has a smaller margin against a large threat spike from a damage dealer.

**Warrior variants**

| Warrior | First 1.5 sec | First 3 sec | First 6 sec | First 10 sec |
| --- | --- | --- | --- | --- |
| Default, with Goblin Sapper Charge (above) | 3,823 | 7,269 | 10,879 | 17,940 |
| No engineering items | 2,563 (−33%) | 5,776 (−21%) | 9,393 (−14%) | 16,330 (−9%) |
| Default set, no engineering items, commit 6ee3c30f35 | 1,968 | 4,609 | 6,962 | 12,881 |
| Default set, Charge at −0.5 sec, 20 yards (Vanguard), commit 6ee3c30f35 | 1,711 (−13%) | 4,213 (−9%) | 7,223 (+4%) | 13,354 (+4%) |

- **Charge does not increase the Warrior burst.** Charge gives 15 rage, but this rage gives no threat. The Charge stun also delays the first boss swings, thus the Warrior receives less rage from boss hits. The Charge rotation does not run on commits 8298ab833 and 9a8624af9: the Warrior does almost no attacks. Thus, the Charge row comes from commit 6ee3c30f35 with the default Warrior set, and its % compare it with the default rotation of that commit. The two rows of commit 6ee3c30f35 are wowsims values × 1.445 (the Warrior multipliers of the notes of 2 November).
- **Charge in combat.** With Vanguard, the Warrior can charge in Defensive Stance. The Vanguard Charge row in the game files still has the "not in combat" attribute. Thus the Warrior can charge only at the pull. A test in the game must confirm this.

**Tank swaps.** Shoulder the Burden (C-P5) moves 50% of the threat of an ally to the Paladin. After 30 sec, the Warrior has about 49,000 threat. Shoulder the Burden on the Warrior then gives the Paladin about 24,500 threat at once. This is 2.8 times the best 3 sec live Paladin window. It does not help at the pull, because no ally has threat yet.

**Conclusion.** The proposed Paladin can hold the boss at the pull better than the Warrior and the Druid, but only with a Fury opener. The live Paladin leads only in the first 1.5 sec. The default opener of wowsims gives it 48% of the Warrior threat in the first 3 sec. After 10 sec, the sustained gap of part 6 returns. In short windows later in the fight, the live Paladin has 62–72% of the Warrior. The proposed Paladin keeps the lead for the first 30 sec, and has 92–107% of the Warrior in short windows. The Druid has the largest short windows.

## 9. Righteous Fury alone: +90% (C25) and +80% (C25a)

This part gives parts 1 to 8 again with Righteous Fury (C25) alone, and with the live trees: all threat +90% in place of +33%. The alternative C25a gives +80%, the value of Defensive Stance.

- **Righteous Fury multiplies all Paladin threat.** Thus, C25 multiplies each Paladin value of the model by 1.43 (1.9 ÷ 1.33), and C25a by 1.35 (1.8 ÷ 1.33).
- **The wowsims values come from new runs.** C25 multiplies the wowsims threat by 1.43, and C25a by 1.35.
- **The Warrior and Druid values do not change.** They use the notes of 2 November, as in parts 1 to 8. The wowsims values are native values of commit 9a8624af9.

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
- **The proposed Paladin with C25 has 114–135%.** The model gives too many Holy Shield blocks (part 6). In wowsims, Redoubt adds 6%, not 15%.

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

**wowsims, one boss (part 6).** New runs, item pool tank sets, tank consumables, 3 min, 3,000 iterations. Damage taken and TMI do not change with Righteous Fury. The cells give TPS, then % of the Warrior and of the Druid.

| Paladin | Live (+33%) | C25 (+90%) | C25a (+80%) |
| --- | --- | --- | --- |
| Live | 1,137 (79%, 65%) | 1,617 (112%, 92%) | 1,533 (106%, 87%) |
| Redoubt (C-P1) | 1,210 (84%, 69%) | 1,722 (119%, 98%) | 1,632 (113%, 93%) |
| All kept proposals (with C-P13) | 1,210 (84%, 69%) | 1,722 (119%, 98%) | 1,632 (113%, 93%) |

The Warrior has 1,448 and the Druid 1,755 (commit 9a8624af9).

- **C25: the live Paladin has 112% of the Warrior threat** in wowsims, and 119% with Redoubt (C-P1). The model gives 100%. The Druid keeps more threat: the Paladin has 92% and 98% of the Druid.
- **C25a: the live Paladin has 106%,** and 113% with Redoubt (C-P1). The model gives 95%.
- **Toughness removal (C-P13)** still does not change threat.

**wowsims, groups (part 7).** TPS on each target, main target first, and the total.

| Tank | 1 target | 3 targets | 5 targets |
| --- | --- | --- | --- |
| Paladin, live, C25 (+90%) | 1,617 | 1,540 / 425 / 425 (total 2,390) | 1,501 / 367 / 367 / 367 / 205 (total 2,807) |
| Paladin, Redoubt (C-P1), C25 (+90%) | 1,722 | 1,534 / 430 / 431 (total 2,396) | 1,491 / 367 / 367 / 367 / 205 (total 2,798) |
| Paladin, live, C25a (+80%) | 1,533 | 1,459 / 403 / 403 (total 2,265) | 1,422 / 348 / 348 / 348 / 194 (total 2,660) |
| Paladin, Redoubt (C-P1), C25a (+80%) | 1,632 | 1,454 / 408 / 408 (total 2,270) | 1,413 / 348 / 348 / 348 / 194 (total 2,651) |
| Warrior | 1,363 | 1,345 / 388 / 133 (total 1,866) | 1,419 / 549 / 126 / 126 / 64 (total 2,284) |
| Druid | 1,422 | 1,694 / 378 / 366 (total 2,439) | 1,877 / 402 / 387 / 63 / 63 (total 2,792) |

- **On the main target of 1 target, the Paladin holds the enemy better than the Warrior and the Druid.** With C25, it has 119% of the Warrior and 114% of the Druid. With C25a, it has 112% and 108%. On 3 and 5 targets, the Druid has the most threat on the main target.
- **In total, the Paladin is above the Warrior and near the Druid.** With C25: 128% of the Warrior on 3 targets and 123% on 5 targets (Druid: 98% and 101%). With C25a: 121% and 116% of the Warrior.
- **On the lowest target, the lead becomes larger.** With C25, the Paladin has 3.2 times the Warrior threat on 3 and on 5 targets.
- **The model gives a larger lead** (part 7). With C25, the proposed Paladin has 172–213% of the stronger tank on 3 targets, and 165–195% on 5 targets.

**Burst threat (part 8).** Threat on the boss after the first seconds, % of the Warrior.

| Tank | First 1.5 sec | First 3 sec | First 6 sec | First 10 sec | First 20 sec | First 30 sec |
| --- | --- | --- | --- | --- | --- | --- |
| Warrior | 3,823 | 7,269 | 10,879 | 17,940 | 34,228 | 48,995 |
| Druid | 4,081 (107%) | 7,018 (97%) | 10,499 (97%) | 17,880 (100%) | 38,190 (112%) | 55,279 (113%) |
| Paladin, live, wowsims opener, C25 (+90%) | 2,001 (52%) | 4,992 (69%) | 10,242 (94%) | 16,103 (90%) | 32,465 (95%) | 47,030 (96%) |
| Paladin, Redoubt (C-P1), wowsims opener, C25 (+90%) | 2,001 (52%) | 4,992 (69%) | 10,742 (99%) | 17,226 (96%) | 34,797 (102%) | 50,477 (103%) |
| Paladin, live, Fury opener, C25 (+90%) | 8,409 (220%) | 9,898 (136%) | 12,742 (117%) | 20,984 (117%) | 36,913 (108%) | 50,955 (104%) |
| Paladin, Redoubt (C-P1), Fury opener, C25 (+90%) | 8,641 (226%) | 10,399 (143%) | 13,740 (126%) | 22,602 (126%) | 39,479 (115%) | 54,571 (111%) |
| Paladin, live, wowsims opener, C25a (+80%) | 1,897 (50%) | 4,732 (65%) | 9,710 (89%) | 15,266 (85%) | 30,777 (90%) | 44,584 (91%) |
| Paladin, Redoubt (C-P1), wowsims opener, C25a (+80%) | 1,897 (50%) | 4,732 (65%) | 10,183 (94%) | 16,330 (91%) | 32,987 (96%) | 47,850 (98%) |
| Paladin, live, Fury opener, C25a (+80%) | 7,970 (208%) | 9,383 (129%) | 12,079 (111%) | 19,892 (111%) | 34,989 (102%) | 48,302 (99%) |
| Paladin, Redoubt (C-P1), Fury opener, C25a (+80%) | 8,190 (214%) | 9,857 (136%) | 13,025 (120%) | 21,425 (119%) | 37,420 (109%) | 51,726 (106%) |

- **With the Fury opener, the Paladin has the best start by a large margin.** With C25, it has 136% of the Warrior after 3 sec and 117% after 10 sec. With C25a, it has 129% and 111%.
- **The lead on the Warrior lasts about 30 sec.** After 30 sec, the live Paladin with C25 has 104% of the Warrior, and C25a 99%. With Redoubt (C-P1), C25 gives 111%. After 20 sec, the Druid has more threat than the live Paladin with C25.
- **With the wowsims default opener, the start is still slow:** 69% after 3 sec with C25, 65% with C25a. After 6 sec, the Paladin has 89–99%.

**Bad pulls (part 8).** Threat on the 10% worst fights, % of the Warrior on its 10% worst fights.

| Tank | First 3 sec | First 6 sec | First 10 sec |
| --- | --- | --- | --- |
| Warrior | 3,414 | 6,676 | 12,443 |
| Paladin, live, Fury opener, C25 (+90%) | 7,446 (218%) | 9,983 (150%) | 17,218 (138%) |
| Paladin, Redoubt (C-P1), Fury opener, C25 (+90%) | 7,938 (233%) | 10,928 (164%) | 18,786 (151%) |
| Paladin, live, Fury opener, C25a (+80%) | 7,057 (207%) | 9,463 (142%) | 16,324 (131%) |
| Paladin, Redoubt (C-P1), Fury opener, C25a (+80%) | 7,526 (220%) | 10,358 (155%) | 17,810 (143%) |

- **A bad pull costs the Paladin less than the Warrior,** as in part 8. With C25, the Paladin has 2.2 times the Warrior threat after 3 sec.

**Best short windows (part 8).** The highest threat in any window of the 3 min fight, % of the Warrior.

| Tank | Best 3 sec | Best 6 sec | Best 10 sec |
| --- | --- | --- | --- |
| Warrior | 12,939 | 18,711 | 24,964 |
| Druid | 15,773 (122%) | 21,728 (116%) | 30,608 (123%) |
| Paladin, live, Fury opener, C25 (+90%) | 12,504 (97%) | 16,704 (89%) | 25,591 (103%) |
| Paladin, Redoubt (C-P1), Fury opener, C25 (+90%) | 12,819 (99%) | 17,296 (92%) | 26,624 (107%) |
| Paladin, live, Fury opener, C25a (+80%) | 11,850 (92%) | 15,832 (85%) | 24,255 (97%) |
| Paladin, Redoubt (C-P1), Fury opener, C25a (+80%) | 12,149 (94%) | 16,392 (88%) | 25,233 (101%) |

- **The best windows are near the Warrior level.** With C25, the live Paladin has 89–103% of the Warrior. The Druid has 116–123%. With C25a, the Paladin has 85–97%.
- **The Paladin still has no threat cooldown.** The Warrior and the Druid keep the largest spikes.

**Conclusion.** C25 (+90%) gives the Paladin the Warrior threat again in the model and in wowsims, with the live trees. It gives the positions of the beta of 30 October again. In wowsims, the Druid keeps more threat: the Paladin with C25 has 92% of the Druid, and 98% with Redoubt (C-P1). C25a (+80%) gives 96–98% of the Warrior on one boss in the late raids in the model, and 106% in wowsims. With Redoubt (C-P1), C25a gives 113% in wowsims. Thus, the recommendation stays C25, because the model is the lower case and the Druid has more threat. Use C25a if Blizzard adopts Redoubt (C-P1).

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
- Threat: Bear Form ×2.15 (notes of 2 November 2026; client 1.60.1.70755: ×1.5), Maul ×1.75, Primal Bite ×3, Swipe ×1.75 (player data). wowsims master 9a8624af9 uses the same values. The ability multipliers are not verified in the game.
- Primal Bite is now the Feral talent in row 7 (31 points). The model keeps it in the rotation.
- Each swing: weapon DPS + Attack Power ÷ 14, with a 2.5 sec swing. Predatory Strikes +90 Attack Power.
- Maul rank 7: +128 damage, +10%, 10 rage. Primal Bite rank 4: weapon damage + 77, 15 rage, 6 sec cooldown. Lacerate rank 3: 15 rage, a stack bleed.
- Faerie Fire in Bear Form: 120 threat, 6 sec cooldown (player data, not verified). wowsims gives it no threat.
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

- Redoubt (C-P1): block 42.3% → 61.6%. The model multiplies the Holy Shield blocks by 1.46 and the Reckoning attacks by 1.29.
- Reckoning (C-P12), withdrawn: extra attacks ×1.48.
- Holy Strike Seal trigger (C1), withdrawn: each Holy Strike that lands also triggers Seal of Fury.

## 11. Method and limits

- **Scripts.** `models/beta-30-oct/threat_tables_b2.py` for the model. `models/wowsims-b2` for wowsims Forever (master commit 9a8624af9 of 4 November 2026, game files of client 1.60.1.70755 and the hotfixes of 4 November), 3,000 iterations. `models/wowsims-b2/tank_gear/run_pool.sh` gives the runs with the item pool threat sets (`logs/checks_9a8624af9_pool.log`), and with the argument `surv` the runs with the survival sets (`logs/checks_9a8624af9_pool_surv.log`). The withdrawn ideas C1 and C-P12 use the runs of master commit 895cd67f9 (1 November). The Warrior and Druid wowsims values are native values. The Paladin has the tank consumables of part 6 (`feedbackConsumables` in `go/feedback_prot_test.go`). `FEEDBACK_CONSUMES=default` gives the Demonic Rune only, as in the runs before 4 November evening.
- **Holy Shield blocks.** The model gives Redoubt (C-P1) too many blocks. Use the wowsims value.
- **Druid multipliers.** The Maul, Swipe and Primal Bite values come from player data. wowsims uses the same values. A test in the game must confirm them (see Open items).
- **Gear.** The model gives all tanks the same gear. wowsims gives each class a threat set and a survival set from the item pool of Analysis, Damage, part 7 (part 6). Parts 7 to 9 use the threat sets. `models/wowsims-b2/tank_gear` has the search and the sets.
- **Righteous Fury.** The values use the wowsims rule: the two multipliers multiply (×2.527). If they add, Holy threat is ×2.23, and the Paladin has about 10% less threat.
- **Holy Shield rank 4** is a level 60 spell since build 70755. The model uses its 221 damage.
- **Righteous Fury (C25).** The `C25` flag of `proposals_sim.go` multiplies all Paladin threat by 1.9 ÷ 1.33. `RF_ALL` sets the value. The sim tank always has Righteous Fury, thus a fixed multiplier gives the same result.
- **Burst threat (part 8).** `models/wowsims-b2/patches/burst-threat.patch` adds the threat recorder. `run.sh` gives the runs. The openers are sim rotations. A player can use a different opener.
- **Groups model.** Trash has no Sunder Armor or Faerie Fire. Demoralizing Shout, Demoralizing Roar and tab targets are not in the model.
- The earlier version of this tab (trees of 18 October) is in the history of the repository.
