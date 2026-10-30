# Damage

This section compares the single-target damage of Retribution with the other damage classes. The unit is damage per second (DPS) on one level 63 boss. The values come from a model, not from combat logs.

The script models/damage/run_tables.py calculates all values of this section. Fury, Arms and Combat Rogue use the Forever spellbook and talents (wowforevertalents.com) and the Forever rage formula (see Threat, part 6). Spell values and combat rules are checked against wowsims Forever (23 October 2026). No value is fitted to the first calculation.

## Summary

- With all proposals and the version 6 talents, Retribution is about equal to Fury Warrior at fresh level 60. It is 103% of Fury and 105% of the average of the pure damage classes.
- The hybrid target is 95% of the pure damage classes. Players report it from developer comments: hybrids do about 5% less damage than pure damage classes. In the beta, Retribution is 93%.
- Holy Strike Seal trigger (C1) gives almost all of the increase. Twist of Light (C-R2) gives the same damage as the beta Seal swap, but the mana lasts for the full fight.
- Retribution increases less with gear than Fury. In Naxxramas, it is about 95% of Fury (also with flatter gear). No talent change closes this gap (part 6).
- Burning Zeal (C-R4) gives more damage in late raids: +0.8% at fresh level 60, +1.3% in Naxxramas. Measure for Measure (C-R5) gives about +1% at all gear levels. RB6 (5/8/38) with both is 105% of the pure average at fresh level 60 and 97% in Naxxramas (part 11). In wowsims, Burning Zeal gives +2.0%, and RB6 is 113% of the pure average. Shock-Retribution with Divine Precision in Holy row 5 (28/0/23) is also 113%.
- Fury increases more with gear than the other classes. Against the pure average, Retribution goes from 105% at fresh level 60 to about 97% in Naxxramas. The hybrid target is 95%.
- Judgement of the Crusader gives Retribution about +10% DPS at fresh level 60. Personal Judgement of the Crusader (C2) makes this possible for each Paladin.

## 1. Build and gear

- **Build.** 9/8/34: v6p2003103-030000000000005-020533100133032152 in calculator version 6 (RB2). All parts use these talents. Vengeance requires Burning Zeal 5/5, and Vindication has 3 ranks (+2/4/6% Attack Power).
  - Holy 9: Divine Intellect 2/5, Improved Seals 3/3, Unyielding Faith 1/2, Reverence 3/3.
  - Protection 8: Benediction 5/5 (M-P1), Precision 3/3.
  - Retribution 34: Conviction 5/5, Improved Judgement 2/2, Vindication 3/3 (C-P3), Burning Zeal 5/5 (C-R4), Sanctified Judgement 3/3, Seal of Command, Two-Handed Weapon Specialization 3/3, Sacred Arbiter, Vengeance 3/3, Measure for Measure 2/3 (C-R5), Champion of the Light 3/3, Instrument of Law 2/2, Twist of Light.
- **Toughness and Divine Strength removal (C-P3) and the values.** Vindication 3/3 (C-P3) gives +6% Attack Power with full uptime, about +7 DPS. The beta rows use Divine Strength 5/5 (+10% Strength, about +7 DPS), no Vindication, no Burning Zeal and no Measure for Measure.
- **Gear.** A real fresh level 60 profile: crafted items, dungeon items and quest rewards. Without talents and buffs: 283 Strength, 74 Agility, 770 Attack Power, 5.9% critical hit, 5% hit, 254 spell damage, 87 Intellect and 2,537 mana.
- **Weapon.** Stormcarver (Blacksmithing, item level 63): 155–233 damage, 3.6 sec, +32 spell damage.
- **With talents and raid buffs.** 1,250 Attack Power, 322 spell damage (Champion of the Light gives 68), 8% hit and 2,931 mana.

## 2. Model

- **Raid buffs.** Blessing of Kings, Blessing of Might (133), Battle Shout (193), Mark of the Wild (+12 to all stats) and Blessing of Wisdom (8 mana per sec). No consumables. No Judgement of the Crusader (see part 7).
- **Boss.** Level 63. 976 armor after 5 Sunder Armor and Faerie Fire. You attack from behind: no parry and no block.
- **Hit table.** 8% miss before hit. Each 1% of hit removes 1% miss. Two weapons: 27% miss. 6.5% dodge. 40% of auto attacks are glancing blows (−35% damage).
- **Critical hit against the boss.** −4.8% for all melee attacks: 3% + up to 1.8% from buffs and talents (wowsims Forever). Special attacks, Seals and Judgements roll the critical hit separately, only on the hits that land. A critical hit does ×2 damage, and ×1.5 for spells. The spell hit cap is 18%.
- **Seals and Judgements** use the melee hit table. Armor does not decrease Holy damage.
- **Seal of Command.** 7 procs each minute: a 42% chance for each hit with a 3.6 sec weapon. Each proc does 70% of weapon damage + 20.3% of spell damage (29% × 70%). With Improved Seals, this is 80.5% of weapon damage + 23.3% of spell damage.
- **Seal of Righteousness.** 67.5 + 12% of spell damage for each hit. The base part (67.5) is for a 3.6 sec weapon, from the range in the tooltip. Weapon speed does not change the spell damage part. It cannot miss. A critical hit does ×2 damage, with a separate roll (see Beta test results, Spells).
- **Judgement.** One each 8 sec (Improved Judgement 2/2): 170–187 (178.2) + 42.9% of spell damage. The boss cannot dodge it.
- **Holy Strike.** One each 10 sec: 50% of (normalized weapon damage (3.3 sec) + 93 + 42.9% of spell damage). Thus, 46.5 + 21.45% of spell damage. All the damage is Holy damage.
- **Hammer of Wrath.** One each 6 sec in the last 20% of the fight. Instant (Instrument of Law): 498 + 42.9% of spell damage.
- **Multipliers.** Two-Handed Weapon Specialization: ×1.06 (melee attacks, Seals, Judgements and Holy Strike). Improved Seals: ×1.15 (Seals and Judgements). They multiply together (×1.219).
- **Vengeance.** A simulation of the stacks (3% each, 3 stacks, 30 sec). The average is +6%. Seal critical hits also give stacks.
- **Twist of Light (C-R2).** One Seal change each 10 sec. Thus, Seal of Command and Seal of Righteousness are both active all the time.
- **Fight.** 2 min. A 5 min fight gives 1% more (Vengeance).
- **Not in the model.** Exorcism, Consecration and Retribution Aura (see part 8).

## 3. Damage sources

All proposals (Holy Strike Seal trigger, C1, as in this document), raid buffs, 2 min fight:

| Source | DPS | Share |
| --- | --- | --- |
| Auto attacks | 118 | 31% |
| Seal of Command | 82 | 22% |
| Judgement | 58 | 15% |
| Seal of Righteousness (Echo) | 52 | 14% |
| Holy Strike | 49 | 13% |
| Hammer of Wrath (last 20% of the fight) | 22 | 6% |
| **Total** | **382** |  |

- About 70% of the damage is Holy damage. Armor does not decrease it.
- The global cooldown is active 52% of the time. Thus, you have time for Exorcism or Consecration.
- Mana: +6.9 mana per sec with Blessing of Wisdom, −1.1 without it (the mana then lasts about 44 min). Sanctified Judgement returns 126 mana for each Judgement (60% of the base Seal cost, before talent cost decreases). With Blessing of Wisdom, the mana does not decrease, except in the last 20% of the fight. There, Hammer of Wrath uses 38 mana per sec. A melee player receives Blessing of Wisdom only with 3 Paladins in the raid (see The problem with Blessings).

## 4. Proposals against the beta

Same gear, raid buffs, 2 min fight. The beta build has the same damage talents in their beta rows. It has no Reverence, no Vindication, no Burning Zeal and no Measure for Measure, but Divine Strength 5/5. The proposed rows use RB2 of version 6: Burning Zeal 5/5 and Measure for Measure 2/3 give about +1.5% of each increase (part 11).

| Version | DPS | Change | Mana |
| --- | --- | --- | --- |
| Beta: a Seal change before each swing | 338 | — | −39.6 per sec: zero after 72 sec |
| Beta: Seal of Command only, no Seal changes | 297 | −12% | Lasts |
| Holy Strike Seal trigger (C1), first version: Holy Strike always triggers Seal of Command, no damage bonus | 389 | +15% | Lasts |
| **Holy Strike Seal trigger (C1), Seal and Echo, Sacred Arbiter as in the beta (+20%)** | **382** | **+13%** | **Lasts** |
| Holy Strike Seal trigger (C1), Seal and Echo, Sacred Arbiter +10% | 377 | +12% | Lasts |
| Holy Strike Seal trigger (C1), Seal and Echo, Sacred Arbiter +0% | 373 | +10% | Lasts |
| Holy Strike Seal trigger (C1): only Seal of Command, by chance, Sacred Arbiter +0% | 358 | +6% | Lasts |

- **Holy Strike Seal trigger (C1) gives the increase.** Holy Strike gives about 38 DPS more than in the beta. Seal of Command triggers on 42% of Holy Strikes, and Seal of Righteousness triggers on all Holy Strikes.
- **Twist of Light (C-R2) does not add damage.** It gives the damage of the beta Seal swap for the full fight. In the beta, the mana is zero after 72 sec. Then the Paladin can use only Seal of Command (297 DPS).
- **The Holy Strike Seal trigger (C1) value is a choice.** The first version (+15%) puts Retribution further above Fury Warrior (see part 5). The version in this document has one rule for all melee attacks and keeps Sacred Arbiter as in the beta. It is 2% less.
- **Sacred Arbiter at +10% changes little.** It gives only 5 DPS (1%) less. From Molten Core, Retribution is already below Fury (part 6).

## 5. Comparison with the other damage classes

The values of the other classes come from [MythicSim](https://mythicsim.com/wow-forever/tier-list): wowsims Forever, beta client 1.60.1.70425, simulated on 22 October 2026 (engine a667dce, 10,000 iterations, no trinkets). It uses curated dungeon and crafted gear, full raid buffs, debuffs and consumables, and a 2 min fight against one level 63 boss. Its Retribution value (847) uses the beta talents. This document uses only its ratios. The Retribution values with the proposals are 847 × the change in part 4.

The pure average is the best spec of each pure damage class: Warrior 929, Rogue 702, Hunter 1,175, Mage 860 and Warlock 879. The average is 909.

| Spec | DPS | Against the pure average (909) |
| --- | --- | --- |
| Survival Hunter (melee attacks between shots) | 1,175 | 129% |
| Retribution, Holy Strike Seal trigger (C1) first version | About 974 | 107% |
| **Retribution, all proposals (version 6)** | **About 955** | **105%** |
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
- **With all proposals, Retribution is 103% of Fury and 105% of the pure average.** Without Combat Rogue (the lowest pure class), the pure average is 961. Retribution is then 99% of it.
- **Retribution is the strongest hybrid** in the beta and with the proposals. In the beta, it is 7% above Feral and 14% above Enhancement.
- **Check with the same gear.** The model also calculates Arms, Fury and Combat Rogue with the gear of part 1 and Forever rage. The beta Retribution is 15% above Arms. wowsims Forever gives 7% with the Arms pre-raid gear, and MythicSim gives 6%. The Arms rotation is now the wowsims rotation: Rend, Overpower, Mortal Strike, Spearing Strike, Slam, then Heroic Strike. Other causes can be the gear, consumables and Windfury Totem. Part 6 uses only the increase with gear.
- **One source only.** The MythicSim page has some errors in its rank order. Its Hunter values add melee attacks between shots. No player has confirmed this in a raid.
- **No raid gear.** MythicSim has no raid gear tiers. Part 6 uses a model for the increase with gear.

## 6. Gear progression

Retribution increases less with gear than the pure melee classes. Blizzard said that it wants more horizontal gear progression. But each tier still gives more power.

**Model**

- The five gear tiers of Threat, part 2. Each tier gives 17.5% more Strength, Agility, Attack Power, critical hit, spell damage and Intellect from gear. Hit goes from 5% to 9%.
- Weapons follow the Classic steps. Two-handed: 54, 56, 63, 66 and 75 damage per sec. One-handed (main hand and off hand, 2.6 sec): 42 and 40 at fresh level 60, then 47/44, 52/49, 57/54 and 64/60.
- Retribution, Fury (two weapons), Arms and Combat Rogue use the same gear and the same raid buffs.
- Fury: Bloodthirst, Whirlwind, then Heroic Strike with the extra rage, and Execute in the last 20% of the fight. Flurry, Death Wish (one use) and Deep Wounds. Rage: the Forever v2 rules. Each swing that lands gives 3.46 rage for each second of weapon speed with the main hand, and 1.73 with the off hand. Critical hits give +100% rage (beta notes, 2 October). Dual Wield Specialization gives +50% off-hand rage (hotfix). Raging Blows (Whirlwind −3 rage) and Improved Execute (−5 rage). Bloodthirst and Whirlwind use 7.2 rage each sec. Fury has 6.6 rage each sec at fresh level 60 and 7.4 in Naxxramas. Thus, Fury has too little rage for Bloodthirst and Whirlwind until Naxxramas.
- Arms: the wowsims Forever rotation. Rend, Overpower, Mortal Strike, Spearing Strike, Slam, then Heroic Strike, and Execute in the last 20% of the fight. Deep Wounds. Bloodthrill 5/5 opens Overpower on 20% of the main-hand swings on a target with Rend. Improved Rend 3/3 (+35%).
- Combat Rogue: Sinister Strike, Slice and Dice, and Eviscerate with 5 combo points. Blade Flurry and Adrenaline Rush (one use each). Eviscerate uses 15% of Attack Power (assumed). No poisons.
- Flatter gear: from Molten Core, the gear increases at half the rate, as in Threat, part 3.
- The model uses only the increase of each class from fresh level 60. Retribution starts at 103% of Fury (part 5).
- Two cases for Retribution: plate gear gives more spell damage at each tier, or the spell damage stays at 254.

**DPS increase from fresh level 60 (Classic steps)**

| Tier | Retribution | Retribution, spell damage stays at 254 | Fury | Arms | Combat Rogue |
| --- | --- | --- | --- | --- | --- |
| Fresh level 60 | ×1.00 | ×1.00 | ×1.00 | ×1.00 | ×1.00 |
| Pre-raid best in slot | ×1.10 | ×1.08 | ×1.14 | ×1.10 | ×1.12 |
| Molten Core | ×1.24 | ×1.19 | ×1.30 | ×1.25 | ×1.25 |
| Blackwing Lair | ×1.39 | ×1.29 | ×1.50 | ×1.40 | ×1.41 |
| Naxxramas | ×1.59 | ×1.45 | ×1.73 | ×1.59 | ×1.61 |

**Retribution as a % of Fury**

| Tier | Classic steps | Classic steps, spell damage stays at 254 | Flatter gear | Flatter gear, spell damage stays at 254 |
| --- | --- | --- | --- | --- |
| Fresh level 60 | 103% | 103% | 103% | 103% |
| Pre-raid best in slot | 100% | 97% | 100% | 97% |
| Molten Core | 98% | 94% | 98% | 95% |
| Blackwing Lair | 95% | 89% | 96% | 91% |
| Naxxramas | 95% | 86% | 95% | 89% |

**Why Retribution increases less**

- **About 25% of the damage is fixed base values.** Gear does not change them: Judgement (178.2), Seal of Righteousness (67.5 for each hit), Hammer of Wrath (498) and the 46.5 of Holy Strike.
- **About 18% comes from spell damage.** The coefficients are small (12–43%). +100 spell damage gives only about +20 DPS.
- **Only about 57% increases with weapon damage and Attack Power:** auto attacks, Seal of Command and the weapon part of Holy Strike. For Fury and Rogue, it is almost 100%.
- **Retribution reaches the hit cap at pre-raid** (Precision 3% + 6% from gear). More hit then does nothing. The two-weapon classes start at 27% miss. Each point of hit helps them until Naxxramas.
- **Critical hit helps Fury two times:** more Flurry and two times the rage. For Retribution, it helps only Vengeance.
- **Improved Seals multiplies the fixed bases** by the same 15% as the weapon part. Thus, it does not change the share that increases with gear.
- **Rage in Forever.** In Classic, rage came from the damage. Better gear gave more rage and more Heroic Strikes. Forever gives rage from the weapon speed. This removes most of that effect. With Classic rage, the gap is larger than these tables show.

**The limit of the Retribution increase**

The increase of each damage source from fresh level 60 to Naxxramas (Classic steps):

| Source | Increase |
| --- | --- |
| Seal of Command | ×1.72 |
| Auto attacks | ×1.67 |
| Holy Strike | ×1.65 |
| Judgement | ×1.49 |
| Seal of Righteousness | ×1.42 |
| Hammer of Wrath | ×1.27 |
| **Retribution** | **×1.59** |
| Fury Warrior | ×1.73 |

- The best sources of Retribution increase about ×1.67–1.72. The slow two-handed weapon, the hit cap and no Flurry limit them.
- Thus, a Retribution with no fixed values increases about ×1.72. This is 99% of the Fury increase. The fixed values cause the gap. But a talent change cannot remove them.
- **Talent tests.** Each test keeps the DPS at fresh level 60 equal. The tests: Seal of Command 85% of weapon damage, more weapon damage on Holy Strike, Vengeance 5 stacks, Vindication +10% Attack Power. Each test gives 0 to 1.6 points against Fury in Naxxramas.
- **Fury is the outlier.** In Naxxramas, Retribution is still 119% of Arms and 135% of Combat Rogue.

**Against the pure average**

The hybrid target is 95% of the pure average (part 5), not 100% of Fury. Fury and Combat Rogue use the increases of this part. The increase of Hunter, Mage and Warlock with raid gear is not known. The table shows three cases.

| Hunter, Mage and Warlock in Naxxramas | Fresh level 60 | Pre-raid best in slot | Molten Core | Blackwing Lair | Naxxramas |
| --- | --- | --- | --- | --- | --- |
| ×1.60 | 105% | 104% | 103% | 103% | 103% |
| ×1.75 | 105% | 103% | 100% | 98% | 97% |
| ×1.90 | 105% | 101% | 97% | 94% | 92% |
| ×1.75, spell damage stays at 254 | 105% | 100% | 95% | 91% | 88% |

- In the middle case, Retribution is 3–10 points above the hybrid target until Blackwing Lair. It is 2 points above the target in Naxxramas.
- Over the full game, the average is near the target.
- **Spell damage on plate items is the largest lever.** It gives 9 points in Naxxramas (88% → 97%). This is an item rule, not a talent.

**Result**

- **Retribution at the level of Fury at fresh level 60 is not too strong for a full content phase.** It is above the hybrid target at all tiers (97% in Naxxramas). From Molten Core, it is 2–5% below Fury, also with flatter gear.
- **Recommendation: keep Holy Strike Seal trigger (C1), with Sacred Arbiter as in the beta (+20%).** Do not change talents to correct the increase with gear.
- **Compare Retribution with the pure average at each gear tier,** not only with Fury (see Watch list, W15).
- **Request to Blizzard:** put spell damage on Paladin plate items at each tier.
- **The tier that Blizzard uses for balance is important.** If Blizzard balances at the raid release (9 December 2026), the proposals are correct for the first weeks. After that, Retribution is below Fury.

## 7. Judgement of the Crusader

Judgement of the Crusader gives about +10% DPS at fresh level 60. It adds 161 Holy damage taken. Each hit receives 161 × its spell damage coefficient. Seal of Command receives the full 29%, not 20.3%. Parts 3–6 do not include it.

| Hit | Bonus for each hit (with Improved Seals and Two-Handed Weapon Specialization) | Hits each sec | DPS |
| --- | --- | --- | --- |
| Seal of Command (29%) | 57 | About 0.15 | +9 |
| Seal of Righteousness (12%) | 24 | About 0.35 | +9 |
| Judgement (42.9%) | 84 | About 0.15 | +13 |
| Holy Strike (21.45%) | 44 | About 0.10 | +5 |
| Hammer of Wrath (42.9%, last 20% of the fight) | 69 | About 0.03 | +2 |
| **Total** |  |  | **About +38 (+10%)** |

- The bonus is about the same % for the beta and for all versions of Holy Strike Seal trigger (C1). Thus, the comparisons in part 4 do not change.
- If MythicSim includes Judgement of the Crusader in its raid debuffs, part 5 is correct. If not, Retribution with a Crusader Paladin in the raid is about 10% higher.
- The +161 does not increase with gear. It is about 10% at fresh level 60 and about 7% in Naxxramas.
- With Personal Judgement of the Crusader (C2), each Retribution Paladin keeps its own Judgement of the Crusader. Holy Strike refreshes it (Sacred Arbiter). This is a strong reason for Personal Judgement of the Crusader (C2).

## 8. Other results

- **Stat values (raid buffs, 5 min fight).** 1 spell damage: 0.22 DPS. 1 Attack Power: 0.12 DPS. 1 Strength: 0.26 DPS. 1% critical hit: 6.1 DPS. 1% hit: 5.2 DPS, up to the cap. Thus, 1 spell damage is worth about 2 Attack Power. Plate items with spell damage are good for Retribution, and Warriors do not want them.
- **Hit cap.** The build has 8% hit (Precision 3% + 5% from gear). The cap is 8%.
- **Consecration on cooldown.** About +13% on one target (382 → 430 DPS). Consecration ticks can be critical hits (×1.5). The mana pool comes from the Retribution gear: 2,931 at fresh level 60 to 4,284 in Naxxramas, with Divine Intellect 2 and no mp5. With Holy Conduit and Benediction (M-P1), the mana is zero after 1 min 33 sec at fresh level 60. In Naxxramas, it is zero after 2 min 17 sec (3 min fight). The average increase is +10% in a 2 min fight and +8% in a 3 min fight. Retribution is then 102–116% of the pure average. Consecration damage and the mana costs come from wowsims Forever. Mana is the balance: the 95% target is for the rotation without Consecration (see Watch list, W16).
- **Consecrated Ground.** It is in Holy row 6 (M-H4). 31 Retribution points and 27 Holy points are more than 51. Thus, Retribution with Twist of Light cannot take it. Shock-Retribution 28/0/23 has no Twist of Light. It takes Holy Power 3/5 (M-H3) and Consecrated Ground 2/2: with Consecration, 352 → 428 DPS (+22%, 99% of RB2 with Consecration). See part 11. The +10% applies to all your Holy damage on the target. Seals and Judgements also do Holy damage, thus this is the tooltip effect.
- **Exorcism against Undead and Demons.** About +12% (428 DPS). If you use it on cooldown, the mana is zero after about 2 min.
- **Two-Handed Weapon Specialization.** The Paladin talent gives 6%. The Warrior talent in Forever gives 3%. Each 1% gives Retribution about 3.4 DPS (0.9%). At 6%, Retribution is 103% of Fury at fresh level 60 and 95% in Naxxramas. At 3%, it is 100% and 92%. The 6% stays: it is an intentional Paladin strength (see Tree balance, Paladin strengths).

## 9. Limits

- The model calculates averages. It is not a full simulation.
- Not confirmed: the critical hit decrease against a boss, the Seal of Righteousness value at 3.6 sec, the off-hand rage of Dual Wield Specialization (Fury: a hotfix, not in the developer notes) and the Attack Power part of Eviscerate (Rogue).
- The Warrior Compendium (Rage on Crit) uses no hit or critical hit decrease against a boss, from the Forever tooltips. It also adds Windfury Totem. With no decrease for all classes, Fury has enough rage at fresh level 60 and increases ×1.68. Retribution increases ×1.56 and is 93% of Fury in Naxxramas.
- The Fury and Combat Rogue rotations and talents are assumptions. Arms uses the wowsims Forever rotation and talents. Recklessness, Sweeping Strikes, Hamstring, Windfury Totem and poisons are not in the model.
- Champion of the Light: this section uses 60% of Intellect. At 30%, Retribution loses about 8 DPS (see Open questions).
- The gear tiers are estimates with Classic steps. The Forever raid items are not known.
- The Fury and Rogue values with the same gear are less certain than their increase with gear. Thus, part 6 uses only the increase.
- Boss armor is the same at all tiers, as in Classic.
- Consumables are not in the model.

## 10. Check with wowsims

wowsims Forever with the proposals gives a smaller Retribution increase than the model (−6.5%). Against Fury, the two results agree.

Conditions: wowsims Forever commit a10f483 (30 October 2026) with the proposals patch (models/wowsims). Presets of wowsims for gear, talents, rotation and consumables. The same raid buffs for all specs, a 3 min fight against one level 63 boss, 3,000 iterations. Beta: the wowsims Retribution preset. Proposed: RB1 of version 6 with Reverence (C-H1), Conviction (C-R1), Holy Strike Seal trigger (C1), Twist of Light (C-R2), Sanctified Judgement (C-R3), Burning Zeal (C-R4) and Measure for Measure (C-R5). The rows for each proposal use RB1 of version 5 (no Burning Zeal or Measure for Measure).

| Value | Model | wowsims | Difference |
| --- | --- | --- | --- |
| Retribution, all proposals against the beta (same talents) | +13% | +5% | −6.5% |
| Beta Retribution against Arms, same gear | 115% | 107% | −6.9% |
| Retribution, all proposals, as a % of Fury | 103% (part 5) | 104% | +0.8% |

- **Proposals against the beta.** In wowsims, Twist of Light (C-R2) gives +2.9% and the Holy Strike Seal trigger (C1) gives +2.0%. Conviction (C-R1), Reverence (C-H1) and Sanctified Judgement (C-R3) each give +0.2% or less in a raid. All of them give +5.4% (alone: +22%).
- **Beta against Arms (−6.9%).** The model uses the gear of part 1 for both specs. wowsims uses the Arms pre-raid gear for both specs, with consumables. Both results put the beta Retribution above Arms.
- **Against Fury.** Part 5 uses the MythicSim ratio for Fury. With this ratio, the model gives 103% and wowsims gives 104%. The model Fury with the gear of part 1 gives a different result (119%). Thus, part 5 does not use the model Fury.

**wowsims result of each spec** (DPS, raid buffs)

| Spec | Raid | Raid, no consumables | Alone (no buffs) |
| --- | --- | --- | --- |
| Mage (Fire) | 844 | 673 | 477 |
| **Retribution, all proposals (RB1)** | **829** | **670** | **299** |
| Fury Warrior (pre-raid gear) | 799 | 714 | 350 |
| Shadow Priest | 770 | 675 | 311 |
| Retribution, beta | 763 | 620 | 273 |
| Hunter (Marksmanship) | 749 | 706 | 241 |
| Balance Druid (pre-raid gear) | 721 | 540 | 314 |
| Arms Warrior (pre-raid gear) | 716 | 646 | 266 |
| Warlock (Destruction) | 695 | 521 | 430 |
| Enhancement Shaman | 649 | 536 | 237 |
| Feral Druid | 625 | 625 | 303 |
| Rogue (Combat gear) | 592 | 548 | 271 |
| Elemental Shaman | 560 | 410 | 181 |
| Pure average (Fury, Rogue, Hunter, Mage, Warlock) | 736 | 632 | 354 |

- In a raid, the beta Retribution is 104% of the pure average and 95% of Fury. With all proposals, it is 113% of the pure average and 104% of Fury.
- Without consumables, Retribution is 98% (beta) and 106% (proposed) of the pure average.
- Alone, Retribution is 77% (beta) and 85% (proposed) of the pure average. Retribution has more raid buffs in its damage than the pure classes.
- **New presets.** The Hunter and Rogue presets of commit a10f483 have new gear and rotations: Hunter 907 → 749, Rogue 649 → 592. Thus, the pure average goes from 787 to 736, and all specs are higher against it. The old presets do not load in the new sim. Against Fury, the proposed Retribution is 104% (commit 69e0e5b: 100%).
- Sacred Arbiter at +10% removes 0.9% of the raid damage. An Echo of 6 sec removes 0.4%.

The scripts are run_damage.py and check.py in models/wowsims. See its README for the setup and the proposal flags.

## 11. New talents: Burning Zeal (C-R4) and Measure for Measure (C-R5)

The script models/damage/run_tables.py (part 11) calculates these values. The base is RB2 without the two talents (Burning Zeal 0/5, Measure for Measure 0/3). This base is not a legal build in version 6, because Vengeance requires Burning Zeal 5/5. It gives the value of each talent. 2 min fight.

- **Burning Zeal (C-R4).** The critical damage bonus of Seals, Judgements and Holy Strike is ×1.2 (critical hits do ×2.2 damage, not ×2). Hammer of Wrath and auto attacks do not change.
- **Measure for Measure (C-R5).** Each dodge or parry of the target decreases the Judgement cooldown by 3 sec. Auto attacks and Holy Strike count. The model uses the average cooldown: 8 sec / (1 + 3 × dodges and parries each sec). From behind, the boss dodges 6.5% and does not parry. From the front, it also parries 14%.

| Talents | Fresh level 60 | Pre-raid | Molten Core | Blackwing Lair | Naxxramas |
| --- | --- | --- | --- | --- | --- |
| Burning Zeal 5/5 | +0.8% | +0.9% | +1.0% | +1.2% | +1.3% |
| Measure for Measure 3/3, from behind | +1.1% | +1.1% | +1.1% | +1.0% | +1.0% |
| Measure for Measure 3/3, from the front | +4.1% | +4.1% | +4.0% | +3.9% | +3.8% |
| Both, from behind | +1.9% | +2.0% | +2.1% | +2.2% | +2.4% |
| RB2 (Burning Zeal 5/5, Measure for Measure 2/3), from behind | +1.5% | +1.6% | +1.7% | +1.9% | +2.0% |
| RB6 (5/8/38), from behind | +1.9% | +2.0% | +2.1% | +2.2% | +2.4% |

**Against the pure average** (Hunter, Mage and Warlock ×1.75, as part 6):

| Build | Fresh level 60 | Pre-raid | Molten Core | Blackwing Lair | Naxxramas |
| --- | --- | --- | --- | --- | --- |
| Base with Burning Zeal 5/5 only | 104% | 102% | 99% | 97% | 96% |
| Base with Measure for Measure 3/3 only | 105% | 102% | 99% | 97% | 96% |
| RB2 (version 6) | 105% | 103% | 100% | 98% | 97% |
| RB6 (5/8/38) | 105% | 103% | 100% | 98% | 97% |

- **RB6.** RB2 with Measure for Measure 3/3, Holy Conduit 1 and Pursuit of Justice 2. The 4 points come from the Holy dip: Improved Seals 3 and Divine Intellect 2 stay. Reverence and Unyielding Faith go. In the model, RB6 is equal to "Both".
- **Mana of RB6.** Without Reverence, the income is about 10 mana per sec less (see Mana). Each extra Judgement gives about +44 mana with Sanctified Judgement 3/3 (return 126, cost 82). From behind, this is about +0.4 mana per sec.
- **Burning Zeal increases with gear.** The critical hit chance of Retribution increases from 11.6% to 16.9%. Thus, Burning Zeal closes a part of the gap with Fury (part 6).
- **Measure for Measure from the front.** Retribution tanks and PvP fights from the front receive about +23% Judgements (W23). A tank with Holy Shield cannot take the talent (see Builds, part 5).
- **Balance.** RB2 and RB6 are 105% of the pure average at fresh level 60. If this is too strong at the raid release, decrease Sacred Arbiter first (W15).

**Check with wowsims.** wowsims Forever commit a10f483 with the flags BZ and MFM (models/wowsims/run_damage.py). Raid buffs and consumables, a 3 min fight, the Retribution preset gear, the Holy Shock rotation. All builds are version 6 builds. The base is RB2 of version 6. Pure average: 736 (part 10).

| Build | Raid | Raid, no consumables | Alone | From the front | Raid, % of the pure average |
| --- | --- | --- | --- | --- | --- |
| RB2 (9/8/34) | 831 | 672 | 311 | 787 | 113% |
| RB2 with no Burning Zeal | 814 (−2.0%) | 660 (−1.8%) | 307 (−1.5%) | 771 (−2.0%) | 111% |
| RB2 with no Measure for Measure | 825 (−0.8%) | 667 (−0.7%) | 312 (+0.1%) | 760 (−3.3%) | 112% |
| RB2 with neither talent | 808 (−2.8%) | 655 (−2.5%) | 307 (−1.4%) | 746 (−5.2%) | 110% |
| RB1 (7/8/36) | 830 (−0.1%) | 670 (−0.3%) | 299 (−4.0%) | 784 (−0.3%) | 113% |
| RB6 (5/8/38) | 835 (+0.4%) | 676 (+0.7%) | 291 (−6.6%) | 799 (+1.5%) | 113% |
| Shock-Retribution (28/0/23) | 830 (−0.1%) | 652 (−3.0%) | 246 (−20.9%) | — | 113% |
| Holy Shock build (21/0/30) | 827 (−0.5%) | 653 (−2.7%) | 243 (−21.9%) | — | 112% |

- **Version 6.** The Retribution layout of version 6 (M-R4, M-R5) puts Burning Zeal before Vengeance. Vindication has 3 ranks with +2/4/6% Attack Power (C-P3). Each Retribution build takes Burning Zeal 5/5 (see Builds, part 4).
- **The four best builds are equal in a raid** (827 to 835, within 1%). Alone, the Holy Shock builds are about 20% below RB2: they have no mana for Holy Shock.
- **Retribution tank** (Righteous Fury, from the front): RB2 897 TPS, RB6 912 TPS (+1.7%), with Measure for Measure 3/3.
- **Burning Zeal gives two times the model value** (+2.0% against +0.9% with pre-raid gear). The preset gear, the raid buffs and the consumables give more critical hits than the model gear.
- **Measure for Measure agrees with the model.** From behind, it gives +0.8% (model: +1.1%). From the front, it gives +3.3% (model: +4.1%).
- **RB6 is 113% of the pure average in wowsims,** and 105% in the model at fresh level 60. The wowsims pure average is lower with the new Hunter and Rogue presets (part 10). See Watch list, W15.
- **Shock-Retribution with Divine Precision (28/0/23).** In version 5, Divine Precision was in Holy row 4 with no requirement. A 21/0/30 build with Divine Precision 2/3 then had 869 DPS, 2.0% above RB6. In version 6, Divine Precision is in its beta place again (Holy row 5), with no requirement (M-H5). It then needs 20 Holy points. The best Shock-Retribution build has 830 DPS with the preset gear, equal to RB6. With its own pre-raid gear, it has 867 DPS, 1.6% below RB6 (881) (see builds/retribution.md and Watch list, W22).
