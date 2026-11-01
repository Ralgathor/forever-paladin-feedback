# Threat

This section compares the threat of the three tanks: Warrior, Druid and Paladin. It uses the beta trees of 30 October 2026. The unit is threat per second (TPS) on one boss. Part 8 compares the tanks against groups of enemies. The tanks are level 60. The boss is level 63.

The values come from a model and from wowsims Forever. The model is not a combat log. The inputs are in part 6. The spell data from beta tests is in Beta test results. The values that are not known are in Open items.

The script models/beta-30-oct/threat_tables_b2.py calculates the model values of this section. It uses the Warrior, the Druid and the gear tiers of models/threat/threat_model.py. The Warrior and Druid values come from the Forever spellbook and talents (wowforevertalents.com) and from player data (see Sources). Part 7 gives the wowsims check.

## Summary

- **Threat is no longer a problem of the Paladin tank.** In the beta of 30 October, the Paladin has 101% of the Warrior threat with the same gear (model). In wowsims, it has 100% of the Warrior. In the beta of 18 October, it had 63% (model).
- **The cause.** Righteous Fury now increases all threat by 33%. Shieldsworn gives a Holy Strike each 6 sec, and each Holy Strike also triggers the Holy Shield damage. Without Shieldsworn, the Paladin has 522 TPS (not 661). Without the +33%, it has 497 TPS.
- **The kept proposals add threat as a side effect.** No proposal is for threat. Redoubt (C-P1) gives more blocks, and thus more Holy Shield damage. Reckoning (C-P12) gives more extra attacks. The Holy Strike Seal trigger (C1) adds Seal of Fury hits. In wowsims, they give +12% together (928 → 1,038 TPS).
- **The proposed Paladin has more threat than the Warrior.** In wowsims, it has 112% of the Warrior threat. The model gives 123–144% from fresh level 60 to Naxxramas. The model gives too much to Redoubt (C-P1) (part 7).
- **Judgement of the Crusader gives the Paladin tank about +72 TPS.** In the beta, the raid can need the only Judgement of the tank for Light or Wisdom. Then the beta tank has 90% of the Warrior threat. With Personal Judgement of the Crusader (C2), the tank keeps it.
- **Consecration is not necessary for threat.** With Consecration on cooldown, the proposed Paladin has 140–167% of the Warrior threat. But at fresh level 60, the mana then lasts about 1 min (see Analysis, Mana).
- **Against 3 or more enemies, the Paladin holds the group best.** In wowsims, it has 1.4 times the Druid threat and 3–4 times the Warrior threat on the lowest target. The proposals do not change this (part 8).
- **The Druid threat multipliers are not known.** The model uses the player data (Maul ×1.75, Primal Bite ×3). wowsims Forever uses Bear Form ×1.5 only. With the wowsims values, the Druid loses about one third of its threat (part 2).

## 1. Result with the same gear

Conditions:

- All tanks have pre-raid gear: 200 spell power, 500 Attack Power, a 45 damage per sec weapon (2.7 sec).
- The beta Paladin uses the tank build 0/38/13 (part 6). The proposed Paladin uses the same talents. It adds the kept proposals: Holy Strike Seal trigger (C1), Personal Judgement of the Crusader (C2), Redoubt (C-P1) and Reckoning (C-P12). Toughness removal (C-P13) does not change threat.
- The boss has 5 Sunder Armor and Faerie Fire.

| Boss hit before armor | Warrior | Druid | Paladin, beta | Paladin, beta, no Crusader | Paladin, proposed | Paladin, proposed + Consecration |
| --- | --- | --- | --- | --- | --- | --- |
| 3,000 | 576 | 551 | 661 | 589 | 802 | 925 |
| 4,500 | 653 | 600 | 661 | 589 | 802 | 925 |
| 6,000 | 676 | 626 | 661 | 589 | 802 | 925 |

- Warrior and Druid receive rage when the boss hits them. Thus, their threat increases when the boss hits harder. Paladin threat does not change with boss damage.
- At 4,500, the beta Paladin has 101% of the Warrior threat and 110% of the Druid threat. The proposed Paladin has 123% and 134%.
- "No Crusader" is the beta tank when the raid needs its Judgement for Light or Wisdom. With Personal Judgement of the Crusader (C2), the tank keeps Crusader in all cases.
- If the boss has no armor debuffs (4,500 hits): Warrior 528 TPS, Druid 464 TPS, beta Paladin 637 TPS, proposed Paladin 773 TPS. Most Paladin threat is Holy damage. Armor does not decrease Holy damage.

**Threat sources of the Warrior and the Druid (4,500 hits)**

| Warrior | TPS | Druid | TPS (player data) | TPS (wowsims multipliers) |
| --- | --- | --- | --- | --- |
| Heroic Strike | 194 | Maul | 271 | 155 |
| Revenge (about 10 each min) | 167 | Primal Bite | 150 | 50 |
| Shield Slam | 121 | Rage | 85 | 85 |
| Rage | 86 | Lacerate | 64 | 64 |
| Sunder Armor | 74 | Faerie Fire (not verified) | 30 | 30 |
| Rend | 11 | | | |
| **Total** | **653** | **Total** | **600** | **384** |

**Threat sources of the Paladin (200 spell power)**

| Source | Beta | Proposed | Cause of the change |
| --- | --- | --- | --- |
| Holy Shield (blocks and Shieldsworn) | 287 | 374 | Redoubt (C-P1): more blocks |
| Judgement of Fury (one each 8 sec, plus Swift Judgement each minute) | 118 | 118 | — |
| Seal of Fury (auto attacks, Reckoning attacks and Holy Strike) | 70 | 108 | Holy Strike Seal trigger (C1) and more Reckoning attacks |
| Holy Strike with Iron Creed 3/3 | 104 | 104 | — |
| Auto attacks | 64 | 64 | — |
| Reckoning extra attacks | 17 | 33 | Reckoning (C-P12) and Redoubt (C-P1) |
| **Total** | **661** | **802** | |

Value of each proposal in the model: Redoubt (C-P1) +96 TPS, Holy Strike Seal trigger (C1) +25 TPS, Reckoning (C-P12) +20 TPS. Personal Judgement of the Crusader (C2) gives +72 TPS when the raid needs the Judgement of the tank.

**Spell power**

Each +100 spell power gives about +45 TPS (beta) and +53 TPS (proposed).

| Spell power | 100 | 150 | 200 | 250 | 300 | 350 |
| --- | --- | --- | --- | --- | --- | --- |
| Paladin, beta | 616 | 639 | 661 | 684 | 706 | 729 |
| Paladin, proposed | 749 | 775 | 802 | 828 | 855 | 881 |

Judgement of the Crusader adds 161 spell power against the boss. This is more than the difference between 150 and 300 spell power.

## 2. Result with gear progression

In raids, the gear and the boss damage increase together. This table shows the five gear tiers of the model.

- The fresh level 60 tier uses a real gear profile (crafted items and dungeon items, without talents).
- The other tiers are estimates. Each tier has about 15–20% more stats, as in Classic.
- The Warrior and the Druid have the same Attack Power and weapon as the Paladin.

| Tier | Spell power | Attack Power | Weapon damage per sec | Maximum mana | Boss hit before armor |
| --- | --- | --- | --- | --- | --- |
| Fresh level 60 (real profile) | 208 | 428 | 27.5 (2.2 sec) | 2,897 | 3,000 |
| Pre-raid best in slot | 260 | 520 | 42 | 3,400 | 3,500 |
| Molten Core | 310 | 600 | 52 | 3,900 | 4,500 |
| Blackwing Lair | 380 | 700 | 60 | 4,400 | 6,000 |
| Naxxramas | 440 | 800 | 66 | 4,900 | 8,000 |

TPS on one boss. The two percentages are the Paladin TPS divided by the Warrior TPS and by the Druid TPS.

| Tier | Warrior | Druid | Paladin, beta | Paladin, beta, no Crusader | **Paladin, proposed** | Proposed + Consecration |
| --- | --- | --- | --- | --- | --- | --- |
| Fresh level 60 | 536 | 475 | 636 (118%, 134%) | 560 (104%, 118%) | **770 (144%, 162%)** | 894 (167%, 188%) |
| Pre-raid best in slot | 605 | 562 | 686 (113%, 122%) | 613 (101%, 109%) | **831 (137%, 148%)** | 960 (159%, 171%) |
| Molten Core | 690 | 652 | 733 (106%, 112%) | 661 (96%, 101%) | **885 (128%, 136%)** | 1,019 (148%, 156%) |
| Blackwing Lair | 751 | 733 | 789 (105%, 108%) | 717 (95%, 98%) | **950 (126%, 130%)** | 1,090 (145%, 149%) |
| Naxxramas | 820 | 814 | 837 (102%, 103%) | 764 (93%, 94%) | **1,005 (123%, 123%)** | 1,151 (140%, 141%) |

- The beta Paladin has more threat than the Warrior and the Druid at all tiers. Its lead decreases from 118% to 102% of the Warrior. The Warrior and the Druid receive more Attack Power and more rage. The Paladin receives only spell power.
- Without Judgement of the Crusader, the beta Paladin is below the Warrior from Molten Core (93–96%).
- The proposed Paladin has 123–144% of the Warrior threat. In wowsims, the lead is smaller: 112% (part 7).
- With the wowsims multipliers (Maul, Primal Bite and Swipe: Bear Form ×1.5 only), the Druid has 297, 349, 412, 467 and 526 TPS. The real multipliers are not known (see Open items).
- Consecration costs 565 mana each 8 sec. With Blessing of Wisdom, the tank can use it on cooldown for about 1 min at fresh level 60. In Naxxramas, it can use it for about 3 min (see Analysis, Mana).

## 3. Result with flatter gear

Blizzard said that it wants flatter gear progression. This is an intention, not a promise. This part shows the result if the gear increases more slowly.

Model:

- Fresh level 60 and pre-raid are the same as in part 2.
- From Molten Core, the gear increases at half the rate of part 2.
- Two cases for boss damage: boss hits as in part 2, or boss hits at half the rate (4,000, 4,750 and 5,750 before armor).

The first value is the percentage of the Warrior TPS. The value in brackets is the percentage of the Druid TPS.

| Tier | Gear as in part 2 | Flatter gear, boss hits as in part 2 | Flatter gear, flatter boss hits |
| --- | --- | --- | --- |
| Beta, Naxxramas | 102% (103%) | 100% (102%) | 104% (106%) |
| Proposed, fresh level 60 | 144% (162%) | 144% (162%) | 144% (162%) |
| Proposed, pre-raid best in slot | 137% (148%) | 137% (148%) | 137% (148%) |
| Proposed, Molten Core | 128% (136%) | 128% (138%) | 132% (142%) |
| Proposed, Blackwing Lair | 126% (130%) | 125% (132%) | 128% (136%) |
| Proposed, Naxxramas | 123% (123%) | 120% (125%) | 126% (132%) |

- Against the Warrior, flatter gear changes the result by 3 points or less.
- The weakest case is flatter gear with boss hits that continue to increase. The Warrior and the Druid still receive more rage from larger hits. The beta Paladin then has 100% of the Warrior threat in Naxxramas.
- Personal Judgement of the Crusader (C2): the +161 spell power from Judgement of the Crusader is more important when gear gives less spell power.

## 4. Why the Paladin is different

- **Righteous Fury.** It now gives ×1.33 to all threat, and ×1.9 more to Holy damage (×2.527 in all). Defensive Stance and Defiance give ×1.495 to all Warrior threat. Bear Form gives ×1.5 to all Druid threat.
- **Most Paladin threat is Holy damage.** Boss armor and rage do not change it. Holy Shield, Judgement of Fury, Holy Strike and Seal of Fury are Holy damage.
- **Shieldsworn.** Holy Strike has a 6 sec cooldown (not 10 sec). Each Holy Strike that lands also triggers the Holy Shield damage, with no charge used.

| Attack | Total threat multiplier | Cooldown |
| --- | --- | --- |
| Primal Bite (Druid, new in Forever) | ×4.5 (×3, Bear Form ×1.5; player data). wowsims Forever: ×1.5 | 6 sec |
| Revenge (Warrior) | ×3.4 (×2.25, Defensive Stance and Defiance ×1.495) | 5 sec. About 10 casts each min: it needs a block, dodge or parry |
| Holy Strike with Iron Creed 3/3 (Paladin) | ×3.3 (Righteous Fury ×2.527, Iron Creed ×1.3) | 6 sec (Shieldsworn) |
| Holy Shield (Paladin) | ×3.0 (Righteous Fury ×2.527, Holy Shield ×1.2) | Each block, and each Holy Strike that lands |
| Maul (Druid) | ×2.6 (×1.75, Bear Form ×1.5; player data). wowsims Forever: ×1.5 | Each swing |
| Paladin auto attacks and Reckoning attacks | ×1.33 | — |

- **Groups of enemies.** Consecration hits all enemies near the Paladin, but its bonus damage hits only 4 of them. Holy Shield does damage only when the Paladin blocks, to the blocked attacker, with 4 charges each 10 sec. Thus, the Paladin spreads threat well on 2 to 4 enemies.

## 5. Is the threat too high?

The design goal of the Protection Paladin is a tank with the same threat as the Warrior. The beta of 30 October reaches it. The kept proposals are for survival, Reckoning and tank tools, not for threat.

- **In wowsims, the proposals add 12%.** Redoubt (C-P1) gives +6%, Reckoning (C-P12) +3% and the Holy Strike Seal trigger (C1) +3%.
- **Redoubt (C-P1) is the largest part.** It is a survival proposal: crushing blows decrease from 11.9% to 1.0% (see Analysis, Crushing blows). Its threat comes from more Holy Shield damage.
- **The gear is not the same.** wowsims uses the default tank set of each class. A Warrior with better gear can make the Paladin lead smaller.
- **Compare the tanks in beta tests.** The model and wowsims do not use real fights. Beta tests with the same gear give the real lead.

## 6. Inputs

**All tanks**

- Level 60, 500 Attack Power, 3% hit.
- One-handed weapon: 45 damage per sec, 2.7 sec speed. Druid: weapon damage per sec + Attack Power ÷ 14, with a 2.5 sec swing (about 220 damage).
- Critical hit chance: 6%. Druid: 12% (Sharpened Claws).

**Attacks against a level 63 boss (from the front)**

- 8% miss, 6.5% dodge, 14% parry. Each 1% of hit removes 1% miss.
- 40% of auto attacks are glancing blows (−35% damage).
- Critical hit decrease: −4.8% (3% + 1.8%). Special attacks roll the critical hit separately, only on the hits that land (wowsims Forever).

**Boss**

- 3,731 armor. 976 armor after 5 Sunder Armor (450 each) and Faerie Fire.
- One swing each 2 sec. 64% of the swings hit the tank.

**Rage (normalized in Forever)**

- Auto attack: 3.46 rage × weapon speed. ×1.3 for two-handed weapons and Bear Form. ×2 for a critical hit. No rage for a miss, dodge or parry.
- Damage taken: 2.5 × 0.6 × boss hit before armor ÷ 243.6 (level 63). ×1.5 for a crushing blow.
- Heroic Strike and Maul hits give no rage (assumed, as in Classic).
- Each rage point gives 5 threat: rage from auto attacks, damage taken, talents and spells (player data).

**Warrior**

- Talents (assumed): Defiance 3/3, Bastion 5/5, Improved Revenge 3/3, Shield Specialization 5/5, Master of Defense 2/2, Improved Sunder Armor 3/3, Focused Rage 3/3, Improved Heroic Strike 3/3.
- Defensive Stance: ×1.3 threat, −10% damage. Defiance 3/3: ×1.15 threat with a shield. Bastion 5/5: +10% damage with a shield.
- Revenge rank 6: 138–168 damage + 28% of Attack Power, +60% (Improved Revenge). Threat = damage × 2.25 (player sheet, see Sources). About 10 casts each min, because Revenge needs a block, dodge or parry (wowsims Forever).
- Rend rank 7: 7 ticks of 21 damage + 2% of Attack Power, 21 sec. A bleed: armor does not decrease it. Threat = damage (wowsims Forever).
- Shield Slam rank 4: 640–670 damage + block value. Threat = damage. The real multiplier is not known.
- Heroic Strike rank 9: +157 damage. Threat = damage + 152.4 (wowsims Forever, measured).
- 5 rage for each block, dodge and parry (Shield Specialization, Master of Defense). Each rage point gives 5 threat (player sheet, see Sources).
- Sunder Armor: 206 threat + 5% of Attack Power (rank 5, game files), before Defensive Stance.
- Bloodrage: 10 rage + 10 rage over 10 sec, 1 min cooldown. Its rage gives threat: 50 + 50 (player data).
- Shield Block on cooldown: 10 rage each 5 sec. It blocks about 80% of the swings. 3% of the swings are crushing blows (see Crushing blows).
- Rage costs with talents: Shield Slam 17, Revenge 2, Rend 7, Sunder Armor 9, Heroic Strike 9.
- Shield Slam and Shield Block are used on cooldown. Revenge follows each block, dodge or parry. Rend stays on the boss. Sunder Armor fills the free global cooldowns. Heroic Strike uses the extra rage.

**Druid**

- Talents (assumed): Ferocity 5/5, Savage Fury 2/2, Feral Instinct 3/3, Sharpened Claws 2/2, Predatory Strikes 3/3, Blood Frenzy 2/2, Natural Reaction 5/5.
- Threat: Bear Form ×1.5, Maul ×1.75, Primal Bite ×3, Swipe ×1.75 (player data). wowsims Forever uses Bear Form ×1.5 only. Neither value is verified (see Open items). Part 2 shows the Druid with both values.
- Damage for each swing: weapon damage per sec + Attack Power ÷ 14, with a 2.5 sec swing (player data). Predatory Strikes gives +90 Attack Power.
- Maul rank 7: +128 damage, +10% (Savage Fury), 10 rage.
- Primal Bite rank 4: weapon damage + 77, 15 rage, 6 sec cooldown.
- Swipe rank 5: 83 damage + 3% of Attack Power, +10% (Savage Fury), +30% (Feral Instinct), 15 rage. Only against groups of enemies.
- Lacerate rank 3: 15 rage. The hit does 10% of weapon damage for each stack. The bleed does 15 damage each 3 sec for each stack: 5 stacks, 15 sec. Threat = damage (wowsims Forever).
- Faerie Fire in Bear Form: 120 threat (2 × level), 6 sec cooldown (player data, not verified). wowsims Forever gives it no threat.
- Blood Frenzy: 5 rage for each critical hit. Natural Reaction: 5 rage for each dodge.
- Enrage: 10 rage + 20 rage over 10 sec, 1 min cooldown. Its rage gives threat: 50 + 100. The −27% base armor of Enrage is not in the model.
- No shield: 15% of the swings are crushing blows (see Crushing blows).
- Primal Bite and Faerie Fire are used on cooldown. Maul uses the extra rage. Lacerate fills the free global cooldowns (wowsims Forever rotation).

**Paladin (beta of 30 October, game files in wowsims Forever)**

- Tank build 0/38/13: Divine Intellect 2, Redoubt 5, Precision 3, Sacred Duty 1, Templar's Bulwark, Shield Specialization 2, Toughness 5, Swift Judgement, Improved Righteous Fury 3, Anticipation 5, Holy Shield, Reckoning 5, Iron Creed 3, Shieldsworn. Retribution: Benediction 5, Improved Judgement 2, Conviction 3, Sanctified Judgement 3.
- Righteous Fury: ×1.33 all threat, and ×1.9 more for Holy damage (×2.527 in all).
- Hit: +3% (Precision). Critical hit chance: +6% (Conviction 3/3, attacks and spells).
- Holy Shield rank 4: 221 Holy damage + 8% of spell power on each block. Threat ×1.2. The model uses 2.5 blocks each 10 sec (beta). Shieldsworn: each Holy Strike that lands also triggers the damage, with no charge used.
- Holy Strike: 50% of (normalized weapon damage (2.4 sec) + 93 + 42.9% of spell power). All of it is Holy damage. 6 sec cooldown (Shieldsworn). Iron Creed 3/3: +30% threat.
- Judgement of Fury: 160 + 42.9% of spell power, Holy damage. One each 8 sec (Improved Judgement 2/2), plus one Swift Judgement each minute. It uses the melee hit table with no dodge or parry. The damage hits before the taunt (beta test).
- Seal of Fury (rank 7): 35 Holy damage + 10% of spell power for each hit. It cannot miss. Its critical hit uses a separate roll. In the beta, Holy Strike does not trigger it.
- Reckoning 5/5: 1 extra attack each 10 sec (model value for the beta).
- Consecration rank 5: 312 damage in 8 sec, + 33.6% of spell power. One cast each 8 sec, 15% of ticks miss. Critical hit ×1.5 (beta test).

**Paladin, kept proposals (values from wowsims, part 7)**

- Redoubt (C-P1): block 42.3% → 61.6%. The model multiplies the Holy Shield blocks by 1.46 (3.6 each 10 sec, maximum 4 charges). Reckoning extra attacks: ×1.29.
- Reckoning (C-P12): extra attacks ×1.48 (9.3 against 6.3 each min, both with Redoubt).
- Holy Strike Seal trigger (C1): each Holy Strike that lands also triggers Seal of Fury.

## 7. Check with wowsims

wowsims Forever gives a second calculation with the full rules of the game.

Conditions: wowsims Forever master commit 895cd67f9 (game files of hotfix push 113554), with the proposals as flags (models/wowsims-b2). The Paladin is Human, with the default tank set, rotation and consumables. Talents 12/32/7 (the wowsims default tank build) with Redoubt 5/5. Warrior: the pre-raid set. Druid: the default Bear set. Full buffs. A 3 min fight against one level 63 boss from the front, 3,000 iterations.

| Tank | TPS (% of the Warrior) | Damage taken each sec | TMI | Crushing blows |
| --- | --- | --- | --- | --- |
| Warrior | 926 (100%) | 281 | 47 | 1.0% |
| Druid | 835 (90%) | 379 | 39.7 | 15.0% |
| Paladin, beta | 928 (100%) | 333 | 57.1 | 11.9% |
| Paladin, Holy Strike Seal trigger (C1) | 954 (103%) | 332 | 57.1 | 11.9% |
| Paladin, Redoubt (C-P1) | 986 (106%) | 288 | 44.0 | 1.0% |
| Paladin, C-P1 and Reckoning (C-P12) | 1,012 (109%) | 289 | 44.0 | 1.0% |
| **Paladin, all kept proposals** | **1,038 (112%)** | **289** | **43.9** | **1.0%** |
| Paladin, all kept proposals, no Toughness (C-P13) | 1,038 (112%) | 295 | 45.0 | 1.0% |

TMI is the damage intake value of wowsims with a 6 sec window: less is better.

- **The beta Paladin has the threat of the Warrior.** In the model, it has 101% (part 1). The two calculations agree.
- **The proposals add less in wowsims.** wowsims gives +110 TPS (+12%). The model gives +141 TPS (+21%). The model multiplies the Holy Shield blocks by the block chance. In wowsims, Redoubt gives +58 TPS, and the model +96 TPS.
- **The other proposals agree.** Holy Strike Seal trigger (C1): wowsims +26, model +25. Reckoning (C-P12): wowsims +26, model +20.
- **Toughness removal (C-P13)** does not change threat. Damage taken increases by 2%.
- **The gear is not the same.** Each class uses its default wowsims set. Thus, the Druid row is a check of the order, not of the level.

The test files are in models/wowsims-b2. See its README for the setup and the proposal flags.

## 8. Several targets

This part compares the tanks against groups of 3 and 5 enemies. The model uses the rules of models/threat/multi_target.py, with the Paladin of the beta of 30 October (threat_tables_b2.py).

Terms:

- **Main target:** the enemy that the tank attacks.
- **Extra targets:** the other enemies of the group.
- **Lowest target:** the extra target with the least threat. A healer or a damage dealer pulls this enemy from the tank first. Thus, it shows how well a tank holds a group.

**Area spells** (wowsims Forever spell data)

| Class | Area spell | Value |
| --- | --- | --- |
| Warrior | Thunder Clap rank 6 | 103 + 7% of Attack Power, 4 targets, 6 sec cooldown, 20 rage, spell hit table, armor applies. Threat ×1 (wowsims: not verified) |
| Warrior | Cleave rank 5 | Weapon + 50, 2 targets, 20 rage, 91.8 flat threat shared between the targets |
| Druid | Swipe rank 5 | 83 + 3% of Attack Power, 3 targets, 20 rage (15 with Ferocity), ×1.75 threat (player data) |
| Paladin | Consecration rank 5 | 96 Holy damage to all enemies. The first 4 enemies also take 216 + 33.6% of spell power. 565 mana each 8 sec |
| Paladin | Holy Shield rank 4 | Damage only on a block, to the blocked attacker. 4 charges. With 2 or more attackers, all 4 charges are used each 10 sec. The Shieldsworn trigger hits the target of Holy Strike |

**Assumptions of the model**

- Each trash mob hits for 1/3 of the boss hit of the tier and swings each 2 sec. Rage from hits increases with the number of mobs.
- Trash has no Sunder Armor or Faerie Fire (armor 3,731).
- Paladin: the tank build of part 6 with Consecration on cooldown. Seal, Judgement, Holy Strike and auto attacks hit the main target. Judgement of the Crusader is on the main target only.
- Warrior: Shield Slam, Revenge (10 casts each min), Shield Block and Rend on the main target. Then Thunder Clap, then Sunder Armor. Cleave uses the rage that stays.
- Druid: Primal Bite and Faerie Fire, then Swipe, then Maul with the rage that stays. On 1 target, Lacerate replaces Swipe.
- Rage threat is shared between all targets.
- Not in the model: Demoralizing Shout and Demoralizing Roar (about 43 threat for each target), tab targets.

**Model result**

Each cell gives the threat per sec on all targets, then the threat per sec on one extra target in brackets. The last column compares the proposed Paladin with the stronger of the Warrior and the Druid.

3 targets:

| Tier | Warrior | Druid | Paladin, beta | Paladin, proposed | Proposed Paladin, % of the stronger tank: all targets / one extra target |
| --- | --- | --- | --- | --- | --- |
| Fresh level 60 | 488 (76) | 500 (85) | 1,064 (205) | 1,109 (205) | 222% / 241% |
| Pre-raid best in slot | 553 (88) | 572 (88) | 1,123 (211) | 1,176 (211) | 205% / 239% |
| Molten Core | 627 (107) | 640 (94) | 1,183 (218) | 1,240 (218) | 194% / 204% |
| Blackwing Lair | 689 (120) | 704 (104) | 1,256 (227) | 1,319 (227) | 187% / 189% |
| Naxxramas | 758 (136) | 772 (117) | 1,320 (234) | 1,387 (234) | 180% / 173% |

5 targets (Consecration: the fifth enemy takes only the 96 base damage):

| Tier | Warrior | Druid | Paladin, beta | Paladin, proposed | Proposed Paladin, % of the stronger tank: all targets / one extra target |
| --- | --- | --- | --- | --- | --- |
| Fresh level 60 | 611 (69) | 567 (53) | 1,198 (146) | 1,243 (146) | 203% / 211% |
| Pre-raid best in slot | 662 (74) | 633 (56) | 1,262 (151) | 1,315 (151) | 199% / 203% |
| Molten Core | 724 (83) | 701 (63) | 1,326 (155) | 1,383 (155) | 191% / 188% |
| Blackwing Lair | 803 (94) | 782 (72) | 1,407 (162) | 1,470 (162) | 183% / 172% |
| Naxxramas | 893 (107) | 872 (84) | 1,476 (167) | 1,544 (167) | 173% / 156% |

- Without Consecration, the proposed Paladin has 127–154% of the stronger tank on 3 targets, and 109–125% on 5 targets.
- The proposals add threat only on the main target. On the extra targets, all 4 Holy Shield charges are already used in the beta.
- **The model lead is too large.** On 1 trash target, the model gives the proposed Paladin 211–269% of the Warrior. wowsims gives 120% (see the next table). In the model, each mob hits for 1/3 of a boss hit. Thus, the Warrior and the Druid receive little rage. Trash also has no Sunder Armor or Faerie Fire. Armor does not decrease Holy damage.

**Check with wowsims Forever**

Setup: the sim of part 7. Each level 63 target hits for 1/3 of the boss. The Paladin uses its default rotation with Consecration. 3 min, 3,000 iterations.

Threat per sec on each target. The main target is first.

| Tank | 1 target | 3 targets | 5 targets |
| --- | --- | --- | --- |
| Paladin, beta | 927 | 914 / 249 / 249 | 915 / 223 / 223 / 223 / 127 |
| Paladin, proposed | 1,038 | 943 / 253 / 253 | 927 / 224 / 224 / 224 / 128 |
| Warrior | 863 | 859 / 227 / 78 | 907 / 344 / 73 / 73 / 33 |
| Druid | 726 | 725 / 184 / 180 | 767 / 187 / 180 / 43 / 43 |

- **Lowest target: the Paladin leads.** On 3 targets, the Paladin has 1.4 times the Druid threat and 3.2 times the Warrior threat. On 5 targets, it has about 3–4 times both.
- **Total threat: the Paladin leads.** On 3 targets, the proposed Paladin has 1,450 TPS on all targets, the Warrior 1,164 (125%) and the Druid 1,089. On 5 targets, the proposed Paladin has 1,726 and the Warrior 1,431 (121%). The beta Paladin has 121% and 120% of the Warrior.
- **The proposals change almost nothing on groups.** They add 1–3% on all targets.
- **Consecration and Holy Shield** give the threat on the extra targets. Consecration gives its full damage to 4 enemies only. Thus, the fifth target has about half of the threat of the others.
- **Warrior.** Cleave hits only 2 targets. Thus, the third target and the others have little Warrior threat.
- **Druid.** Swipe hits 3 targets. Against 5 targets, the fourth and fifth targets have little Druid threat.

**Conclusion**

- Against 3 or more enemies, the Paladin holds the group best. It has the most threat on the lowest target. The model and wowsims agree.
- No proposal is necessary for threat against groups.

## 9. Limits

- **Holy Shield blocks.** The model uses 2.5 blocks each 10 sec for the beta and multiplies them by the block chance for Redoubt (C-P1). wowsims gives a smaller increase. Use the wowsims value for Redoubt (C-P1).
- **Druid multipliers.** The real Maul, Primal Bite and Swipe multipliers are not known (see Open items).
- **Gear.** The model gives all tanks the same gear. wowsims uses the default set of each class.
- **Righteous Fury.** The values use the wowsims rule: the +33% and the ×1.9 multiply (×2.527 for Holy damage). If the two add, Holy threat is ×2.23 and the Paladin has about 10% less threat.
- **Holy Shield rank 4.** It has no cost or level yet in the game files. The model uses its 221 damage.
- **The beta of 18 October.** The earlier version of this tab used the trees of 18 October. It is in the history of the repository.
