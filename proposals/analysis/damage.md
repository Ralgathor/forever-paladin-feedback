# Damage

**Question.** How much damage does Retribution do on one boss, against the other damage classes?

All values are DPS on one level 63 boss. The start values come from wowsims (master of 1 November 2026). The increase with gear comes from the damage model.

"Pure average" is the average DPS of the best spec of each pure damage class (Warrior, Rogue, Hunter, Mage, Warlock) in wowsims. Each spec uses the best set from the same pre-raid item pool (part 7). The design target for a hybrid class is 95% of the pure average. Players report this target from developer comments. No official text gives the number.

## Short answer

- **The live Retribution is above the target.** It does 906 DPS in wowsims: 108% of the pure average at fresh 60. In Naxxramas, it is 104% (model), 9 points above the target.
- **The wowsims update of 1 November** gives Retribution +7% (848 → 906): a new rotation, the Unsealed Wrath fix and new weapon oils.
- **The Holy Strike Seal trigger (C1) gave +5.3–5.7%.** With C1, Retribution had 114% of the pure average at fresh 60 and 110% in Naxxramas.
- **C1 is withdrawn (2 November 2026).** It put Retribution 15–19 points above the target, and Sacred Arbiter +10% removed only 0.7 points. The C1 rows below stay for reference.
- **Retribution increases less with gear than Fury:** ×1.65 against ×1.73 to Naxxramas. Fixed base values in the Paladin spells cause this. No talent change can fix it.
- **Judgement of the Crusader** adds +9.0% at fresh 60 and +6.0% in Naxxramas.

## 1. Against the pure average

wowsims values with the same item pool for each spec, with enchants and consumables (part 7): Fury Warrior 902, Combat Rogue 685, Hunter 829, Fire Mage 916, Demonology Warlock 919. The pure average is 850. Without the Rogue, it is 891. Retribution does 921 in the same runs.

- **At fresh 60,** the live Retribution is 108% of the pure average and 102% of Fury. With C1 (withdrawn), it was 114% and 108%.
- **Without the Rogue,** the live version is 103%. C1 gave 109%.
- **The tables use ratios.** Retribution (906, full buffs and consumables) is the start value. The other classes keep their ratio to Retribution in the same item pool runs.

The increase of Hunter, Mage and Warlock with gear is not known. The table uses ×1.75 to Naxxramas. The method part gives ×1.60 and ×1.90.

| Build | Fresh 60 | Pre-raid | Molten Core | Blackwing Lair | Naxxramas |
| --- | --- | --- | --- | --- | --- |
| **Live** | **108%** | **107%** | **107%** | **105%** | **104%** |
| C1 (withdrawn) | 114% | 114% | 113% | 111% | 110% |
| C1 (withdrawn), Sacred Arbiter +10% | 113% | 112% | 112% | 110% | 109% |
| C1 (withdrawn), Sacred Arbiter +0% | 112% | 111% | 110% | 108% | 108% |
| Live, no more spell damage on plate after fresh 60 | 108% | 105% | 102% | 98% | 96% |
| C1 (withdrawn), no more spell damage on plate after fresh 60 | 114% | 111% | 108% | 104% | 101% |

- **The live version is above the target at all gear levels.** It is 13 points above at fresh 60 and 9 points above in Naxxramas.
- **C1 was 15–19 points above the target.** At fresh 60, Retribution with C1 was 8% above Fury.
- **Spell damage on plate gear is important.** Without new spell damage on plate items, the live Paladin has only 96% in Naxxramas.
- **Why C1 is withdrawn.** It gave one Seal rule for all melee attacks and +2.6% tank threat. Retribution reaches the target without it, and the tank threat is already above the Warrior (see Threat).
- **The balance lever is Sacred Arbiter (W15).** If raid logs confirm the wowsims level, decrease it to +10%: −0.7% damage in wowsims. This change alone does not bring Retribution to 95%. With C1, the gain fell only from +5.5% to +4.5%.
- **Check again later.** The pure average uses wowsims of 1 November. A wowsims update can change the other classes.

## 2. Where the damage comes from

Fresh 60, raid buffs, 2 min fight, wowsims rotation (plan 1 + 3, model).

| Source | Live | Share | With C1 (withdrawn) | Share |
| --- | --- | --- | --- | --- |
| Auto attacks | 115 | 35% | 116 | 33% |
| Seal of Command | 81 | 25% | 96 | 27% |
| Judgement | 51 | 15% | 51 | 15% |
| Holy Strike | 45 | 14% | 45 | 13% |
| Seal of Righteousness | 18 | 5% | 21 | 6% |
| Hammer of Wrath (last 20% of the fight) | 22 | 7% | 22 | 6% |
| **Total** | **332** | | **351 (+5.6%)** | |

- **About 65% of the damage is Holy damage** (67% with C1). Boss armor does not decrease it.
- **C1 let Holy Strike trigger the active Seal.** This gave about one extra Seal hit each 10 sec, with no mana cost.

## 3. Increase with gear

The five gear levels of Threat, part 2. Each level gives 17.5% more stats from gear. Retribution, Fury, Arms and Combat Rogue have the same gear and buffs.

| Gear level | Retribution | Retribution, no more spell damage on plate | Fury | Arms | Combat Rogue |
| --- | --- | --- | --- | --- | --- |
| Fresh 60 | ×1.00 | ×1.00 | ×1.00 | ×1.00 | ×1.00 |
| Pre-raid best | ×1.12 | ×1.10 | ×1.14 | ×1.10 | ×1.12 |
| Molten Core | ×1.29 | ×1.23 | ×1.30 | ×1.25 | ×1.25 |
| Blackwing Lair | ×1.44 | ×1.35 | ×1.50 | ×1.40 | ×1.41 |
| Naxxramas | ×1.65 | ×1.53 | ×1.73 | ×1.59 | ×1.61 |

**Retribution as a % of Fury**

| Gear level | Live | Live, no more spell damage on plate | Live, flatter gear | C1 (withdrawn) | C1 (withdrawn), no more spell damage on plate | C1 (withdrawn), flatter gear |
| --- | --- | --- | --- | --- | --- | --- |
| Fresh 60 | 102% | 102% | 102% | 108% | 108% | 108% |
| Pre-raid best | 101% | 98% | 101% | 106% | 104% | 106% |
| Molten Core | 101% | 97% | 101% | 107% | 102% | 106% |
| Blackwing Lair | 98% | 92% | 99% | 104% | 97% | 104% |
| Naxxramas | 98% | 90% | 98% | 103% | 95% | 103% |

**Why Retribution increases less**

| Source | Increase to Naxxramas |
| --- | --- |
| Seal of Command | ×1.79 |
| Auto attacks | ×1.71 |
| Holy Strike | ×1.68 |
| Judgement | ×1.51 |
| Seal of Righteousness | ×1.44 |
| Hammer of Wrath | ×1.30 |
| **Retribution** | **×1.65** |
| Fury Warrior | ×1.73 |

- **About 19% of the damage is fixed base values.** Gear does not change them. Examples: Judgement 178.2, Seal of Righteousness 67.5 for each hit, Hammer of Wrath 498.
- **About 17% comes from spell damage,** with small coefficients (12–43%).
- **Only about 65% increases with the weapon and Attack Power.** For Fury and Rogue, it is almost 100%.
- **Hit.** Retribution has 6% hit at fresh 60, near the 8% cap. The classes with two weapons start at 27% miss. Thus, each hit point helps them until Naxxramas.
- **Fury is the outlier.** In Naxxramas, the live Retribution is 117% of Arms (same gear, model) and 138% of Combat Rogue.

## 4. Judgement of the Crusader

Judgement of the Crusader adds 161 Holy damage taken. Each hit receives 161 × its spell damage coefficient. The other parts do not include it.

| Build | Fresh 60 | Naxxramas |
| --- | --- | --- |
| Live | +30 (+9.0%) | +33 (+6.0%) |
| C1 (withdrawn) | +32 (+9.2%) | +35 (+6.1%) |

- **The +161 does not increase with gear.** Thus, its percentage decreases in raids.
- **Personal Judgement of the Crusader (C2)** lets each Retribution Paladin keep its own Crusader.

## 5. Mana and the Seal plans

The wowsims rotation uses plan 1 + 3: 1 swing with Seal of Righteousness, then 3 swings with Seal of Command. The first swing with the new Seal releases the stored copies. The copies of Seal of Command ignore the 1 sec cooldown of the proc. The mana pool is 3,029 (fresh 60, Blessing of Wisdom).

| Seal plan | wowsims: live, full buffs, 2 min | Model: damage | Model: mana each sec | Model: mana empty after |
| --- | --- | --- | --- | --- |
| 1 + 3 (wowsims rotation) | 906 DPS | 100% | 27.8 | 3 min 43 sec |
| 1 + 2 | −0.4% | 99.2% | 35.6 | 2 min 21 sec |
| 2 + 2 | −1.8% | 97.5% | 27.8 | 3 min 43 sec |
| 1 + 1 (a Seal change after each swing) | −3.0% | 97.5% | 51.2 | 1 min 21 sec |
| 3 + 1 | −5.9% | 94.9% | 27.8 | 3 min 43 sec |
| Seal of Command only | — | 85.7% | 10.2 | No limit |

- **Plan 1 + 3 is the best plan.** A copy of Seal of Command has more value than a copy of Seal of Righteousness.
- **At fresh 60, plan 1 + 3 lasts for a 3 min fight.** In a 5 min fight, plan 3 + 3 is the best (−2.5%). In Naxxramas, plan 1 + 3 lasts 5 min.
- **In wowsims, the mana lasts 5 min,** because the consumables include Major Mana Potion.
- **A 20% Seal cost decrease on Unsealed Wrath (W29)** gives 0% in a 2 min fight and +2.6% in a 5 min fight (model). In wowsims, it gives 0%.
- **The model tables of this tab use plan 1 + 3 and no mana limit.** The start value (906) comes from wowsims with the same plan.

## 6. Stat values

Live, raid buffs, 5 min fight (model).

| Stat | DPS for each point |
| --- | --- |
| 1 spell damage | 0.17 |
| 1 Attack Power | 0.11 |
| 1 Strength | 0.26 |
| 1 Intellect | 0.12 |
| 1% critical hit | 4.9 |
| 1% hit (up to the cap) | 4.7 |

- **1 spell damage is worth about 1.5 Attack Power.** Plate items with spell damage are good for Retribution, and Warriors do not want them.
- **Two-Handed Weapon Specialization 3/3** gives +6.5 DPS (+2.0%). It now increases only physical damage.
- For the wowsims stat weights, see builds/retribution.md.

## 7. Check with wowsims

Default Retribution gear, rotation and consumables. One level 63 boss, 3,000 iterations. "Lean buffs" is a small set of buffs.

| Case | 2 min | 5 min |
| --- | --- | --- |
| Live, full buffs | 906 | 914 |
| C1 (withdrawn), full buffs | 956 (+5.6%) | 962 (+5.3%) |
| Live, lean buffs | 653 | 660 |
| C1 (withdrawn), lean buffs | 690 (+5.6%) | 696 (+5.5%) |
| Fury Warrior, pre-raid gear | 826 | 821 |
| Arms Warrior, pre-raid gear | 729 | 723 |

- **C1 (withdrawn):** +5.3–5.6% in wowsims, +5.6–5.7% in the model. They agree.
- **No run is out of mana.**
- **The wowsims update of 1 November,** step by step: 836 → 852 (Unsealed Wrath fix) → 889 (new rotation and presets) → 901 (new weapon oils), in the wowsims test suite.
- **wowsims Fury.** With the wowsims test sets, the live Retribution is 110% of Fury, but the two sets have different quality. With the same item pool, enchants and consumables, it is 102% of Fury (see below).

**Same item pool for each spec (2 November 2026).** This run gives the pure average of parts 1 and 3. All specs take their items from one pre-raid pool. The best set for each spec comes from a search in wowsims.

- **Item pool.** Uncommon, rare and epic items of item level 63 or lower, for level 60 or lower. No raid drops, no world boss drops, no PvP items and no PvP reputation items. Items with random enchantments are not in the pool. Each spec keeps its armor and weapon types, and its weapon setup (two-handed weapon, two weapons, or weapon and off-hand item).
- **Search.** The start is the wowsims test set, without the items outside the pool. For each slot, the search tests the best items for the stat values of the spec, and all items with an effect. It keeps the best item, and repeats until no slot changes.
- **Same conditions for all.** Retribution raid buffs and debuffs, with Judgement of the Crusader. Level 63 boss, 2 min, 10,000 iterations. The class weapon items stay (oils, stones, poisons).
- **Enchants.** The wowsims preset enchants of each spec, slot by slot. Mage and Warlock have no enchanted preset: they use the Balance Druid caster enchants, with +30 spell power on the weapon.
- **Consumables.** Each spec keeps its wowsims flask, food and potions. All specs use the same elixirs and extra items: all of those in the six presets. The Hunter preset has no flask, thus the Hunter uses the Fury flask. The Fire Mage keeps its own elixirs, because the full list stops the sim. Physical elixirs do not help a caster: the Warlock changes by 0.2%.

| Spec | No enchants, no consumables | Enchants | Consumables | Enchants and consumables | Average item level | Epic items |
| --- | --- | --- | --- | --- | --- | --- |
| Fury Warrior | 678 | 754 | 825 | 902 | 59.6 | 12 |
| Hunter | 674 | 720 | 779 | 829 | 59.8 | 7 |
| Fire Mage | 662 | 713 | 862 | 916 | 58.9 | 11 |
| Demonology Warlock | 655 | 710 | 861 | 919 | 59.0 | 8 |
| Combat Rogue | 545 | 578 | 648 | 685 | 59.4 | 9 |
| **Pure average** | **643** | **695** | **795** | **850** | | |
| **Retribution, live** | **682 (106%)** | **729 (105%)** | **870 (109%)** | **921 (108%)** | **59.6** | **12** |
| Retribution, % of Fury | 101% | 97% | 106% | 102% | | |

- **Parts 1 and 3 use the last column.** The start value of the model (906) has full buffs and consumables. Thus, the other classes need the same.
- **Enchants decrease the Retribution lead by 1 point.** The physical enchants help Fury most.
- **Consumables increase the Retribution lead by 3 points.** Retribution uses physical elixirs and spell elixirs. A pure class uses only one of the two groups.
- **The two together give +2 points:** 108% of the pure average, and 102% of Fury.
- **The wowsims presets are not the same for each class.** With each preset as it is, Retribution has 113% (9 elixirs). The Rogue preset has no elixir. Thus, this run gives the same elixirs to all specs.
- **The Rogue is low in this sim.** Without the Rogue, the pure average is 891, and Retribution is 103%.
- **Limits.** Many Forever items have no source in the game data. Some reputation and crafted items from later content can stay in the pool. The same rule applies to all specs. The search can stop at a local best set.
- **wowsims links.** The final set of each spec, with enchants, consumables, raid buffs and the fight: [Fury Warrior](https://wowsims.github.io/forever/warrior/dps/#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), [Combat Rogue](https://wowsims.github.io/forever/rogue/dps/#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), [Hunter](https://wowsims.github.io/forever/hunter/dps/#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), [Fire Mage](https://wowsims.github.io/forever/mage/dps/#eJzEVE1oK1UUzrkzL3Pm5D0yvY3leu0iL/X5XkcLN4mB/ogZC2K11RRX4qLUH8RIaV1U7UYoRagu1KKl0OBCWku1RFqjCxMoQnARF4oIqeCmpVgULdh0obgRuTPTNgvpTj2Lueeec77vm3MuHOpGcEBAEm7BJDwPL8I8wOsA7wN8CMATfpbpbD94MALj8ATIZhTJQfkqWVgrgzjpJAubn4EoeWTiL8tAJn6zBBTFxrQoD5OF9Q0QrSGysFIGsT9EJh69DWTh9kKI3imDrjRxb0Oj3zh2yMSVT7T/5RcOWTj/uyManWTibys6+NF78VTSaRRv/To1/uYabAG9VVwsHq/Hj9bjO/DXH84BvFYcxqA3D2qsR+VURuUySqWVSvflcjmllEpnsiqdzapsuk+pbIOZ37LYIfvJpDsJZZRM/PMdSIkKuw0NbpdYGNEZYn1pfkP2UKfbgQZnT0akfWqEBYcQI/vBl2eeeWq2ODPNczJLvfwmdbkJBG7XQZe1qkJeIYMgS9dSMbJPoY1dn9yWlq7A7wv8FfkSTfEXaFD2k3QFGvxaHYhM3P4UOHNYwJQ7y9X+KXePdC/B3ktXU0R4ClpxvyCDg6dkkrpdicDjdbh6ARIQ0g5G+CNyhO7n99HdspdiP0SRTNytCgGhml3zO9utChmOcLk52t7zcnNUhifvkgmKVUBzfK05/P/4scB75HUSbhdGOW5BMBSJJaa9zeBnNwvnA9svCMNdg/YneFg+RN1cBrIVX7bWeJTs70ztVltjmZvhi1dbY3THAggy8N0J2eHGMcrZ0xFp0RUyBgZu+O3qVn2qc3xwXYOz64XIJVw/s2dPWMYHEUNILRp2xLcJryNwEt7tpVVtX+WvP+fbXj5zwISVzLufs8j/YrPefyJz18f/ms6A/338A++BMOBN6p23CsHtIO8auPTYcNtqVG3rTy/JOZhjfwcAAP//EhnJbg==), [Demonology Warlock](https://wowsims.github.io/forever/warlock/dps/#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), [Retribution](https://wowsims.github.io/forever/paladin/retribution/#eJzEV11sE1cW9hnb4+tjnElunGRyCWTWEEhmN+x4vJaABWISdhfIZtdN1EKlqmVIhsTIianHiahUVfSPHxXRPlAqeKAVBglFtPy0DxAVqaKloryUqhVtqSipq0pVG5SUBx7cl2rGcfxDfopK2/swGp85Puc7373nO7pYR6AcRJCgEbZAH+yAXQB7Ad4AOAlAfdZXzvy6HMKwHiKwGdhLNcRdzrGnkSejW8XxSnSR58+CuNeFDvLDQUAXef8EiJ/w6CIfvCOI35ahi7x3AsTdPnSRq6dAPBBGBzl4rRxd5Ke3IBvhq1Mg3ipDB9k7Vo4Oss96HjoL6CBnXjVj/nwIxLEytKGDfHzX628vvxJtvB1T7m6NTCw4At4bay9HPowc6rrwxM0DMAyLTml7ovujB6LDJ+HLlHArJXyTEtIp4buU8GNKGEsJ4ylhFF6ITsCFk0IrybIQhhGuXgkpakhRFLU5pASalZAaDCqBgKoEgkogGApc4RzXOC7NjftwKc5Pg4jVa7uT0SEtqUuaYUR7B/QeSRtMaH6CPDqaVcVACX3DUIFChp+HGBmMxaSENtCrF3gsxto0VKMvktB3SF26FpPi26S2eH+/NtDjd6ET7c1BA/+G9WmoQ1bk1Rnt7Uvq8UFjQDcMvxtd6GwOLAsZ2IR1aajFmjbNSOahbR/s6dX79YFkgStdzPxY5p+HeIe40NlIyM1IGgT0dsSHdCkZl/r1mK7TWlaD3gyPSDb9W+od1BI9jEcHOX0UrAAL5TrCU26ljfkyfAUK6/SY9pTUoW2PJ6S2dcZKG21lYfwHU7FWriFAPUc4gnyjnZy+CGYg5BQDq+RKYqfOOy6O2JnFj7JMNdiUI/0v24gtdHUJEPT6Peg+BpN4cEGGZyhuNGuVEroWixr90o5EPKl3J6PxAZYrkjawRViT4X1Iu/rig7EeKaFvS+hGn9QVb7OSOsn5FMzm1mm5EXL5KNBKVpGGMpzXFh8w9O6EZuaiAvOmAZH8a2c80R01+kW73DDTmaEe5rbAOcnFiLxuxr2jTWwpzs/wIlav14xpHCxQPPnsKMjd058q2s424Gr6T6z3L5g1FIoZvgorHzb00hB5guTjMNuppC8Cew5wiCbnzrYww8/H2sJsRaEwwP6OdX42MyoU/F70pIkJDshrr0N+g+SvHaVnegLYbcD9QPfB7LgKI2IHa58FgN8vzVnGVLiXd0WyrZfmXOjsjw/pAfpY7qVqGCiWZ3gvejpMuFndoN6EB913SK75yFQbuvxOtI84bBQLDm9Zoqix6XVgnwIa9MnZCzabtYhKE2kpt3NsRXFhaq4w9bcWlm230sJ2AXsGgzQw9yErxhWk/8m93C+uEghyT77P6Wb2CLbTDZakOanzEjclaZY8V8iCKZdbbczS94DSUCpiFspjkAtuCQNPrkbkaInEPMo2PdhM2cPzbgpU/0wcUit+MjGoq/XTbn6BQ8MsnVDgVnvPzKCTY0H1Fc7NrFUNqb7iXXKiHSGkrsqPBarQZRYrfMlICRg5cwFZplndzU03C+g40LEH3vcr2XL03OCnWhWb6FL0nIO8QZSriYN6RvImlkWMYbbm3vb8K21C7w0ec85iNgJPPZeAoIN8sSciArN4CswxI9Wr0xHRSd/m6BnOyj5XqfdoRRHUNWzVfer4jNxZalDIXdZQxJ1lynH3EPv/r5C2AjKtf0+SCTkyP8+TGZyLzNaZv9El8mLioO7hXDeyqnMcJRx1H3PlLKb0fc/1THDqs3abtVaER8CBHNr8e+zurOnxcEX2xReuPXLYXB+1/GWbta63qKOc6JJa5POc7U9ZyfAfkmbJm79bnhXWs/N4eO2kIbzFvCkdhuyv0RbZTl75X2vBhUopuDSZV6udsJP7JQAA//+a1vNp). A later wowsims version can give a different DPS.
- **Files.** `models/wowsims-b2/matched_gear/` (search scripts, sets and logs).

**All damage specs with the wowsims test sets (2 November 2026).** Each spec uses its wowsims test character with pre-raid gear: dungeon, quest, craft and early reputation items. No raid or PvP items. The same raid buffs for all, no consumables (poisons and weapon stones from the class stay). 2 min, 3,000 iterations. The pure average is the best spec of each pure class: 600 DPS.

| Spec | DPS | % of the pure average |
| --- | --- | --- |
| Fury Warrior | 703 | 117% |
| Hunter | 643 | 107% |
| Demonology Warlock | 576 | 96% |
| Rogue | 566 | 94% |
| Fire Mage | 515 | 86% |
| Feral Druid | 674 | 112% |
| **Retribution, live** | **672** | **112%** |
| Shadow Priest | 597 | 99% |
| Enhancement Shaman | 525 | 87% |
| Balance Druid | 496 | 83% |
| Elemental Shaman | 405 | 67% |

- **The gear is not the same for each class.** The sets have different quality: Retribution has 7 epic items, the Hunter and the Warlock have 1. Ret in the Warrior armor does 571 (−15%), and the Warrior in the Ret armor does 562 (−20%). Thus, parts 1 and 3 use the same item pool run above.
- **Retribution and Feral are 12% above the pure average.** The other hybrids are at 67–99%. In this sim, no hybrid group is at 95%.
- **Changes to the test sets.** Fury uses the wowsims pre-raid Fury set, with Dark Iron Destroyer in place of Annihilator (a world drop). The raid and PvP items of the Mage set are replaced with the Warlock choices. The new blue items of Forever (for example Adaptive Combat Assistant) have no source in the game data. All sets keep them.
- **Files.** `models/wowsims-b2/allspecs_main.go` and `allspecs.log`.

## 8. Options that were not kept

- **Burning Zeal (C-R4).** +0.8% at fresh 60 to +1.4% in Naxxramas. Withdrawn: the live Retribution is already above the target.
- **Measure for Measure (C-R5).** About +1% at all gear levels. Withdrawn.
- **Holy Strike Seal trigger (C1).** +5.3–5.7% at all gear levels. Withdrawn on 2 November 2026: Retribution is already above the target.
- **Twist of Light (C-R2).** The live version removes it. Unsealed Wrath takes its place.

## 9. Inputs of the model

**Build.** The wowsims default Retribution build, 14/6/31 ([`b2050250002-501-05233011201301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2050250002-501-05233011201301351)).

- Holy: Divine Strength 5/5, Reverence 2/2, Improved Seals 5/5, Holy Conduit 2/2.
- Protection: Divine Intellect 5/5, Precision 1/1.
- Retribution: Benediction 5/5, Improved Judgement 2/2, Conviction 3/3, Sanctified Judgement 3/3, Unyielding Faith 1, Seal of Command, Pursuit of Justice 2, Sacred Arbiter, Two-Handed Weapon Specialization 3/3, Repentance, Vengeance 3/3, Champion of the Light 5/5, Unsealed Wrath.

**Gear.** Fresh 60 gear (crafted, dungeon and quest items). Weapon: Stormcarver, 155–233 damage, 3.6 sec, +32 spell damage. With talents and raid buffs: 1,244 Attack Power, 326 spell damage, 6% hit, 12.6% critical hit, 3,029 mana.

**Fight**

- Raid buffs: Blessing of Kings, Blessing of Might, Battle Shout, Mark of the Wild, Blessing of Wisdom. No consumables, no Judgement of the Crusader.
- Boss: level 63, 976 armor after debuffs. The Paladin attacks from behind: no parry and no block.
- 8% miss, 6.5% dodge, 40% glancing blows (−35% damage), critical hit −4.8%.
- 2 min fight. A 5 min fight gives +0.6%.

**Spells**

- Unsealed Wrath: each auto attack that lands stores a copy of the active Seal (3 copies). A swing with the other Seal releases them. Seal of Command copies ignore the 1 sec cooldown of the proc.
- Seal plan 1 + 3, the wowsims rotation: 1 swing with Seal of Righteousness, then 3 swings with Seal of Command.
- Seal of Command: 7 procs each min, 70% of weapon damage + 23.3% of spell damage.
- Seal of Righteousness: 67.5 + 12% of spell damage for each hit.
- Judgement: one each 8 sec, 178.2 + 42.9% of spell damage.
- Holy Strike: one each 10 sec, 50% of (weapon damage + 93 + 42.9% of spell damage). Sacred Arbiter +20%.
- Hammer of Wrath: one each 6 sec in the last 20% of the fight, 498 + 42.9% of spell damage.
- Improved Seals ×1.15 (Seals and Judgements). Two-Handed Weapon Specialization ×1.06 (physical only). Conviction +6% critical hit. Vengeance: average +5.4%.
- Not in the model: Exorcism, Consecration, Retribution Aura.

**Other gear growth cases (live / C1 withdrawn, Naxxramas):** ×1.60 gives 110% / 116%. ×1.90 gives 99% / 104%.

## 10. Method and limits

- **Scripts.** `models/beta-30-oct/retribution_b2.py` (model) and `damage_tables_b2.py` (tables). wowsims tests in `models/wowsims-b2`. Other classes: wowsims with the same item pool (part 7) and `models/damage` (increase with gear of Fury, Arms and Combat Rogue).
- The model calculates averages. It is not a full simulation.
- Not confirmed: the critical hit decrease against a boss, and the Seal of Righteousness value with a 3.6 sec weapon.
- The Fury and Combat Rogue rotations and talents are assumptions. Arms uses the wowsims rotation.
- The gear levels are estimates with Classic steps. The Forever raid items are not known.
