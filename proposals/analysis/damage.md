# Damage

This section compares the single-target damage of Retribution with the other damage classes. The unit is damage per second (DPS) on one level 63 boss. The values come from a model, not from combat logs.

The script models/damage/run_tables.py calculates all values of this section. Fury, Arms and Combat Rogue use the Forever spellbook and talents (wowforevertalents.com) and the Forever rage formula (see Threat, part 6). No value is fitted to the first calculation.

## Summary

- With all proposals, Retribution is about equal to Fury Warrior at fresh level 60. It is 100% of Fury and 103% of the average of the pure damage classes.
- The hybrid target is 95% of the pure damage classes. Players report it from developer comments: hybrids do about 5% less damage than pure damage classes. In the beta, Retribution is 93%.
- C16 gives almost all of the increase. C17 gives the same damage as the beta Seal swap, but the mana lasts for the full fight.
- Retribution increases less with gear than Fury. In Naxxramas, it is about 93% of Fury (94% with flatter gear). No talent change closes this gap (part 6).
- Fury increases more with gear than the other classes. Against the pure average, Retribution goes from 103% at fresh level 60 to about 95% in Naxxramas. The hybrid target is 95%.
- Judgement of the Crusader gives Retribution about +10% DPS at fresh level 60. C18 makes this possible for each Paladin.

## 1. Build and gear

- **Build.** 12/7/32: v2p00032030200002-032000000000002-0325531001330321 in the calculator (RB2).
  - Holy 12: Improved Seals 3/3, Unyielding Faith 2/2, Reverence 3/3, Infusion of Light 2/2, Consecrated Ground 2/2.
  - Protection 7: Precision 3/3, Guardian's Favor 2/2, Holy Conduit 2/2 (C8).
  - Retribution 32: Conviction 5/5, Benediction 3/3 (C21), Improved Judgement 2/2, Vindication 5/5 (C8), Sanctified Judgement 3/3, Seal of Command, Two-Handed Weapon Specialization 3/3, Sacred Arbiter, Vengeance 3/3, Champion of the Light 3/3, Instrument of Law 2/2, Twist of Light.
- **C8 and the values.** The tables use the build of version 1, with Divine Strength 5/5 and no Vindication. C8 removes Divine Strength (about −7 DPS) and adds Vindication 5/5 (+5% Attack Power, about +7 DPS with full uptime). The net change is less than 0.5%. Thus, the tables keep their values.
- **Gear.** A real fresh level 60 profile: crafted items, dungeon items and quest rewards. Without talents and buffs: 283 Strength, 74 Agility, 770 Attack Power, 5.9% critical hit, 5% hit, 254 spell damage, 87 Intellect and 2,537 mana.
- **Weapon.** Stormcarver (Blacksmithing, item level 63): 155–233 damage, 3.6 sec, +32 spell damage.
- **With talents and raid buffs.** 1,244 Attack Power, 319 spell damage (Champion of the Light gives 65), 8% hit and 2,866 mana.

## 2. Model

- **Raid buffs.** Blessing of Kings, Blessing of Might (133), Battle Shout (193), Mark of the Wild (+12 to all stats) and Blessing of Wisdom (8 mana per sec). No consumables. No Judgement of the Crusader (see part 7).
- **Boss.** Level 63. 976 armor after 5 Sunder Armor and Faerie Fire. You attack from behind: no parry and no block.
- **Hit table.** 9% miss before hit (8%, and the first 1% of hit has no effect). 6.5% dodge. 40% of auto attacks are glancing blows (−35% damage).
- **Critical hit against the boss.** −4.8% for auto attacks and −3% for other attacks (Classic 1.12 rule). A critical hit does ×2 damage, and ×1.5 for spells. The spell hit cap is 18%.
- **Seals and Judgements** use the melee hit table. Armor does not decrease Holy damage.
- **Seal of Command.** 7 procs each minute: a 42% chance for each hit with a 3.6 sec weapon. Each proc does 70% of weapon damage + 20.3% of spell damage (29% × 70%). With Improved Seals, this is 80.5% of weapon damage + 23.3% of spell damage.
- **Seal of Righteousness.** 67.5 + 12% of spell damage for each hit. The base part (67.5) is for a 3.6 sec weapon, from the range in the tooltip. Weapon speed does not change the spell damage part (see Beta test results, Spells).
- **Judgement.** One each 8 sec (Improved Judgement 2/2): 186.5 + 42.9% of spell damage.
- **Holy Strike.** One each 10 sec: 50% of normalized weapon damage (3.3 sec) + 93 + 21.45% of spell damage. All the damage is Holy damage.
- **Hammer of Wrath.** One each 6 sec in the last 20% of the fight. Instant (Instrument of Law): 498 + 42.9% of spell damage.
- **Multipliers.** Two-Handed Weapon Specialization: ×1.06 (melee attacks, Seals, Judgements and Holy Strike). Improved Seals: ×1.15 (Seals and Judgements). They multiply together (×1.219).
- **Vengeance.** A simulation of the stacks (3% each, 3 stacks, 30 sec). The average is +5%.
- **Twist of Light (C17).** One Seal change each 10 sec. Thus, Seal of Command and Seal of Righteousness are both active all the time.
- **Fight.** 2 min. A 5 min fight gives 1% more (Vengeance).
- **Not in the model.** Exorcism, Consecration and Retribution Aura (see part 8).

## 3. Damage sources

All proposals (C16 as in this document), raid buffs, 2 min fight:

| Source | DPS | Share |
| --- | --- | --- |
| Auto attacks | 115 | 31% |
| Seal of Command | 80 | 22% |
| Holy Strike | 55 | 15% |
| Judgement | 52 | 14% |
| Seal of Righteousness (Echo) | 47 | 13% |
| Hammer of Wrath (last 20% of the fight) | 22 | 6% |
| **Total** | **371** |  |

- About 70% of the damage is Holy damage. Armor does not decrease it.
- The global cooldown is active 52% of the time. Thus, you have time for Exorcism or Consecration.
- Mana: −2.6 mana per sec with Blessing of Wisdom. The mana lasts about 18 min. A melee player gets Blessing of Wisdom only with 3 Paladins in the raid (see The problem with Blessings). Without it: −10.6 mana per sec, and the mana lasts about 4.5 min.

## 4. Proposals against the beta

Same build and gear, raid buffs, 2 min fight. The beta build has the same damage talents in their beta rows. It has no Reverence.

| Version | DPS | Change | Mana |
| --- | --- | --- | --- |
| Beta: a Seal change before each swing | 337 | — | −39.6 per sec: zero after 72 sec |
| Beta: Seal of Command only, no Seal changes | 302 | −10% | Lasts |
| C16, first version: Holy Strike always triggers Seal of Command, no damage bonus | 380 | +13% | Lasts |
| **C16: Holy Strike triggers your Seal and Echo, Sacred Arbiter as in the beta (+20%)** | **371** | **+10%** | **Lasts** |
| C16: Holy Strike triggers your Seal and Echo, Sacred Arbiter +10% | 367 | +9% | Lasts |
| C16: Holy Strike triggers your Seal and Echo, Sacred Arbiter +0% | 362 | +8% | Lasts |
| C16: only Seal of Command, by chance, Sacred Arbiter +0% | 349 | +4% | Lasts |

- **C16 gives the increase.** Holy Strike gives about 34 DPS more than in the beta. Seal of Command triggers on 42% of Holy Strikes, and Seal of Righteousness triggers on all Holy Strikes.
- **C17 does not add damage.** It gives the damage of the beta Seal swap for the full fight. In the beta, the mana is zero after 72 sec. Then the Paladin can use only Seal of Command (302 DPS).
- **The C16 value is a choice.** The first version (+13%) puts Retribution above Fury Warrior (see part 5). The version in this document has one rule for all melee attacks and keeps Sacred Arbiter as in the beta. It is 2% less.
- **Sacred Arbiter at +10% changes little.** It gives only 4 DPS (1%) less. From Molten Core, Retribution is already below Fury (part 6).

## 5. Comparison with the other damage classes

The values of the other classes come from [MythicSim](https://mythicsim.com/wow-forever/tier-list): wowsims Forever, beta client 1.60.1.70425, simulated on 22 October 2026 (engine a667dce, 10,000 iterations, no trinkets). It uses curated dungeon and crafted gear, full raid buffs, debuffs and consumables, and a 2 min fight against one level 63 boss. Its Retribution value (847) uses the beta talents. This document uses only its ratios. The Retribution values with the proposals are 847 × the change in part 4.

The pure average is the best spec of each pure damage class: Warrior 929, Rogue 702, Hunter 1,175, Mage 860 and Warlock 879. The average is 909.

| Spec | DPS | Against the pure average (909) |
| --- | --- | --- |
| Survival Hunter (melee weaving) | 1,175 | 129% |
| Retribution, C16 first version | About 955 | 105% |
| **Retribution, all proposals** | **About 933** | **103%** |
| Fury Warrior | 929 | 102% |
| Demonology Warlock | 879 | 97% |
| Fire Mage | 860 | 95% |
| Retribution, beta | 847 | 93% |
| Arms Warrior | 800 | 88% |
| Feral Druid | 794 | 87% |
| Shadow Priest | 771 | 85% |
| Enhancement Shaman | 741 | 82% |
| Combat Rogue | 702 | 77% |
| Balance Druid | 657 | 72% |
| Elemental Shaman | 519 | 57% |

- **The hybrid target is 95% of the pure average.** In the beta, Retribution is 93%.
- **With all proposals, Retribution is 100% of Fury and 103% of the pure average.** Without Combat Rogue (the lowest pure class), the pure average is 961. Retribution is then 97% of it.
- **Retribution is the strongest hybrid** in the beta and with the proposals. In the beta, it is 7% above Feral and 14% above Enhancement.
- **Check with the same gear.** The model also calculates Arms, Fury and Combat Rogue with the gear of part 1 and Forever rage. The beta Retribution is 29% above Arms (MythicSim: 6%). Thus, the model gives too little damage to the Warriors with the same gear. The causes can be the gear (no hit for two weapons), consumables or the rotation. Part 6 uses only the increase with gear.
- **One source only.** The MythicSim page has some errors in its rank order. Its Hunter values use melee weaving. No player has confirmed melee weaving in a raid.
- **No raid gear.** MythicSim has no raid gear tiers. Part 6 uses a model for the increase with gear.

## 6. Gear progression

Retribution increases less with gear than the pure melee classes. Blizzard said that it wants more horizontal gear progression. But each tier still gives more power.

**Model**

- The five gear tiers of Threat, part 2. Each tier gives 17.5% more Strength, Agility, Attack Power, critical hit, spell damage and Intellect from gear. Hit goes from 5% to 9%.
- Weapons follow the Classic steps. Two-handed: 54, 56, 63, 66 and 75 damage per sec. One-handed (main hand and off hand, 2.6 sec): 42 and 40 at fresh level 60, then 47/44, 52/49, 57/54 and 64/60.
- Retribution, Fury (two weapons), Arms and Combat Rogue get the same gear and the same raid buffs.
- Fury: Bloodthirst, Whirlwind, then Heroic Strike with the extra rage, and Execute in the last 20% of the fight. Flurry, Death Wish (one use) and Deep Wounds. Rage: the Forever v2 rules (announced fix): critical hits give +100% rage, and Dual Wield Specialization gives +50% off-hand rage. Bloodthirst and Whirlwind are then on cooldown with all gear.
- Arms: Mortal Strike, Overpower after a dodge, Slam, then Heroic Strike, and Execute in the last 20% of the fight. Deep Wounds.
- Combat Rogue: Sinister Strike, Slice and Dice, and Eviscerate with 5 combo points. Blade Flurry and Adrenaline Rush (one use each). Eviscerate gets 15% of Attack Power (assumed). No poisons.
- Flatter gear: from Molten Core, the gear increases at half the rate, as in Threat, part 3.
- The model uses only the increase of each class from fresh level 60. Retribution starts at 100% of Fury (part 5).
- Two cases for Retribution: plate gear gives more spell damage at each tier, or the spell damage stays at 254.

**DPS increase from fresh level 60 (Classic steps)**

| Tier | Retribution | Retribution, spell damage stays at 254 | Fury | Arms | Combat Rogue |
| --- | --- | --- | --- | --- | --- |
| Fresh level 60 | ×1.00 | ×1.00 | ×1.00 | ×1.00 | ×1.00 |
| Pre-raid best in slot | ×1.11 | ×1.09 | ×1.14 | ×1.11 | ×1.12 |
| Molten Core | ×1.25 | ×1.20 | ×1.30 | ×1.26 | ×1.26 |
| Blackwing Lair | ×1.40 | ×1.31 | ×1.49 | ×1.42 | ×1.42 |
| Naxxramas | ×1.60 | ×1.46 | ×1.73 | ×1.65 | ×1.62 |

**Retribution as a % of Fury**

| Tier | Classic steps | Classic steps, spell damage stays at 254 | Flatter gear | Flatter gear, spell damage stays at 254 |
| --- | --- | --- | --- | --- |
| Fresh level 60 | 100% | 100% | 100% | 100% |
| Pre-raid best in slot | 99% | 96% | 99% | 96% |
| Molten Core | 97% | 93% | 97% | 94% |
| Blackwing Lair | 94% | 88% | 95% | 91% |
| Naxxramas | 93% | 85% | 94% | 88% |

**Why Retribution increases less**

- **About 24% of the damage is fixed base values.** Gear does not change them: Judgement (186.5), Seal of Righteousness (67.5 for each hit), Hammer of Wrath (498) and the +93 of Holy Strike.
- **About 18% comes from spell damage.** The coefficients are small (12–43%). +100 spell damage gives only about +20 DPS.
- **Only about 58% increases with weapon damage and Attack Power:** auto attacks, Seal of Command and the weapon part of Holy Strike. For Fury and Rogue, it is almost 100%.
- **Retribution gets the hit cap at pre-raid** (Precision 3% + 6% from gear). More hit then does nothing. The two-weapon classes start at 28% miss. Each point of hit helps them until Naxxramas.
- **Critical hit helps Fury two times:** more Flurry and two times the rage. For Retribution, it helps only Vengeance.
- **Improved Seals multiplies the fixed bases** by the same 15% as the weapon part. Thus, it does not change the share that increases with gear.
- **Rage in Forever.** In Classic, rage came from the damage. Better gear gave more rage and more Heroic Strikes. Forever gives rage from the weapon speed. This removes most of that effect. With Classic rage, the gap is larger than these tables show.

**The limit of the Retribution increase**

The increase of each damage source from fresh level 60 to Naxxramas (Classic steps):

| Source | Increase |
| --- | --- |
| Seal of Command | ×1.75 |
| Auto attacks | ×1.70 |
| Holy Strike | ×1.60 |
| Judgement | ×1.49 |
| Seal of Righteousness | ×1.36 |
| Hammer of Wrath | ×1.29 |
| **Retribution** | **×1.60** |
| Fury Warrior | ×1.73 |

- The best sources of Retribution increase about ×1.70–1.75. The slow two-handed weapon, the hit cap and no Flurry limit them.
- Thus, a Retribution with no fixed values increases about ×1.75. This is about the Fury increase (101%). The fixed values cause the gap. But a talent change cannot remove them.
- **Talent tests.** Each test keeps the DPS at fresh level 60 equal. The tests: Seal of Command 85% of weapon damage, more weapon damage on Holy Strike, Vengeance 5 stacks, Vindication +10% Attack Power. Each test gives 0 to 1.4 points against Fury in Naxxramas.
- **Fury is the outlier.** In Naxxramas, Retribution is still 113% of Arms and 131% of Combat Rogue.

**Against the pure average**

The hybrid target is 95% of the pure average (part 5), not 100% of Fury. Fury and Combat Rogue use the increases of this part. The increase of Hunter, Mage and Warlock with raid gear is not known. The table shows three cases.

| Hunter, Mage and Warlock in Naxxramas | Fresh level 60 | Pre-raid best in slot | Molten Core | Blackwing Lair | Naxxramas |
| --- | --- | --- | --- | --- | --- |
| ×1.60 | 103% | 103% | 102% | 102% | 101% |
| ×1.75 | 103% | 102% | 99% | 97% | 95% |
| ×1.90 | 103% | 100% | 96% | 93% | 90% |
| ×1.75, spell damage stays at 254 | 103% | 99% | 95% | 91% | 87% |

- In the middle case, Retribution is 4–8 points above the hybrid target until Molten Core. It is at the target in Naxxramas.
- Over the full game, the average is near the target.
- **Spell damage on plate items is the largest lever.** It gives 8 points in Naxxramas (87% → 95%). This is an item rule, not a talent.

**Result**

- **Retribution at the level of Fury at fresh level 60 is not too strong for a full content phase.** It is above the hybrid target until Blackwing Lair, and at the target in Naxxramas. From Molten Core, it is 3–7% below Fury (3–6% with flatter gear).
- **Recommendation: keep C16, with Sacred Arbiter as in the beta (+20%).** Do not change talents to correct the increase with gear.
- **Compare Retribution with the pure average at each gear tier,** not only with Fury (see Watch list, W15).
- **Request to Blizzard:** put spell damage on Paladin plate items at each tier.
- **The tier that Blizzard uses for balance is important.** If Blizzard balances at the raid release (9 December 2026), the proposals are correct for the first weeks. After that, Retribution falls behind.

## 7. Judgement of the Crusader

Judgement of the Crusader gives about +10% DPS at fresh level 60. It adds 161 Holy damage taken. Each hit gets 161 × its spell damage coefficient. Seal of Command gets the full 29%, not 20.3%. Parts 3–6 do not include it.

| Hit | Bonus for each hit (with Improved Seals and Two-Handed Weapon Specialization) | Hits each sec | DPS |
| --- | --- | --- | --- |
| Seal of Command (29%) | 57 | About 0.15 | +9 |
| Seal of Righteousness (12%) | 24 | About 0.35 | +9 |
| Judgement (42.9%) | 84 | About 0.13 | +11 |
| Holy Strike (21.45%) | 44 | About 0.10 | +5 |
| Hammer of Wrath (42.9%, last 20% of the fight) | 69 | About 0.03 | +2 |
| **Total** |  |  | **About +36 (+10%)** |

- The bonus is about the same % for the beta and for all versions of C16. Thus, the comparisons in part 4 do not change.
- If MythicSim includes Judgement of the Crusader in its raid debuffs, part 5 is correct. If not, Retribution with a Crusader Paladin in the raid is about 10% higher.
- The +161 does not increase with gear. It is about 10% at fresh level 60 and about 6% in Naxxramas.
- With C18, each Retribution Paladin keeps its own Judgement of the Crusader. Holy Strike refreshes it (Sacred Arbiter). This is a strong reason for C18.

## 8. Other results

- **Stat values (raid buffs, 5 min fight).** 1 spell damage: 0.21 DPS. 1 Attack Power: 0.11 DPS. 1 Strength: 0.26 DPS. 1% critical hit: 5.2 DPS. 1% hit: 4.9 DPS, up to the cap. Thus, 1 spell damage is worth about 1.9 Attack Power. Plate items with spell damage are good for Retribution, and Warriors do not want them.
- **Hit cap.** The build has 8% hit (Precision 3% + 5% from gear). The cap is about 9%.
- **Consecrated Ground with Consecration on cooldown.** About +23% on one target (371 → 457 DPS). This is true if the +10% applies to all your Holy damage on the target, as the beta tests show. The mana is zero after 70 sec. It is strong burst for 2 Holy points (see Watch list, W16).
- **Exorcism against Undead and Demons.** About +13% (418 DPS). If you use it on cooldown, the mana is zero after about 2 min.
- **Two-Handed Weapon Specialization.** The Paladin talent gives 6%. The Warrior talent in Forever gives 3%. Each 1% gives Retribution about 3.3 DPS (0.9%). At 6%, Retribution is 100% of Fury at fresh level 60 and 93% in Naxxramas. At 3%, it is 98% and 90%. The 6% stays: it is an intentional Paladin strength (see Tree balance, Paladin strengths).

## 9. Limits

- The model calculates averages. It is not a full simulation.
- Not confirmed: the critical hit decrease against a boss, the Seal of Righteousness value at 3.6 sec, the Forever v2 rage rules (Fury: announced, not in the beta yet) and the Attack Power part of Eviscerate (Rogue).
- The Fury, Arms and Combat Rogue rotations and talents are assumptions. Recklessness, Rend, Sweeping Strikes and poisons are not in the model.
- Champion of the Light: this section uses 60% of Intellect. At 30%, Retribution loses about 7 DPS (see Open questions).
- The gear tiers are estimates with Classic steps. The Forever raid items are not known.
- The Fury and Rogue values with the same gear are less certain than their increase with gear. Thus, part 6 uses only the increase.
- Boss armor is the same at all tiers, as in Classic.
- Consumables are not in the model.
