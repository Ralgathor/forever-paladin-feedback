# Threat

**Question.** Does the Paladin tank hold a boss and a group as well as the Warrior and the Druid?

All values are threat each sec (TPS). The tanks are level 60 and the boss is level 63. The values come from a model and from wowsims. The proposed values include Righteous Fury +90% (C25). Part 9 compares C25 alone with the alternative C25a (+80%). Part 10 gives the inputs.

The Warrior and Druid values use the development notes of 2 November 2026. Defensive Stance gives +80% threat (was +30%) and Defiance 7/13/20% (was 5/10/15%). Bear Form and Dire Bear Form give +115% (was +50%). The game files of client 1.60.1.70755 (3 November 2026) still have the earlier values. A test on the live realms must confirm the new values.

## Short answer

- **No. After the development notes of 2 November 2026, the Paladin tank has less threat than the Warrior and the Druid.** The notes give the Warrior ×1.44 and the Druid ×1.43 more threat. This replaces Blessing of Salvation (1 ÷ 0.7 = ×1.43). The Paladin received ×1.33 from Righteous Fury in the beta of 30 October, and no more on 2 November.
- **With the same gear, the live Paladin has 70% of the Warrior threat** in the model and 69% in wowsims. Before the notes, it had 101% and 100%.
- **From fresh 60 to Naxxramas, the live Paladin has 71–82% of the Warrior threat.** With Consecration on cooldown, it has 83–98%, but the mana does not last (see Mana).
- **With the proposals, the Paladin has the Warrior threat again.** Righteous Fury (C25) gives +90% to all threat (live: +33%). In wowsims, the proposed Paladin has 105% of the Warrior threat (C25 alone: 98%). In the model, it has 114–135% from Naxxramas to fresh 60.
- **With +80% (C25a), the live Paladin has 93% in wowsims** and 96–111% in the model. With Redoubt (C-P1), it has 99% in wowsims.
- **Righteous Fury (C25) closes the gap.** Redoubt (C-P1) gives more blocks, thus more Holy Shield damage: +6% in wowsims (74% of the Warrior). C25 multiplies all Paladin threat by 1.42.
- **Two threat proposals were withdrawn on 2 November 2026.** The Holy Strike Seal trigger (C1) and Reckoning (C-P12) each added +3% in wowsims. They do not close the gap.
- **Judgement of the Crusader is important.** It gives the tank about 72 TPS. In the live version, the raid can need the tank Judgement for Light or Wisdom. The tank then has 62% of the Warrior threat. With Personal Judgement of the Crusader (C2), the tank keeps Crusader.
- **At the pull, the Paladin has the best burst threat, but only with a Fury opener** (part 8). The Paladin casts Seal of Fury and Holy Shield before the pull. Two Judgements of Fury and Holy Strike then hit at 0 sec. The live Paladin then has 110% of the Warrior threat after 3 sec and 86% after 10 sec. The proposed Paladin has 162% and 129%. With the wowsims default opener, the live Paladin has 51% after 3 sec.
- **In its best short windows, the live Paladin has about 60% of the Warrior** (part 8). The proposed Paladin has 82–91%. The Warrior has large spikes from Shield Slam, Revenge and Heroic Strike critical hits.
- **Against 3 or more enemies, the Paladin still holds the group well.** On the enemy with the least threat, the live Paladin has 2.2–2.6 times the Warrior threat. The proposed Paladin has 3.2–3.8 times. With the proposals, its total threat is 118–120% of the Warrior.
- **The Druid values are not certain.** The real Druid threat multipliers are not known yet (part 2).

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

| Warrior | TPS | Druid | TPS, player data | TPS, wowsims multipliers |
| --- | --- | --- | --- | --- |
| Heroic Strike | 281 | Maul | 388 | 222 |
| Revenge (about 10 each min) | 241 | Primal Bite | 215 | 72 |
| Shield Slam | 174 | Rage | 122 | 122 |
| Rage | 125 | Lacerate | 92 | 92 |
| Sunder Armor | 106 | Faerie Fire (not verified) | 43 | 43 |
| Rend | 16 | | | |
| **Total** | **943** | **Total** | **861** | **551** |

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
- **The proposed Paladin has 114–135%** of the Warrior threat in the model. Without C25, it has 80–94%. wowsims gives a smaller gain from Redoubt (part 6): the proposed Paladin has 105% there.
- **Consecration does not close the gap.** The live Paladin with Consecration on cooldown has 83–98% of the Warrior threat. It costs 565 mana each 8 sec. At fresh 60, the mana lasts only about 1 min with Consecration on cooldown. In Naxxramas, it lasts about 3 min (see Mana).
- **The Druid with wowsims multipliers** has 426, 500, 590, 670 and 754 TPS. The real multipliers are not known (see Open items).

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
| Primal Bite (Druid) | ×6.45 (player data). wowsims: ×2.15 | 6 sec |
| Revenge (Warrior) | ×4.9 | 5 sec. About 10 casts each min, because it needs a block, dodge or parry |
| Maul (Druid) | ×3.8 (player data). wowsims: ×2.15 | Each swing |
| Holy Strike with Iron Creed 3/3 (Paladin) | ×3.3 | 6 sec |
| Holy Shield (Paladin) | ×3.0 | Each block, and each Holy Strike that lands |
| Paladin auto attacks and Reckoning attacks | ×1.33 | — |

**Groups.** Consecration hits all enemies near the Paladin. Its full damage hits only 4 of them. Holy Shield hits only the attacker that the Paladin blocks, with 4 charges each 10 sec. Thus, the Paladin spreads threat well on 2 to 4 enemies.

## 5. Is the threat too low?

The design goal is a Paladin tank with the threat of the Warrior. The beta of 30 October reached it (101%). The development notes of 2 November give the Warrior and the Druid about ×1.44, and the Paladin no change. Thus, the live Paladin has 70% of the Warrior threat.

- **Why the gap.** Blessing of Salvation decreased the threat of the damage dealers by 30%. Blizzard removed it and gave the tanks about ×1.43 (1 ÷ 0.7). The Paladin received ×1.33 from Righteous Fury in the beta of 30 October. But the Paladin needed this ×1.33 to reach the Warrior before the notes.
- **Redoubt (C-P1) adds 6% in wowsims.** With Redoubt only, the tank has 74% of the Warrior threat.
- **The Holy Strike Seal trigger (C1) and Reckoning (C-P12) were withdrawn.** Each added only +3% in wowsims. They do not close the gap.
- **The fix: Righteous Fury (C25).** The Paladin needs about ×1.44 on all threat. C25 changes the first part of Righteous Fury from +33% to +90% to all threat: ×1.43. The model needs +62% at fresh 60 and +88% in Naxxramas. wowsims needs +92%. This is a baseline spell, thus the talent rule (a % only) is not necessary.
- **With C25, the model gives 101–117% of the Warrior threat** from Naxxramas to fresh 60. Before the notes, the live Paladin had 101–118%. With all proposals, wowsims gives 105%.
- **The gear is not the same.** wowsims gives each class its default tank set. A Warrior with better gear can make the gap larger.
- **Live tests give the real answer.** First, confirm the new Defensive Stance and Bear Form values on the live realms. Then compare the tanks with the same gear in real fights.

## 6. Check with wowsims

wowsims Forever plays the fight with the full rules of the game. Each class has its default tank gear. Full buffs, one level 63 boss from the front, 3 min fight. The Paladin has the wowsims default tank build (12/32/7) with Redoubt 5/5.

wowsims has the threat values of client 1.60.1.70755 (the same as 70707). The Warrior and Druid TPS below are the wowsims values × 1.445 (Warrior: 2.16 ÷ 1.495) and × 1.433 (Druid: 2.15 ÷ 1.5). The stance and form multipliers apply to all threat, thus this gives the same result as a new run.

| Tank | TPS (% of the Warrior) | Damage taken each sec | TMI | Crushing blows |
| --- | --- | --- | --- | --- |
| Warrior | 1,338 (100%) | 281 | 47 | 1.0% |
| Druid | 1,197 (89%) | 379 | 39.7 | 15.0% |
| Paladin, live | 928 (69%) | 333 | 57.1 | 11.9% |
| Paladin, C1 (withdrawn) | 954 (71%) | 332 | 57.1 | 11.9% |
| Paladin, Redoubt (C-P1) | 986 (74%) | 288 | 44.0 | 1.0% |
| Paladin, Righteous Fury (C25) | 1,316 (98%) | 333 | 57.1 | 11.9% |
| **Paladin, all kept proposals (C-P1, C-P13, C25)** | **1,401 (105%)** | **295** | **45.0** | **1.0%** |

- **The live Paladin has about 70% of the Warrior threat.** The model (70%) and wowsims (69%) agree. Before the notes of 2 November, they gave 101% and 100%.
- **Redoubt adds less in wowsims:** +58 TPS (+6%) against +96 TPS (+15%) in the model. The model gives too many Holy Shield blocks.
- **Righteous Fury (C25) multiplies all Paladin threat by 1.42.** With all kept proposals, the Paladin has 105% of the Warrior threat. The model gives 115% (part 1).
- **C1 (withdrawn) agrees:** +26 in wowsims, +25 in the model.
- **Reckoning (C-P12), withdrawn.** With C1, it gave +27 more in wowsims (1,038 TPS, 78%) and +20 in the model.
- **Toughness removal (C-P13)** does not change threat. Damage taken increases by 2%.
- **The Druid row checks the order, not the level,** because each class has different gear.

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

**wowsims result.** Each enemy is level 63 and hits for 1/3 of a boss hit. The Paladin uses its default rotation with Consecration. The values are TPS on each target, with the main target first. The Warrior and Druid values have the multipliers of the notes of 2 November (part 6).

| Tank | 1 target | 3 targets | 5 targets |
| --- | --- | --- | --- |
| Paladin, live | 927 | 914 / 249 / 249 | 915 / 223 / 223 / 223 / 127 |
| Paladin, proposed | 1,400 | 1,304 / 356 / 357 | 1,297 / 316 / 318 / 317 / 180 |
| Warrior | 1,247 | 1,241 / 328 / 113 | 1,310 / 497 / 105 / 105 / 48 |
| Druid | 1,041 | 1,039 / 264 / 258 | 1,099 / 268 / 258 / 62 / 62 |

- **On the lowest target, the Paladin still leads the Warrior.** On 3 targets, the live Paladin has 2.2 times the Warrior threat and the same threat as the Druid. On 5 targets, it has 2.6 times the Warrior threat and 2 times the Druid threat.
- **The proposed Paladin leads by more.** On the lowest target, it has 3.2 times the Warrior threat on 3 targets and 3.8 times on 5 targets.
- **In total, the live Paladin is below.** On 3 targets: live Paladin 1,412, Warrior 1,682, Druid 1,561. On 5 targets: live Paladin 1,711, Warrior 2,065, Druid 1,749.
- **The proposed Paladin is first in total.** On 3 targets: 2,017 (120% of the Warrior). On 5 targets: 2,428 (118%).
- **Redoubt changes almost nothing on groups:** +1%. On extra targets, all Holy Shield charges are already used in the live version. The gain comes from Righteous Fury (C25).
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

**Conclusion.** Against 3 or more enemies, the Paladin holds the extra enemies better than the Warrior, and as well as the Druid on 3 enemies. The live total threat is lower. The problem is the main target (parts 1 and 6). With Righteous Fury (C25), the Paladin is first on the main target and in total.

## 8. Burst threat

This part compares the threat in the first seconds of a pull and in the best short windows of a fight. A damage dealer pulls the boss when it has more threat than the tank. At the start of a pull, and after a large threat spike, this can occur before the sustained values of part 6 apply.

**Setup.** wowsims, as in part 6: default tank gear, full buffs, one level 63 boss from the front, 3 min fight, 3,000 iterations. A recorder adds the threat on the boss in steps of 0.1 sec. The Warrior and Druid values have the multipliers of the notes of 2 November.

- **Warrior.** Default rotation, 0 rage at the pull. Bloodrage and a rage potion at −1.5 sec. No Goblin Sapper Charge, because the Paladin and Druid rotations do not use it.
- **Druid.** Default rotation, 25 rage at the pull.
- **Boss armor.** The boss has no armor debuff at the pull. Only a Warrior (Sunder Armor) or a Rogue (Expose Armor) can apply it. wowsims adds 1 Sunder Armor stack each 1.5 sec, thus 5 stacks at 6 sec.

**The Paladin openers**

| Opener | Before the pull | First casts |
| --- | --- | --- |
| wowsims default | Seal of the Crusader at −1.5 sec | 0 sec: Judgement of the Crusader, then Seal of Fury. 1.5 sec: Swift Judgement (Judgement of Fury), Consecration. 3 sec: Holy Shield. 4.5 sec: Holy Strike |
| Fury opener | Seal of Fury at −3 sec, Holy Shield at −1.5 sec | 0 sec: Judgement of Fury, Swift Judgement, Holy Strike (with the Shieldsworn Holy Shield hit). 1.5 sec: Consecration. Then the default order |

Judgement and Swift Judgement are not on the global cooldown, thus both hit at 0 sec. The Fury opener does not use Judgement of the Crusader. The raid debuffs of the sim already have it, thus the 3 min threat decreases by only 1%.

**Threat in the first seconds** (threat on the boss, % of the Warrior)

| Tank | First 1.5 sec | First 3 sec | First 6 sec | First 10 sec | First 20 sec | 3 min (TPS) |
| --- | --- | --- | --- | --- | --- | --- |
| Warrior | 2,008 (100%) | 4,718 (100%) | 7,123 (100%) | 13,151 (100%) | 26,848 (100%) | 1,332 (100%) |
| Druid | 2,413 (120%) | 4,336 (92%) | 6,752 (95%) | 10,911 (83%) | 24,031 (90%) | 1,192 (90%) |
| Paladin, live, wowsims opener | 577 (29%) | 2,418 (51%) | 5,335 (75%) | 8,778 (67%) | 18,344 (68%) | 925 (69%) |
| Paladin, live, Fury opener | 4,251 (212%) | 5,211 (110%) | 6,670 (94%) | 11,364 (86%) | 20,424 (76%) | 916 (69%) |
| Paladin, proposed, wowsims opener | 816 (41%) | 3,426 (73%) | 7,814 (110%) | 13,015 (99%) | 27,394 (102%) | 1,401 (105%) |
| Paladin, proposed, Fury opener | 4,656 (232%) | 7,646 (162%) | 9,944 (140%) | 16,927 (129%) | 30,433 (113%) | 1,388 (104%) |

- **With the wowsims default opener, the Paladin starts slowly.** The first global cooldown goes to Judgement of the Crusader. Holy Shield starts at 3 sec, and Holy Strike at 4.5 sec.
- **With the Fury opener, the Paladin has the best start of the three tanks.** About 3,500 threat hits the boss at 0 sec. Two Judgements of Fury give about 1,770, Holy Strike about 1,100 and the Shieldsworn Holy Shield hit about 600.
- **The live lead does not last.** After 10 sec, the live Fury opener has 86% of the Warrior. After 30 sec, it has 69%, the sustained gap of part 6.
- **The proposed Paladin keeps the lead.** With the Fury opener, it has 129% of the Warrior after 10 sec and 113% after 20 sec. In the first 3 sec, all of the gain comes from Righteous Fury (C25). Redoubt starts after the first blocks.
- **The Warrior and the Druid need rage first.** The Warrior starts with 0 rage. Its threat increases fast from 2 sec, when the boss hits give rage. The Druid uses its 25 rage at once, and then it waits for rage.
- **Boss armor helps the Paladin.** In the first 6 sec, the boss has less than 5 Sunder Armor stacks. This decreases Warrior and Druid physical damage. Most Paladin threat is Holy damage, thus boss armor does not decrease it.
- **With one Judgement at 0 sec,** Swift Judgement hits at 1.5 sec. Only the first 1.5 sec change: 3,204 threat (160%) in place of 4,251. From 3 sec, the two openers have the same threat.

**Bad pulls** (threat on the 10% worst fights, % of the Warrior on its 10% worst fights)

| Tank | First 3 sec | First 6 sec | First 10 sec |
| --- | --- | --- | --- |
| Warrior | 1,396 (100%) | 3,576 (100%) | 8,131 (100%) |
| Druid | 2,100 (150%) | 3,872 (108%) | 7,028 (86%) |
| Paladin, live, wowsims opener | 1,667 (119%) | 3,739 (105%) | 6,775 (83%) |
| Paladin, live, Fury opener | 3,657 (262%) | 4,939 (138%) | 9,032 (111%) |
| Paladin, proposed, Fury opener | 5,354 (384%) | 7,438 (208%) | 13,606 (167%) |

- **The Warrior has the worst bad pulls.** When its first attacks miss or the boss attacks miss it, it has no rage. Its threat after 3 sec decreases to 30% of its mean.
- **A bad pull costs the Paladin less.** Judgement of Fury cannot be dodged or parried. Holy Shield and Seal of Fury cannot miss.

**Best short windows** (the highest threat in a window at any time in the 3 min fight, % of the Warrior)

| Tank | Best 3 sec | Best 6 sec | Best 10 sec | Best 3 sec ÷ mean 3 sec |
| --- | --- | --- | --- | --- |
| Warrior | 12,736 (100%) | 16,449 (100%) | 24,054 (100%) | ×3.1 |
| Druid | 10,143 (80%) | 14,948 (91%) | 20,855 (87%) | ×2.9 |
| Paladin, live, wowsims opener | 7,238 (57%) | 9,800 (60%) | 14,751 (61%) | ×2.6 |
| Paladin, live, Fury opener | 7,152 (56%) | 9,619 (58%) | 14,530 (60%) | ×2.6 |
| Paladin, proposed, wowsims opener | 10,650 (84%) | 14,532 (88%) | 21,870 (91%) | ×2.5 |
| Paladin, proposed, Fury opener | 10,386 (82%) | 14,227 (86%) | 21,478 (89%) | ×2.5 |

- **The Paladin has no threat cooldown.** Its best windows come from Holy Strike, Judgement and Holy Shield in the same 3 sec, with critical hits. The Warrior adds Shield Slam, Revenge and Heroic Strike critical hits to the rage from boss hits.
- **The best-window gap is larger than the sustained gap.** Live: about 60% against 69%. Proposed: 82–91% against 105%. Thus the Paladin has a smaller margin against a large threat spike from a damage dealer.

**Warrior variants**

| Warrior | First 1.5 sec | First 3 sec | First 6 sec | First 10 sec |
| --- | --- | --- | --- | --- |
| Default (above) | 2,008 | 4,718 | 7,123 | 13,151 |
| Charge at −0.5 sec, 20 yards (Vanguard) | 1,739 (−13%) | 4,304 (−9%) | 7,382 (+4%) | 13,663 (+4%) |
| Goblin Sapper Charge | 2,933 (+46%) | 5,489 (+16%) | 8,390 (+18%) | 14,520 (+10%) |

- **Charge does not increase the Warrior burst.** Charge gives 15 rage, but this rage gives no threat. The Charge stun also delays the first boss swings, thus the Warrior receives less rage from boss hits.
- **Against the Warrior with Charge,** the proposed Paladin with the Fury opener has 178%, 135% and 124% after 3, 6 and 10 sec.
- **Charge in combat.** With Vanguard, the Warrior can charge in Defensive Stance. The Vanguard Charge row in the game files still has the "not in combat" attribute. Thus the Warrior can charge only at the pull. A test in the game must confirm this.

**Tank swaps.** Shoulder the Burden (C-P5) moves 50% of the threat of an ally to the Paladin. After 30 sec, the Warrior has about 40,000 threat. Shoulder the Burden on the Warrior then gives the Paladin about 20,000 threat at once. This is 2.7 times the best 3 sec Paladin window. It does not help at the pull, because no ally has threat yet.

**Conclusion.** The Paladin can hold the boss at the pull better than the Warrior and the Druid, but only with a Fury opener. The default opener of wowsims gives it half of the Warrior threat in the first 3 sec. After 10 sec, the sustained gap of part 6 returns. In short windows later in the fight, the live Paladin has about 60% of the Warrior. The proposed Paladin keeps the lead after 10 sec, and has 82–91% in short windows.

## 9. Righteous Fury alone: +90% (C25) and +80% (C25a)

This part gives parts 1 to 8 again with Righteous Fury (C25) alone, and with the live trees: all threat +90% in place of +33%. The alternative C25a gives +80%, the value of Defensive Stance.

- **Righteous Fury multiplies all Paladin threat.** Thus, C25 multiplies each Paladin value of the model by 1.43 (1.9 ÷ 1.33), and C25a by 1.35 (1.8 ÷ 1.33).
- **The wowsims values come from new runs.** C25 multiplies the wowsims threat by 1.42, and C25a by 1.35.
- **The Warrior and Druid values do not change.** They use the notes of 2 November, as in parts 1 to 8.

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

**wowsims, one boss (part 6).** New runs, 3 min, 3,000 iterations. Damage taken and TMI do not change with Righteous Fury.

| Paladin | Live (+33%) | C25 (+90%) | C25a (+80%) |
| --- | --- | --- | --- |
| Live | 928 (69%, 78%) | 1,316 (98%, 110%) | 1,247 (93%, 104%) |
| Redoubt (C-P1) | 986 (74%, 82%) | 1,401 (105%, 117%) | 1,328 (99%, 111%) |
| All kept proposals (with C-P13) | 986 (74%, 82%) | 1,401 (105%, 117%) | 1,328 (99%, 111%) |

The Warrior has 1,338 and the Druid 1,197.

- **C25: the live Paladin has 98% of the Warrior threat** in wowsims, and 105% with Redoubt (C-P1). The model and wowsims agree: 100% and 98%.
- **C25a: the live Paladin has 93%,** and 99% with Redoubt (C-P1).
- **Toughness removal (C-P13)** still does not change threat.

**wowsims, groups (part 7).** TPS on each target, main target first, and the total.

| Tank | 1 target | 3 targets | 5 targets |
| --- | --- | --- | --- |
| Paladin, live, C25 (+90%) | 1,315 | 1,301 / 352 / 353 (total 2,006) | 1,302 / 315 / 316 / 315 / 179 (total 2,427) |
| Paladin, Redoubt (C-P1), C25 (+90%) | 1,400 | 1,304 / 356 / 357 (total 2,017) | 1,297 / 316 / 318 / 317 / 180 (total 2,428) |
| Paladin, live, C25a (+80%) | 1,246 | 1,233 / 334 / 334 (total 1,901) | 1,234 / 299 / 299 / 299 / 169 (total 2,300) |
| Paladin, Redoubt (C-P1), C25a (+80%) | 1,327 | 1,235 / 338 / 338 (total 1,911) | 1,229 / 300 / 301 / 300 / 170 (total 2,301) |
| Warrior | 1,247 | 1,241 / 328 / 113 (total 1,682) | 1,310 / 497 / 105 / 105 / 48 (total 2,065) |
| Druid | 1,041 | 1,039 / 264 / 258 (total 1,561) | 1,099 / 268 / 258 / 62 / 62 (total 1,749) |

- **On the main target, the Paladin now holds the boss as well as the Warrior.** With C25, it has 105% of the Warrior on 1 target. With C25a, it has 100%.
- **In total, the Paladin is first again.** With C25: 119% of the Warrior on 3 targets and 118% on 5 targets. With C25a: 113% and 111%.
- **On the lowest target, the lead becomes larger.** With C25, the Paladin has 3.1 times the Warrior threat on 3 targets and 3.7 times on 5 targets.
- **The model gives a larger lead** (part 7). With C25, the proposed Paladin has 172–213% of the stronger tank on 3 targets, and 165–195% on 5 targets.

**Burst threat (part 8).** Threat on the boss after the first seconds, % of the Warrior.

| Tank | First 1.5 sec | First 3 sec | First 6 sec | First 10 sec | First 20 sec | First 30 sec |
| --- | --- | --- | --- | --- | --- | --- |
| Warrior | 2,008 | 4,718 | 7,123 | 13,151 | 26,848 | 41,452 |
| Druid | 2,413 (120%) | 4,336 (92%) | 6,752 (95%) | 10,911 (83%) | 24,031 (90%) | 37,549 (91%) |
| Paladin, live, wowsims opener, C25 (+90%) | 816 (41%) | 3,426 (73%) | 7,578 (106%) | 12,464 (95%) | 26,067 (97%) | 37,729 (91%) |
| Paladin, Redoubt (C-P1), wowsims opener, C25 (+90%) | 816 (41%) | 3,426 (73%) | 7,814 (110%) | 13,015 (99%) | 27,394 (102%) | 39,919 (96%) |
| Paladin, live, Fury opener, C25 (+90%) | 4,555 (227%) | 7,407 (157%) | 9,478 (133%) | 16,128 (123%) | 28,984 (108%) | 39,842 (96%) |
| Paladin, Redoubt (C-P1), Fury opener, C25 (+90%) | 4,656 (232%) | 7,646 (162%) | 9,944 (140%) | 16,927 (129%) | 30,433 (113%) | 42,118 (102%) |
| Paladin, live, wowsims opener, C25a (+80%) | 774 (39%) | 3,250 (69%) | 7,184 (101%) | 11,817 (90%) | 24,712 (92%) | 35,768 (86%) |
| Paladin, Redoubt (C-P1), wowsims opener, C25a (+80%) | 774 (39%) | 3,250 (69%) | 7,408 (104%) | 12,339 (94%) | 25,970 (97%) | 37,842 (91%) |
| Paladin, live, Fury opener, C25a (+80%) | 4,318 (215%) | 7,023 (149%) | 8,986 (126%) | 15,289 (116%) | 27,475 (102%) | 37,768 (91%) |
| Paladin, Redoubt (C-P1), Fury opener, C25a (+80%) | 4,414 (220%) | 7,249 (154%) | 9,428 (132%) | 16,046 (122%) | 28,847 (107%) | 39,924 (96%) |

- **With the Fury opener, the Paladin has the best start by a large margin.** With C25, it has 157% of the Warrior after 3 sec and 123% after 10 sec. With C25a, it has 149% and 116%.
- **The lead lasts longer.** After 30 sec, the live Paladin with C25 has 96% of the Warrior, and C25a 91%. With Redoubt (C-P1), C25 gives 102%.
- **With the wowsims default opener, the start is still slow:** 73% after 3 sec with C25, 69% with C25a. After 6 sec, the Paladin has 101–110%.

**Bad pulls (part 8).** Threat on the 10% worst fights, % of the Warrior on its 10% worst fights.

| Tank | First 3 sec | First 6 sec | First 10 sec |
| --- | --- | --- | --- |
| Warrior | 1,396 | 3,576 | 8,131 |
| Paladin, live, Fury opener, C25 (+90%) | 5,120 (367%) | 7,039 (197%) | 12,712 (156%) |
| Paladin, Redoubt (C-P1), Fury opener, C25 (+90%) | 5,354 (384%) | 7,438 (208%) | 13,606 (167%) |
| Paladin, live, Fury opener, C25a (+80%) | 4,856 (348%) | 6,672 (187%) | 12,049 (148%) |
| Paladin, Redoubt (C-P1), Fury opener, C25a (+80%) | 5,077 (364%) | 7,052 (197%) | 12,902 (159%) |

- **A bad pull costs the Paladin less than the Warrior,** as in part 8. With C25, the Paladin has 3.7 times the Warrior threat after 3 sec.

**Best short windows (part 8).** The highest threat in any window of the 3 min fight, % of the Warrior.

| Tank | Best 3 sec | Best 6 sec | Best 10 sec |
| --- | --- | --- | --- |
| Warrior | 12,736 | 16,449 | 24,054 |
| Druid | 10,143 (80%) | 14,948 (91%) | 20,855 (87%) |
| Paladin, live, Fury opener, C25 (+90%) | 10,084 (79%) | 13,736 (84%) | 20,663 (86%) |
| Paladin, Redoubt (C-P1), Fury opener, C25 (+90%) | 10,386 (82%) | 14,227 (86%) | 21,478 (89%) |
| Paladin, live, Fury opener, C25a (+80%) | 9,558 (75%) | 13,020 (79%) | 19,586 (81%) |
| Paladin, Redoubt (C-P1), Fury opener, C25a (+80%) | 9,844 (77%) | 13,485 (82%) | 20,357 (85%) |

- **The best windows become near the Druid.** With C25, the live Paladin has 79–86% of the Warrior. The Druid has 80–91%. With C25a, the Paladin has 75–81%.
- **The Paladin still has no threat cooldown.** The Warrior keeps the largest spikes.

**Conclusion.** C25 (+90%) gives the Paladin the Warrior threat again in the model and in wowsims, with the live trees. It gives the positions of the beta of 30 October again. C25a (+80%) gives 93–96% of the Warrior on one boss in the late raids. With Redoubt (C-P1), C25a gives 99%. Thus, the recommendation stays C25. Use C25a if Blizzard adopts Redoubt (C-P1).

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
- Threat: Bear Form ×2.15 (notes of 2 November 2026; client 1.60.1.70755: ×1.5), Maul ×1.75, Primal Bite ×3, Swipe ×1.75 (player data). wowsims uses Bear Form only. The ability multipliers are not verified.
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

- **Scripts.** `models/beta-30-oct/threat_tables_b2.py` for the model. `models/wowsims-b2` for wowsims Forever (master commit 895cd67f9, game files of hotfix push 113554), 3,000 iterations. The Warrior and Druid wowsims values are scaled to the multipliers of the notes of 2 November (part 6).
- **Holy Shield blocks.** The model gives Redoubt (C-P1) too many blocks. Use the wowsims value.
- **Druid multipliers.** The real values are not known (see Open items).
- **Gear.** The model gives all tanks the same gear. wowsims gives each class its default set.
- **Righteous Fury.** The values use the wowsims rule: the two multipliers multiply (×2.527). If they add, Holy threat is ×2.23, and the Paladin has about 10% less threat.
- **Holy Shield rank 4** is a level 60 spell since build 70755. The model uses its 221 damage.
- **Righteous Fury (C25).** The `C25` flag of `proposals_sim.go` multiplies all Paladin threat by 1.9 ÷ 1.33. `RF_ALL` sets the value. The sim tank always has Righteous Fury, thus a fixed multiplier gives the same result.
- **Burst threat (part 8).** `models/wowsims-b2/burst-threat.patch` adds the threat recorder. `run.sh` gives the runs. The openers are sim rotations. A player can use a different opener.
- **Groups model.** Trash has no Sunder Armor or Faerie Fire. Demoralizing Shout, Demoralizing Roar and tab targets are not in the model.
- The earlier version of this tab (trees of 18 October) is in the history of the repository.
