# Threat

This section compares the threat of the three tanks: Warrior, Druid and Paladin. The unit is threat per second (TPS) on one boss. The tanks are level 60. The boss is level 63.

The values come from a model. The model uses beta tests and developer notes. It is not a combat log. The inputs are in part 6. The spell data from beta tests is in Beta test results. The values that are not known are in Open questions.

The script models/threat/run_tables.py calculates all values of this section from the inputs of part 6. The Warrior and Druid values come from the Forever spellbook and talents (wowforevertalents.com) and from player data (see Sources). Some threat values are not known. Part 6 shows them.

## Summary

- With all proposals, the Paladin has 85–92% of the Druid threat and 77–86% of the Warrior threat.
- With Consecration on cooldown, the Paladin has 100–114% of the Druid threat. But the mana then lasts about 1 min at fresh level 60 and 6.5 min in Naxxramas (see Analysis, Mana).
- Without the proposals, the Paladin has less threat than the other two tanks at all gear levels.
- C14 (Holy Shield damage increases with block value) is necessary. Without C14, the Paladin falls further behind in raids (67% of the Druid threat in Naxxramas).
- Judgement of the Crusader gives the Paladin tank about +55 TPS. Judgement of Fury does not remove it. C18 lets the tank keep it when the raid also needs the Judgement of the tank for Light or Wisdom.
- If the gear progression is flatter, the Paladin has 81–85% of the Druid threat in Naxxramas.
- C16 (Holy Strike triggers Seal of Fury) gives about +8 TPS more. The tables do not include it.

## 1. Result with the same gear

Conditions:

- All tanks have pre-raid gear.
- The Paladin has 200 spell power and 60 block value. The Paladin uses the talents of PB1 (see Analysis, Builds).
- The boss has 5 Sunder Armor and Faerie Fire.

| Boss hit before armor | Warrior | Druid | Paladin, beta | Paladin, all proposals | Paladin, all proposals + Consecration |
| --- | --- | --- | --- | --- | --- |
| 3,000 | 630 | 575 | 395 | 535 | 640 |
| 4,500 | 710 | 665 | 395 | 535 | 640 |
| 6,000 | 730 | 700 | 395 | 535 | 640 |

All values are approximate.

- Warrior and Druid receive rage when the boss hits them. Thus, their threat increases when the boss hits harder. Paladin threat does not change with boss damage.
- At 4,500 and 6,000, the Warrior uses Heroic Strike on all swings. Thus, its threat increases more slowly.
- If Shield Slam has a ×2.25 threat multiplier (not tested), add 155 TPS to the Warrior.
- Both Paladin columns include Judgement of the Crusader. Judgement of Fury does not remove it. In the beta, a raid can need the tank's only Judgement for Light or Wisdom. Then the beta Paladin has no Crusader and about 340 TPS. With C18, the tank keeps Crusader in all cases.
- Without C14, the proposed Paladin has about 450 TPS (555 TPS with Consecration).
- If the boss has no armor debuffs (4,500 hits): Warrior 565 TPS, Druid 500 TPS, Paladin 500 TPS. Most Paladin threat is Holy damage. Armor does not decrease Holy damage.
- Retribution Aura gives the Paladin about +25 TPS. But the Paladin then does not have Devotion Aura (735 armor).

**Threat sources of the proposed Paladin (200 spell power, 60 block value)**

| Source | TPS |
| --- | --- |
| Holy Shield blocks: 178 from the base damage, 82 from block value (C14) | 260 |
| Judgement of Fury: one each 10 sec, plus one Swift Judgement each minute | 78 |
| Holy Strike with Iron Creed | 60 |
| Auto attacks | 56 |
| Seal of Fury (auto attacks and Reckoning attacks) | 43 |
| Reckoning extra attacks (C11) | 36 |
| **Total** | **533** |

The proposals give the Paladin about +140 TPS more than the beta:

- C14 (block value on Holy Shield): about +80 TPS.
- C6 (more Holy Shield blocks) and C11 (Reckoning): about +60 TPS.
- C18 (Judgement of the Crusader for each Paladin): +50 TPS more when the raid needs the tank's Judgement for Light or Wisdom (beta Paladin).

**Spell power**

Each +100 spell power gives about +35 TPS.

| Spell power | 100 | 150 | 200 | 250 | 300 | 350 |
| --- | --- | --- | --- | --- | --- | --- |
| Paladin, all proposals (60 block value) | 500 | 515 | 535 | 550 | 565 | 585 |

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

| Tier | Warrior | Druid | Paladin, beta | Paladin, proposals without C14 | **Paladin, all proposals** | All proposals + Consecration |
| --- | --- | --- | --- | --- | --- | --- |
| Fresh level 60 | 590 | 495 | 370 (75%) | 420 (85%) | **460 (92%)** | 565 |
| Pre-raid best in slot | 660 | 600 | 410 (68%) | 470 (78%) | **550 (92%)** | 660 |
| Molten Core | 750 | 720 | 445 (62%) | 510 (71%) | **620 (86%)** | 730 |
| Blackwing Lair | 815 | 810 | 485 (60%) | 555 (68%) | **690 (85%)** | 810 |
| Naxxramas | 885 | 890 | 515 (58%) | 595 (67%) | **765 (86%)** | 890 |

- All Paladin columns include Judgement of the Crusader. Without it (a raid that needs the beta tank's Judgement for Light or Wisdom), subtract about 50 TPS from the beta column.
- With all proposals, the Paladin has 85–92% of the Druid threat at all tiers. With Consecration on cooldown, it has 100–114%. But Consecration costs 565 mana each 8 sec (see Analysis, Mana).
- Without C14, the Paladin falls further behind the Druid: 85% at fresh level 60, 67% in Naxxramas. The Warrior and the Druid receive more Attack Power and more rage. The Paladin receives only spell power.
- The beta Paladin is behind at all tiers: 75% of the Druid at fresh level 60, and 58% in Naxxramas.
- Shield Specialization gives 4% of maximum mana. Thus, more mana gives more mana return. Tanking without Consecration gives about +4 mana per sec at fresh level 60 and about +30 mana per sec in Naxxramas (see Analysis, Mana).

## 3. Result with flatter gear

Blizzard said that it wants flatter gear progression. This is an intention, not a promise. This part shows the result if the gear increases more slowly.

Model:

- Fresh level 60 and pre-raid are the same as in part 2.
- From Molten Core, the gear increases at half the rate of part 2. Block value is 70, 80 and 92 (not 80, 100 and 125).
- Two cases for boss damage: boss hits as in part 2, or boss hits that also increase at half the rate (4,000, 4,750 and 5,750 before armor).

Paladin with all proposals. The first value is the percentage of the Druid TPS. The value in brackets is the percentage of the Warrior TPS.

| Tier | Gear as in part 2 | Flatter gear, boss hits as in part 2 | Flatter gear, flatter boss hits |
| --- | --- | --- | --- |
| Fresh level 60 | 92% (77%) | 92% (77%) | 92% (77%) |
| Pre-raid best in slot | 92% (84%) | 92% (84%) | 92% (84%) |
| Molten Core | 86% (83%) | 85% (80%) | 89% (83%) |
| Blackwing Lair | 85% (85%) | 83% (80%) | 85% (82%) |
| Naxxramas | 86% (86%) | 81% (80%) | 85% (83%) |
| Naxxramas, without C14 | 67% | 66% | 69% |

- With C14 at 200%, the Paladin has 81–92% of the Druid threat in all three cases. At 300%, it has 89–95% of the Druid threat in Naxxramas. At 150%, it has 77–81%.
- Without C14, the Paladin falls behind in all cases. Thus, C14 is more important with flatter gear.
- The weakest case is flatter gear with boss hits that continue to increase. The Warrior and the Druid still receive more rage from larger hits. Monitor the block value of each gear tier.
- Mana: if maximum mana increases more slowly (3,650, 3,900 and 4,150), tanking without Consecration gives +14, +17 and +20 mana per sec. C13 is more important.
- Defense: if gear gives Defense more slowly, tanks reach 440 Defense later. The boss can then make critical hits for a longer time. C6 and the Reckoning critical-hit trigger stay useful for a longer time.
- C18: the +161 bonus from Judgement of the Crusader is more important when gear gives less spell power.
- The PvP burst check (C11) uses fresh and pre-raid stats. It stays correct for a longer time.

## 4. Why the Paladin is different

- **No stance or form multiplier.** Righteous Fury (×1.9) is for Holy damage only. Paladin auto attacks and Reckoning attacks get ×1.0. Defensive Stance gives ×1.495 to all Warrior damage. Bear Form gives ×1.5 to all Druid damage.
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

Use these steps only if tests show that Protection threat is too low with C14. They are not proposals now.

| Step | Effect |
| --- | --- |
| Iron Creed: Holy Strike threat +20/40/60/80/100% (not +5/10/15/20/25%) | +30 to +50 TPS at each tier. Threat only, no PvP effect |
| A shield attack in Protection row 4: 6 sec cooldown, weapon damage + 100 Holy damage, ×2 threat | +95 to +155 TPS. Adds a button. The new Druid attack Primal Bite is the precedent |

Other options were examined and rejected. See Withdrawn ideas.

## 6. Inputs

**All tanks**

- Level 60, 500 Attack Power, 3% hit.
- One-handed weapon: 45 damage per sec, 2.7 sec speed. Druid: weapon damage per sec + Attack Power ÷ 14, with a 2.5 sec swing (about 220 damage).
- Critical hit chance: 6%. Druid: 12% (Sharpened Claws).

**Attacks against a level 63 boss (from the front)**

- 6% miss, 6.5% dodge, 14% parry.
- 40% of auto attacks are glancing blows (−35% damage).

**Boss**

- 3,731 armor. 976 armor after 5 Sunder Armor (450 each) and Faerie Fire.
- One swing each 2 sec. 64% of the swings hit the tank.

**Rage (normalized in Forever)**

- Auto attack: 3.46 rage × weapon speed. ×1.3 for two-handed weapons and Bear Form. ×2 for a critical hit. No rage for a miss, dodge or parry.
- Damage taken: 2.5 × 0.6 × boss hit before armor ÷ 243.6 (level 63). ×1.5 for a crushing blow.
- Heroic Strike and Maul hits give no rage (assumed, as in Classic).
- Each rage point gives 5 threat.

**Warrior**

- Talents (assumed): Defiance 3/3, Bastion 5/5, Improved Revenge 3/3, Shield Specialization 5/5, Master of Defense 2/2, Improved Sunder Armor 3/3, Focused Rage 3/3, Improved Heroic Strike 3/3.
- Defensive Stance: ×1.3 threat, −10% damage. Defiance 3/3: ×1.15 threat with a shield. Bastion 5/5: +10% damage with a shield.
- Revenge rank 6: 138–168 damage + 28% of Attack Power, +60% (Improved Revenge). Threat = damage × 2.25 (player sheet, see Sources).
- Shield Slam rank 4: 640–670 damage + block value. Threat = damage. The real multiplier is not known.
- Heroic Strike rank 9: +157 damage. Threat = damage + about 145. The Forever threat bonus is not known (Classic value).
- 5 rage for each block, dodge and parry (Shield Specialization, Master of Defense). Each rage point gives 5 threat (player sheet, see Sources).
- Sunder Armor: 199 threat + 5% of Attack Power (rank 5), before Defensive Stance. The player sheet gives rank 1 (35) and rank 2 (76). Rank 5 uses +41 for each rank.
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
- No shield: 15% of the swings are crushing blows (see Crushing blows).
- Primal Bite and Faerie Fire are used on cooldown. Maul uses the extra rage. Swipe fills the free global cooldowns.
- Lacerate is not in the model. Its threat is not known.

**Paladin**

- Righteous Fury: ×1.9 threat for Holy damage only.
- One-Handed Weapon Specialization: +10% damage (not for Consecration or Retribution Aura).
- Improved Seals: +15% (8-point dip into Holy).
- Spell power coefficients: Seal of Fury 10% for each hit, Judgement of Fury 42.9%, Holy Strike 21.45%, Holy Shield 10.7% for each block (assumed: 42.9% divided by 4 charges), Consecration 33.6% (15% of ticks miss).
- Holy Shield: 3 blocks each 10 sec (beta: 2.5). Redoubt 5/5 gives about 1 of these blocks.
- Reckoning: 2.0 extra attacks each 10 sec (beta: 1.0). With C11, Holy Strike releases them. Thus, they are not glancing blows.
- Holy Strike: 50% of normalized weapon damage (2.4 sec) + 81–105 Holy damage. Righteous Fury multiplies all of its threat (beta test).
- Judgement of Fury: 153–167 Holy damage. Judgements and Holy Strike use the melee hit table.
- Seal of Fury cannot miss. Its critical hit uses a separate roll.
- Consecration rank 5: 384 damage in 8 sec, one cast each 8 sec. Critical hit ×1.5 with C15.
