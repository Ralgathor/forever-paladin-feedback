# Threat

This section compares the threat of the three tanks: Warrior, Druid and Paladin. The unit is threat per second (TPS) on one boss. The tanks are level 60. The boss is level 63.

The values come from a model. The model uses beta tests and developer notes. It is not a combat log. The inputs are in part 6. The spell data from beta tests is in Beta test results. The values that are not known are in Open questions.

## Summary

- With all proposals, the Paladin has about the same threat as the Druid and the Warrior.
- Without the proposals, the Paladin has less threat than the other two tanks at all gear levels.
- C14 (Holy Shield damage increases with block value) is necessary. Without C14, the Paladin falls behind in raids.
- Judgement of the Crusader gives the Paladin tank about +50 TPS. Judgement of Fury does not remove it. C18 lets the tank keep it when the raid also needs the Judgement of the tank for Light or Wisdom.
- If the gear progression is flatter, C14 at 200% is still correct.
- C16 (Holy Strike triggers Seal of Fury) gives about +10 TPS more. The tables do not include it.

## 1. Result with the same gear

Conditions:

- All tanks have pre-raid gear.
- The Paladin has 200 spell power and 60 block value.
- The boss has 5 Sunder Armor and Faerie Fire.

| Boss hit before armor | Warrior | Druid | Paladin, beta | Paladin, all proposals | Paladin, all proposals + Consecration |
| --- | --- | --- | --- | --- | --- |
| 3,000 | 525 | 520 | 400 | 540 | 625 |
| 4,500 | 600 | 585 | 400 | 540 | 625 |
| 6,000 | 660 | 650 | 400 | 540 | 625 |

All values are approximate.

- Warrior and Druid get rage when the boss hits them. Thus, their threat increases when the boss hits harder. Paladin threat does not change with boss damage.
- If Shield Slam has a ×2.25 threat multiplier (not tested), add 135 TPS to the Warrior.
- Both Paladin columns include Judgement of the Crusader. Judgement of Fury does not remove it. In the beta, a raid can need the tank's only Judgement for Light or Wisdom. Then the beta Paladin has no Crusader and about 355 TPS. With C18, the tank keeps Crusader in all cases.
- Without C14, the proposed Paladin has about 455 TPS (545 TPS with Consecration).
- If the boss has no armor debuffs (4,500 hits): Warrior 470 TPS, Druid 425 TPS, Paladin 515 TPS. Most Paladin threat is Holy damage. Armor does not decrease Holy damage.
- Retribution Aura gives the Paladin about +25 TPS. But the Paladin then does not have Devotion Aura (735 armor).

**Threat sources of the proposed Paladin (200 spell power, 60 block value)**

| Source | TPS |
| --- | --- |
| Holy Shield blocks: 180 from the base damage, 80 from block value (C14) | 260 |
| Judgement of Fury: one each 10 sec, plus one Swift Judgement each minute | 70 |
| Holy Strike with Iron Creed | 57 |
| Reckoning extra attacks (C11) | 53 |
| Seal of Fury | 49 |
| Auto attacks | 49 |
| **Total** | **540** |

The proposals give the Paladin about +140 TPS more than the beta:

- C14 (block value on Holy Shield): about +80 TPS.
- C6 (more Holy Shield blocks) and C11 (Reckoning): about +60 TPS.
- C18 (Judgement of the Crusader for each Paladin): +50 TPS more when the raid needs the tank's Judgement for Light or Wisdom.

**Spell power**

Each +100 spell power gives about +32 TPS.

| Spell power | 100 | 150 | 200 | 250 | 300 | 350 |
| --- | --- | --- | --- | --- | --- | --- |
| Paladin, all proposals (60 block value) | 505 | 525 | 540 | 555 | 570 | 585 |

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
| Fresh level 60 | 490 | 405 | 380 (94%) | 430 (107%) | **470 (116%)** | 555 |
| Pre-raid best in slot | 545 | 455 | 415 (91%) | 470 (104%) | **555 (122%)** | 645 |
| Molten Core | 640 | 530 | 450 (86%) | 515 (97%) | **625 (118%)** | 720 |
| Blackwing Lair | 755 | 635 | 495 (78%) | 565 (89%) | **700 (111%)** | 800 |
| Naxxramas | 815 | 760 | 535 (70%) | 605 (80%) | **775 (102%)** | 880 |

- All Paladin columns include Judgement of the Crusader. Without it (a raid that needs the beta tank's Judgement for Light or Wisdom), subtract about 50 TPS from the beta column.
- With all proposals, the Paladin is between the Druid and the Warrior at all tiers.
- Without C14, the Paladin falls behind from Molten Core. The Warrior and the Druid get more Attack Power and more rage. The Paladin gets only spell power.
- The beta Paladin is behind at all tiers: 94% of the Druid at fresh level 60, and 70% in Naxxramas.
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
| Fresh level 60 | 116% (96%) | 116% (96%) | 116% (96%) |
| Pre-raid best in slot | 122% (101%) | 122% (101%) | 122% (101%) |
| Molten Core | 118% (97%) | 114% (95%) | 120% (99%) |
| Blackwing Lair | 111% (93%) | 104% (88%) | 115% (95%) |
| Naxxramas | 102% (95%) | 94% (89%) | 110% (91%) |
| Naxxramas, without C14 | 80% | 76% | 89% |

- C14 at 200% is correct for all three cases. At 150%, the Paladin falls to 89% of the Druid if boss hits continue to increase. At 300%, the Paladin has more threat than the Warrior if all values are flat.
- Without C14, the Paladin falls behind in all cases. Thus, C14 is more important with flatter gear.
- The weakest case is flatter gear with boss hits that continue to increase. The Warrior and the Druid still get more rage from bigger hits. Monitor the block value of each gear tier.
- Mana: if maximum mana increases more slowly (3,650, 3,900 and 4,150), tanking without Consecration gives +14, +17 and +20 mana per sec. C13 is more important.
- Defense: if gear gives Defense more slowly, tanks get to 440 Defense later. The boss can then make critical hits for a longer time. C6 and the Reckoning critical-hit trigger stay useful for a longer time.
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
| A shield attack in Protection row 4: 6 sec cooldown, weapon damage + 100 Holy damage, ×2 threat | +170 to +200 TPS. Adds a button. The new Druid attack Primal Bite is the precedent |

## 6. Inputs

**All tanks**

- Level 60, 500 Attack Power, 3% hit.
- One-handed weapon: 45 damage per sec, 2.7 sec speed. Druid: 260 damage for each swing, 2.5 sec.
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

- Defensive Stance: ×1.3 threat, −10% damage. Defiance 3/3: ×1.15 threat.
- One-Handed Weapon Specialization: +10% damage. Improved Revenge 3/3.
- Revenge: threat = damage × 2.25. Damage includes 28% of Attack Power.
- Shield Slam: 640–670 damage + 50 block value. Threat = damage.
- Heroic Strike rank 9: threat = damage + about 145.
- 5 rage for each block, dodge and parry.
- Extra rage goes to Sunder Armor (about 225 threat before Defensive Stance).

**Druid**

- Bear Form ×1.5, Maul ×1.75, Primal Bite ×3, Swipe ×1.75.
- Ferocity 5/5, Savage Fury 2/2, Feral Instinct 3/3.
- Lacerate and Faerie Fire are not in the model.

**Paladin**

- Righteous Fury: ×1.9 threat for Holy damage only.
- One-Handed Weapon Specialization: +10% damage (not for Consecration or Retribution Aura).
- Improved Seals: +15% (8-point dip into Holy).
- Spell power coefficients: Seal of Fury 10% for each hit, Judgement of Fury 42.9%, Holy Strike 21.45%, Holy Shield 10.7% for each block (assumed: 42.9% divided by 4 charges), Consecration 33.6% (15% of ticks miss).
- Holy Shield: 3 blocks each 10 sec (beta: 2.5).
- Reckoning: 2.0 extra attacks each 10 sec (beta: 1.0).
