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
