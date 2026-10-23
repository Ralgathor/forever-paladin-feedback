# Damage

This section compares the single-target damage of Retribution with the other damage classes. The unit is damage per second (DPS) on one level 63 boss. The values come from a model, not from combat logs.

## Summary

- With all proposals, Retribution is about equal to Fury Warrior at fresh level 60. It is 101% of Fury and 103% of the average of the pure damage classes.
- The hybrid target is 95% of the pure damage classes. Players report it from developer comments: hybrids do about 5% less damage than pure damage classes. In the beta, Retribution is 93%.
- C16 gives almost all of the increase. C17 gives the same damage as the beta Seal swap, but the mana lasts for the full fight.
- Retribution increases less with gear than Fury. In Naxxramas, it is about 82% of Fury (87% with flatter gear). No talent change can close this gap (part 6).
- Fury increases more with gear than the other classes. Against the pure average, Retribution goes from 103% at fresh level 60 to about 92% in Naxxramas. The hybrid target is 95%.
- Judgement of the Crusader gives Retribution about +9% DPS at fresh level 60. C18 makes this possible for each Paladin.

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
| Holy Strike | 54 | 15% |
| Judgement | 52 | 14% |
| Seal of Righteousness (Echo) | 47 | 13% |
| Hammer of Wrath (last 20% of the fight) | 22 | 6% |
| **Total** | **370** |  |

- About 70% of the damage is Holy damage. Armor does not decrease it.
- The global cooldown is active 54% of the time. Thus, you have time for Exorcism or Consecration.
- Mana: −2.6 mana per sec with Blessing of Wisdom. The mana lasts about 18 min. A melee player gets Blessing of Wisdom only with 3 Paladins in the raid (see The problem with Blessings). Without it: −10.6 mana per sec, and the mana lasts about 4.5 min.

## 4. Proposals against the beta

Same build and gear, raid buffs, 2 min fight. The beta build has the same damage talents in their beta rows. It has no Reverence.

| Version | DPS | Change | Mana |
| --- | --- | --- | --- |
| Beta: a Seal change before each swing | 336 | — | −39.6 per sec: zero after 72 sec |
| Beta: Seal of Command only, no Seal changes | 301 | −10% | Lasts |
| C16, first version: Holy Strike always triggers Seal of Command, no damage bonus | 379 | +13% | Lasts |
| **C16: Holy Strike triggers your Seal and Echo, Sacred Arbiter as in the beta (+20%)** | **370** | **+10%** | **Lasts** |
| C16: Holy Strike triggers your Seal and Echo, Sacred Arbiter +10% | 366 | +9% | Lasts |
| C16: Holy Strike triggers your Seal and Echo, Sacred Arbiter +0% | 361 | +8% | Lasts |
| C16: only Seal of Command, by chance, Sacred Arbiter +0% | 349 | +4% | Lasts |

- **C16 gives the increase.** Holy Strike gives about 34 DPS more than in the beta. Seal of Command triggers on 42% of Holy Strikes, and Seal of Righteousness triggers on all Holy Strikes.
- **C17 does not add damage.** It gives the damage of the beta Seal swap for the full fight. In the beta, the mana is zero after 72 sec. Then the Paladin can use only Seal of Command (301 DPS).
- **The C16 value is a choice.** The first version (+13%) puts Retribution above Fury Warrior (see part 5). The version in this document has one rule for all melee attacks and keeps Sacred Arbiter as in the beta. It is 2% less.
- **Sacred Arbiter at +10% changes little.** It gives only 4 DPS (1%) less. From Molten Core, Retribution is already below Fury (part 6).

## 5. Comparison with the other damage classes

The values of the other classes come from [MythicSim](https://mythicsim.com/wow-forever/tier-list): wowsims Forever, beta client 1.60.1.70425, simulated on 22 October 2026 (engine a667dce, 10,000 iterations, no trinkets). It uses curated dungeon and crafted gear, full raid buffs, debuffs and consumables, and a 2 min fight against one level 63 boss. Its Retribution value (847) uses the beta talents. This document uses only its ratios. The Retribution values with the proposals are 847 × the change in part 4.

The pure average is the best spec of each pure damage class: Warrior 929, Rogue 702, Hunter 1,175, Mage 860 and Warlock 879. The average is 909.

| Spec | DPS | Against the pure average (909) |
| --- | --- | --- |
| Survival Hunter (melee weaving) | 1,175 | 129% |
| Retribution, C16 first version | About 957 | 105% |
| **Retribution, all proposals** | **About 934** | **103%** |
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
- **With all proposals, Retribution is 101% of Fury and 103% of the pure average.** Without Combat Rogue (the lowest pure class), the pure average is 961. Retribution is then 97% of it.
- **Retribution is the strongest hybrid** in the beta and with the proposals. In the beta, it is 7% above Feral and 14% above Enhancement.
- **Check with the same gear.** The model also calculates an Arms Warrior with the gear of part 1. The beta Retribution is 5% above Arms. MythicSim gives 6%. Thus, the model and MythicSim agree.
- **One source only.** The MythicSim page has some errors in its rank order. Its Hunter values use melee weaving. No player has confirmed melee weaving in a raid.
- **No raid gear.** MythicSim has no raid gear tiers. Part 6 uses a model for the increase with gear.

## 6. Gear progression

Retribution increases less with gear than the pure melee classes. Blizzard said that it wants more horizontal gear progression. But each tier still gives more power.

**Model**

- The five gear tiers of Threat, part 2. Each tier gives about 15–20% more Attack Power, critical hit and spell damage from gear. Hit goes from 5% to 9%.
- Weapons follow the Classic steps. Two-handed: 54, 56, 63, 66 and 75 damage per sec. One-handed (main hand and off hand): 42 and 40 at fresh level 60, up to 64 and 60 in Naxxramas.
- Retribution, Fury (two weapons), Arms and Combat Rogue get the same gear and the same raid buffs.
- Flatter gear: from Molten Core, the gear increases at half the rate, as in Threat, part 3.
- The model uses only the increase of each class from fresh level 60. Retribution starts at 101% of Fury (part 5).
- Two cases for Retribution: plate gear gives more spell damage at each tier, or the spell damage stays at 254.

**DPS increase from fresh level 60 (Classic steps)**

| Tier | Retribution | Retribution, spell damage stays at 254 | Fury | Arms | Combat Rogue |
| --- | --- | --- | --- | --- | --- |
| Fresh level 60 | ×1.00 | ×1.00 | ×1.00 | ×1.00 | ×1.00 |
| Pre-raid best in slot | ×1.14 | ×1.11 | ×1.22 | ×1.15 | ×1.16 |
| Molten Core | ×1.28 | ×1.22 | ×1.43 | ×1.34 | ×1.31 |
| Blackwing Lair | ×1.42 | ×1.33 | ×1.68 | ×1.52 | ×1.49 |
| Naxxramas | ×1.61 | ×1.48 | ×1.98 | ×1.78 | ×1.71 |

**Retribution as a % of Fury**

| Tier | Classic steps | Classic steps, spell damage stays at 254 | Flatter gear | Flatter gear, spell damage stays at 254 |
| --- | --- | --- | --- | --- |
| Fresh level 60 | 101% | 101% | 101% | 101% |
| Pre-raid best in slot | 94% | 92% | 94% | 92% |
| Molten Core | 90% | 86% | 92% | 89% |
| Blackwing Lair | 85% | 80% | 89% | 85% |
| Naxxramas | 82% | 75% | 87% | 82% |

**Why Retribution increases less**

- **About 24% of the damage is fixed base values.** Gear does not change them: Judgement (186.5), Seal of Righteousness (67.5 for each hit), Hammer of Wrath (498) and the +93 of Holy Strike.
- **About 12% comes from spell damage.** The coefficients are small (12–43%). +100 spell damage gives only about +20 DPS.
- **Only about 64% increases with weapon damage and Attack Power:** auto attacks, Seal of Command and the weapon part of Holy Strike. For Fury and Rogue, it is almost 100%.
- **Retribution gets the hit cap at pre-raid** (Precision 3% + 6% from gear). More hit then does nothing. The two-weapon classes start at 28% miss. Each point of hit helps them until Naxxramas.
- **Critical hit helps Fury two times:** more Flurry and two times the rage. For Retribution, it helps only Vengeance.
- **Improved Seals multiplies the fixed bases** by the same 15% as the weapon part. Thus, it does not change the share that increases with gear.
- **Rage in Forever.** In Classic, rage came from the damage. Better gear gave more rage and more Heroic Strikes. Forever gives rage from the weapon speed. This removes most of that effect. With Classic rage, the gap is bigger than these tables show.

**The limit of the Retribution increase**

The increase of each damage source from fresh level 60 to Naxxramas (Classic steps):

| Source | Increase |
| --- | --- |
| Seal of Command | ×1.78 |
| Auto attacks | ×1.74 |
| Holy Strike | ×1.64 |
| Judgement | ×1.49 |
| Seal of Righteousness | ×1.43 |
| Hammer of Wrath | ×1.26 |
| **Retribution** | **×1.61** |
| Fury Warrior | ×1.98 |

- The best sources of Retribution increase only about ×1.75. The slow two-handed weapon, the hit cap and no Flurry limit them.
- Thus, a Retribution with no fixed values also increases only about ×1.75. This is 88% of the Fury increase. No talent change can close the gap to Fury.
- **Talent tests.** Each test keeps the DPS at fresh level 60 equal. The tests: Seal of Command 85% of weapon damage, more weapon damage on Holy Strike, Vengeance 5 stacks, Vindication +10% Attack Power. Each test gives 0 to 2 points against Fury in Naxxramas.
- **Fury is the outlier.** In Naxxramas, Retribution is still 106% of Arms and 125% of Combat Rogue.

**Against the pure average**

The hybrid target is 95% of the pure average (part 5), not 100% of Fury. Fury and Combat Rogue use the increases of this part. The increase of Hunter, Mage and Warlock with raid gear is not known. The table shows three cases.

| Hunter, Mage and Warlock in Naxxramas | Fresh level 60 | Pre-raid best in slot | Molten Core | Blackwing Lair | Naxxramas |
| --- | --- | --- | --- | --- | --- |
| ×1.60 | 103% | 104% | 103% | 101% | 98% |
| ×1.75 (as Arms and Rogue) | 103% | 102% | 100% | 97% | 92% |
| ×1.90 | 103% | 101% | 98% | 93% | 88% |
| ×1.75, spell damage stays at 254 | 103% | 99% | 96% | 91% | 85% |

- In the middle case, Retribution is 2–8 points above the hybrid target until Molten Core. It is 3 points below the target in Naxxramas.
- Over the full game, the average is near the target.
- **Spell damage on plate items is the largest lever.** It gives 7 points in Naxxramas (85% → 92%). This is an item rule, not a talent.

**Result**

- **Retribution at the level of Fury at fresh level 60 is not too strong for a full content phase.** It is above the hybrid target until about Molten Core. From Molten Core, it is 10–18% below Fury (8–13% with flatter gear).
- **Recommendation: keep C16, with Sacred Arbiter as in the beta (+20%).** Do not change talents to correct the increase with gear.
- **Compare Retribution with the pure average at each gear tier,** not only with Fury (see Watch list, W15).
- **Request to Blizzard:** put spell damage on Paladin plate items at each tier.
- **The tier that Blizzard uses for balance is important.** If Blizzard balances at the raid release (9 December 2026), the proposals are correct for the first weeks. After that, Retribution falls behind.

## 7. Judgement of the Crusader

Judgement of the Crusader gives about +9% DPS at fresh level 60. It adds 161 Holy damage taken. Each hit gets 161 × its spell damage coefficient. Seal of Command gets the full 29%, not 20.3%. Parts 3–6 do not include it.

| Hit | Bonus for each hit (with Improved Seals and Two-Handed Weapon Specialization) | Hits each sec | DPS |
| --- | --- | --- | --- |
| Seal of Command (29%) | 57 | About 0.15 | +9 |
| Seal of Righteousness (12%) | 24 | About 0.35 | +8 |
| Judgement (42.9%) | 84 | About 0.13 | +11 |
| Holy Strike (21.45%) | 44 | About 0.10 | +4 |
| Hammer of Wrath (42.9%, last 20% of the fight) | 69 | About 0.03 | +2 |
| **Total** |  |  | **About +34 (+9%)** |

- The bonus is about the same % for the beta and for all versions of C16. Thus, the comparisons in part 4 do not change.
- If MythicSim includes Judgement of the Crusader in its raid debuffs, part 5 is correct. If not, Retribution with a Crusader Paladin in the raid is about 9% higher.
- The +161 does not increase with gear. It is about 9% at fresh level 60 and about 6% in Naxxramas.
- With C18, each Retribution Paladin keeps its own Judgement of the Crusader. Holy Strike refreshes it (Sacred Arbiter). This is a strong reason for C18.

## 8. Other results

- **Stat values (raid buffs, 5 min fight).** 1 spell damage: 0.20 DPS. 1 Attack Power: 0.12 DPS. 1 Strength: 0.29 DPS. 1% critical hit: 5.0 DPS. 1% hit: 5.4 DPS, up to the cap. Thus, 1 spell damage is worth about 1.7 Attack Power. Plate items with spell damage are good for Retribution, and Warriors do not want them.
- **Hit cap.** The build has 8% hit (Precision 3% + 5% from gear). The cap is about 9%.
- **Consecrated Ground with Consecration on cooldown.** About +23% on one target (370 → 456 DPS). This is true if the +10% applies to all your Holy damage on the target, as the beta tests show. The mana is zero after 70 sec. It is strong burst for 2 Holy points (see Watch list, W16).
- **Exorcism against Undead and Demons.** About +12% (414 DPS). If you use it on cooldown, the mana is zero after about 2 min.
- **Two-Handed Weapon Specialization.** The Paladin talent gives 6%. The Warrior talent in Forever gives 3%. Each 1% gives Retribution about 3.3 DPS (0.9%). At 6%, Retribution is 101% of Fury at fresh level 60 and 82% in Naxxramas. At 3%, it is 98% and 79%. The 6% stays: it is an intentional Paladin strength (see Tree balance, Paladin strengths).

## 9. Limits

- The model calculates averages. It is not a full simulation.
- Not confirmed: the critical hit decrease against a boss, the Seal of Righteousness value at 3.6 sec, the cooldown of Slam (Arms) and the rage from off-hand attacks (Fury).
- Champion of the Light: this section uses 60% of Intellect. At 30%, Retribution loses about 7 DPS (see Open questions).
- The gear tiers are estimates with Classic steps. The Forever raid items are not known.
- The Fury and Rogue values with the same gear are less certain than their increase with gear. Thus, part 6 uses only the increase.
- Boss armor is the same at all tiers, as in Classic.
- Consumables are not in the model.
