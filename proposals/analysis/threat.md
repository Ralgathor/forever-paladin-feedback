# Threat

This section compares the threat of the three tanks: Warrior, Druid and Paladin. The unit is threat per second (TPS) on one boss. Part 8 compares the tanks against groups of enemies. The tanks are level 60. The boss is level 63.

The values come from a model. The model uses beta tests and developer notes. It is not a combat log. The inputs are in part 6. The spell data from beta tests is in Beta test results. The values that are not known are in Open questions.

The script models/threat/run_tables.py calculates all values of this section from the inputs of part 6. The Warrior and Druid values come from the Forever spellbook and talents (wowforevertalents.com) and from player data (see Sources). Spell values and combat rules are checked against wowsims Forever (23 October 2026). The rotations of the three tanks are checked against the wowsims Forever rotations (28 October 2026). Parts 2, 7 and 8 also use the best tank builds and the pre-raid gear of builds/protection.md (29 October 2026). Some threat values are not known. Part 6 shows them.

## Summary

- With all proposals, the Paladin has 96–102% of the Druid threat and 91–97% of the Warrior threat.
- With Consecration on cooldown, the Paladin has 109–122% of the Druid threat. But the mana then lasts about 1 min at fresh level 60 and 6.5 min in Naxxramas (see Analysis, Mana).
- Without the proposals, the Paladin has less threat than the other two tanks at all gear levels.
- Holy Shield (C-P9: damage increases with block value) is necessary. Without Holy Shield (C-P9), the Paladin is further below the other tanks in raids (75% of the Druid threat in Naxxramas).
- Judgement of the Crusader gives the Paladin tank about +55 TPS. Judgement of Fury does not remove it. With Personal Judgement of the Crusader (C2), the tank keeps it. This is also true when the raid needs the Judgement of the tank for Light or Wisdom.
- If the gear progression is flatter, the Paladin has 92–97% of the Druid threat in Naxxramas.
- The Druid threat multipliers are not known. The model uses the player data (Maul ×1.75, Primal Bite ×3). wowsims Forever uses Bear Form ×1.5 only. With the wowsims values, the Druid loses about one third of its threat (part 2).
- Against 3 or more enemies, the Paladin has the most threat on the extra targets (part 8). With the pre-raid gear of builds/protection.md, the proposed Paladin also has the most total threat in wowsims.
- Holy Strike Seal trigger (C1: Holy Strike triggers Seal of Fury) gives about +14 TPS more. The tables do not include it. wowsims gives +24 TPS with the PT3 tank.
- **Pre-raid gear has more block value than the model.** The gear search of builds/protection.md gives the proposed tank 108 block value from items with Shield Specialization, and about 118 with Strength. The model uses 60 for pre-raid and 125 for Naxxramas (part 2).
- **Shield block in wowsims is too high.** For epic shields, wowsims gives about 32% more block than the Wowhead Forever tooltips. All runs use the Wowhead values (part 7).
- **wowsims with the new builds and gear.** The proposed tank PT3 has 123% of the Warrior threat and 52% of its TMI. The beta tank BT4b has 89% of the Warrior threat (part 7).

## 1. Result with the same gear

Conditions:

- All tanks have pre-raid gear.
- The Paladin has 200 spell power and 60 block value. The Paladin uses the talents of the 8/35/8 tank (see Analysis, Builds, part 3). PB1 has 2% more threat.
- The boss has 5 Sunder Armor and Faerie Fire.

| Boss hit before armor | Warrior | Druid | Paladin, beta | Paladin, all proposals | Paladin, all proposals + Consecration |
| --- | --- | --- | --- | --- | --- |
| 3,000 | 570 | 550 | 410 | 555 | 645 |
| 4,500 | 645 | 600 | 410 | 555 | 645 |
| 6,000 | 670 | 625 | 410 | 555 | 645 |

All values are approximate.

- Warrior and Druid receive rage when the boss hits them. Thus, their threat increases when the boss hits harder. Paladin threat does not change with boss damage.
- At 4,500 and 6,000, the Warrior uses Heroic Strike on all swings. Thus, its threat increases more slowly.
- If Shield Slam has a ×2.25 threat multiplier (not tested), add 140 TPS to the Warrior.
- Both Paladin columns include Judgement of the Crusader. Judgement of Fury does not remove it. In the beta, a raid can need the tank's only Judgement for Light or Wisdom. Then the beta Paladin has no Crusader and about 360 TPS. With Personal Judgement of the Crusader (C2), the tank keeps Crusader in all cases.
- Without Holy Shield (C-P9), the proposed Paladin has about 470 TPS (565 TPS with Consecration).
- If the boss has no armor debuffs (4,500 hits): Warrior 525 TPS, Druid 465 TPS, Paladin 530 TPS. Most Paladin threat is Holy damage. Armor does not decrease Holy damage.
- Retribution Aura gives the Paladin about +25 TPS. But the Paladin then does not have Devotion Aura (735 armor).

**Threat sources of the Warrior and the Druid (4,500 hits)**

| Warrior | TPS | Druid | TPS (player data) | TPS (wowsims multipliers) |
| --- | --- | --- | --- | --- |
| Heroic Strike | 194 | Maul | 271 | 155 |
| Revenge (about 10 each min) | 167 | Primal Bite | 150 | 50 |
| Shield Slam | 113 | Rage | 85 | 85 |
| Rage | 86 | Lacerate | 64 | 64 |
| Sunder Armor | 74 | Faerie Fire (not verified) | 30 | 30 |
| Rend | 11 | | | |
| **Total** | **645** | **Total** | **600** | **384** |

**Threat sources of the proposed Paladin (200 spell power, 60 block value)**

| Source | TPS |
| --- | --- |
| Holy Shield blocks: 171 from the base damage, 82 from block value (C-P9) | 253 |
| Judgement of Fury: one each 10 sec, plus one Swift Judgement each minute | 90 |
| Seal of Fury (auto attacks and Reckoning attacks) | 79 |
| Auto attacks | 51 |
| Holy Strike with Iron Creed | 48 |
| Reckoning extra attacks (C-P6) | 33 |
| **Total** | **554** |

The proposals give the Paladin about +145 TPS more than the beta:

- Holy Shield (C-P9: block value): about +80 TPS.
- Redoubt (C-P1: more Holy Shield blocks) and Reckoning (C-P6): about +60 TPS.
- Personal Judgement of the Crusader (C2): +50 TPS more when the raid needs the tank's Judgement for Light or Wisdom (beta Paladin).

**Spell power**

Each +100 spell power gives about +33 TPS.

| Spell power | 100 | 150 | 200 | 250 | 300 | 350 |
| --- | --- | --- | --- | --- | --- | --- |
| Paladin, all proposals (60 block value) | 520 | 535 | 555 | 570 | 585 | 605 |

Judgement of the Crusader adds 161 spell power against the boss. This is more than the difference between 150 and 300 spell power.

Spell power at level 60 is not known. At level 30, players have 100–120 spell power. The estimates for level 60 are:

- Pre-raid tank gear: about 150.
- Pre-raid gear with some threat items: 200–250.
- First raid gear: 300–350.

## 2. Result with gear progression

In raids, the gear and the boss damage increase together. This table shows the five gear tiers of the model.

- The fresh level 60 tier uses a real gear profile (crafted items and dungeon items, without talents).
- The other tiers are estimates. Each tier has about 15–20% more stats, as in Classic.
- The Warrior and the Druid have the same Attack Power and weapon as the Paladin.

| Tier | Spell power | Attack Power | Weapon damage per sec | Block value (with Shield Specialization) | Maximum mana | Boss hit before armor |
| --- | --- | --- | --- | --- | --- | --- |
| Fresh level 60 (real profile) | 208 | 428 | 27.5 (2.2 sec) | 26 | 2,897 | 3,000 |
| Pre-raid best in slot | 260 | 520 | 42 | 60 | 3,400 | 3,500 |
| Molten Core | 310 | 600 | 52 | 80 | 3,900 | 4,500 |
| Blackwing Lair | 380 | 700 | 60 | 100 | 4,400 | 6,000 |
| Naxxramas | 440 | 800 | 66 | 125 | 4,900 | 8,000 |

TPS on one boss. The percentage is the Paladin TPS divided by the Druid TPS.

| Tier | Warrior | Druid | Paladin, beta | Paladin, proposals without Holy Shield (C-P9) | **Paladin, all proposals** | All proposals + Consecration |
| --- | --- | --- | --- | --- | --- | --- |
| Fresh level 60 | 535 | 475 | 395 (84%) | 450 (95%) | **485 (102%)** | 580 |
| Pre-raid best in slot | 595 | 560 | 425 (76%) | 490 (87%) | **570 (102%)** | 665 |
| Molten Core | 680 | 650 | 460 (70%) | 525 (81%) | **635 (98%)** | 735 |
| Blackwing Lair | 740 | 735 | 495 (68%) | 570 (78%) | **705 (96%)** | 810 |
| Naxxramas | 805 | 815 | 530 (65%) | 605 (75%) | **780 (96%)** | 885 |

- All Paladin columns include Judgement of the Crusader. Without it (a raid that needs the beta tank's Judgement for Light or Wisdom), subtract about 50 TPS from the beta column.
- With all proposals, the Paladin has 96–102% of the Druid threat at all tiers. With Consecration on cooldown, it has 109–122%. But Consecration costs 565 mana each 8 sec (see Analysis, Mana).
- Without Holy Shield (C-P9), the Paladin is further below the Druid: 95% at fresh level 60, 75% in Naxxramas. The Warrior and the Druid receive more Attack Power and more rage. The Paladin receives only spell power.
- The beta Paladin is behind at all tiers: 84% of the Druid at fresh level 60, and 65% in Naxxramas.
- With the wowsims multipliers (Maul, Primal Bite and Swipe: Bear Form ×1.5 only), the Druid has 295, 350, 410, 465 and 525 TPS. The proposed Paladin then has 148–164% of the Druid threat. The real multipliers are not known (see Open items).
- Shield Specialization gives 6% of maximum mana. Thus, more mana gives more mana return. Without Consecration, the tank receives about +21 mana per sec at fresh level 60 and about +59 mana per sec in Naxxramas (see Analysis, Mana).

**Check with the pre-raid gear search** (builds/protection.md)

The gear search of builds/protection.md gives real pre-raid stats. The table uses the wowsims stat sheet of each set, with no buffs and no consumables. The model talents are PT3 (proposed) and BT4b (beta).

| Gear | Spell power | Attack Power | Block value | Weapon |
| --- | --- | --- | --- | --- |
| Model, pre-raid best in slot | 260 | 520 | 60 | 42 damage per sec, 2.7 sec |
| Path gear, proposed (PT3) | 111 | 616 | 108 (83 × 1.3, Shield Specialization) | Greenhammer: 47.3 damage per sec, 2.3 sec |
| Path gear, beta (BT4b) | 125 | 476 | 44 (no Shield Specialization) | Greenhammer |

Block value comes from the Wowhead Forever tooltips. The model leaves out the Strength part (about +10). wowsims gives epic shields about 32% more block (part 7).

TPS on one boss. The values in brackets are the percentages of the Druid and of the Warrior.

| Gear | Warrior | Druid | Paladin, beta (BT4b) | PT3 without Holy Shield (C-P9) | **PT3, all proposals** | PT3, Holy Shield (C-P9) 150% | PT3, Holy Shield (C-P9) 100% |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Model, pre-raid best in slot | 597 | 562 | 395 (70%, 66%) | 529 (94%, 89%) | **611 (109%, 102%)** | 590 (105%, 99%) | 570 (101%, 95%) |
| Path gear, proposed | 655 | 618 | 372 (60%, 57%) | 498 (81%, 76%) | **645 (104%, 99%)** | 609 (99%, 93%) | 572 (93%, 87%) |
| Path gear, beta | 604 | 578 | 365 (63%, 60%) | 487 (84%, 81%) | 547 (95%, 91%) | 532 (92%, 88%) | 517 (89%, 86%) |

- **The gear search takes block value, not spell power.** The proposed set has the block value of the Naxxramas tier, and less spell power than fresh level 60.
- **Holy Shield (C-P9) gives more.** With the proposed set, the block value part of Holy Shield gives 148 TPS. With the tier estimate, it gives 82 TPS.
- **The result with all proposals does not change much.** PT3 has 104% of the Druid and 99% of the Warrior. With the tier estimate, it has 109% and 102%. The higher Attack Power also gives the Warrior and the Druid more threat.
- **Holy Shield (C-P9) is more important.** Without it, PT3 has only 81% of the Druid with the proposed set (94% with the tier estimate).
- **The beta tank is further behind.** BT4b has 60–63% of the Druid. The beta gear search takes Defense and Stamina against crushing blows.
- **Raid tiers.** If raid gear adds block value at the rate of part 2, Holy Shield (C-P9) gives more than part 2 shows. Monitor the block value of raid gear (see Open items).
- Sacred Arbiter (+20% Holy Strike damage) is in PT3. The model adds it to Holy Strike.

## 3. Result with flatter gear

Blizzard said that it wants flatter gear progression. This is an intention, not a promise. This part shows the result if the gear increases more slowly.

Model:

- Fresh level 60 and pre-raid are the same as in part 2.
- From Molten Core, the gear increases at half the rate of part 2. Block value is 70, 80 and 92 (not 80, 100 and 125).
- Two cases for boss damage: boss hits as in part 2, or boss hits that also increase at half the rate (4,000, 4,750 and 5,750 before armor).

Paladin with all proposals. The first value is the percentage of the Druid TPS. The value in brackets is the percentage of the Warrior TPS.

| Tier | Gear as in part 2 | Flatter gear, boss hits as in part 2 | Flatter gear, flatter boss hits |
| --- | --- | --- | --- |
| Fresh level 60 | 102% (91%) | 102% (91%) | 102% (91%) |
| Pre-raid best in slot | 102% (96%) | 102% (96%) | 102% (96%) |
| Molten Core | 98% (94%) | 97% (91%) | 100% (94%) |
| Blackwing Lair | 96% (96%) | 94% (91%) | 97% (93%) |
| Naxxramas | 96% (97%) | 92% (90%) | 97% (94%) |
| Naxxramas, without Holy Shield (C-P9) | 75% | 75% | 79% |

- With Holy Shield (C-P9) at 200%, the Paladin has 92–102% of the Druid threat in all three cases. At 300%, it has 100–106% of the Druid threat in Naxxramas. At 150%, it has 88–92%.
- Without Holy Shield (C-P9), the Paladin is behind in all cases. Thus, Holy Shield (C-P9) is more important with flatter gear.
- The weakest case is flatter gear with boss hits that continue to increase. The Warrior and the Druid still receive more rage from larger hits. Monitor the block value of each gear tier.
- Mana: if maximum mana increases more slowly (3,650, 3,900 and 4,150), the tank receives +36, +40 and +45 mana per sec without Consecration. Shield Specialization (C-P8) is more important.
- Defense: if gear gives Defense more slowly, tanks reach 440 Defense later. The boss can then make critical hits for a longer time. Redoubt (C-P1) and the Reckoning critical-hit trigger stay useful for a longer time.
- Personal Judgement of the Crusader (C2): the +161 bonus from Judgement of the Crusader is more important when gear gives less spell power.
- The PvP burst check (Reckoning, C-P6) uses fresh and pre-raid stats. It stays correct for a longer time.

## 4. Why the Paladin is different

- **No stance or form multiplier.** Righteous Fury (×1.9) is for Holy damage only. Paladin auto attacks and Reckoning attacks have ×1.0. Defensive Stance gives ×1.495 to all Warrior damage. Bear Form gives ×1.5 to all Druid damage.
- **No strong attack with a short cooldown.**

| Attack | Total threat multiplier | Cooldown |
| --- | --- | --- |
| Primal Bite (Druid, new in Forever) | ×4.5 (×3, Bear Form ×1.5; player data). wowsims Forever: ×1.5 | 6 sec |
| Revenge (Warrior) | ×3.4 (×2.25, Defensive Stance and Defiance ×1.495) | 5 sec. About 10 casts each min: it needs a block, dodge or parry |
| Maul (Druid) | ×2.6 (×1.75, Bear Form ×1.5; player data). wowsims Forever: ×1.5 | Each swing |
| Holy Strike with Iron Creed 5/5 (Paladin) | ×2.4 (Righteous Fury ×1.9, Iron Creed ×1.25) | 10 sec |
| Paladin auto attacks and Reckoning attacks | ×1.0 | — |

- **Paladin advantages.** Boss armor and rage do not change Paladin threat. Consecration hits all enemies near the Paladin, but its bonus damage hits only 4 of them. Holy Shield does damage only when the Paladin blocks, to the blocked attacker, with 4 charges each 10 sec. Thus, the Paladin spreads threat well on 2 to 4 enemies.

## 5. Next steps if threat is too low

Use these steps only if tests show that Protection threat is too low with Holy Shield (C-P9). They are not proposals now.

| Step | Effect |
| --- | --- |
| Iron Creed: Holy Strike threat +20/40/60/80/100% (not +5/10/15/20/25%) | +25 to +40 TPS at each tier. Threat only, no PvP effect |
| A shield attack in Protection row 4: 6 sec cooldown, weapon damage + 100 Holy damage, ×2 threat | +90 to +140 TPS. Adds a button. The new Druid attack Primal Bite is the precedent |

Other options were examined and rejected. See Withdrawn ideas.

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

**Paladin**

- Righteous Fury: ×1.9 threat for Holy damage only.
- One-Handed Weapon Specialization: +10% damage (not for Consecration or Retribution Aura).
- Improved Seals: +15% (8-point dip into Holy).
- Spell power coefficients: Seal of Fury 10% for each hit, Judgement of Fury 42.9%, Holy Strike 21.45%, Holy Shield 8% for each block (game files), Consecration 33.6% (15% of ticks miss).
- Holy Shield: 3 blocks each 10 sec (beta: 2.5). Redoubt 5/5 gives about 1 of these blocks.
- Reckoning: 2.0 extra attacks each 10 sec (beta: 1.0). With Reckoning (C-P6), Holy Strike releases them. Thus, they are not glancing blows.
- Holy Strike: 50% of (normalized weapon damage (2.4 sec) + 93 + 42.9% of spell power). All of it is Holy damage: armor does not decrease it. Righteous Fury multiplies all of its threat (beta test). Holy Power gives Holy Strike +3% critical hit for each rank.
- Judgement of Fury: 153–167 Holy damage. It uses the melee hit table with no dodge or parry. The damage hits before the taunt (beta test). Holy Strike uses the melee hit table.
- Seal of Fury (rank 7): 35 Holy damage + 10% of spell power for each hit. It cannot miss. Its critical hit uses a separate roll.
- Consecration rank 5: 312 damage in 8 sec (8 ticks of 12 + 27), one cast each 8 sec. Critical hit ×1.5 (beta test). Conviction (C-R1) adds to its critical hit chance.

## 7. Check with wowsims

wowsims Forever gives a second calculation with the full rules of the game. This part has two checks. The first uses the best builds and the pre-raid gear of builds/protection.md. The second is the first check, with Julien's gear and PB1.

Conditions: wowsims Forever commit 69e0e5b with the proposals patch (models/wowsims). The patch also has the Seal of Fury trigger of C1 and Vindication with 5 ranks (C-P3). The Paladin is Human. Weapon skill racials are not in WoW Forever. Warrior and Druid: the wowsims pre-raid presets. A 3 min fight against one level 63 boss, 3,000 iterations.

Epic shields use the block value of the Wowhead Forever tooltips. wowsims takes shield block from a table by item level, and the table gives about 32% more. Examples: The Immovable Object 66 (wowsims 79), Evergreen Shield 44 (58), Blessed Qiraji Bulwark 70 (88). Other items with block value agree. The Warrior shield is a rare item and agrees.

### Best builds and pre-raid gear (29 October 2026)

Proposed: PT3 with all proposals. Beta: BT4b. Each build uses its pre-raid path gear with reputation items (builds/protection.md).

| Tank | TPS (% of the Warrior) | TMI (% of the Warrior) | Crushing blows | TPS, no consumables (% of the Warrior) |
| --- | --- | --- | --- | --- |
| Warrior | 996 (100%) | 43.6 (100%) | 0.9% | 904 (100%) |
| Druid | 711 (71%) | 34.0 (78%) | 15.0% | 673 (74%) |
| Paladin, beta (BT4b, beta gear) | 883 (89%) | 26.2 (60%) | 6.0% | 650 (72%) |
| Paladin, beta (BT4b, proposed gear) | 904 (91%) | 30.8 (71%) | 12.0% | 671 (74%) |
| Paladin, PT3 talents, no proposals (proposed gear) | 960 (96%) | 34.9 (80%) | 11.5% | 734 (81%) |
| **Paladin, all proposals (PT3, proposed gear)** | **1,221 (123%)** | **23.0 (53%)** | **0.5%** | **1,019 (113%)** |
| Paladin, all proposals (PT3, beta gear) | 1,108 (111%) | 23.7 (54%) | 0.5% | 909 (101%) |
| PT3, Holy Shield 150% of block value | 1,186 (119%) | 23.0 (53%) | 0.5% | 983 (109%) |
| PT3, Holy Shield 100% of block value | 1,151 (116%) | 23.0 (53%) | 0.5% | 948 (105%) |
| PT3, Iron Creed 6% | 1,221 (123%) | 24.6 (56%) | 0.5% | 1,019 (113%) |

TMI is the damage intake value of wowsims: less is better.

**Value of each proposal** (PT3, proposed gear, raid). Each row removes one proposal.

| Proposal | TPS | Other effect |
| --- | --- | --- |
| Holy Shield (C-P9) | +140 | — |
| Redoubt (C-P1) | +72 | TMI 32.4 → 23.0. Crushing blows 11.4% → 0.5% |
| Reckoning (C-P6) | +61 | — |
| Holy Strike Seal trigger (C1) | +24 | — |
| Conviction (C-R1) | +3 | — |
| Iron Creed (C-P2) | 0 | TMI 24.6 → 23.0 |
| Shield Specialization (C-P8) | −5 (no consumables: +20) | Without it, 20 sec out of mana with no consumables |
| **All proposals** | **+261 (+27%)** | TMI 34.9 → 23.0 |

- **The increase agrees with the model.** The model gives +245 TPS for the same inputs (−6%). The inputs are 397 spell power and 1,180 Attack Power (raid buffs), with Consecration and Retribution Aura.
- **Block value doubles the value of Holy Shield (C-P9).** With Julien's gear (47 block value), it gives about +64 TPS. With the proposed gear (108 block value), it gives +140 TPS.
- **Holy Shield at 150% of block value removes 35 TPS.** PT3 then has 119% of the Warrior threat. TMI does not change.
- **The beta gear trades threat for survival.** Against Julien's gear, the beta path gear gives −11% TPS and −33% TMI. Crushing blows stay at 6–8%.
- **The level does not agree with the model.** wowsims puts PT3 at 123% of the Warrior, and the model at 99% (part 2). The cause is the same as in the first check.
- **The Warrior gear is not searched.** The Paladin gear comes from a gear search, but the Warrior uses the wowsims preset. Warrior gear of the same quality can make the Paladin lead smaller.

### First check: Julien's gear and PB1 (27 October 2026)

wowsims Forever and the model give the same TPS increase from the proposals: +142 and +143. The TPS level against the Warrior is not the same. wowsims puts the beta Paladin at 99% of the Warrior, and the model at 64%.

Conditions: wowsims Forever commit 69e0e5b with the proposals patch (models/wowsims). Julien's gear, talents and rotation (Consecration on cooldown). Proposed: PB1 with Redoubt (C-P1), Iron Creed (C-P2), Reckoning (C-P6), Shield Specialization (C-P8) and Holy Shield (C-P9). Warrior and Druid: the wowsims pre-raid presets. A 3 min fight against one level 63 boss, 3,000 iterations.

| Value | Model | wowsims | Difference |
| --- | --- | --- | --- |
| Proposals, TPS added to the beta Paladin | +143 | +142 | −0.8% |
| Beta Paladin as a % of the Warrior | 64% | 99% | +56% |
| Proposed Paladin as a % of the Warrior | 86% | 114% | +33% |

- **The increase agrees.** Thus, the model value of each proposal is correct.
- **The level does not agree.** Julien's gear gives 468 spell power with consumables and 42.6% melee critical hit chance. It also has a fast weapon with an extra attack, Windfury and Consecration. Part 1 uses 200 spell power, 6% critical hit chance and no Consecration. Curse of the Elements in the sim raid adds 10% to Holy damage taken.
- **The model with the sim inputs.** With these inputs, the model gives 1,001 TPS for the same sources, and wowsims gives 894 (−11%). wowsims has fewer Holy Shield blocks (−26%), fewer boss hits for Retribution Aura (−24%) and less auto attack threat (−28%). Seal of Fury is 6% higher in wowsims. check.py gives this table for each source.
- **The Warrior is also different.** The model Warrior and the wowsims Warrior do not use the same gear and talents. The cause of the Warrior difference is not confirmed. Thus, part 1 compares the tanks with the same model inputs.

**wowsims result of each tank** (Julien's gear for the Paladin)

| Tank | TPS (% of the Warrior) | TMI (% of the Warrior) | Crushing blows | TPS, no consumables (% of the Warrior) |
| --- | --- | --- | --- | --- |
| Warrior | 996 (100%) | 43.6 (100%) | 0.9% | 904 (100%) |
| Druid | 711 (71%) | 34.0 (78%) | 15.0% | 673 (74%) |
| Paladin, beta | 988 (99%) | 38.7 (89%) | 10.8% | 789 (87%) |
| Paladin, Redoubt (C-P1) only | 1,021 (103%) | 33.6 (77%) | 0.6% | 824 (91%) |
| **Paladin, all proposals** | **1,130 (114%)** | **31.2 (72%)** | **0.6%** | **925 (102%)** |
| Paladin, all proposals, Holy Shield 150% of block value | 1,114 (112%) | 31.2 (72%) | 0.6% | 909 (101%) |
| Paladin, all proposals, Holy Shield 100% of block value | 1,098 (110%) | 31.2 (72%) | 0.6% | 892 (99%) |
| Paladin, all proposals, Iron Creed 6% | 1,131 (114%) | 33.3 (76%) | 0.6% | 925 (102%) |

TMI is the damage intake value of wowsims: less is better.

- Redoubt (C-P1) removes the crushing blows: 10.8% to 0.6%.
- With all proposals, the Paladin has 114% of the Warrior TPS, and 102% without consumables.
- Holy Shield at 150% of block value removes 16 TPS. Iron Creed at 6% increases TMI by 2.1.

The scripts are run_threat.py and check.py in models/wowsims. See its README for the setup and the proposal flags.

## 8. Several targets

This part compares the tanks against groups of 3 and 5 enemies. The script is models/threat/multi_target.py. It uses the builds and rotations of part 6.

Terms:

- **Main target:** the enemy that the tank attacks.
- **Extra targets:** the other enemies of the group.
- **Lowest target:** the extra target with the least threat. A healer or a damage dealer pulls this enemy from the tank first. Thus, it shows how well a tank holds a group.

**Summary**

- On the extra targets, the Paladin has the most threat of the three tanks. The model and wowsims agree.
- On total threat (all targets), wowsims gives the proposed Paladin 130–139% of the Warrior with the pre-raid path gear (builds/protection.md). With the default wowsims gear, it was about equal. The model gives the Paladin about 1.5 times more. This model lead comes from the assumptions, not from the extra targets (see "Where the lead comes from").
- Consecration and Holy Shield give the threat on the extra targets.
- In wowsims, the beta Paladin has about the same threat as the Druid on the lowest target (pre-raid path gear: 19% more). With the proposals, the Paladin leads by 57%.
- No proposal is necessary for threat against groups.

**Area spells** (wowsims Forever spell data)

| Class | Area spell | Value |
| --- | --- | --- |
| Warrior | Thunder Clap rank 6 | 103 + 7% of Attack Power, 4 targets, 6 sec cooldown, 20 rage, spell hit table, armor applies. Threat ×1 (wowsims: not verified) |
| Warrior | Cleave rank 5 | Weapon + 50, 2 targets, 20 rage, 91.8 flat threat shared between the targets |
| Druid | Swipe rank 5 | 83 + 3% of Attack Power, 3 targets, 20 rage (15 with Ferocity), ×1.75 threat (player data) |
| Paladin | Consecration rank 5 | 96 Holy damage to all enemies. The first 4 enemies also take 216 + 33.6% of spell power. 565 mana each 8 sec |
| Paladin | Holy Shield rank 3 | Damage only on a block, to the blocked attacker. 4 charges. With 2 or more attackers, all 4 charges are used each 10 sec |

**Assumptions of the model**

- Each trash mob hits for 1/3 of the boss hit of the tier and swings each 2 sec. Rage from hits increases with the number of mobs.
- Trash has no Sunder Armor or Faerie Fire (armor 3,731).
- Paladin: PB1 with Consecration on cooldown. Seal, Judgement, Holy Strike and auto attacks hit the main target. Judgement of the Crusader is on the main target only.
- Warrior: Shield Slam, Revenge (10 casts each min), Shield Block and Rend on the main target. Then Thunder Clap, then Sunder Armor. Cleave uses the rage that stays.
- Druid: Primal Bite and Faerie Fire, then Swipe, then Maul with the rage that stays. On 1 target, Lacerate replaces Swipe.
- Rage threat is shared between all targets.
- Not in the model: Demoralizing Shout and Demoralizing Roar (about 43 threat for each target), tab targets.

**Model result**

Each cell gives the threat per sec on all targets, then the threat per sec on one extra target in brackets. The last column compares the proposed Paladin with the stronger of the Warrior and the Druid.

3 targets:

| Tier | Warrior | Druid | Paladin, beta | Paladin, proposed | Proposed Paladin, % of the stronger tank: all targets / one extra target |
| --- | --- | --- | --- | --- | --- |
| Fresh level 60 | 488 (76) | 500 (85) | 725 (152) | 795 (168) | 159% / 197% |
| Pre-raid best in slot | 548 (88) | 572 (88) | 763 (157) | 901 (193) | 157% / 219% |
| Molten Core | 620 (107) | 640 (94) | 803 (161) | 982 (210) | 154% / 197% |
| Blackwing Lair | 681 (120) | 704 (104) | 855 (168) | 1,074 (229) | 153% / 191% |
| Naxxramas | 746 (136) | 772 (117) | 900 (173) | 1,167 (250) | 151% / 184% |

5 targets (Consecration: the fifth enemy takes only the 96 base damage):

| Tier | Warrior | Druid | Paladin, beta | Paladin, proposed | Proposed Paladin, % of the stronger tank: all targets / one extra target |
| --- | --- | --- | --- | --- | --- |
| Fresh level 60 | 611 (69) | 567 (53) | 823 (108) | 893 (118) | 146% / 170% |
| Pre-raid best in slot | 656 (74) | 633 (56) | 864 (111) | 1,003 (134) | 153% / 180% |
| Molten Core | 718 (83) | 701 (63) | 908 (115) | 1,087 (144) | 152% / 174% |
| Blackwing Lair | 794 (94) | 782 (72) | 965 (119) | 1,184 (156) | 149% / 167% |
| Naxxramas | 881 (107) | 872 (84) | 1,014 (123) | 1,282 (169) | 146% / 158% |

- Without Consecration, the proposed Paladin has 109–112% of the stronger tank on 3 targets, and 89–99% on 5 targets.
- With the wowsims Druid multipliers (Bear Form ×1.5 only), the Druid has about one third less threat on all targets.

**Where the lead comes from**

The model lead on all targets is large. Most of it is not from the extra targets.

| Tier (3 targets) | Paladin, beta: % of the stronger tank | Paladin, proposed: % of the stronger tank | TPS added by the proposals |
| --- | --- | --- | --- |
| Fresh level 60 | 145% | 159% | +70 |
| Naxxramas | 116% | 151% | +268 |

- **The lead is there on 1 trash target.** At fresh level 60, the proposed Paladin has 574 TPS, the Warrior 326 and the Druid 268. Each extra target adds about the same threat to the three tanks.
- **Low rage.** Each mob hits for 1/3 of a boss hit. Thus, the Warrior and the Druid receive little rage. If each mob hits as hard as a boss, the lead is about half.
- **Armor.** Trash has no Sunder Armor or Faerie Fire. This decreases Warrior and Druid physical damage. Armor does not decrease Holy damage.
- **Consecration.** The Paladin uses it on cooldown here: +91 to +107 TPS on the main target. Parts 1 to 3 do not include it.
- **The proposals.** At fresh level 60, they add little. In Naxxramas, they give about half of the lead, mostly with Holy Shield (C-P9 and C-P1). On each extra target, they add 16 TPS at fresh level 60 and 77 TPS in Naxxramas.

**Check with wowsims Forever** (29 October 2026)

Setup: wowsims Forever commit 69e0e5b with the proposals patch (models/wowsims). Paladin: PT3 (all proposals) and BT4b (beta), each with its pre-raid path gear (builds/protection.md) and Julien's rotation. Warrior: pre-raid preset. Druid: default preset, with Swipe on 2 or more targets. All tanks have the same raid buffs and debuffs. Each level 63 target hits for 1/3 of the boss. 3 min, 2,000 iterations. The script is run_threat.py in models/wowsims.

Threat per sec on each target. The main target is first.

| Tank | 1 target | 3 targets | 5 targets |
| --- | --- | --- | --- |
| Paladin, beta (BT4b) | 883 | 881 / 245 / 245 | 877 / 214 / 214 / 214 / 115 |
| Paladin, proposed (PT3) | 1,219 | 1,095 / 323 / 323 | 1,042 / 263 / 263 / 263 / 163 |
| Warrior | 926 | 944 / 241 / 71 | 1,001 / 370 / 70 / 69 / 28 |
| Druid | 614 | 614 / 213 / 206 | 646 / 217 / 209 / 31 / 31 |

- **Lowest target: the Paladin leads.** On 3 targets, the proposed Paladin has about 4.5 times the Warrior threat and 1.6 times the Druid threat. On 5 targets, it has 5 to 6 times both.
- **The beta Paladin also leads on the lowest target.** On 3 targets, BT4b has 245 TPS and the Druid 206. With the default wowsims gear of the first check, the beta Paladin was equal to the Druid.
- **Total threat: the proposed Paladin leads.** On 3 targets, PT3 has 1,741 TPS on all targets, and the Warrior 1,256 (139%). On 5 targets, PT3 has 1,994 and the Warrior 1,538 (130%). The beta Paladin has 109% and 106% of the Warrior.
- **Holy Shield.** With 3 or 5 attackers, Holy Shield does damage 3.6 times each 10 sec. With the proposals, it gives about 150 TPS on each extra target against 3 targets (beta: about 74). The proposed gear has more block value than the default gear of the first check (about 120 TPS).
- **Consecration.** It gives about 124 TPS on each of the first 4 targets. The fifth target takes only the base damage (about 24 TPS).
- **Warrior.** Cleave hits only 2 targets, and Thunder Clap gives only about 41 TPS on each target. Thus, the third target and the others have little Warrior threat.
- **Druid.** Swipe hits 3 targets. Against 5 targets, the fourth and fifth targets have little Druid threat. In wowsims, Maul and Primal Bite also hit a second and third target for a part of their damage.
- **First check** (28 October 2026, commit 05ce531, the default wowsims gear of each tank). Lowest target on 3 targets: proposed PB1 255, beta 203, Druid 206, Warrior 71. Total threat: Paladin about equal to the Warrior (3 targets: 1,269 against 1,261).
- The Druid multipliers are not verified (see part 6).

**Conclusion**

- Against 3 or more enemies, the Paladin holds the group best. It has the most threat on the lowest target. The model and wowsims agree.
- On total threat, wowsims gives the proposed Paladin 130–139% of the Warrior with the pre-raid path gear. With the default wowsims gear, the Paladin was about equal to the Warrior. The model gives about 1.5 times, from low rage on trash, trash armor and Consecration.
- Consecration and Holy Shield give the threat on extra targets. Consecration gives its full damage to 4 enemies only.
- The proposals give the lead on the lowest target. Holy Shield (C-P9) and Redoubt (C-P1) add Holy Shield damage, and Shield Specialization (C-P8) pays for Consecration.
- No proposal is necessary for threat against groups.
