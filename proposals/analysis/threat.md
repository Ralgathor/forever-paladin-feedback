# Threat

**Question.** Does the Paladin tank hold a boss and a group as well as the Warrior and the Druid?

All values are threat each sec (TPS). The tanks are level 60 and the boss is level 63. The values come from a model and from wowsims. Part 8 gives the inputs.

The Warrior and Druid values use the development notes of 2 November 2026. Defensive Stance gives +80% threat (was +30%) and Defiance 7/13/20% (was 5/10/15%). Bear Form and Dire Bear Form give +115% (was +50%). The game files of client 1.60.1.70707 still have the earlier values. A test on the live realms must confirm the new values.

## Short answer

- **No. After the development notes of 2 November 2026, the Paladin tank has less threat than the Warrior and the Druid.** The notes give the Warrior ×1.44 and the Druid ×1.43 more threat. This replaces Blessing of Salvation (1 ÷ 0.7 = ×1.43). The Paladin received ×1.33 from Righteous Fury in the beta of 30 October, and no more on 2 November.
- **With the same gear, the live Paladin has 70% of the Warrior threat** in the model and 69% in wowsims. Before the notes, it had 101% and 100%.
- **From fresh 60 to Naxxramas, the live Paladin has 71–82% of the Warrior threat.** With Consecration on cooldown, it has 83–98%, but the mana does not last (see Mana).
- **A Righteous Fury bonus of about +90% to all threat gives the Warrior threat again** (live: +33%). The model gives +62% at fresh 60 and +88% in Naxxramas. wowsims gives +92%. This is not a proposal yet.
- **The proposals add threat, but they are not for threat.** Redoubt (C-P1) gives more blocks, thus more Holy Shield damage. Together with Toughness removal (C-P13), they give +6% in wowsims: 74% of the Warrior.
- **Two threat proposals were withdrawn on 2 November 2026.** The Holy Strike Seal trigger (C1) and Reckoning (C-P12) each added +3% in wowsims. They do not close the gap.
- **Judgement of the Crusader is important.** It gives the tank about 72 TPS. In the live version, the raid can need the tank Judgement for Light or Wisdom. The tank then has 62% of the Warrior threat. With Personal Judgement of the Crusader (C2), the tank keeps Crusader.
- **Against 3 or more enemies, the Paladin still holds the group well.** On the enemy with the least threat, it has 2.2–2.6 times the Warrior threat. It has the Druid threat on 3 enemies and 2 times the Druid threat on 5 enemies.
- **The Druid values are not certain.** The real Druid threat multipliers are not known yet (part 2).

## 1. One boss, same gear

All tanks have pre-raid gear: 200 spell power, 500 Attack Power and a 45 DPS weapon (2.7 sec). The boss has 5 Sunder Armor and Faerie Fire. The proposed Paladin has C2 and C-P1.

| Boss hit before armor | Warrior | Druid | Paladin, live | Paladin, live, no Crusader | Paladin, proposed | Paladin, proposed, with Consecration |
| --- | --- | --- | --- | --- | --- | --- |
| 3,000 | 832 | 790 | 661 | 589 | 757 | 880 |
| 4,500 | 943 | 861 | 661 | 589 | 757 | 880 |
| 6,000 | 976 | 897 | 661 | 589 | 757 | 880 |

- **Warrior and Druid threat increases with the boss damage.** They receive rage when the boss hits them. Paladin threat does not change.
- **At 4,500,** the live Paladin has 70% of the Warrior threat. The proposed Paladin has 80%.
- **"No Crusader"** is the live tank when the raid takes its Judgement for Light or Wisdom.
- **Boss armor does not change Paladin threat much.** With no armor debuffs, the Warrior has 763 TPS, the Druid 665, the live Paladin 637 and the proposed Paladin 731. Most Paladin threat is Holy damage, and armor does not decrease Holy damage.

**Where the Paladin threat comes from (200 spell power)**

| Source | Live | Proposed | Cause of the change |
| --- | --- | --- | --- |
| Holy Shield (blocks and Shieldsworn) | 287 | 374 | Redoubt (C-P1): more blocks |
| Judgement of Fury | 118 | 118 | — |
| Seal of Fury | 70 | 74 | More Reckoning attacks |
| Holy Strike with Iron Creed 3/3 | 104 | 104 | — |
| Auto attacks | 64 | 64 | — |
| Reckoning extra attacks | 17 | 22 | Redoubt (C-P1): more blocks |
| **Total** | **661** | **757** | |

In the model, Redoubt (C-P1) gives +96 TPS. The withdrawn ideas gave more: the Holy Strike Seal trigger (C1) +25 and the Reckoning change (C-P12) +20. Personal Judgement of the Crusader (C2) gives +72 when the raid needs the tank Judgement.

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

**Spell power.** Each +100 spell power gives about +45 TPS to the live Paladin and +48 TPS to the proposed Paladin.

| Spell power | 100 | 150 | 200 | 250 | 300 | 350 |
| --- | --- | --- | --- | --- | --- | --- |
| Paladin, live | 616 | 639 | 661 | 684 | 706 | 729 |
| Paladin, proposed | 709 | 733 | 757 | 781 | 805 | 829 |

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
| Fresh 60 | 775 | 681 | 636 (82%, 93%) | 560 (72%, 82%) | **730 (94%, 107%)** | 854 (110%, 125%) |
| Pre-raid best | 874 | 806 | 686 (78%, 85%) | 613 (70%, 76%) | **783 (90%, 97%)** | 912 (104%, 113%) |
| Molten Core | 996 | 934 | 733 (74%, 78%) | 661 (66%, 71%) | **834 (84%, 89%)** | 967 (97%, 104%) |
| Blackwing Lair | 1,085 | 1,051 | 789 (73%, 75%) | 717 (66%, 68%) | **892 (82%, 85%)** | 1,033 (95%, 98%) |
| Naxxramas | 1,185 | 1,167 | 837 (71%, 72%) | 764 (65%, 66%) | **943 (80%, 81%)** | 1,089 (92%, 93%) |

- **The live Paladin is below the Warrior at all gear levels,** and the gap increases: 82% at fresh 60, 71% in Naxxramas. The Warrior and the Druid receive more Attack Power and rage from gear. The Paladin receives only spell power.
- **Without Crusader,** the live Paladin has 65–72% of the Warrior threat.
- **The proposed Paladin has 80–94%** of the Warrior threat in the model. wowsims gives a smaller gain from the proposals (part 6).
- **Consecration does not close the gap.** The live Paladin with Consecration on cooldown has 83–98% of the Warrior threat. It costs 565 mana each 8 sec. At fresh 60, the mana lasts only about 1 min with Consecration on cooldown. In Naxxramas, it lasts about 3 min (see Mana).
- **The Druid with wowsims multipliers** has 426, 500, 590, 670 and 754 TPS. The real multipliers are not known (see Open items).

## 3. If the gear increases more slowly

Blizzard said that it wants flatter gear progression. This is an intention, not a promise. In this part, the gear from Molten Core increases at half the rate of part 2. There are two cases for boss damage: as in part 2, or at half the rate (4,000, 4,750 and 5,750 before armor).

Each cell gives the Paladin TPS as a percentage of the Warrior TPS, then of the Druid TPS in brackets.

| Gear level | Gear as in part 2 | Flatter gear, boss hits as in part 2 | Flatter gear, flatter boss hits |
| --- | --- | --- | --- |
| Live, Naxxramas | 71% (72%) | 69% (72%) | 72% (76%) |
| Proposed, fresh 60 | 94% (107%) | 94% (107%) | 94% (107%) |
| Proposed, pre-raid best | 90% (97%) | 90% (97%) | 90% (97%) |
| Proposed, Molten Core | 84% (89%) | 83% (90%) | 86% (93%) |
| Proposed, Blackwing Lair | 82% (85%) | 81% (86%) | 83% (89%) |
| Proposed, Naxxramas | 80% (81%) | 78% (82%) | 82% (86%) |

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
- **The proposals add 6% in wowsims,** all from Redoubt (C-P1). The proposed tank has 74% of the Warrior threat.
- **The Holy Strike Seal trigger (C1) and Reckoning (C-P12) were withdrawn.** Each added only +3% in wowsims. They do not close the gap.
- **One fix: a larger Righteous Fury bonus.** The Paladin needs about ×1.44 on all threat. Righteous Fury +33% → about +90% to all threat gives this. The model gives +62% at fresh 60 and +88% in Naxxramas. wowsims gives +92%. This is a baseline spell, thus the talent rule (a % only) is not necessary. It is not a proposal yet.
- **The gear is not the same.** wowsims gives each class its default tank set. A Warrior with better gear can make the gap larger.
- **Live tests give the real answer.** First, confirm the new Defensive Stance and Bear Form values on the live realms. Then compare the tanks with the same gear in real fights.

## 6. Check with wowsims

wowsims Forever plays the fight with the full rules of the game. Each class has its default tank gear. Full buffs, one level 63 boss from the front, 3 min fight. The Paladin has the wowsims default tank build (12/32/7) with Redoubt 5/5.

wowsims has the threat values of client 1.60.1.70707. The Warrior and Druid TPS below are the wowsims values × 1.445 (Warrior: 2.16 ÷ 1.495) and × 1.433 (Druid: 2.15 ÷ 1.5). The stance and form multipliers apply to all threat, thus this gives the same result as a new run.

| Tank | TPS (% of the Warrior) | Damage taken each sec | TMI | Crushing blows |
| --- | --- | --- | --- | --- |
| Warrior | 1,338 (100%) | 281 | 47 | 1.0% |
| Druid | 1,197 (89%) | 379 | 39.7 | 15.0% |
| Paladin, live | 928 (69%) | 333 | 57.1 | 11.9% |
| Paladin, C1 (withdrawn) | 954 (71%) | 332 | 57.1 | 11.9% |
| Paladin, Redoubt (C-P1) | 986 (74%) | 288 | 44.0 | 1.0% |
| **Paladin, all kept proposals (with Toughness removal, C-P13)** | **986 (74%)** | **295** | **45.2** | **1.0%** |

- **The live Paladin has about 70% of the Warrior threat.** The model (70%) and wowsims (69%) agree. Before the notes of 2 November, they gave 101% and 100%.
- **The proposals add less in wowsims:** +58 TPS (+6%) against +96 TPS (+15%) in the model. Both values come from Redoubt. The model gives too many Holy Shield blocks.
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
| Paladin, proposed | 986 | 917 / 253 / 252 | 912 / 224 / 224 / 224 / 128 |
| Warrior | 1,247 | 1,241 / 328 / 113 | 1,310 / 497 / 105 / 105 / 48 |
| Druid | 1,041 | 1,039 / 264 / 258 | 1,099 / 268 / 258 / 62 / 62 |

- **On the lowest target, the Paladin still leads the Warrior.** On 3 targets, it has 2.2 times the Warrior threat and the same threat as the Druid. On 5 targets, it has 2.6 times the Warrior threat and 2 times the Druid threat.
- **In total, the Paladin is now below.** On 3 targets: proposed Paladin 1,422, Warrior 1,682, Druid 1,561. On 5 targets: proposed Paladin 1,712, Warrior 2,065, Druid 1,749.
- **The proposals change almost nothing on groups:** +1%. On extra targets, all Holy Shield charges are already used in the live version.
- **The fifth enemy has less Paladin threat** because Consecration gives its full damage to 4 enemies only.
- **The Warrior** holds only 2 targets well: Cleave hits 2 targets. **The Druid** holds only 3: Swipe hits 3 targets.

**Model result.** The model gives a larger Paladin lead: 115–149% of the stronger of the two other tanks on all targets. The model lead is too large. In the model, trash hits for only 1/3 of a boss hit, thus the Warrior and the Druid receive little rage.

| Gear level | 3 targets: Warrior | Druid | Paladin, live | Paladin, proposed | 5 targets: Warrior | Druid | Paladin, live | Paladin, proposed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fresh 60 | 705 | 716 | 1,064 | 1,070 | 883 | 813 | 1,198 | 1,204 |
| Pre-raid best | 799 | 820 | 1,123 | 1,132 | 956 | 908 | 1,262 | 1,270 |
| Molten Core | 906 | 917 | 1,183 | 1,192 | 1,046 | 1,004 | 1,326 | 1,335 |
| Blackwing Lair | 996 | 1,009 | 1,256 | 1,266 | 1,160 | 1,120 | 1,407 | 1,417 |
| Naxxramas | 1,095 | 1,107 | 1,320 | 1,331 | 1,290 | 1,250 | 1,476 | 1,487 |

Values are TPS on all targets. Without Consecration, the proposed Paladin has 83–102% of the stronger tank on 3 targets, and 71–82% on 5 targets.

**Conclusion.** Against 3 or more enemies, the Paladin holds the extra enemies better than the Warrior, and as well as the Druid on 3 enemies. The total threat is lower. The problem is the main target (parts 1 and 6).

## 8. Inputs of the model

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
- Defensive Stance ×1.8 threat and −10% damage. Defiance ×1.2 threat with a shield. Bastion +10% damage with a shield. (Notes of 2 November 2026. Client 1.60.1.70707: ×1.3 and ×1.15.)
- Revenge rank 6: 138–168 + 28% of Attack Power, +60%. Threat = damage × 2.25.
- Shield Slam rank 4: 640–670 + block value. Threat = damage (the real multiplier is not known).
- Heroic Strike rank 9: +157 damage. Threat = damage + 152.4 (wowsims).
- Sunder Armor: 206 threat + 5% of Attack Power. Rend rank 7: 7 ticks of 21 + 2% of Attack Power.
- 5 rage for each block, dodge and parry. Bloodrage: 20 rage each min.
- Shield Block on cooldown: it covers about 80% of the swings. 3% of the swings are crushing blows.
- Order: Shield Slam and Shield Block on cooldown, Revenge after each block, dodge or parry, Rend on the boss, Sunder Armor in the free global cooldowns. Heroic Strike uses the extra rage.

**Druid**

- Talents: Ferocity 5/5, Savage Fury 2/2, Feral Instinct 3/3, Sharpened Claws 2/2, Predatory Strikes 3/3, Blood Frenzy 2/2, Natural Reaction 5/5.
- Threat: Bear Form ×2.15 (notes of 2 November 2026; client 1.60.1.70707: ×1.5), Maul ×1.75, Primal Bite ×3, Swipe ×1.75 (player data). wowsims uses Bear Form only. The ability multipliers are not verified.
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

## 9. Method and limits

- **Scripts.** `models/beta-30-oct/threat_tables_b2.py` for the model. `models/wowsims-b2` for wowsims Forever (master commit 895cd67f9, game files of hotfix push 113554), 3,000 iterations. The Warrior and Druid wowsims values are scaled to the multipliers of the notes of 2 November (part 6).
- **Holy Shield blocks.** The model gives Redoubt (C-P1) too many blocks. Use the wowsims value.
- **Druid multipliers.** The real values are not known (see Open items).
- **Gear.** The model gives all tanks the same gear. wowsims gives each class its default set.
- **Righteous Fury.** The values use the wowsims rule: the two multipliers multiply (×2.527). If they add, Holy threat is ×2.23, and the Paladin has about 10% less threat.
- **Holy Shield rank 4** has no cost or level yet in the game files. The model uses its 221 damage.
- **Groups model.** Trash has no Sunder Armor or Faerie Fire. Demoralizing Shout, Demoralizing Roar and tab targets are not in the model.
- The earlier version of this tab (trees of 18 October) is in the history of the repository.
