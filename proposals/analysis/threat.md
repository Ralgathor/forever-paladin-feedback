# Threat

This section compares the threat of the three tanks: Warrior, Druid and Paladin. The unit is threat per second (TPS) on one boss. The tanks are level 60. The boss is level 63.

The values come from a model. The model uses beta tests and developer notes. It is not a combat log. The inputs are in part 6. The spell data from beta tests is in Beta test results. The values that are not known are in Open questions.

The script models/threat/run_tables.py calculates all values of this section from the inputs of part 6. The Warrior and Druid values come from the Forever spellbook and talents (wowforevertalents.com) and from player data (see Sources). Spell values and combat rules are checked against wowsims Forever (23 October 2026). Some threat values are not known. Part 6 shows them.

## Summary

- With all proposals, the Paladin has 94–105% of the Druid threat and 86–93% of the Warrior threat.
- With Consecration on cooldown, the Paladin has 108–124% of the Druid threat. But the mana then lasts about 1 min at fresh level 60 and 6.5 min in Naxxramas (see Analysis, Mana).
- Without the proposals, the Paladin has less threat than the other two tanks at all gear levels.
- Holy Shield (C-P9: damage increases with block value) is necessary. Without Holy Shield (C-P9), the Paladin is further below the other tanks in raids (74% of the Druid threat in Naxxramas).
- Judgement of the Crusader gives the Paladin tank about +55 TPS. Judgement of Fury does not remove it. With Personal Judgement of the Crusader (C2), the tank keeps it. This is also true when the raid needs the Judgement of the tank for Light or Wisdom.
- If the gear progression is flatter, the Paladin has 90–95% of the Druid threat in Naxxramas.
- Holy Strike Seal trigger (C1: Holy Strike triggers Seal of Fury) gives about +14 TPS more. The tables do not include it.

## 1. Result with the same gear

Conditions:

- All tanks have pre-raid gear.
- The Paladin has 200 spell power and 60 block value. The Paladin uses the talents of the 8/35/8 tank (see Analysis, Builds, part 3). PB1 has 2% more threat.
- The boss has 5 Sunder Armor and Faerie Fire.

| Boss hit before armor | Warrior | Druid | Paladin, beta | Paladin, all proposals | Paladin, all proposals + Consecration |
| --- | --- | --- | --- | --- | --- |
| 3,000 | 595 | 540 | 410 | 555 | 645 |
| 4,500 | 670 | 620 | 410 | 555 | 645 |
| 6,000 | 695 | 645 | 410 | 555 | 645 |

All values are approximate.

- Warrior and Druid receive rage when the boss hits them. Thus, their threat increases when the boss hits harder. Paladin threat does not change with boss damage.
- At 4,500 and 6,000, the Warrior uses Heroic Strike on all swings. Thus, its threat increases more slowly.
- If Shield Slam has a ×2.25 threat multiplier (not tested), add 140 TPS to the Warrior.
- Both Paladin columns include Judgement of the Crusader. Judgement of Fury does not remove it. In the beta, a raid can need the tank's only Judgement for Light or Wisdom. Then the beta Paladin has no Crusader and about 360 TPS. With Personal Judgement of the Crusader (C2), the tank keeps Crusader in all cases.
- Without Holy Shield (C-P9), the proposed Paladin has about 470 TPS (565 TPS with Consecration).
- If the boss has no armor debuffs (4,500 hits): Warrior 540 TPS, Druid 470 TPS, Paladin 530 TPS. Most Paladin threat is Holy damage. Armor does not decrease Holy damage.
- Retribution Aura gives the Paladin about +25 TPS. But the Paladin then does not have Devotion Aura (735 armor).

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
| Fresh level 60 | 565 | 465 | 395 (85%) | 450 (97%) | **485 (105%)** | 580 |
| Pre-raid best in slot | 625 | 560 | 425 (76%) | 490 (87%) | **570 (102%)** | 665 |
| Molten Core | 710 | 670 | 460 (69%) | 525 (79%) | **635 (95%)** | 735 |
| Blackwing Lair | 770 | 745 | 495 (67%) | 570 (76%) | **705 (95%)** | 810 |
| Naxxramas | 835 | 825 | 530 (64%) | 605 (74%) | **780 (94%)** | 885 |

- All Paladin columns include Judgement of the Crusader. Without it (a raid that needs the beta tank's Judgement for Light or Wisdom), subtract about 50 TPS from the beta column.
- With all proposals, the Paladin has 94–105% of the Druid threat at all tiers. With Consecration on cooldown, it has 108–124%. But Consecration costs 565 mana each 8 sec (see Analysis, Mana).
- Without Holy Shield (C-P9), the Paladin is further below the Druid: 97% at fresh level 60, 74% in Naxxramas. The Warrior and the Druid receive more Attack Power and more rage. The Paladin receives only spell power.
- The beta Paladin is behind at all tiers: 85% of the Druid at fresh level 60, and 64% in Naxxramas.
- Shield Specialization gives 4% of maximum mana. Thus, more mana gives more mana return. Without Consecration, the tank receives about +4 mana per sec at fresh level 60 and about +30 mana per sec in Naxxramas (see Analysis, Mana).

## 3. Result with flatter gear

Blizzard said that it wants flatter gear progression. This is an intention, not a promise. This part shows the result if the gear increases more slowly.

Model:

- Fresh level 60 and pre-raid are the same as in part 2.
- From Molten Core, the gear increases at half the rate of part 2. Block value is 70, 80 and 92 (not 80, 100 and 125).
- Two cases for boss damage: boss hits as in part 2, or boss hits that also increase at half the rate (4,000, 4,750 and 5,750 before armor).

Paladin with all proposals. The first value is the percentage of the Druid TPS. The value in brackets is the percentage of the Warrior TPS.

| Tier | Gear as in part 2 | Flatter gear, boss hits as in part 2 | Flatter gear, flatter boss hits |
| --- | --- | --- | --- |
| Fresh level 60 | 105% (86%) | 105% (86%) | 105% (86%) |
| Pre-raid best in slot | 102% (91%) | 102% (91%) | 102% (91%) |
| Molten Core | 95% (90%) | 94% (87%) | 98% (90%) |
| Blackwing Lair | 95% (92%) | 92% (87%) | 95% (90%) |
| Naxxramas | 94% (93%) | 90% (86%) | 95% (90%) |
| Naxxramas, without Holy Shield (C-P9) | 74% | 73% | 77% |

- With Holy Shield (C-P9) at 200%, the Paladin has 90–105% of the Druid threat in all three cases. At 300%, it has 98–105% of the Druid threat in Naxxramas. At 150%, it has 86–90%.
- Without Holy Shield (C-P9), the Paladin is behind in all cases. Thus, Holy Shield (C-P9) is more important with flatter gear.
- The weakest case is flatter gear with boss hits that continue to increase. The Warrior and the Druid still receive more rage from larger hits. Monitor the block value of each gear tier.
- Mana: if maximum mana increases more slowly (3,650, 3,900 and 4,150), the tank receives +14, +17 and +20 mana per sec without Consecration. Shield Specialization (C-P8) is more important.
- Defense: if gear gives Defense more slowly, tanks reach 440 Defense later. The boss can then make critical hits for a longer time. Redoubt (C-P1) and the Reckoning critical-hit trigger stay useful for a longer time.
- Personal Judgement of the Crusader (C2): the +161 bonus from Judgement of the Crusader is more important when gear gives less spell power.
- The PvP burst check (Reckoning, C-P6) uses fresh and pre-raid stats. It stays correct for a longer time.

## 4. Why the Paladin is different

- **No stance or form multiplier.** Righteous Fury (×1.9) is for Holy damage only. Paladin auto attacks and Reckoning attacks have ×1.0. Defensive Stance gives ×1.495 to all Warrior damage. Bear Form gives ×1.5 to all Druid damage.
- **No strong attack with a short cooldown.**

| Attack | Total threat multiplier | Cooldown |
| --- | --- | --- |
| Primal Bite (Druid, new in Forever) | ×4.5 (×3, Bear Form ×1.5) | 6 sec |
| Revenge (Warrior) | ×3.4 (×2.25, Defensive Stance and Defiance ×1.495) | 5 sec |
| Maul (Druid) | ×2.6 (×1.75, Bear Form ×1.5) | Each swing |
| Holy Strike with Iron Creed 5/5 (Paladin) | ×2.4 (Righteous Fury ×1.9, Iron Creed ×1.25) | 10 sec |
| Paladin auto attacks and Reckoning attacks | ×1.0 | — |

- **Paladin advantages.** Boss armor and rage do not change Paladin threat. Consecration and Holy Shield hit all attackers. Thus, the Paladin is strongest against groups of enemies.

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
- Revenge rank 6: 138–168 damage + 28% of Attack Power, +60% (Improved Revenge). Threat = damage × 2.25 (player sheet, see Sources).
- Shield Slam rank 4: 640–670 damage + block value. Threat = damage. The real multiplier is not known.
- Heroic Strike rank 9: +157 damage. Threat = damage + 152.4 (wowsims Forever, measured).
- 5 rage for each block, dodge and parry (Shield Specialization, Master of Defense). Each rage point gives 5 threat (player sheet, see Sources).
- Sunder Armor: 206 threat + 5% of Attack Power (rank 5, game files), before Defensive Stance.
- Bloodrage: 10 rage + 10 rage over 10 sec, 1 min cooldown. Its rage gives threat: 50 + 50 (player data).
- Shield Block on cooldown: 10 rage each 5 sec. It blocks about 80% of the swings. 3% of the swings are crushing blows (see Crushing blows).
- Rage costs with talents: Shield Slam 17, Revenge 2, Sunder Armor 9, Heroic Strike 9.
- Sunder Armor fills the free global cooldowns. Heroic Strike uses the extra rage.

**Druid**

- Talents (assumed): Ferocity 5/5, Savage Fury 2/2, Feral Instinct 3/3, Sharpened Claws 2/2, Predatory Strikes 3/3, Blood Frenzy 2/2, Natural Reaction 5/5.
- Threat: Bear Form ×1.5, Maul ×1.75, Primal Bite ×3, Swipe ×1.75 (player data).
- Damage for each swing: weapon damage per sec + Attack Power ÷ 14, with a 2.5 sec swing (player data). Predatory Strikes gives +90 Attack Power.
- Maul rank 7: +128 damage, +10% (Savage Fury), 10 rage.
- Primal Bite rank 4: weapon damage + 77, 15 rage, 6 sec cooldown.
- Swipe rank 5: 83 damage + 3% of Attack Power, +10% (Savage Fury), +30% (Feral Instinct), 15 rage.
- Faerie Fire in Bear Form: 120 threat (2 × level), 6 sec cooldown.
- Blood Frenzy: 5 rage for each critical hit. Natural Reaction: 5 rage for each dodge.
- Enrage: 10 rage + 20 rage over 10 sec, 1 min cooldown. Its rage gives threat: 50 + 100. The −27% base armor of Enrage is not in the model.
- No shield: 15% of the swings are crushing blows (see Crushing blows).
- Primal Bite and Faerie Fire are used on cooldown. Maul uses the extra rage. Swipe fills the free global cooldowns.
- Lacerate is not in the model. Its threat is not known.

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
