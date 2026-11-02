# Damage

**Question.** How much damage does Retribution do on one boss, against the other damage classes?

All values are DPS on one level 63 boss. The start values come from wowsims (master of 1 November 2026). The increase with gear comes from the damage model.

"Pure average" is the average DPS of the best spec of each pure damage class (Warrior, Rogue, Hunter, Mage, Warlock) in wowsims. Each spec uses the best set from the same pre-raid item pool (part 7). The design target for a hybrid class is 95% of the pure average. Players report this target from developer comments. No official text gives the number.

## Short answer

- **The live Retribution is above the target.** It does 906 DPS in wowsims: 112% of the pure average at fresh 60. In Naxxramas, it is 107% (model), 12 points above the target.
- **The wowsims update of 1 November** gives Retribution +7% (848 → 906): a new rotation, the Unsealed Wrath fix and new weapon oils.
- **The Holy Strike Seal trigger (C1) gave +5.3–5.7%.** With C1, Retribution had 118% of the pure average at fresh 60 and 113% in Naxxramas.
- **C1 is withdrawn (2 November 2026).** It put Retribution 18–23 points above the target, and Sacred Arbiter +10% removed only 0.7 points. The C1 rows below stay for reference.
- **Retribution increases less with gear than Fury:** ×1.65 against ×1.73 to Naxxramas. Fixed base values in the Paladin spells cause this. No talent change can fix it.
- **Judgement of the Crusader** adds +9.0% at fresh 60 and +6.0% in Naxxramas.

## 1. Against the pure average

wowsims values with the same item pool, enchants and consumables for each spec (part 7). Fury Warrior 805, Combat Rogue 646, Hunter 800, Fire Mage 824, Demonology Warlock 846. The pure average is 784. Without the Rogue, it is 819. Retribution does 874 in the same runs.

- **At fresh 60,** the live Retribution is 112% of the pure average and 109% of Fury. With C1 (withdrawn), it was 118% and 115%.
- **Without the Rogue,** the live version is 107%. C1 gave 113%.
- **The tables use ratios.** Retribution (906, full buffs and consumables) is the start value. The other classes keep their ratio to Retribution in the same item pool runs.

The increase of Hunter, Mage and Warlock with gear is not known. The table uses ×1.75 to Naxxramas. The method part gives ×1.60 and ×1.90.

| Build | Fresh 60 | Pre-raid | Molten Core | Blackwing Lair | Naxxramas |
| --- | --- | --- | --- | --- | --- |
| **Live** | **112%** | **111%** | **110%** | **108%** | **107%** |
| C1 (withdrawn) | 118% | 117% | 116% | 114% | 113% |
| C1 (withdrawn), Sacred Arbiter +10% | 117% | 116% | 115% | 113% | 112% |
| C1 (withdrawn), Sacred Arbiter +0% | 115% | 114% | 114% | 112% | 111% |
| Live, no more spell damage on plate after fresh 60 | 112% | 108% | 105% | 101% | 99% |
| C1 (withdrawn), no more spell damage on plate after fresh 60 | 118% | 114% | 111% | 107% | 104% |

- **The live version is above the target at all gear levels.** It is 17 points above at fresh 60 and 12 points above in Naxxramas.
- **C1 was 18–23 points above the target.** At fresh 60, Retribution with C1 was 15% above Fury.
- **Spell damage on plate gear is important.** Without new spell damage on plate items, the live Paladin has only 99% in Naxxramas.
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
| Fresh 60 | 109% | 109% | 109% | 115% | 115% | 115% |
| Pre-raid best | 107% | 105% | 107% | 113% | 111% | 113% |
| Molten Core | 107% | 103% | 107% | 113% | 109% | 113% |
| Blackwing Lair | 104% | 98% | 105% | 110% | 104% | 111% |
| Naxxramas | 104% | 96% | 104% | 110% | 101% | 110% |

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
- **Fury is the outlier.** In Naxxramas, the live Retribution is 117% of Arms (same gear, model) and 139% of Combat Rogue.

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
- **wowsims Fury.** With the wowsims test sets, the live Retribution is 110% of Fury, but the two sets have different quality. With the same item pool, enchants and consumables, it is 109% of Fury (see below).

**Same item pool for each spec (2 November 2026).** This run gives the pure average of parts 1 and 3. All specs take their items from one pre-raid pool. The best set for each spec comes from a search in wowsims.

- **Item pool.** Uncommon, rare and epic items of item level 63 or lower, for level 60 or lower. Only content of the game start and Dire Maul: no Classic items of patch 1.6 or later (item ids 19000–23999). Thus, no Zul'Gurub, Ahn'Qiraj or Naxxramas era items, no dungeon set 2 and no battleground rewards. No raid drops, no world boss drops and no PvP items. No items that need Revered or Exalted reputation. Items with random enchantments are not in the pool. Each spec keeps its armor and weapon types, and its weapon setup (two-handed weapon, two weapons, or weapon and off-hand item).
- **Search.** The start is the wowsims test set, without the items outside the pool. For each slot, the search tests the best items for the stat values of the spec, and all items with an effect. It keeps the best item, and repeats until no slot changes.
- **Same conditions for all.** Retribution raid buffs and debuffs, with Judgement of the Crusader. Level 63 boss, 2 min, 10,000 iterations. The class weapon items stay (oils, stones, poisons).
- **Enchants.** The wowsims preset enchants of each spec, slot by slot. Mage and Warlock have no enchanted preset: they use the Balance Druid caster enchants, with +30 spell power on the weapon.
- **Consumables.** Each spec keeps its wowsims flask, food and potions. All specs use the same elixirs and extra items: all of those in the six presets. The Hunter preset has no flask, thus the Hunter uses the Fury flask. The Fire Mage keeps its own elixirs, because the full list stops the sim. Physical elixirs do not help a caster: the Warlock changes by 0.2%.

| Spec | No enchants, no consumables | Enchants | Consumables | Enchants and consumables | Average item level | Epic items |
| --- | --- | --- | --- | --- | --- | --- |
| Fury Warrior | 593 | 663 | 736 | 805 | 58.6 | 5 |
| Hunter | 652 | 704 | 745 | 800 | 59.2 | 4 |
| Fire Mage | 581 | 629 | 772 | 824 | 57.6 | 3 |
| Demonology Warlock | 589 | 643 | 789 | 846 | 57.0 | 3 |
| Combat Rogue | 514 | 546 | 615 | 646 | 58.5 | 3 |
| **Pure average** | **586** | **637** | **731** | **784** | | |
| **Retribution, live** | **646 (110%)** | **692 (109%)** | **824 (113%)** | **874 (112%)** | **59.1** | **5** |
| Retribution, % of Fury | 109% | 104% | 112% | 109% | | |

- **Parts 1 and 3 use the last column.** The start value of the model (906) has full buffs and consumables. Thus, the other classes need the same.
- **Enchants decrease the Retribution lead by 1 point.** The physical enchants help Fury most.
- **Consumables increase the Retribution lead by 3 points.** Retribution uses physical elixirs and spell elixirs. A pure class uses only one of the two groups.
- **The two together give +2 points:** 112% of the pure average, and 109% of Fury.
- **The wowsims presets are not the same for each class.** With each preset as it is, Retribution has 116% (9 elixirs). The Rogue preset has no elixir. Thus, this run gives the same elixirs to all specs.
- **The Rogue is low in this sim.** Without the Rogue, the pure average is 819, and Retribution is 107%.
- **The later items helped the pure classes more.** With the first pool (ZG, AQ, battleground and dungeon set 2 items), Retribution had 108% and Fury 102%. Retribution keeps Forever items (Vindicator's Belt, Timbermaw Tunic) and Arcanite Reaper.
- **Limits.** Many Forever items have no source in the game data. They stay in the pool. The same rule applies to all specs. The search can stop at a local best set.
- **wowsims links.** The final set of each spec, with enchants, consumables, raid buffs and the fight: [Fury Warrior](https://www.wowsims.com/forever/warrior/dps/#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), [Combat Rogue](https://www.wowsims.com/forever/rogue/dps/#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), [Hunter](https://www.wowsims.com/forever/hunter/dps/#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), [Fire Mage](https://www.wowsims.com/forever/mage/dps/#eJzEVE9IdFUUn3Pf++add+aT97xOcru5mG/s6/t8JdyZacA/0byEyNIaaRUtxP4QTYi2sBLcmAS2KaUkcHAhGlhWFLZpBiSVFtOiiMKCNookWblwXBQtirjvPXUW4a6+s7j3nvs75/e751w41IbggoAU3IQReB5ehGmA1wGWAd4D4MkAZRrtAh/6YQieAPldHMlFOUUWVmdAnLRQHE+mRNknEw+3HDLx63mgONbGxId9ZOEH246o95KFR3Mg9np11JzGt8Z0roXv/OLqQBPLv7pk4qvHev3ic73+teSQhdO/u6LWQiYubzeRie8vOemUWyvd/G106I0VWAd6szRbOl51DledT+DvP9x9eK3Uh2FlPlRZu8qrrMpnlcoolenM5/NKKZXJ5lQml1O5TKdSuRozv2GJA/azSXcSyjiZ+OdbkBYb7DY0uF1m0Y1GiHVm+HXZTi1eMxqcPRmT9qkRBRxAguwHXx5/5qmJ0vgYz8scdfAb1OolEbi9AzqsXhHyChkEOWpKJ8g+hQZ2vXNbWjoCfyjyV+RLNMpfoB7ZRdITaPCmHSAy8eNPgTOXhUz5M6z6b9g90rsk9166mibCU9CKe0UZbjwtU9TmSQTu7MDViyQBEW1PjD8i++l+fh/dLTso8WMcycTNihAQqdnVoLLNipBRCxd2BxprXtgdkNHOW2WSEhugOb7SHME7firydnmNhNeKcY7rEDZFYpnp01r42LXiecP2isLwVqDxCx6WD1Ebl6HsRiBbrT1K9remPlbqg9kb0Y9X6oN0xwwIMvDtYdnsORjn7OmYtOgKGd3d14NydakB1Xl+6K7AmXshcgnXEXv2hGWDJGII6VnDjgU27DeHh6R/e3lR25eFa88F9n0hu8+ElSp4n7HYLbEJ/3+Rueuj/0ynO1gff9d/ILrwR/TEW4TQ2y94Bs4/1tcwGFXD8NMjchIm2T8BAAD//6t/ygY=), [Demonology Warlock](https://www.wowsims.com/forever/warlock/dps/#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), [Retribution](https://www.wowsims.com/forever/paladin/retribution/#eJzEV29sU2UX77ltb5+e0t3uWbfdPQx238Jg6/uO9/b2bQK8wMqGCsxp3aJgYpS77bKVdCv2dgv6wQyi/EkI8sGoEIOG8oEsGgxKAotogqLIB8VoEEiQWWNidGQLH/jQT+berusf9kci6vPh5vbc03N+5/c853fyYC0BD4ggQQNsgz7YCcMA+wHeATgJQL3mV874uhLCsBEisBXYgWri9HDsReTJWJc4UYEO8uavHnG/A23k+h5AB/nqMIjf8Oggn30oiD+VoYO8dUYQ93qRJ9e6xENhtJHXrnjQQT4+I2QDXJ8UxFtlaCPD4x60kd3m84u08fz0Ew/yZLJbHC9DC9rI13fdvjbPpWjD7Zh8tysyuegouG+svxj5PPJ657nnbh6CEVjyrrovejB6KDpyEq6nhFsp4ceUkE4JP6eE31LCeEqYSAlj8HJ0Es6dFFpIloMwjHJ1ckhWQrIsK00hOdAkh5RgUA4EFDkQlAPBUOASZ7vCcWluwovLcWEaRKxa352MDqlJTVJ1Pdo7oPVI6mBC9RHk0dakyDpK6B2BchQy/ALEyGAsJiXUgV6twGMp1qShCr2RhLZT6tTUmBTfLrXG+/vVgR6fA+1obQrq+B+sS0MtsiKvjmhvX1KLD+oDmq77nOhAe1NgRUjHRqxNQw1Wt6p6Mg9tx2BPr9avDSQLXOlS5sMy3wLEO8SB9gZCbkbSIKC7PT6kScm41K/FNI3WsGp0Z3hEsuVhqXdQTfQwHm3k1DEwAyz21xKecqstzJvhy1HYoMXUF6R2dUc8IbVu0FdbaAsL4/+YgjX+agLUdZQjyDdYyanzYARCTtax0l9BrNR+x8ERKzP5kVcoOpt2pI+yzdhM15YAQbfPhc7jMIUHF2V4huJmo1YpoamxqN4v7UzEk1p3MhofYLkiaT1bgtUZ3ou0sy8+GOuREtr2hKb3SZ3xVjOpnZxNwVxuHaYbIRePAa1g5WkowwWt8QFd606oRi4qMHcaEMlDu+KJ7qjeL1r99bOdGepiThOcnZyP+DfMune0kS3HhRlexKqNqj6DgwmKJ98dA3/3zKeKtrFNuJb+H+t8i+YMhWKGr8SKJ3WtNESeIP8JmOtU0leA7QEcosn5sy3O8AuxpjBbUSgMsP9irY/NjgoFnxtdaWKAA/LG25DfIP8PttIzPQnsNuBBoAdgblyFEbGdtc0BwOeT5i1jOtyrw5Fs66U5B9r740NagD6Te6kcAYqeDO9GV7sBN6sb1J1wofMOyTUfmW5Dh8+O1lGbhWLB4S1LFDU2vQrsW0CdPj93wUazFlFpIC3ldp6tKC5MyRWm/NnCsu1WWtgwsJcwSAPzH7JiXEH6SO7lfnGVQPD35PucbmVPYRvdZEqandovcNOSZspzuV8w5LLLwkx9D8j1pSJmojwOueCmMPDkcsQfLZGYp9mWB5spe3g+SoHim41DasZPJgY1pW7GzS9wqJ+jEwrcau6ZGXRqLCjewrmZtSohxVu8S3a0IoSUNfmxQGW6wmSFLxkpAT1nLiDLMCt7uZlmAZ0AOv7A+341W4muG/x0q2IjXY6u05A3iP4qYqOu0byJZRFjmK27tz3/TRvRfYPHnLOYjcBT1wUgaCPX9kVEYCZPgXlmpHJ5JiI66AccfZ8zs89X6j1aUQR1HVtznzo+K3emGhRylzUUcWeactw9wR7/A9JWQKb57ykyIUfm93kyg/OR2TL7N7rMv5TYqHMk142s8jRHCUedxx05iyF9v3A9k5yy22ox16rwKNiQQ4tvn9WZNT0bLs++eMM1R48Y68vmf20319VmZYwTHVKz/yxn+UdWMvy3pFn23l+WZ5X57DgRXj9lCG8z7klHIPtrrNlvJYcfaym4TskFVybjYrULdnG/BwAA//8n9/Pw). A later wowsims version can give a different DPS.
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

**Other gear growth cases (live / C1 withdrawn, Naxxramas):** ×1.60 gives 113% / 120%. ×1.90 gives 102% / 107%.

## 10. Method and limits

- **Scripts.** `models/beta-30-oct/retribution_b2.py` (model) and `damage_tables_b2.py` (tables). wowsims tests in `models/wowsims-b2`. Other classes: wowsims with the same item pool (part 7) and `models/damage` (increase with gear of Fury, Arms and Combat Rogue).
- The model calculates averages. It is not a full simulation.
- Not confirmed: the critical hit decrease against a boss, and the Seal of Righteousness value with a 3.6 sec weapon.
- The Fury and Combat Rogue rotations and talents are assumptions. Arms uses the wowsims rotation.
- The gear levels are estimates with Classic steps. The Forever raid items are not known.
