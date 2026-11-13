# Threat

**Question.** Does the Paladin tank hold a boss and a group as well as the Warrior and the Druid?

All values are threat each sec (TPS). The tanks are level 60 and the boss is level 63. The values come from a model and from wowsims. The proposed values include Righteous Fury +90% (C25). Part 9 compares C25 alone with the alternative C25a (+80%). Part 10 gives the inputs.

The Warrior and Druid values use the development notes of 2 November 2026. Defensive Stance gives +80% threat (was +30%) and Defiance 7/13/20% (was 5/10/15%). Bear Form and Dire Bear Form give +115% (was +50%). The hotfix pushes of 4 November 2026 (113600 and 113605) have these values, and wowsims Forever master 9a8624af9 reads them from the game data. Thus the wowsims Warrior and Druid values are now native values, with no scaling. A test on the live realms must confirm them.

All tanks in wowsims have tank consumables. The Paladin has the same consumables as the Warrior, with two Paladin choices: Greater Arcane Elixir (spell power) and Brilliant Wizard Oil on the weapon (part 6).

## Short answer

- **No. After the development notes of 2 November 2026, the Paladin tank has less threat than the Warrior and the Druid.** The notes give the Warrior ×1.44 and the Druid ×1.43 more threat. This replaces Blessing of Salvation (1 ÷ 0.7 = ×1.43). The Paladin received ×1.33 from Righteous Fury in the beta of 30 October, and no more on 2 November.
- **With the same gear, the live Paladin has 70% of the Warrior threat** in the model. In wowsims, with item pool tank sets and tank consumables, it has 75% of the Warrior and 50% of the Druid. Before the notes, it had 101% and 108% of the Warrior.
- **The Druid has 149% of the Warrior threat on one boss in wowsims.** Master 52471a100 (12 November) gives Lacerate 10/3 threat for each point of damage: Druid +43%. Master 129fcd89e (12 November evening) decreases the Hand of Justice and Ironfoe procs: Warrior −3%, Druid −1%. On 13 November, the new Warrior set has 5% less threat and takes 9% less damage. wowsims measured this rule in the game only on rank 2, at levels 38 to 50. Its own note says that the later ranks fit it only in part (part 6). On 11 November, the Druid had 99% of the Warrior.
- **From fresh 60 to Naxxramas, the live Paladin has 71–82% of the Warrior threat.** With Consecration on cooldown, it has 83–98%, but the mana does not last (see Mana).
- **With the proposals, the Paladin is above the Warrior.** Righteous Fury (C25) gives +90% to all threat (live: +33%). In wowsims, the proposed Paladin has 112% of the Warrior threat and 75% of the Druid (C25 alone: 106% and 71%). In the model, it has 114–135% of the Warrior from Naxxramas to fresh 60.
- **With +80% (C25a), the live Paladin has 101% of the Warrior in wowsims** and 96–111% in the model. With Redoubt (C-P1), it has 106% of the Warrior and 71% of the Druid in wowsims.
- **Righteous Fury (C25) closes the gap.** Redoubt (C-P1) gives more blocks, thus more Holy Shield damage: +5% in wowsims (78% of the Warrior). C25 multiplies all Paladin threat by 1.43.
- **Two threat proposals were withdrawn on 2 November 2026.** The Holy Strike Seal trigger (C1) and Reckoning (C-P12) each added +3% in wowsims of 1 November. They do not close the gap.
- **Judgement of the Crusader is important.** It gives the tank about 72 TPS. In the live version, the raid can need the tank Judgement for Light or Wisdom. The tank then has 62% of the Warrior threat. With Personal Judgement of the Crusader (C2), the tank keeps Crusader.
- **At the pull, the proposed Paladin has the best burst threat, but only with a Fury opener** (part 8). The Paladin casts Seal of Fury and Holy Shield before the pull. Two Judgements of Fury and Holy Strike then hit at 0 sec. The live Paladin then has 154% of the Warrior threat after 1.5 sec, 98% after 3 sec and 84% after 10 sec. The proposed Paladin has 145% after 3 sec and 126% after 10 sec. With the wowsims default opener, the live Paladin has 50% after 3 sec.
- **In its best short windows, the live Paladin has 60–69% of the Warrior** (part 8). The proposed Paladin has 87–101%. The Druid has 124–139%. The Warrior has large spikes from Shield Slam, Revenge and Heroic Strike critical hits.
- **Against 3 or more enemies, the Paladin still holds the extra enemies well.** On the enemy with the least threat, the live Paladin has 2.4 times the Warrior threat. The proposed Paladin has 3.5 times. With the proposals, its total threat is 120–125% of the Warrior and 110–114% of the Druid.
- **Threat sets and survival sets give the same threat order** (part 6). With the survival sets, the live Paladin has 79% of the Warrior and the proposed Paladin 117%.
- **With the same consumables, Redoubt (C-P1) brings the Paladin near the damage taken of the Warrior** (part 6). The live Paladin takes 17% more damage than the Warrior. With Redoubt, it takes 5% more damage (threat sets) or 8% more damage (survival sets). With the survival sets, its TMI is lower than the Warrior TMI. Before 4 November evening, the Paladin test had no consumables, and the gap was 28%.
- **The wowsims tank sets obey the item pool rules** (part 6): no raid drops, no Zul'Gurub or Ahn'Qiraj items, no PvP items, no Revered or Exalted reputation items, item level 63 or lower. The wowsims default sets had these items.
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
- **The proposed Paladin has 114–135%** of the Warrior threat in the model. Without C25, it has 80–94%. wowsims gives a smaller gain from Redoubt (part 6): the proposed Paladin has 120% there.
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

The design goal is a Paladin tank with the threat of the Warrior. The beta of 30 October reached it (101%). The development notes of 2 November give the Warrior and the Druid about ×1.44, and the Paladin no change. Thus, the live Paladin has 70% of the Warrior threat in the model, and 75% in wowsims.

- **Why the gap.** Blessing of Salvation decreased the threat of the damage dealers by 30%. Blizzard removed it and gave the tanks about ×1.43 (1 ÷ 0.7). The Paladin received ×1.33 from Righteous Fury in the beta of 30 October. But the Paladin needed this ×1.33 to reach the Warrior before the notes.
- **Redoubt (C-P1) adds 5% in wowsims.** With Redoubt only, the tank has 78% of the Warrior threat. The live tank blocks 44% of the swings, and 59% with Redoubt (part 6).
- **The Holy Strike Seal trigger (C1) and Reckoning (C-P12) were withdrawn.** Each added only +3% in wowsims of 1 November. They do not close the gap.
- **The fix: Righteous Fury (C25).** The Paladin needs about ×1.44 on all threat. C25 changes the first part of Righteous Fury from +33% to +90% to all threat: ×1.43. The model needs +62% at fresh 60 and +88% in Naxxramas. wowsims needs +78% to reach the Warrior with the item pool tank sets and tank consumables. To reach the Druid of 12 November, it needs +166%. This is a baseline spell, thus the talent rule (a % only) is not necessary.
- **With C25, the model gives 101–117% of the Warrior threat** from Naxxramas to fresh 60. Before the notes, the live Paladin had 101–118%. With all proposals, wowsims gives 112% of the Warrior and 75% of the Druid.
- **The gear is not the same.** wowsims gives each class a tank set from the same item pool (part 6), but the items are different for each class. A Warrior with better gear can make the gap larger.
- **Consumables are important.** The Paladin test of wowsims has only a Demonic Rune. With the tank consumables of the Warrior test and two Paladin choices, the live Paladin has +10% threat and −11% damage taken (part 6).
- **Live tests give the real answer.** First, confirm the new Defensive Stance and Bear Form values on the live realms. Then compare the tanks with the same gear in real fights.

## 6. Check with wowsims

wowsims Forever plays the fight with the full rules of the game. Full buffs, one level 63 boss from the front, 3 min fight. The Paladin has the wowsims default tank build (12/32/7) with Redoubt 5/5.

**Tank sets.** Each class has two tank sets from the item pool of Analysis, Damage, part 7: a threat set and a survival set. Threat sets: [Protection Paladin](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-pool-protection-paladin.html), [Protection Warrior](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-pool-protection-warrior.html) and [Bear Druid](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-pool-bear-druid.html). Survival sets: [Protection Paladin](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-surv-protection-paladin.html), [Protection Warrior](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-surv-protection-warrior.html) and [Bear Druid](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-surv-bear-druid.html).

- **Item pool rules.** No raid drops. No items of the Zul'Gurub and Ahn'Qiraj patches (item ids 19000 to 23999). No PvP items. No Revered or Exalted reputation items. Item level 63 or lower.
- **Search.** The search starts from the wowsims default tank set of each class. It replaces each item that is not in the pool. For each slot, it runs the 12 best pool items for the tank stats in wowsims, 1,000 iterations each. Since 11 November, it also runs all pool items with an effect that wowsims implements, in all slots. Examples are the proc weapons Ironfoe and Flurry Axe. It keeps the item with the best tank score. Threat set: 40% threat, 20% damage, 20% damage taken and 20% TMI. Survival set: 40% threat, 30% damage taken and 30% TMI. The final set runs with 3,000 iterations. The enchants do not change. Scripts: `models/wowsims-b2/tank_gear`.
- **Replaced items.** Paladin: 10 items, for example Arena Grand Master, Force Reactive Disk and Dark Iron Destroyer. Warrior: 8 items, for example Annihilator, Hyperion Legplates and Ring of Awareness. Druid: 11 items, for example the PvP bracers, the Stormpike Insignia, Timbermaw Brawlers and the Premier Grand Marshal's Battle Hammer.
- **The default sets** of wowsims have raid, PvP and reputation items. The [default sets](https://ralgathor.github.io/forever-paladin-feedback/sets/) page keeps their links. The Builds tab uses the two item pool Protection Paladin sets.

- **Consumables.** All tanks have tank consumables. The Warrior and the Druid use the consumables of their wowsims tests. wowsims has no Protection Paladin consumables (only a Demonic Rune). Thus the Paladin has the consumables of the Warrior test, with two Paladin choices: Greater Arcane Elixir in place of Winterfall Firewater, and Brilliant Wizard Oil in place of the Dense Sharpening Stone. The other items are Major Frenzy Potion, Smoked Desert Dumplings, EZ-Thro Dark Bomb, Goblin Sapper Charge, Major Healthstone, Rumsey Rum and the Elixirs of Ferocity, the Mongoose, Greater Defense and the Phalanx. A test of seven mixes on the survival set with Redoubt (C-P1) gave the most threat with this mix.

wowsims Forever master commit 9a8624af9 (4 November 2026) has the game data of client 1.60.1.70755 and the hotfixes of 4 November. This data has Holy Shield rank 4 (221 damage, 4 charges), Defensive Stance +80%, Defiance 7/13/20% and Bear Form +115%. The Warrior and Druid values are native wowsims values. The Paladin spells did not change since commit 8298ab833.

Master commit 9f254e8d8 (9 November 2026, hotfix push 113823) adds 262 items. It also changes the Windfury Totem rule and the Warrior and Druid threat rules. With the sets of 8 November, the Warrior gains 1.5% (1,489 → 1,512). The Druid loses 10% (1,756 → 1,582), and the live Paladin 2.8% (1,229 → 1,195). The search ran again for all tank sets. The Paladin threat set takes Warder's Gloves, Scalding Flamehoof (new) and Volunteer's Lucky Seal. It loses Justicar's Gloves and Enriched Seal: −0.6% threat and −3.9% damage taken. The Druid survival set takes Warden's Leather Bracers, Thrall's Resolve (new) and Scalding Flamehoof. The other sets do not change. On 8 November (commit ae9b8c23a), the Paladin threat set took Lightforge Belt, Hand of Edward the Odd and Argent Defender. On 6 November (commit df57e2571), Scarlet Kris replaced Greatflank Flayer in the Warrior set (1,448 → 1,503).

Master commit 3633d376a (11 November 2026, client 1.60.1.70888, hotfixes of 10 and 11 November) adds 464 items, for example Ironfoe. It also gives Shield Slam ranks 2 to 4 flat threat. It fixes an error: until this commit, wowsims applied the proc buff of Argent Defender (+18% block for 10 sec) all the time. Now wowsims lists this proc as not implemented, and the shield gives only its stats. With the sets of 9 November, the live Paladin loses 4.5% (1,187 → 1,133) and takes 6% more damage. The Warrior gains 5.3% (1,512 → 1,592), and the Druid 0.7% (1,582 → 1,593). The search ran again for all tank sets, also with the proc items that wowsims implements. The Warrior threat set takes Ironfoe (a proc weapon), Grimy Metal Boots, Myrmidon's Signet, Royal Seal of Eldre'Thalas, Eaglehorn Long Bow and Hand of Justice. The Druid threat set takes Ouroboros Ring and Hand of Justice. The Paladin survival set takes Intricately Runed Shield in place of Argent Defender, and five other items. The Paladin threat set does not change: Argent Defender still has the best stats. In the Paladin main hand, Flurry Axe and Ironfoe come second and third, after Hand of Edward the Odd. The Warrior survival set takes Skullflame Shield, Force Imbued Gauntlets, Hand of Justice and two other items.

Master commit 52471a100 (12 November 2026, hotfixes of 11 and 12 November) adds 69 items, for example Darrowshire Strongguard and Warmaster Legguards. Weapon procs no longer trigger from Shield Slam, Shield Bash, Thunder Clap and abilities with magic DefenseType. Lacerate now gives 10/3 threat for each point of damage, from the hit and from the ticks. Faerie Fire in Bear Form gives 2 × level threat. With the sets of 11 November, the Warrior loses 0.5% (1,632 → 1,624). The Druid gains 43% (1,614 → 2,302). The Paladin values do not change. The search ran again for all tank sets. The Warrior threat set takes Skullflame Shield and Deep Jungle Rifle (+1.0% score). The Warrior survival set takes Ironfoe, Warmaster Legguards, Royal Seal of Eldre'Thalas, Mark of Tyranny and five other items (+0.7%). The other sets do not change.

Master commit 129fcd89e (12 November 2026 evening, hotfixes of 12 November and push 114027) changes two proc items. Hand of Justice now has its full proc chance (3%) only against Dwarves, and 1% against other targets. Ironfoe has 6% against Orcs and 3% against other targets. Weapon procs no longer trigger from melee abilities with no DefenseType. wowsims now gives the set bonuses of 113 item sets, and adds Blackhand's Breadth. With the sets of 12 November, the Warrior loses 3.0% (1,650 → 1,601) and the Druid 1.1% (2,302 → 2,277). The Paladin values do not change: its sets have no Hand of Justice and no Ironfoe. The search ran again for all tank sets. The Warrior survival set takes Hammer of the Vesper in place of Ironfoe, Naglering and Sentinel's Gloves (+0.7% score). The other sets stay. The threat set searches gave −0.3% to +0.06%. The Paladin survival set search gave +0.4% (Cloudkeeper Legplates), less than the 0.5% run noise.

The values below come from master commit 8c7b5a5f5 (13 November 2026, client 1.60.1.70938, hotfixes of 13 November). It changes Redoubt and Shieldsworn: each melee swing or ability against the Paladin rolls the 10% Redoubt chance, avoided attacks included. The hotfixes of 11 November make the judgements ranged attacks. The late hotfix of 13 November makes Judgement of Command a melee attack again. The tank uses Judgement of Fury, thus the tank values do not change. Since 13 November, our runs use this rule (`patches/judgement-ranged.patch`): Judgement of Righteousness and Judgement of Fury no longer trigger melee weapon procs. The commit also adds 46 items, for example The Lion Horn of Stormwind. When the tank is struck, it has a 10% chance to give 725 armor for 30 sec. With the sets of 12 November, evening, the live Paladin gains 0.7% threat (1,133 → 1,141) and takes 2.4% less damage (336 → 328). Redoubt (C-P1) loses 0.5% (1,208 → 1,202). The Warrior and the Druid do not change. The search ran again for all tank sets. Four sets change, all with The Lion Horn of Stormwind. The Paladin threat set takes Draconian Deflector in place of Argent Defender, Storm Gauntlets, Bolt's Charged Eyeball and four other items (+0.6% score). It has 0.2% less threat and takes 3.9% less damage. The Warrior threat set takes Scaleguard Scimitar in place of Ironfoe, Sabatons of Heroism and three other items (+2.0% score). It has 4.7% less threat and takes 8.8% less damage. The Paladin survival set (+2.3%) and the Druid survival set (+1.5%) also change.

| Tank | TPS (% of the Warrior, % of the Druid) | Damage taken each sec | TMI | Crushing blows |
| --- | --- | --- | --- | --- |
| Warrior | 1,525 (100%, 67%) | 269 | 38 | 1.0% |
| Druid | 2,277 (149%, 100%) | 359 | 37.9 | 15.0% |
| Paladin, live | 1,139 (75%, 50%) | 316 | 50.4 | 10.1% |
| Paladin, Redoubt (C-P1) | 1,196 (78%, 53%) | 282 | 40.9 | 1.2% |
| Paladin, Righteous Fury (C25) | 1,621 (106%, 71%) | 316 | 50.4 | 10.1% |
| **Paladin, all kept proposals (C-P1, C-P13, C25)** | **1,703 (112%, 75%)** | **287** | **41.8** | **1.2%** |

- **The live Paladin has 75% of the Warrior threat in wowsims.** The model gives 70%. The model has no consumables. Before the notes of 2 November, they gave 101% and 108%.
- **The Argent Defender error.** From 8 to 10 November, wowsims gave the live Paladin 55% block in place of 41%, and 5% more threat. It had 5.6% crushing blows in place of 12.0%. Now the live Paladin blocks 44% of the swings and takes 10.1% crushing blows (Analysis, Crushing blows). Since 13 November, its threat set has Draconian Deflector in place of Argent Defender. Hand of Edward the Odd gives 90 spell damage.
- **The Druid has 149% of the Warrior threat.** Master 52471a100 gives Lacerate 10/3 threat for each point of damage, and the Druid gains 43% (99% → 140% of the Warrior). On master 129fcd89e, the Warrior loses more threat than the Druid from the Hand of Justice change (142%). On master 8c7b5a5f5, the new Warrior set has less threat (149%). wowsims measured this rule in the game only on rank 2 in Bear Form, at levels 38 to 50. Its note says that the later ranks in Dire Bear Form fit 10/3 only in part. A test at level 60 must confirm it (Open items).
- **Where the Druid gain comes from.** On both commits, the Druid has the same set and rotation: 80 Lacerate casts in 3 min. The Lacerate hit goes from 175 to 585 threat each sec (×10/3). The Lacerate ticks go from 65 to 349 threat each sec. Since 12 November, a Lacerate dose keeps the tick timer of the bleed, thus the ticks do 62% more damage. Maul, Primal Bite and the melee hits do not change. Lacerate now gives 41% of the Druid threat (was 15%). Log: `logs/druid_threat_by_ability_52471a100.log`.
- **wowsims applies its rules correctly.** Each ability has the threat for each point of damage that its rule gives: melee hits 2.15 (Bear Form +115%), Maul 3.76 (×1.75), Primal Bite 6.45 (×3), Lacerate hit and ticks 7.17 (×10/3). Our runs give the same values as the wowsims runs. The only open point is the Lacerate rule at level 60.
- **If the Lacerate rule is different at level 60 (commit 52471a100).** wowsims notes that rank 5 in Dire Bear Form fits 10/3 only in part. With ×2 in place of ×10/3, the Druid has 1,929 threat each sec (117% of the Warrior). With no Lacerate bonus, it has 1,649 (100%). The live Paladin then has 59% and 69% of the Druid. With C25 and C-P1, it has 89% and 104%.
- **The Druid values before 12 November.** wowsims master 9a8624af9 gives Bear Form +115% and Maul ×1.75, Swipe ×1.75 and Primal Bite ×3. Master 9f254e8d8 decreases the Druid threat by 10% (118% → 105% of the Warrior). Master 3633d376a gives the Warrior Shield Slam flat threat (105% → 101%). Hand of Justice in the Warrior set gives 99%. The earlier runs gave Bear Form only, and the Druid had 77% of the Warrior.
- **The consumables give the Paladin +10% threat and −11% damage taken.** Without them (Demonic Rune only), the live Paladin had 1,029 TPS and 384 damage taken each sec (set of 4 November).
- **With Redoubt (C-P1), the Paladin takes 5% more damage than the Warrior** (282 against 269 each sec). Its TMI is also higher (40.9 against 38). The live Paladin takes 17% more damage than the Warrior. With all kept proposals, it takes 7% more damage than the Warrior (287 against 269). The Warrior set of 13 November takes 9% less damage than the set of 12 November (269 against 295).
- **Redoubt adds less in wowsims:** +57 TPS (+5%) against +96 TPS (+15%) in the model. The model gives too many Holy Shield blocks. The live Paladin blocks 44% of the swings (Redoubt: 59%). Since 13 November, the live Redoubt rolls on more attacks, thus C-P1 adds less (+7% before).
- **Righteous Fury (C25) multiplies all Paladin threat by 1.43.** With all kept proposals, the Paladin has 112% of the Warrior threat and 75% of the Druid. The model gives 115% of the Warrior (part 1).
- **Holy Shield rank 4 adds 6% in wowsims.** With the default set and rank 3 (wowsims of 1 November), the live Paladin had 928 TPS. With rank 4, it had 980 TPS.
- **C1 (withdrawn) agrees:** +26 in wowsims of 1 November, +25 in the model. The C1 flag does not run on commit d97252f2a.
- **Reckoning (C-P12), withdrawn.** With C1, it gave +27 more in wowsims of 1 November and +20 in the model.
- **Toughness removal (C-P13)** does not change threat. Damage taken increases by 2%.

**Survival sets.** The same runs with the survival set of each class.

| Tank | TPS (% of the Warrior, % of the Druid) | Damage taken each sec | TMI | Crushing blows |
| --- | --- | --- | --- | --- |
| Warrior | 1,386 (100%, 64%) | 251 | 39 | 0.9% |
| Druid | 2,163 (156%, 100%) | 334 | 35.1 | 15.1% |
| Paladin, live | 1,090 (79%, 50%) | 300 | 43.6 | 10.0% |
| Paladin, Redoubt (C-P1) | 1,141 (82%, 53%) | 270 | 35.9 | 1.2% |
| Paladin, Righteous Fury (C25) | 1,551 (112%, 72%) | 300 | 43.6 | 10.0% |
| **Paladin, all kept proposals (C-P1, C-P13, C25)** | **1,624 (117%, 75%)** | **275** | **36.7** | **1.2%** |

- **The threat order does not change.** The Paladin loses 4% threat with its survival set (1,139 → 1,090), the Warrior 9% (1,525 → 1,386) and the Druid 5%. The Paladin keeps 79% (live) and 117% (all kept proposals) of the Warrior.
- **The TMI decreases for the Paladin and the Druid:** Paladin 50.4 → 43.6 (live) and 41.8 → 36.7 (all kept proposals), Druid 37.9 → 35.1. The Warrior TMI stays almost the same (38 → 39): its threat set of 13 November already takes less damage.
- **With Redoubt (C-P1), the Paladin takes 8% more damage than the Warrior** (270 against 251 each sec), but its TMI is lower (35.9 against 39). The live Paladin takes 20% more damage. The Warrior dodges more (25.6% against 16.1%), and the boss has 1.4% critical hits on the live Paladin (Warrior: 0.1%).
- **C25a (+80%)** gives 106% of the Warrior (live) and 111% with C-P1 (threat sets: 101% and 106%).

**Other fights (wowsims, 3 min, item pool threat sets).** TPS, % of the Warrior in brackets. "Fast" is a swing each 1.2 sec with 60% damage, thus the same damage each sec. "Two weapons" is a boss with a second weapon. The 5 min row has C-P1 only: Toughness removal (C-P13) does not change threat.

| Boss | Warrior | Paladin, live | Paladin, C-P1 and C-P13 | Paladin, all kept proposals (×1.43) |
| --- | --- | --- | --- | --- |
| Normal, 5 min | 1,508 | 1,137 (75%) | 1,193 (79%) | 1,705 (113%) |
| Fast | 1,607 | 1,258 (78%) | 1,293 (80%) | 1,847 (115%) |
| Two weapons | 1,661 | 1,298 (78%) | 1,321 (80%) | 1,887 (114%) |
| Fast, two weapons | 1,753 | 1,380 (79%) | 1,380 (79%) | 1,971 (112%) |

- **Faster boss attacks help the Warrior and the Paladin.** The Warrior receives more rage. The Paladin blocks more, thus Holy Shield hits more.
- **Against a boss with two weapons, Redoubt adds little threat** (0% to +1.7%). The Holy Shield charges are empty too soon (Crushing blows, part 3).

**Other Seals (wowsims, 3 min, item pool threat set).** Threat each sec, damage taken each sec and TMI. Seal of Command needs a build with 13 Retribution points: [`b201005-05302102213301531-50223001`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b201005-05302102213301531-50223001). It takes Conviction 2, Sanctified Judgement 3 and Seal of Command in place of Divine Strength 4 and Holy Conduit 2.

| Build and Seal | Live: threat | Live: damage taken | Live: TMI | C25 and C-P1: threat |
| --- | --- | --- | --- | --- |
| Live build, Seal of Fury | 1,139 | 316 | 50.4 | 1,703 |
| Live build, Seal of Righteousness | 1,123 (−1.4%) | 329 | 52.7 | 1,681 (−1.3%) |
| Seal of Command build, Seal of Fury | 1,161 | 316 | 50.4 | 1,735 |
| Seal of Command build, Seal of Righteousness | 1,144 (−1.5%) | 329 | 52.7 | 1,711 (−1.4%) |
| Seal of Command build, Seal of Command | 1,065 (−8.3%) | 332 | 53.1 | 1,592 (−8.2%) |

- **Seal of Fury stays the best tank Seal.** Seal of Righteousness gives 1.4% less threat, and Seal of Command 8% less. The proposals do not change this order.
- **The other Seals also cost survival.** Without the Seal of Fury absorb shield, the Paladin takes 4–5% more damage, and the TMI increases by 2–3 points.
- **Seal of Command procs only on a part of the swings.** Seal of Fury and Seal of Righteousness hit on each swing. These runs have the judgement hotfixes: Judgement of Command is a melee attack, and Judgement of Righteousness is a ranged attack.
- **The Seal of Command build has more threat with Seal of Fury** (+1.9% against the live build, 1,161 against 1,139). It also has more than BS2 (1,154, Builds). Conviction and Sanctified Judgement give more than Divine Strength and Holy Conduit. A new talent search is due.
- **Files.** `models/wowsims-b2/apl/sor.apl.siml` and `soc.apl.siml` (flag `FEEDBACK_APL`), log `logs/seals_8c7b5a5f5.log`.

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

**wowsims result.** Item pool tank sets and tank consumables (part 6). Each enemy is level 63 and hits for 1/3 of a boss hit. The Paladin uses its default rotation with Consecration. The values are TPS on each target, with the main target first. All values come from commit 8c7b5a5f5 (part 6).

| Tank | 1 target | 3 targets | 5 targets |
| --- | --- | --- | --- |
| Paladin, live | 1,139 | 1,079 / 298 / 299 | 1,053 / 256 / 256 / 256 / 138 |
| Paladin, proposed | 1,702 | 1,539 / 427 / 426 | 1,500 / 364 / 364 / 364 / 196 |
| Warrior | 1,426 | 1,432 / 365 / 123 | 1,501 / 528 / 117 / 117 / 56 |
| Druid | 1,891 | 1,616 / 280 / 280 | 1,742 / 293 / 293 / 57 / 57 |

- **On the lowest target, the Paladin still leads the Warrior.** On 3 targets, the live Paladin has 2.4 times the Warrior threat and 106% of the Druid. On 5 targets, it has 2.5 times the Warrior threat and 2.4 times the Druid threat.
- **The proposed Paladin leads by more.** On the lowest target, it has 3.5 times the Warrior threat on 3 and 5 targets. It has 152% of the Druid on 3 targets and 3.5 times on 5 targets.
- **In total, the live Paladin is last.** On 3 targets: live Paladin 1,677, Warrior 1,921, Druid 2,177. On 5 targets: live Paladin 1,959, Warrior 2,320, Druid 2,442.
- **The proposed Paladin has more than the Druid total.** On 3 targets: 2,392 (125% of the Warrior, 110% of the Druid). On 5 targets: 2,790 (120% of the Warrior, 114% of the Druid).
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

**Conclusion.** Against 3 or more enemies, the Paladin holds the extra enemies better than the Warrior. On 5 targets, it holds them better than the Druid too. The live total threat is the lowest of the three tanks. The problem is the main target (parts 1 and 6). With Righteous Fury (C25), the Paladin is above the Warrior on the main target and in total, and above the Druid total.

## 8. Burst threat

This part compares the threat in the first seconds of a pull and in the best short windows of a fight. A damage dealer pulls the boss when it has more threat than the tank. At the start of a pull, and after a large threat spike, this can occur before the sustained values of part 6 apply.

**Setup.** wowsims, as in part 6: item pool tank sets, tank consumables, full buffs, one level 63 boss from the front, 3 min fight, 3,000 iterations. A recorder adds the threat on the boss in steps of 0.1 sec. All values come from commit 8c7b5a5f5, except the Warrior variants of commit 6ee3c30f35 (default sets).

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
| Warrior | 3,836 (100%) | 7,130 (100%) | 10,924 (100%) | 18,019 (100%) | 34,901 (100%) | 1,522 (100%) |
| Druid | 3,586 (93%) | 6,258 (88%) | 10,418 (95%) | 18,405 (102%) | 43,596 (125%) | 2,266 (149%) |
| Paladin, live, wowsims opener | 1,427 (37%) | 3,529 (50%) | 7,306 (67%) | 11,605 (64%) | 23,327 (67%) | 1,138 (75%) |
| Paladin, live, Fury opener | 5,889 (154%) | 6,968 (98%) | 9,125 (84%) | 15,057 (84%) | 26,367 (76%) | 1,156 (76%) |
| Paladin, proposed, wowsims opener | 2,032 (53%) | 5,016 (70%) | 10,715 (98%) | 17,198 (95%) | 34,782 (100%) | 1,699 (112%) |
| Paladin, proposed, Fury opener | 8,579 (224%) | 10,349 (145%) | 13,796 (126%) | 22,646 (126%) | 39,527 (113%) | 1,731 (114%) |

- **With the wowsims default opener, the Paladin starts slowly.** The first global cooldown goes to Judgement of the Crusader. Holy Shield starts at 3 sec, and Holy Strike at 4.5 sec.
- **With the Fury opener, the Paladin has the best start of the three tanks in the first 1.5 sec.** Two Judgements of Fury, Holy Strike, the Shieldsworn Holy Shield hit and the explosives hit the boss at the pull.
- **The live lead does not last.** After 3 sec, the live Fury opener has 98% of the Warrior, and after 10 sec 84%. After 20 sec, it has 76%, near the sustained gap of part 6.
- **The proposed Paladin keeps the lead.** With the Fury opener, it has 126% of the Warrior after 10 sec and 113% after 20 sec. In the first 3 sec, all of the gain comes from Righteous Fury (C25). Redoubt starts after the first blocks.
- **The Druid starts a little slower than the Warrior, but it is first after 20 sec.** It uses its 25 rage at once, but it has 88–95% of the Warrior in the first 6 sec. After 20 sec, it has 125% of the Warrior, and the proposed Paladin with the Fury opener 113%. The Lacerate threat of 12 November gives the Druid this gain (part 6).
- **The Warrior needs rage first.** It starts with 0 rage. Its threat increases fast from 2 sec, when the boss hits give rage.
- **Boss armor helps the Paladin.** In the first 6 sec, the boss has less than 5 Sunder Armor stacks. This decreases Warrior and Druid physical damage. Most Paladin threat is Holy damage, thus boss armor does not decrease it.
- **With one Judgement at 0 sec,** Swift Judgement hits at 1.5 sec. Only the first 1.5 sec change: 4,581 threat (119%) in place of 5,889. From 3 sec, the two openers have the same threat.

**Bad pulls** (threat on the 10% worst fights, % of the Warrior on its 10% worst fights)

| Tank | First 3 sec | First 6 sec | First 10 sec |
| --- | --- | --- | --- |
| Warrior | 3,106 (100%) | 6,848 (100%) | 12,360 (100%) |
| Druid | 2,886 (93%) | 6,077 (89%) | 12,333 (100%) |
| Paladin, live, wowsims opener | 2,608 (84%) | 5,432 (79%) | 9,326 (75%) |
| Paladin, live, Fury opener | 5,228 (168%) | 7,099 (104%) | 12,350 (100%) |
| Paladin, proposed, Fury opener | 7,882 (254%) | 10,919 (159%) | 18,806 (152%) |

- **A bad pull costs the Warrior and the Druid the most.** When their first attacks miss or the boss attacks miss them, they have no rage. The Warrior threat after 3 sec decreases to 44% of its mean. The Druid keeps 46%, and the live Paladin 74%.
- **A bad pull costs the Paladin less.** Judgement of Fury cannot be dodged or parried. Holy Shield and Seal of Fury cannot miss.

**Best short windows** (the highest threat in a window at any time in the 3 min fight, % of the Warrior)

| Tank | Best 3 sec | Best 6 sec | Best 10 sec | Best 3 sec ÷ mean 3 sec |
| --- | --- | --- | --- | --- |
| Warrior | 13,587 (100%) | 19,046 (100%) | 26,168 (100%) | ×3.0 |
| Druid | 16,849 (124%) | 25,148 (132%) | 36,313 (139%) | ×2.5 |
| Paladin, live, wowsims opener | 8,094 (60%) | 11,599 (61%) | 17,521 (67%) | ×2.4 |
| Paladin, live, Fury opener | 8,677 (64%) | 11,733 (62%) | 17,975 (69%) | ×2.5 |
| Paladin, proposed, wowsims opener | 11,855 (87%) | 17,054 (90%) | 25,741 (98%) | ×2.3 |
| Paladin, proposed, Fury opener | 12,675 (93%) | 17,194 (90%) | 26,390 (101%) | ×2.5 |

- **The Paladin has no threat cooldown.** Its best windows come from Holy Strike, Judgement and Holy Shield in the same 3 sec, with critical hits. The Warrior adds Shield Slam, Revenge and Heroic Strike critical hits to the rage from boss hits. The Druid has larger windows than the Warrior (124–139%), from Maul, Primal Bite and Lacerate.
- **The best-window gap is larger than the sustained gap.** Live: 60–69% against 75%. Proposed: 87–101% against 112%. Thus the Paladin has a smaller margin against a large threat spike from a damage dealer.

**Warrior variants**

| Warrior | First 1.5 sec | First 3 sec | First 6 sec | First 10 sec |
| --- | --- | --- | --- | --- |
| Default, with Goblin Sapper Charge (above) | 3,836 | 7,130 | 10,924 | 18,019 |
| No engineering items | 2,241 (−42%) | 5,495 (−23%) | 9,374 (−14%) | 16,495 (−8%) |
| Default set, no engineering items, commit 6ee3c30f35 | 1,968 | 4,609 | 6,962 | 12,881 |
| Default set, Charge at −0.5 sec, 20 yards (Vanguard), commit 6ee3c30f35 | 1,711 (−13%) | 4,213 (−9%) | 7,223 (+4%) | 13,354 (+4%) |

- **Charge does not increase the Warrior burst.** Charge gives 15 rage, but this rage gives no threat. The Charge stun also delays the first boss swings, thus the Warrior receives less rage from boss hits. The Charge rotation does not run on commits 8298ab833, 9a8624af9, ae9b8c23a, 9f254e8d8, 3633d376a, 52471a100, 129fcd89e and 8c7b5a5f5: the Warrior does almost no attacks. Thus, the Charge row comes from commit 6ee3c30f35 with the default Warrior set, and its % compare it with the default rotation of that commit. The two rows of commit 6ee3c30f35 are wowsims values × 1.445 (the Warrior multipliers of the notes of 2 November).
- **Charge in combat.** With Vanguard, the Warrior can charge in Defensive Stance. The Vanguard Charge row in the game files still has the "not in combat" attribute. Thus the Warrior can charge only at the pull. A test in the game must confirm this.

**Tank swaps.** Shoulder the Burden (C-P5) moves 50% of the threat of an ally to the Paladin. After 30 sec, the Warrior has about 50,000 threat. Shoulder the Burden on the Warrior then gives the Paladin about 25,000 threat at once. This is 3 times the best 3 sec live Paladin window. It does not help at the pull, because no ally has threat yet.

**Conclusion.** With a Fury opener, the proposed Paladin holds the boss at the pull better than the Warrior and the Druid for 10 sec. The live Paladin leads only in the first 1.5 sec. The default opener of wowsims gives it 50% of the Warrior threat in the first 3 sec. After 10 sec, the sustained gap of part 6 returns. In short windows later in the fight, the live Paladin has 60–69% of the Warrior. The proposed Paladin keeps the lead on the Warrior for the first 20 sec, and has 87–101% of the Warrior in short windows. The Druid passes the Warrior after 10 to 20 sec, and its short windows are larger than the Warrior windows.

## 9. Righteous Fury alone: +90% (C25) and +80% (C25a)

This part gives parts 1 to 8 again with Righteous Fury (C25) alone, and with the live trees: all threat +90% in place of +33%. The alternative C25a gives +80%, the value of Defensive Stance.

- **Righteous Fury multiplies all Paladin threat.** Thus, C25 multiplies each Paladin value of the model by 1.43 (1.9 ÷ 1.33), and C25a by 1.35 (1.8 ÷ 1.33).
- **The wowsims values come from new runs.** C25 multiplies the wowsims threat by 1.43, and C25a by 1.35.
- **The Warrior and Druid values do not change.** They use the notes of 2 November, as in parts 1 to 8. The wowsims values are native values of commit 8c7b5a5f5.

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

**wowsims, one boss (part 6).** New runs, item pool tank sets, tank consumables, 3 min, 3,000 iterations. Damage taken and TMI do not change with Righteous Fury. The cells give TPS, then % of the Warrior and of the Druid.

| Paladin | Live (+33%) | C25 (+90%) | C25a (+80%) |
| --- | --- | --- | --- |
| Live | 1,139 (75%, 50%) | 1,621 (106%, 71%) | 1,536 (101%, 67%) |
| Redoubt (C-P1) | 1,196 (78%, 53%) | 1,703 (112%, 75%) | 1,614 (106%, 71%) |
| All kept proposals (with C-P13) | 1,196 (78%, 53%) | 1,703 (112%, 75%) | 1,614 (106%, 71%) |

The Warrior has 1,525 and the Druid 2,277 (commit 8c7b5a5f5).

- **C25: the live Paladin has 106% of the Warrior threat** in wowsims, and 112% with Redoubt (C-P1). The model gives 100%. Against the Druid of 12 November, it has 71% and 75% (part 6).
- **C25a: the live Paladin has 101%,** and 106% with Redoubt (C-P1). The model gives 95%. The Paladin has 67% and 71% of the Druid. The Warrior set of 13 November has 5% less threat, thus C25a now reaches the Warrior in wowsims.
- **Toughness removal (C-P13)** still does not change threat.

**wowsims, groups (part 7).** TPS on each target, main target first, and the total.

| Tank | 1 target | 3 targets | 5 targets |
| --- | --- | --- | --- |
| Paladin, live, C25 (+90%) | 1,620 | 1,540 / 424 / 424 (total 2,389) | 1,503 / 364 / 364 / 364 / 195 (total 2,792) |
| Paladin, Redoubt (C-P1), C25 (+90%) | 1,702 | 1,539 / 427 / 426 (total 2,392) | 1,500 / 364 / 364 / 364 / 196 (total 2,790) |
| Paladin, live, C25a (+80%) | 1,536 | 1,459 / 402 / 402 (total 2,264) | 1,424 / 345 / 345 / 345 / 185 (total 2,646) |
| Paladin, Redoubt (C-P1), C25a (+80%) | 1,613 | 1,458 / 405 / 404 (total 2,267) | 1,421 / 345 / 345 / 345 / 186 (total 2,644) |
| Warrior | 1,426 | 1,432 / 365 / 123 (total 1,921) | 1,501 / 528 / 117 / 117 / 56 (total 2,320) |
| Druid | 1,891 | 1,616 / 280 / 280 (total 2,177) | 1,742 / 293 / 293 / 57 / 57 (total 2,442) |

- **On 1 target, the Paladin with C25 holds the enemy better than the Warrior, but not the Druid.** With C25, it has 114% of the Warrior and 86% of the Druid. With C25a, it has 108% and 81%. On 3 and 5 targets, the Druid has the most threat on the main target.
- **In total, the Paladin is above the Warrior and the Druid.** With C25: 124% of the Warrior on 3 targets and 120% on 5 targets (Druid: 110% and 114%). With C25a: 118% and 114% of the Warrior.
- **On the lowest target, the lead becomes larger.** With C25, the Paladin has 3.4 times the Warrior threat on 3 targets and 3.5 times on 5 targets.
- **The model gives a larger lead** (part 7). With C25, the proposed Paladin has 172–213% of the stronger tank on 3 targets, and 165–195% on 5 targets.

**Burst threat (part 8).** Threat on the boss after the first seconds, % of the Warrior.

| Tank | First 1.5 sec | First 3 sec | First 6 sec | First 10 sec | First 20 sec | First 30 sec |
| --- | --- | --- | --- | --- | --- | --- |
| Warrior | 3,836 | 7,130 | 10,924 | 18,019 | 34,901 | 50,298 |
| Druid | 3,586 (93%) | 6,258 (88%) | 10,418 (95%) | 18,405 (102%) | 43,596 (125%) | 65,834 (131%) |
| Paladin, live, wowsims opener, C25 (+90%) | 2,032 (53%) | 5,016 (70%) | 10,394 (95%) | 16,503 (92%) | 33,187 (95%) | 48,030 (95%) |
| Paladin, Redoubt (C-P1), wowsims opener, C25 (+90%) | 2,032 (53%) | 5,016 (70%) | 10,715 (98%) | 17,198 (95%) | 34,782 (100%) | 50,522 (100%) |
| Paladin, live, Fury opener, C25 (+90%) | 8,389 (219%) | 9,918 (139%) | 12,985 (119%) | 21,430 (119%) | 37,532 (108%) | 51,835 (103%) |
| Paladin, Redoubt (C-P1), Fury opener, C25 (+90%) | 8,579 (224%) | 10,349 (145%) | 13,796 (126%) | 22,646 (126%) | 39,527 (113%) | 54,658 (109%) |
| Paladin, live, wowsims opener, C25a (+80%) | 1,926 (50%) | 4,755 (67%) | 9,852 (90%) | 15,644 (87%) | 31,457 (90%) | 45,526 (91%) |
| Paladin, Redoubt (C-P1), wowsims opener, C25a (+80%) | 1,926 (50%) | 4,755 (67%) | 10,157 (93%) | 16,302 (90%) | 32,968 (94%) | 47,888 (95%) |
| Paladin, live, Fury opener, C25a (+80%) | 7,950 (207%) | 9,400 (132%) | 12,308 (113%) | 20,312 (113%) | 35,574 (102%) | 49,131 (98%) |
| Paladin, Redoubt (C-P1), Fury opener, C25a (+80%) | 8,130 (212%) | 9,809 (138%) | 13,076 (120%) | 21,464 (119%) | 37,463 (107%) | 51,806 (103%) |

- **With the Fury opener, the Paladin has the best start by a large margin.** With C25, it has 139% of the Warrior after 3 sec and 119% after 10 sec. With C25a, it has 132% and 113%.
- **Without Redoubt, the lead on the Warrior is small after 30 sec.** After 30 sec, the live Paladin with C25 has 103% of the Warrior, and C25a 98%. With Redoubt (C-P1), C25 gives 109%. After 30 sec, the Druid has 131% of the Warrior.
- **With the wowsims default opener, the start is still slow:** 70% after 3 sec with C25, 67% with C25a. After 6 sec, the Paladin has 90–98%.

**Bad pulls (part 8).** Threat on the 10% worst fights, % of the Warrior on its 10% worst fights.

| Tank | First 3 sec | First 6 sec | First 10 sec |
| --- | --- | --- | --- |
| Warrior | 3,106 | 6,848 | 12,360 |
| Paladin, live, Fury opener, C25 (+90%) | 7,444 (240%) | 10,104 (148%) | 17,568 (142%) |
| Paladin, Redoubt (C-P1), Fury opener, C25 (+90%) | 7,882 (254%) | 10,919 (159%) | 18,806 (152%) |
| Paladin, live, Fury opener, C25a (+80%) | 7,059 (227%) | 9,575 (140%) | 16,652 (135%) |
| Paladin, Redoubt (C-P1), Fury opener, C25a (+80%) | 7,471 (241%) | 10,349 (151%) | 17,826 (144%) |

- **A bad pull costs the Paladin less than the Warrior,** as in part 8. With C25, the Paladin has 2.4 times the Warrior threat after 3 sec.

**Best short windows (part 8).** The highest threat in any window of the 3 min fight, % of the Warrior.

| Tank | Best 3 sec | Best 6 sec | Best 10 sec |
| --- | --- | --- | --- |
| Warrior | 13,587 | 19,046 | 26,168 |
| Druid | 16,849 (124%) | 25,148 (132%) | 36,313 (139%) |
| Paladin, live, Fury opener, C25 (+90%) | 12,360 (91%) | 16,706 (88%) | 25,592 (98%) |
| Paladin, Redoubt (C-P1), Fury opener, C25 (+90%) | 12,675 (93%) | 17,194 (90%) | 26,390 (101%) |
| Paladin, live, Fury opener, C25a (+80%) | 11,714 (86%) | 15,834 (83%) | 24,256 (93%) |
| Paladin, Redoubt (C-P1), Fury opener, C25a (+80%) | 12,013 (88%) | 16,296 (86%) | 25,011 (96%) |

- **The best windows stay below the Warrior level.** With C25, the live Paladin has 88–98% of the Warrior. The Druid has 124–139%. With C25a, the Paladin has 83–93%.
- **The Paladin still has no threat cooldown.** The Warrior and the Druid keep the largest spikes.

**Conclusion.** C25 (+90%) gives the Paladin the Warrior threat again in the model and in wowsims, with the live trees. It gives the positions of the beta of 30 October again. In wowsims of 13 November, the Paladin with C25 has 71% of the Druid threat, and 75% with Redoubt (C-P1). This Druid value comes from a Lacerate rule that has no level 60 test yet (part 6). C25a (+80%) gives 96–98% of the Warrior on one boss in the late raids in the model, and 101% in wowsims. With Redoubt (C-P1), C25a gives 106% in wowsims. In wowsims, C25a now reaches the Warrior, because the Warrior set of 13 November has 5% less threat. The model still gives C25a only 96–98% in the late raids. Thus, the recommendation stays C25. Use C25a only if Blizzard also adopts Redoubt (C-P1).

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

- Redoubt (C-P1): block 44.0% → 58.8% (item pool set of 13 November, commit 8c7b5a5f5; set of 11 November, commit 3633d376a: 41.2% → 60.7%; on commit 9f254e8d8, with the Argent Defender error: 55.0% → 61.9%; set of 4 November: 42.3% → 61.6%). The model multiplies the Holy Shield blocks by 1.46 and the Reckoning attacks by 1.29.
- Reckoning (C-P12), withdrawn: extra attacks ×1.48.
- Holy Strike Seal trigger (C1), withdrawn: each Holy Strike that lands also triggers Seal of Fury.

## 11. Method and limits

- **Scripts.** `models/beta-30-oct/threat_tables_b2.py` for the model. `models/wowsims-b2` for wowsims Forever (master commit 8c7b5a5f5 of 13 November 2026, with the ranged judgements of `patches/judgement-ranged.patch`), 3,000 iterations. `models/wowsims-b2/tank_gear/run_pool.sh` gives the runs with the item pool threat sets (`logs/checks_8c7b5a5f5_pool.log`), and with the argument `surv` the runs with the survival sets (`logs/checks_8c7b5a5f5_pool_surv.log`). The runs of 4, 6, 8, 9, 11 and 12 November are in `logs/checks_9a8624af9_pool.log`, `logs/checks_df57e2571_pool.log`, `logs/checks_ae9b8c23a_pool.log`, `logs/checks_9f254e8d8_pool.log`, `logs/checks_3633d376a_pool.log`, `logs/checks_52471a100_pool.log` and `logs/checks_129fcd89e_pool.log`. The earlier sets on the new commits: `logs/checks_52471a100_pool_old_sets.log`, `logs/checks_129fcd89e_pool_old_sets.log` and `logs/checks_8c7b5a5f5_pool_old_sets.log`. The withdrawn ideas C1 and C-P12 use the runs of master commit 895cd67f9 (1 November). The Warrior and Druid wowsims values are native values. The Paladin has the tank consumables of part 6 (`feedbackConsumables` in `go/feedback_prot_test.go`). `FEEDBACK_CONSUMES=default` gives the Demonic Rune only, as in the runs before 4 November evening.
- **Holy Shield blocks.** The model gives Redoubt (C-P1) too many blocks. Use the wowsims value.
- **Druid multipliers.** The Maul, Swipe and Primal Bite values come from player data. wowsims uses the same values. A test in the game must confirm them (see Open items). The same applies to the Lacerate threat of wowsims master 52471a100 at level 60.
- **Gear.** The model gives all tanks the same gear. wowsims gives each class a threat set and a survival set from the item pool of Analysis, Damage, part 7 (part 6). Parts 7 to 9 use the threat sets. `models/wowsims-b2/tank_gear` has the search and the sets.
- **Righteous Fury.** The values use the wowsims rule: the two multipliers multiply (×2.527). If they add, Holy threat is ×2.23, and the Paladin has about 10% less threat.
- **Holy Shield rank 4** is a level 60 spell since build 70755. The model uses its 221 damage.
- **Righteous Fury (C25).** The `C25` flag of `proposals_sim.go` multiplies all Paladin threat by 1.9 ÷ 1.33. `RF_ALL` sets the value. The sim tank always has Righteous Fury, thus a fixed multiplier gives the same result.
- **Burst threat (part 8).** `models/wowsims-b2/patches/burst-threat.patch` adds the threat recorder. `run.sh` gives the runs. The openers are sim rotations. A player can use a different opener.
- **Groups model.** Trash has no Sunder Armor or Faerie Fire. Demoralizing Shout, Demoralizing Roar and tab targets are not in the model.
- The earlier version of this tab (trees of 18 October) is in the history of the repository.
