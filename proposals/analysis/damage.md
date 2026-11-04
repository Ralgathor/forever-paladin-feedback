# Damage

**Question.** How much damage does Retribution do on one boss, against the other damage classes?

All values are DPS on one level 63 boss. The start values come from wowsims (master commit 8298ab833 of 4 November 2026, game files of client 1.60.1.70755). The increase with gear comes from the damage model.

"Pure average" is the average DPS of the best spec of each pure damage class (Warrior, Rogue, Hunter, Mage, Warlock) in wowsims. Each spec uses the best set from the same pre-raid item pool (part 7). The design target for a hybrid class is 95% of the pure average. Players report this target from developer comments. No official text gives the number.

## Short answer

- **The live Retribution is above the target.** It does 938 DPS in wowsims: 112% of the pure average at fresh 60. In Naxxramas, it is 108% (model), 13 points above the target.
- **Build 70755 gives Retribution +3.5% in wowsims (906 → 938).** Vengeance stacks up to 5 times, and Two-Handed Weapon Specialization also increases Holy damage. The pure classes lose 0–5% in the same update (part 7).
- **The hotfix 113578 ports of 4 November give the pure classes +5–17% in wowsims.** Fury +6%, Combat Rogue +5%, Hunter +17%. The pure average goes from 770 to 812, and Retribution from 118% to 112% (part 7).
- **wowsims master 8298ab833 (4 November, later) changes the pure classes by −3.5% to +1.4%.** Hunter −3.5% (new reaction times), Demonology Warlock +1.4% (patch of 3 November and new elixirs), Combat Rogue +0.8%, Fury +0.3%. The pure average goes from 812 to 809. Retribution stays at 112%.
- **The wowsims update of 1 November** gives Retribution +7% (848 → 906): a new rotation, the Unsealed Wrath fix and new weapon oils.
- **The Holy Strike Seal trigger (C1) gave +5.3–5.7%.** With C1, Retribution has 119% of the pure average at fresh 60 and 114% in Naxxramas.
- **C1 is withdrawn (2 November 2026).** It puts Retribution 18–23 points above the target, and Sacred Arbiter +10% removed only 0.7 points. The C1 rows below stay for reference.
- **Retribution increases less with gear than Fury:** ×1.65 against ×1.73 to Naxxramas. Fixed base values in the Paladin spells cause this. No talent change can fix it.
- **Judgement of the Crusader** adds +9.0% at fresh 60 and +6.0% in Naxxramas.

## 1. Against the pure average

wowsims values with the same item pool, enchants and consumables for each spec (part 7). Fury Warrior 839, Combat Rogue 672, Hunter 856, Fire Mage 824, Demonology Warlock 856. The pure average is 809. Without the Rogue, it is 844. Retribution does 908 in the same runs.

- **At fresh 60,** the live Retribution is 112% of the pure average and 108% of Fury. With C1 (withdrawn), it is 119% and 114%.
- **Without the Rogue,** the live version is 108%. C1 gives 114%.
- **The tables use ratios.** Retribution (938, full buffs and consumables) is the start value. The other classes keep their ratio to Retribution in the same item pool runs.

The increase of Hunter, Mage and Warlock with gear is not known. The table uses ×1.75 to Naxxramas. The method part gives ×1.60 and ×1.90.

| Build | Fresh 60 | Pre-raid | Molten Core | Blackwing Lair | Naxxramas |
| --- | --- | --- | --- | --- | --- |
| **Live** | **112%** | **111%** | **111%** | **109%** | **108%** |
| C1 (withdrawn) | 119% | 118% | 117% | 115% | 114% |
| C1 (withdrawn), Sacred Arbiter +10% | 117% | 116% | 116% | 114% | 113% |
| C1 (withdrawn), Sacred Arbiter +0% | 116% | 115% | 114% | 112% | 111% |
| Live, no more spell damage on plate after fresh 60 | 112% | 109% | 106% | 102% | 99% |
| C1 (withdrawn), no more spell damage on plate after fresh 60 | 119% | 115% | 112% | 108% | 105% |

- **The live version is above the target at all gear levels.** It is 17 points above at fresh 60 and 13 points above in Naxxramas.
- **C1 is 19–24 points above the target.** At fresh 60, Retribution with C1 is 14% above Fury.
- **Spell damage on plate gear is important.** Without new spell damage on plate items, the live Paladin has only 99% in Naxxramas.
- **Why C1 is withdrawn.** It gave one Seal rule for all melee attacks and +2.6% tank threat. Retribution reaches the target without it, and the tank threat is already above the Warrior (see Threat).
- **The balance lever is Sacred Arbiter (W15).** If raid logs confirm the wowsims level, decrease it to +10%: −0.7% damage in wowsims. This change alone does not bring Retribution to 95%. With C1, the gain fell only from +5.5% to +4.5%.
- **Check again later.** The pure average uses wowsims master 8298ab833 of 4 November. The Warrior, Rogue and Hunter have the changes of hotfix 113578, and the Warlock has the patch of 3 November. The Mage changes of the development notes are not in wowsims yet (W15).

**DPS of each class.** The start values keep the ratio to Retribution of the same item pool runs (part 7), with Retribution at 938. The increase comes from the model. Hunter, Mage and Warlock use ×1.75.

| Spec | Fresh 60 | Pre-raid | Molten Core | Blackwing Lair | Naxxramas |
| --- | --- | --- | --- | --- | --- |
| **Retribution, live** | **938 (112%)** | **1,050 (111%)** | **1,206 (111%)** | **1,351 (109%)** | **1,551 (108%)** |
| Demonology Warlock | 884 (106%) | 999 (106%) | 1,166 (107%) | 1,333 (107%) | 1,548 (108%) |
| Hunter | 884 (106%) | 998 (106%) | 1,165 (107%) | 1,332 (107%) | 1,546 (107%) |
| Fury Warrior | 867 (104%) | 986 (104%) | 1,128 (103%) | 1,299 (104%) | 1,499 (104%) |
| Fire Mage | 851 (102%) | 961 (102%) | 1,122 (103%) | 1,282 (103%) | 1,489 (103%) |
| **Pure average** | **836** | **944** | **1,090** | **1,245** | **1,439** |
| Combat Rogue | 694 (83%) | 774 (82%) | 869 (80%) | 978 (79%) | 1,116 (78%) |

- **Retribution is first at all gear levels.** At fresh 60, it is 6% above the Warlock and the Hunter. In Naxxramas, the three are within 0.3%.
- **The Rogue decreases the pure average.** Without the Rogue, the pure average is 871 at fresh 60 (844 in the item pool run).
- **The calculator Damage cards show these values.**

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
| Fresh 60 | 108% | 108% | 108% | 114% | 114% | 114% |
| Pre-raid best | 107% | 104% | 107% | 112% | 110% | 112% |
| Molten Core | 107% | 103% | 107% | 113% | 108% | 113% |
| Blackwing Lair | 104% | 98% | 104% | 110% | 103% | 110% |
| Naxxramas | 104% | 95% | 104% | 109% | 101% | 109% |

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
- **Two-Handed Weapon Specialization 3/3** gives +6.5 DPS (+2.0%) in the model, on physical damage only. Build 70755 also gives it Holy damage (part 7).
- For the wowsims stat weights, see builds/retribution.md.

## 7. Check with wowsims

Default Retribution gear, rotation and consumables. One level 63 boss, 3,000 iterations. "Lean buffs" is a small set of buffs.

| Case | 2 min | 5 min |
| --- | --- | --- |
| Live, full buffs | 938 | 949 |
| C1 (withdrawn), full buffs | 990 (+5.6%) | 1,000 (+5.3%) |
| Live, lean buffs | 682 | 693 |
| C1 (withdrawn), lean buffs | 720 (+5.6%) | 730 (+5.4%) |
| Fury Warrior, pre-raid gear | 865 | 858 |
| Arms Warrior, pre-raid gear | 814 | 810 |

- **C1 (withdrawn):** +5.3–5.6% in wowsims, +5.6–5.7% in the model. They agree.
- **No run is out of mana.**
- **The wowsims update of 1 November,** step by step: 836 → 852 (Unsealed Wrath fix) → 889 (new rotation and presets) → 901 (new weapon oils), in the wowsims test suite.
- **Build 70755 (master commit d97252f2a, 3 November).** The live Retribution increases from 906 to 938 (+3.5%). The two test flags on master of 1 November gave 981 (+8.3%), thus the game data gives less. wowsims now also uses the trainer ranks of Strength of Earth Totem and Grace of Air Totem in the raid buffs. With the Ruins of Ahn'Qiraj book ranks, Retribution has 949.
- **Master commit 6ee3c30f35 (4 November).** The Paladin values do not change. The hotfix 113578 ports give Fury +7% in the wowsims pre-raid set (807 → 865) and Arms +5% (773 → 814).
- **Master commit 8298ab833 (4 November, later).** The Paladin values do not change. Fury stays at 865 in the wowsims pre-raid set, and Arms goes to 826 (+1.5%).
- **wowsims Fury.** With the wowsims test sets, the live Retribution is 108% of Fury, but the two sets have different quality. With the same item pool, enchants and consumables, it is also 108% of Fury (see below).

**Same item pool for each spec (search of 2 November 2026, values of 4 November).** This run gives the pure average of parts 1 and 3. All specs take their items from one pre-raid pool. The best set for each spec comes from a search in wowsims of 1 November. On 4 November, the same sets ran again on master commits 6ee3c30f35 and 8298ab833. The values below come from commit 8298ab833. The item database of this commit adds no item to the pool.

- **Item pool.** Uncommon, rare and epic items of item level 63 or lower, for level 60 or lower. Only content of the game start and Dire Maul: no Classic items of patch 1.6 or later (item ids 19000–23999). Thus, no Zul'Gurub, Ahn'Qiraj or Naxxramas era items, no dungeon set 2 and no battleground rewards. No raid drops, no world boss drops and no PvP items. No items that need Revered or Exalted reputation. Items with random enchantments are not in the pool. Each spec keeps its armor and weapon types, and its weapon setup (two-handed weapon, two weapons, or weapon and off-hand item).
- **Search.** The start is the wowsims test set, without the items outside the pool. For each slot, the search tests the best items for the stat values of the spec, and all items with an effect. It keeps the best item, and repeats until no slot changes.
- **Same conditions for all.** The full wowsims test raid buffs and debuffs, the same for all specs: melee and caster buffs, totems, auras, and all debuffs with Judgement of the Crusader. Level 63 boss, 2 min, 10,000 iterations. The class weapon items stay (oils, stones, poisons). With the buffs and debuffs of the own wowsims preset of each spec, all six values stay the same.
- **Enchants.** The wowsims preset enchants of each spec, slot by slot. Mage and Warlock have no enchanted preset: they use the Balance Druid caster enchants, with +30 spell power on the weapon.
- **Consumables.** Each spec keeps its wowsims flask, food and potions. All specs use the same elixirs and extra items: all of those in the six presets. The Hunter preset has no flask, thus the Hunter uses the Fury flask. The Fire Mage keeps its own elixirs, because the full list stops the sim. Physical elixirs do not help a caster: the Warlock changes by 0.2%.

| Spec | No enchants, no consumables | Enchants | Consumables | Enchants and consumables | Average item level | Epic items | Set |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Demonology Warlock | 589 | 643 | 799 | 856 | 57.0 | 3 | [Open in wowsims](https://www.wowsims.com/forever/warlock/dps/#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) |
| Hunter | 684 | 740 | 795 | 856 | 59.2 | 4 | [Open in wowsims](https://www.wowsims.com/forever/hunter/dps/#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) |
| Fury Warrior | 611 | 685 | 763 | 839 | 58.6 | 5 | [Open in wowsims](https://www.wowsims.com/forever/warrior/dps/#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) |
| Fire Mage | 583 | 632 | 772 | 824 | 57.6 | 3 | [Open in wowsims](https://www.wowsims.com/forever/mage/dps/#eJzEVE9IdFUUn3Pf++add+aT97xOcru5mG/s6/t8JdyZacA/0byEyNIaaRUtxP4QTYi2sBLcmAS2KaUkcHAhGlhWFLZpBiSVFtOiiMKCNookWblwXBQtirjvPXUW4a6+s7j3nvs75/e751w41IbggoAU3IQReB5ehGmA1wGWAd4D4MkAZRrtAh/6YQieAPldHMlFOUUWVmdAnLRQHE+mRNknEw+3HDLx63mgONbGxId9ZOEH246o95KFR3Mg9np11JzGt8Z0roXv/OLqQBPLv7pk4qvHev3ic73+teSQhdO/u6LWQiYubzeRie8vOemUWyvd/G106I0VWAd6szRbOl51DledT+DvP9x9eK3Uh2FlPlRZu8qrrMpnlcoolenM5/NKKZXJ5lQml1O5TKdSuRozv2GJA/azSXcSyjiZ+OdbkBYb7DY0uF1m0Y1GiHVm+HXZTi1eMxqcPRmT9qkRBRxAguwHXx5/5qmJ0vgYz8scdfAb1OolEbi9AzqsXhHyChkEOWpKJ8g+hQZ2vXNbWjoCfyjyV+RLNMpfoB7ZRdITaPCmHSAy8eNPgTOXhUz5M6z6b9g90rsk9166mibCU9CKe0UZbjwtU9TmSQTu7MDViyQBEW1PjD8i++l+fh/dLTso8WMcycTNihAQqdnVoLLNipBRCxd2BxprXtgdkNHOW2WSEhugOb7SHME7firydnmNhNeKcY7rEDZFYpnp01r42LXiecP2isLwVqDxCx6WD1Ebl6HsRiBbrT1K9remPlbqg9kb0Y9X6oN0xwwIMvDtYdnsORjn7OmYtOgKGd3d14NydakB1Xl+6K7AmXshcgnXEXv2hGWDJGII6VnDjgU27DeHh6R/e3lR25eFa88F9n0hu8+ElSp4n7HYLbEJ/3+Rueuj/0ynO1gff9d/ILrwR/TEW4TQ2y94Bs4/1tcwGFXD8NMjchIm2T8BAAD//6t/ygY=) |
| Combat Rogue | 531 | 567 | 635 | 672 | 58.5 | 3 | [Open in wowsims](https://www.wowsims.com/forever/rogue/dps/#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) |
| **Pure average** | **600** | **653** | **753** | **809** | | | |
| **Retribution, live** | **667 (111%)** | **715 (110%)** | **855 (114%)** | **908 (112%)** | **59.1** | **5** | [Open in wowsims](https://www.wowsims.com/forever/paladin/retribution/#eJzEV11sE1cW9hnb4+tjnHFunGRyCWTWEBJGG3Y8XksLC8Qk7C4/m12LqIVKVcskGRIjJ6YeJ6J9qAJqG1RVlIeqLahKq5hKKGpFhYoEEbQSbVrahxYk1EIkRGqEVBVaIh548FM1Y5zYJomFStv7MJp77tE53/nu+dHFegI+EEGCZtgNfbAPhgEOAbwHcAKA+q1Tzjz9B0RgC0RhF7C7NcTt49gLyJPpLvFuFbrI2z/5xEMudJBrBwFd5JsjIF7m0UU+/1gQb1agi7xzWhBf8SNPrnaJhyPoIG9c8qGLfHJayBm4NiOINyrQQYbv+NBBDljfLzPm97NPfciTmW7xTgXa0EG+ve8N/N93Mdb8c1y53xWdWXYMvFObJqNfRN/sPPvs9cMwDk23gh9t+UAbib0WOxwbPwHX0sKNtPBDWsikhVtp4XZauJMW7qaFaXgpNgNnTwhtJMdDBCa4BiWsqGFFUdSWsBJsUcJqKKQEg6oSDCnBUDh4kXNc4rgMd9mPTbg0AyLWbOpOxYa0lC5phhHrHdB7JG0wqQUI8uhoURUDJfSPQyUKWX4JYnQwHpeS2kCvXqCxEusyUIP+aFLfJ3XqWlxK7JHaE/392kBPwIVOtLeEDPwrNmSgHlmR1o5Yb19KTwwaA7phBNzoQmdLcE3YwNVYn4E6rG3XjNQctL2DPb16vz6QKlClK1kAKwJLEO8RFzqbCbkezYCA3o7EkC6lElK/Htd1Wsdq0ZvlEcnOf0u9g1qyh/HoICdHwTKwXK4nPOXW2Zg/y1eisFmPa89LHdreRFJq32yss9E2FsG/MxXr5FoC1HOMI8g328nJ82AaQk4xsFquInbqvOfiiJ1Z/ChrVIPNKtL/sm3YSjeUAEFvwIPuMXiAB5dleYbiNjNWKalr8ZjRL+1LJlJ6dyqWGGD5IGkjW4G1Wd6PtLMvMRjvkZL6nqRu9EmdiXbLqZOcScNiajssNUImR4FWscoMVOCS9sSAoXcnNdMXFZg3A4jkX/sTye6Y0S/a5caFcoZ6mNsC5yTno/LmBe+OrmZNuDTLi1izRTPmUbBA8eTKKMjd82cV3c624gb6T2wILFvUFIpZvhqrnjD0UhNzBMnHYbGspC8DOwg4RFPlvS3P8kuxrtBbkSkMsr9hfYAtjAqFgBc9GWKCA/LWuzB3QfKUozSnfwF2G/BVoCOwOK5Ci2hytzCAQEAqG4Y7Q8xcfX04miu8DOdCZ39iSA/Sp/M/1eNA0ZflvejpMMHmugb1Jj3ovkfypUdmi9AVcKJ9wmGjWJC6FcmisqZXgF0GfI4mFg83wjbmamoOZymvZa6hOCw1H5b6W8PKlVppWMPAXsQQDZZPsGJcIfqf/M+j4iqBIPfM1TjdxZ7E7XSr1c6c1HmBm21nVmuulAWzVXbZmNXbg0pjaQOzUI5B3rjVFHjydVSOlbSXp9jOx+splzrn0qAGFuKQWvZTyUFdbZj38gsUGhepggK1uofmBX0wElR/4czMSdWw6i++JSfaEcLq+rmRQBW6xmKFLxknQSMvLiDLFKtZmG8O0JtApx9zzZtT0D3Fm9szacBGugLdpyC/rZH9xEHdE3kByyHF9WxdaVGupk3omeJJTlEEFOUawlPPBTBFV0eiIjCLm2CZmaie4+abbvR9jo5xuJGtLxveQ/2hAKaJ/NG69gJsTY4WsWVui9iaHJ1lq4NtL9vCCuibHM3TB3n6vp+jL1SOvraFz+gqeaWJcDxfc6z6FEcJR91jrrzEbHA/cj0znHrAbrPW2sgEOJBDW2DE7s6JnolU5n78kbpjR831Vetf9ljru1Z1mhNdUqt8hrP9KSsV+UPcrPrwd/Oz1vruOB7Z9EAQ2W2+ho5CbjfdKtvJkf+1FTyalIKHkfl82g/7uV8DAAD///pq8xU=) |
| Retribution, % of Fury | 109% | 104% | 112% | 108% | | | |

- **Set links.** Each link opens the final set of the spec in wowsims, with enchants, consumables, raid buffs and the fight. Select Simulate to run it. A later wowsims version can give a different DPS.
- **Master commit 8298ab833 (later on 4 November) changes the pure classes again.** Against commit 6ee3c30f35 (both columns): Hunter −3.5% (new reaction times), Demonology Warlock +1.4% (patch of 3 November and the elixirs of its new preset), Combat Rogue +0.8%, Fury +0.3%, Mage 0%. Retribution +0.2% (the new elixirs). On commit 6ee3c30f35, the pure average was 812 and Retribution 906 (112%).

- **The hotfix 113578 ports of 4 November change the pure classes.** Against the run of 3 November (both columns): Fury +6.2%, Combat Rogue +5.0%, Hunter +16.5%, Mage and Warlock 0%. Retribution 0%. On 3 November, the pure average was 770 and Retribution 906 (118%).
- **Build 70755 changed the pure classes too (3 November).** Against the run of 1 November (both columns): Fury −2.1%, Hunter −4.8%, Combat Rogue −1.7%, Mage and Warlock 0%. Retribution +3.7%. wowsims now uses the trainer ranks of the totems and of the Hunter spells, not the Ruins of Ahn'Qiraj book ranks. On 1 November, the pure average was 784 and Retribution 874 (112%).
- **Parts 1 and 3 use the last column.** The start value of the model (938) has full buffs and consumables. Thus, the other classes need the same.
- **Enchants decrease the Retribution lead by 2 points.** The physical enchants help Fury most.
- **Consumables increase the Retribution lead by 2 points.** Retribution uses physical elixirs and spell elixirs. A pure class uses only one of the two groups.
- **The two together give +1 point:** 112% of the pure average, and 108% of Fury.
- **The wowsims presets are not the same for each class.** With each preset as it is, Retribution had 116% on 1 November (9 elixirs). The Rogue preset has no elixir. Thus, this run gives the same elixirs to all specs.
- **The Rogue is low in this sim.** Without the Rogue, the pure average is 844, and Retribution is 108%. On 1 November, the six wowsims Rogue talent presets gave 315–657 DPS on the same set. The best one (Combat Backstab) gave only +2%. With a Rogue at the Fury level, Retribution is 108%. The wowsims Rogue is not complete. Issue 13 has the stat values and the gear effects open. Issue 28 has 40 of 100 items open, among them Coup de Grace and Occult Poison. A rerun is due when issue 13 closes.
- **Fight length (1 November).** At 3 min, Retribution was 114% of the pure average. At 5 min, it was 115%. The casters and the Rogue lose DPS in longer fights, and Retribution gains a little.
- **The later items helped the pure classes more.** With the first pool (ZG, AQ, battleground and dungeon set 2 items), Retribution had 108% and Fury 102%. Retribution keeps Forever items (Vindicator's Belt, Timbermaw Tunic) and Arcanite Reaper.
- **Limits.** Many Forever items have no source in the game data. They stay in the pool. The same rule applies to all specs. The search can stop at a local best set.
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
- **Files.** `models/wowsims-b2/go/allspecs_main.go` and `logs/allspecs.log`.

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

**Other gear growth cases (live / C1 withdrawn, Naxxramas):** ×1.60 gives 114% / 121%. ×1.90 gives 102% / 108%.

## 10. Method and limits

- **Scripts.** `models/beta-30-oct/retribution_b2.py` (model) and `damage_tables_b2.py` (tables). wowsims tests in `models/wowsims-b2`. Other classes: wowsims with the same item pool (part 7) and `models/damage` (increase with gear of Fury, Arms and Combat Rogue).
- The model calculates averages. It is not a full simulation.
- The model keeps the rules of 30 October: Vengeance 3 stacks, and Two-Handed Weapon Specialization on physical damage only. The start value (938) has the changes of build 70755. Thus, the increase with gear is an estimate.
- Not confirmed: the critical hit decrease against a boss, and the Seal of Righteousness value with a 3.6 sec weapon.
- The Fury and Combat Rogue rotations and talents are assumptions. Arms uses the wowsims rotation.
- The gear levels are estimates with Classic steps. The Forever raid items are not known.
