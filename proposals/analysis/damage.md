# Damage

**Question.** How much damage does Retribution do on one boss, against the other damage classes?

All values are DPS on one level 63 boss. The start values come from wowsims (master commit ae9b8c23a of 8 November 2026, hotfixes of 7 and 8 November). The increase with gear comes from the damage model.

"Pure average" is the average DPS of the best spec of each pure damage class (Warrior, Rogue, Hunter, Mage, Warlock) in wowsims. Each spec uses the best set from the same pre-raid item pool (part 7). The six sets open in wowsims from the [item pool sets](https://ralgathor.github.io/forever-paladin-feedback/sets/) page. The design target for a hybrid class is 95% of the pure average. Players report this target from developer comments. No official text gives the number.

## Short answer

- **The live Retribution is above the target.** It does 939 DPS in wowsims with the item pool set: 109% of the pure average at fresh 60. In Naxxramas, it is 104% (model), 9 points above the target.
- **Build 70755 gives Retribution +3.5% in wowsims (default set: 906 → 938).** Vengeance stacks up to 5 times, and Two-Handed Weapon Specialization also increases Holy damage. The pure classes lose 0–5% in the same update (part 7).
- **The hotfix 113578 ports of 4 November give the pure classes +5–17% in wowsims.** Fury +6%, Combat Rogue +5%, Hunter +17%. The pure average goes from 770 to 812, and Retribution from 118% to 112% (part 7).
- **wowsims master 8298ab833 (4 November, later) changes the pure classes by −3.5% to +1.4%.** Hunter −3.5% (new reaction times), Demonology Warlock +1.4% (patch of 3 November and new elixirs), Combat Rogue +0.8%, Fury +0.3%. The pure average goes from 812 to 809. Retribution stays at 112%.
- **wowsims master 9a8624af9 (4 November, evening) changes only Fury: +0.2%** (839 → 841, one Reckless Swings before the pull). The pure average stays at 809.6 (809.3 before), and Retribution at 112.2%.
- **wowsims master df57e2571 (6 November) adds 2,447 items. A new item search gives the pure average +0.9%** (809.6 → 817.1). The same commit halves the Natural flasks. Combat Rogue +5.2%, Hunter +2.0%, Demonology Warlock +0.7%, Fury −1.5%, Fire Mage −1.0%. Retribution does not change. It then had 111% of the pure average (part 7).
- **wowsims master ae9b8c23a (8 November) adds 362 pool items for a Paladin, for example Hand of Justice and Cape of the Black Baron. A new item search gives the pure average +5.4%** (817.1 → 861.1). Fire Mage +8.9%, Demonology Warlock +6.9%, Fury +4.3%, Combat Rogue +3.4%, Hunter +3.3%. Retribution +3.1% (908 → 937). It now has 109% of the pure average (part 7).
- **The wowsims update of 1 November** gives Retribution +7% (848 → 906): a new rotation, the Unsealed Wrath fix and new weapon oils.
- **The Holy Strike Seal trigger (C1) gave +5.3–5.7%.** With C1, Retribution has 115% of the pure average at fresh 60 and 110% in Naxxramas.
- **C1 is withdrawn (2 November 2026).** It puts Retribution 15–20 points above the target, and Sacred Arbiter +10% removed only 0.7 points. The C1 rows below stay for reference.
- **Retribution increases less with gear than Fury:** ×1.65 against ×1.73 to Naxxramas. Fixed base values in the Paladin spells cause this. No talent change can fix it.
- **Judgement of the Crusader** adds +9.0% at fresh 60 and +6.0% in Naxxramas.

## 1. Against the pure average

wowsims values with the same item pool, enchants and consumables for each spec (part 7). Fury Warrior 864, Combat Rogue 730, Hunter 902, Fire Mage 888, Demonology Warlock 922. The pure average is 861. Without the Rogue, it is 894. Retribution does 937 in the same runs.

- **At fresh 60,** the live Retribution is 109% of the pure average and 108% of Fury. With C1 (withdrawn), it is 115% and 114%.
- **Without the Rogue,** the live version is 105%. C1 gives 111%.
- **The tables use ratios.** Retribution (939, item pool set, full buffs and consumables, 2 min) is the start value. The other classes keep their ratio to Retribution in the same item pool runs.

The increase of Hunter, Mage and Warlock with gear is not known. The table uses ×1.75 to Naxxramas. The method part gives ×1.60 and ×1.90.

| Build | Fresh 60 | Pre-raid | Molten Core | Blackwing Lair | Naxxramas |
| --- | --- | --- | --- | --- | --- |
| **Live** | **109%** | **108%** | **107%** | **105%** | **104%** |
| C1 (withdrawn) | 115% | 114% | 113% | 111% | 110% |
| C1 (withdrawn), Sacred Arbiter +10% | 114% | 113% | 112% | 110% | 109% |
| C1 (withdrawn), Sacred Arbiter +0% | 112% | 112% | 111% | 109% | 108% |
| Live, no more spell damage on plate after fresh 60 | 109% | 106% | 103% | 99% | 96% |
| C1 (withdrawn), no more spell damage on plate after fresh 60 | 115% | 112% | 109% | 105% | 102% |

- **The live version is above the target at all gear levels.** It is 14 points above at fresh 60 and 9 points above in Naxxramas.
- **C1 is 15–20 points above the target.** At fresh 60, Retribution with C1 is 14% above Fury.
- **Spell damage on plate gear is important.** Without new spell damage on plate items, the live Paladin has only 96% in Naxxramas.
- **Why C1 is withdrawn.** It gave one Seal rule for all melee attacks and +2.6% tank threat. Retribution reaches the target without it, and Righteous Fury (C25) already gives the tank the Warrior threat (see Threat).
- **The balance lever is Sacred Arbiter (W15).** If raid logs confirm the wowsims level, decrease it to +10%: −0.7% damage in wowsims. This change alone does not bring Retribution to 95%. With C1, the gain fell only from +5.5% to +4.5%.
- **Check again later.** The pure average uses the item pool sets of wowsims master ae9b8c23a of 8 November (new search after 362 new pool items, part 7). The Warrior, Rogue and Hunter have the changes of hotfix 113578, and the Warlock has the patch of 3 November. The Mage changes of the development notes are not in wowsims yet (W15).

**DPS of each class.** The start values keep the ratio to Retribution of the same item pool runs (part 7), with Retribution at 939. The increase comes from the model. Hunter, Mage and Warlock use ×1.75.

| Spec | Fresh 60 | Pre-raid | Molten Core | Blackwing Lair | Naxxramas |
| --- | --- | --- | --- | --- | --- |
| **Retribution, live** | **939 (109%)** | **1,051 (108%)** | **1,207 (107%)** | **1,352 (105%)** | **1,553 (104%)** |
| Demonology Warlock | 924 (107%) | 1,044 (107%) | 1,218 (108%) | 1,393 (108%) | 1,617 (109%) |
| Hunter | 904 (105%) | 1,021 (105%) | 1,192 (106%) | 1,362 (106%) | 1,582 (106%) |
| Fire Mage | 890 (103%) | 1,006 (103%) | 1,174 (104%) | 1,342 (104%) | 1,558 (105%) |
| Fury Warrior | 866 (100%) | 985 (101%) | 1,127 (100%) | 1,298 (101%) | 1,498 (101%) |
| **Pure average** | **863** | **975** | **1,126** | **1,285** | **1,487** |
| Combat Rogue | 732 (85%) | 817 (84%) | 917 (81%) | 1,033 (80%) | 1,178 (79%) |

- **Retribution is first up to the pre-raid level.** At fresh 60, it is 2% above the Warlock and 4% above the Hunter. From Molten Core, the Warlock is first: Retribution has 99% of the Warlock in Molten Core, 97% in Blackwing Lair and 96% in Naxxramas.
- **The Rogue decreases the pure average.** Without the Rogue, the pure average is 896 at fresh 60 (894 in the item pool run).
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
| Pre-raid best | 107% | 105% | 107% | 113% | 110% | 113% |
| Molten Core | 107% | 103% | 107% | 113% | 109% | 113% |
| Blackwing Lair | 104% | 98% | 105% | 110% | 103% | 110% |
| Naxxramas | 104% | 96% | 104% | 109% | 101% | 110% |

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
- **Fury is the outlier.** In Naxxramas, the live Retribution is 117% of Arms (same gear, model) and 132% of Combat Rogue.

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
| 1 + 3 (wowsims rotation) | 910 DPS | 100% | 27.8 | 3 min 43 sec |
| 1 + 2 | −0.6% | 99.2% | 35.6 | 2 min 21 sec |
| 2 + 2 | −1.9% | 97.5% | 27.8 | 3 min 43 sec |
| 1 + 1 (a Seal change after each swing) | −3.0% | 97.5% | 51.2 | 1 min 21 sec |
| 3 + 1 | −5.3% | 94.9% | 27.8 | 3 min 43 sec |
| Seal of Command only | — | 85.7% | 10.2 | No limit |

- **Plan 1 + 3 is the best plan.** A copy of Seal of Command has more value than a copy of Seal of Righteousness.
- **At fresh 60, plan 1 + 3 lasts for a 3 min fight.** In a 5 min fight, plan 3 + 3 is the best (−2.5%). In Naxxramas, plan 1 + 3 lasts 5 min.
- **In wowsims, the mana lasts 5 min,** because the consumables include Major Mana Potion.
- **A 20% Seal cost decrease on Unsealed Wrath (W29)** gives 0% in a 2 min fight and +2.6% in a 5 min fight (model). In wowsims, it gives 0%.
- **The model tables of this tab use plan 1 + 3 and no mana limit.** The start value (939) comes from wowsims with the same plan.

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

Item pool Retribution set (part 7) with the default enchants, rotation and consumables. Fury and Arms: the wowsims pre-raid sets. One level 63 boss, 3,000 iterations. "Lean buffs" is a small set of buffs.

| Case | 2 min | 5 min |
| --- | --- | --- |
| Live, full buffs | 939 | 952 |
| C1 (withdrawn), full buffs | 991 (+5.5%) | 1,002 (+5.3%) |
| Live, lean buffs | 686 | 697 |
| C1 (withdrawn), lean buffs | 724 (+5.6%) | 733 (+5.2%) |
| Fury Warrior, pre-raid gear | 865 | 860 |
| Arms Warrior, pre-raid gear | 826 | 824 |

- **C1 (withdrawn):** +5.2–5.6% in wowsims, +5.6–5.7% in the model. They agree.
- **Almost no run is out of mana.** Only the 5 min runs with lean buffs have no mana, for less than 1 sec.
- **The wowsims update of 1 November,** step by step: 836 → 852 (Unsealed Wrath fix) → 889 (new rotation and presets) → 901 (new weapon oils), in the wowsims test suite.
- **Build 70755 (master commit d97252f2a, 3 November).** With the default set, the live Retribution increases from 906 to 938 (+3.5%). The two test flags on master of 1 November gave 981 (+8.3%), thus the game data gives less. wowsims now also uses the trainer ranks of Strength of Earth Totem and Grace of Air Totem in the raid buffs. With the Ruins of Ahn'Qiraj book ranks, Retribution has 949 (item pool set: 920).
- **Master commit 6ee3c30f35 (4 November).** The Paladin values do not change. The hotfix 113578 ports give Fury +7% in the wowsims pre-raid set (807 → 865) and Arms +5% (773 → 814).
- **Master commit 8298ab833 (4 November, later).** The Paladin values do not change. Fury stays at 865 in the wowsims pre-raid set, and Arms goes to 826 (+1.5%).
- **wowsims Fury.** Against the wowsims Fury pre-raid set, the item pool Retribution is 109% of Fury, but the two sets have different quality. With the same item pool, enchants and consumables, it is 108% of Fury (see below).

**Same item pool for each spec (search of 2 November 2026, new searches on 6 and 8 November).** This run gives the pure average of parts 1 and 3. All specs take their items from one pre-raid pool. The first search ran in wowsims of 1 November. On 4 November, the same sets ran again on master commits 6ee3c30f35, 8298ab833 and 9a8624af9. On 6 November, master commit df57e2571 adds 2,447 items. 241 of them obey the pool rules for a Paladin and have item level 45 or higher. The search ran again on this commit for all six specs, from the sets of 4 November, with the same rules and steps. On 8 November, master commit ae9b8c23a adds the items of the hotfixes of 7 and 8 November. 362 of them obey the pool rules for a Paladin, for example Hand of Justice, Blackhand's Breadth and Cape of the Black Baron. The search ran again for all six specs, from the sets of 6 November. The values below come from commit ae9b8c23a.

- **Item pool.** Uncommon, rare and epic items of item level 63 or lower, for level 60 or lower. Only content of the game start and Dire Maul: no Classic items of patch 1.6 or later (item ids 19000–23999). Thus, no Zul'Gurub, Ahn'Qiraj or Naxxramas era items, no dungeon set 2 and no battleground rewards. No raid drops, no world boss drops and no PvP items. No items that need Revered or Exalted reputation. Items with random enchantments are not in the pool. Each spec keeps its armor and weapon types, and its weapon setup (two-handed weapon, two weapons, or weapon and off-hand item).
- **Search.** The start is the wowsims test set, without the items outside the pool. For each slot, the search tests the best items for the stat values of the spec, and all items with an effect. It keeps the best item, and repeats until no slot changes.
- **Same conditions for all.** The full wowsims test raid buffs and debuffs, the same for all specs: melee and caster buffs, totems, auras, and all debuffs with Judgement of the Crusader. Level 63 boss, 2 min, 10,000 iterations. The class weapon items stay (oils, stones, poisons). With the buffs and debuffs of the own wowsims preset of each spec, all six values stay the same.
- **Enchants.** The wowsims preset enchants of each spec, slot by slot. Mage and Warlock have no enchanted preset: they use the Balance Druid caster enchants, with +30 spell power on the weapon.
- **Consumables.** Each spec keeps its wowsims flask, food and potions. All specs use the same elixirs and extra items: all of those in the six presets. The Hunter preset has no flask, thus the Hunter uses the Fury flask. Fury, Rogue and Hunter use Flask of Natural Aggression. Commit df57e2571 halves this flask. The Fire Mage keeps its own elixirs, because the full list stops the sim. Physical elixirs do not help a caster: the Warlock changes by 0.2%.

| Spec | No enchants, no consumables | Enchants | Consumables | Enchants and consumables | Average item level | Epic items | Set |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Demonology Warlock | 644 | 699 | 863 | 922 | 59.2 | 3 | [Demonology Warlock set](https://ralgathor.github.io/forever-paladin-feedback/sets/demonology-warlock.html) |
| Hunter | 742 | 796 | 844 | 902 | 60.0 | 3 | [Hunter set](https://ralgathor.github.io/forever-paladin-feedback/sets/hunter.html) |
| Fire Mage | 648 | 699 | 835 | 888 | 58.8 | 3 | [Fire Mage set](https://ralgathor.github.io/forever-paladin-feedback/sets/fire-mage.html) |
| Fury Warrior | 651 | 726 | 790 | 864 | 58.3 | 3 | [Fury Warrior set](https://ralgathor.github.io/forever-paladin-feedback/sets/fury-warrior.html) |
| Combat Rogue | 580 | 622 | 684 | 730 | 58.9 | 3 | [Combat Rogue set](https://ralgathor.github.io/forever-paladin-feedback/sets/combat-rogue.html) |
| **Pure average** | **653** | **708** | **803** | **861** | | | |
| **Retribution, live** | **689 (106%)** | **740 (104%)** | **881 (110%)** | **937 (109%)** | **59.3** | **4** | [Retribution set](https://ralgathor.github.io/forever-paladin-feedback/sets/retribution.html) |
| Retribution, % of Fury | 106% | 102% | 112% | 108% | | | |

- **Set links.** Each link opens the final set of the spec in wowsims, with enchants, consumables, raid buffs and the fight. Select Simulate to run it. A later wowsims version can give a different DPS. All six links: [item pool sets](https://ralgathor.github.io/forever-paladin-feedback/sets/).
- **Master commit ae9b8c23a (8 November) and the new search.** Against commit df57e2571 (both columns): Fire Mage +8.9% (815.6 → 888.2), Demonology Warlock +6.9% (862.5 → 921.6), Fury +4.3% (828.5 → 863.8), Combat Rogue +3.4% (706.2 → 730.4), Hunter +3.3% (872.7 → 901.6). Retribution +3.1% (908.3 → 936.6). The pure average goes from 817.1 to 861.1, and Retribution from 111.2% to 108.8%.
- **Two causes (8 November).** With the sets of 6 November on commit ae9b8c23a, only the Hunter changes: +1.8% (872.7 → 888.5). Attack Power on gear now also gives ranged Attack Power. The pure average is then 820.4, and Retribution 110.7%. The new items give the rest.
- **New items in the sets (8 November).** Hand of Justice and Cape of the Black Baron: Fury, Combat Rogue, Hunter and Retribution. Fury also takes Sentimental Locket, Warpwood Bracers, Magni's Will and Mirah's Song. Combat Rogue: Blackstone Ring and Precisely Calibrated Boomstick. Hunter: Hermit's Pauldron and Tarnished Elven Ring. Fire Mage and Demonology Warlock: Crimson Felt Hat, Songstone of Ironforge, Maiden's Circle, Eye of the Beast, Second Wind, Arbiter's Blade and Lord Sakrasis' Scepter. The Fire Mage also takes Rotgrip Mantle and Magister's Leggings. Hermit's Pauldron and Magister's Leggings were in the pool before. All other items are new in the database. The sets of 6 November are in `sets_df57e2571/`.
- **Master commit df57e2571 (6 November) and the new search.** Against commit 9a8624af9 (both columns): Combat Rogue +5.2% (671.6 → 706.2), Hunter +2.0% (855.6 → 872.7), Demonology Warlock +0.7% (856.3 → 862.5), Fury −1.5% (840.7 → 828.5), Fire Mage −1.0% (823.9 → 815.6). The Retribution set does not change: 908.3. The pure average goes from 809.6 to 817.1, and Retribution from 112.2% to 111.2%.
- **Two causes (6 November).** With the sets of 4 November on commit df57e2571, the flask change alone gives Fury −1.9%, Hunter −1.9% and Rogue −1.2%. The pure average is then 801.7, and Retribution 113.3%. The new sets give +1.9% to the pure average.
- **New items in the sets (6 November).** Fury: Timbermaw Tunic, Deepfury Bracers (new), Bagh Nakh, Skypierce Javelin (new). Combat Rogue: Bagh Nakh in the main hand. Hunter: Flawless Arcanite Rifle. Fire Mage: Lapidis Tankard of Tidesippe (new) and Red Mageweave Headband. Demonology Warlock: Lapidis Tankard of Tidesippe. Bagh Nakh, Flawless Arcanite Rifle, Timbermaw Tunic and Red Mageweave Headband were in the pool before. The first search stopped at a local best set.
- **Fire Mage (6 November).** The search runs without enchants and consumables. There, Lapidis Tankard of Tidesippe was better (+0.6%). With both, the Fire Mage lost 1.0%. The rules keep the result of the search.
- **Master commit 8298ab833 (later on 4 November) changes the pure classes again.** Against commit 6ee3c30f35 (both columns): Hunter −3.5% (new reaction times), Demonology Warlock +1.4% (patch of 3 November and the elixirs of its new preset), Combat Rogue +0.8%, Fury +0.3%, Mage 0%. Retribution +0.2% (the new elixirs). On commit 6ee3c30f35, the pure average was 812 and Retribution 906 (112%).
- **Master commit 9a8624af9 (evening of 4 November).** Fury +0.2% (839.2 → 840.7): Fury casts one Reckless Swings before the pull. The other specs and Retribution do not change. The pure average was 809.6, and Retribution 112.2% (108.0% of Fury).
- **The hotfix 113578 ports of 4 November change the pure classes.** Against the run of 3 November (both columns): Fury +6.2%, Combat Rogue +5.0%, Hunter +16.5%, Mage and Warlock 0%. Retribution 0%. On 3 November, the pure average was 770 and Retribution 906 (118%).
- **Build 70755 changed the pure classes too (3 November).** Against the run of 1 November (both columns): Fury −2.1%, Hunter −4.8%, Combat Rogue −1.7%, Mage and Warlock 0%. Retribution +3.7%. wowsims now uses the trainer ranks of the totems and of the Hunter spells, not the Ruins of Ahn'Qiraj book ranks. On 1 November, the pure average was 784 and Retribution 874 (112%).
- **Parts 1 and 3 use the last column.** The start value of the model (939, the same set with the Retribution test buffs) has full buffs and consumables. Thus, the other classes need the same.
- **Enchants decrease the Retribution lead by 1 point.** The physical enchants help Fury most.
- **Consumables increase the Retribution lead by 4 points.** Retribution uses physical elixirs and spell elixirs. A pure class uses only one of the two groups.
- **The two together give +3 points:** 109% of the pure average, and 108% of Fury.
- **The wowsims presets are not the same for each class.** With each preset as it is, Retribution had 116% on 1 November (9 elixirs). The Rogue preset has no elixir. Thus, this run gives the same elixirs to all specs.
- **The Rogue is low in this sim.** Without the Rogue, the pure average is 894, and Retribution is 105%. On 1 November, the six wowsims Rogue talent presets gave 315–657 DPS on the same set. The best one (Combat Backstab) gave only +2%. With a Rogue at the Fury level, Retribution is 105%. The wowsims Rogue is not complete. Issue 13 has the stat values and the gear effects open. Issue 28 has 40 of 100 items open, among them Coup de Grace and Occult Poison. A rerun is due when issue 13 closes.
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

**Other gear growth cases (live / C1 withdrawn, Naxxramas):** ×1.60 gives 111% / 117%. ×1.90 gives 99% / 105%.

## 10. Method and limits

- **Scripts.** `models/beta-30-oct/retribution_b2.py` (model) and `damage_tables_b2.py` (tables). wowsims tests in `models/wowsims-b2`. Other classes: wowsims with the same item pool (part 7) and `models/damage` (increase with gear of Fury, Arms and Combat Rogue).
- The model calculates averages. It is not a full simulation.
- The model keeps the rules of 30 October: Vengeance 3 stacks, and Two-Handed Weapon Specialization on physical damage only. The start value (939) has the changes of build 70755. Thus, the increase with gear is an estimate.
- Not confirmed: the critical hit decrease against a boss, and the Seal of Righteousness value with a 3.6 sec weapon.
- The Fury and Combat Rogue rotations and talents are assumptions. Arms uses the wowsims rotation.
- The gear levels are estimates with Classic steps. The Forever raid items are not known.
