# Pure damage specs with the same item pool (2 November 2026, new searches on 6, 8, 9 and 11 November)

This run gives the pure average of Analysis, Damage (parts 1, 3 and 7).

The item search ran on wowsims Forever, master commit `895cd67f9` (1 November 2026). On 3 November 2026, the same sets ran again on master commit `d97252f2a` (game files of client 1.60.1.70755), on 4 November on master commit `6ee3c30f35` (the hotfix 113578 ports of the Warrior, Rogue and Hunter), and later on 4 November on master commit `8298ab833` (the Warlock patch of 3 November, new Hunter reaction times, Rogue rotation tuning). The item database of commit `8298ab833` adds no item to the pool: only two low-level items and the End of Beta event items. wowsims denies these items.

**New search (6 November 2026).** Master commit `df57e2571` (hotfix push 113693, client 1.60.1.70790) adds 2,447 items to the database. 241 of them obey the pool rules for a Paladin and have item level 45 or higher. The same commit halves the Natural flasks: 30 Stamina and 2% (was 60 Stamina and 4–5%). The Fury, Rogue and Hunter runs use Flask of Natural Aggression. The search ran again on this commit for all six specs. Each search starts from the set of 4 November (`sets_9a8624af9/`, `SEED` in main.py), with the same rules and steps. The sets of 6 November and their logs are in `sets_df57e2571/`, their values in `ec_results_df57e2571.json`.

**New search (8 November 2026).** Master commit `ae9b8c23a` (hotfixes of 7 and 8 November, client 1.60.1.70862) adds 362 items that obey the pool rules for a Paladin, for example Hand of Justice and Cape of the Black Baron. The same commit makes Attack Power on gear also give ranged Attack Power (Hunter). The search ran again on this commit for all six specs. Each search starts from the set of 6 November (`sets_df57e2571/`, `SEED` in main.py), with the same rules and steps. The sets of 8 November and their logs are in `sets_ae9b8c23a/`, their values in `ec_results_ae9b8c23a.json`.

**New search (9 November 2026).** Master commit `9f254e8d8` (hotfix push 113823) adds 262 items to the database. The same commit changes the Windfury Totem rule: Windfury now procs only from auto attacks and from main-hand or next-swing abilities. Holy Strike and Judgement of Command do not proc it (0 of 78 and 0 of 105 in the Forever logs). The search ran again on this commit for all six specs. Each search starts from the set of 8 November (`sets_ae9b8c23a/`, `SEED` in main.py), with the same rules and steps. The sets of 9 November and their logs are in `sets_9f254e8d8/`, their values in `ec_results_9f254e8d8.json`.

**New search (11 November 2026).** Master commit `3633d376a` (client 1.60.1.70888, hotfixes of 10 and 11 November) adds 464 items to the database. 335 of them obey the pool rules for a Paladin, for example Ironfoe, Dal'Rend's Sacred Charge and Blackhand Doomsaw. The commit also changes the Warlock dots (Wrack), the Arcane Missiles channel and many Warrior and Druid rules. With the sets of 9 November on this commit (`ec_results_3633d376a_old_sets.json`), no spec changes by more than 0.1% (both). The pure average is 868.7, and Retribution 97.1%. The search ran again for all six specs. Each search starts from the set of 9 November (`sets_9f254e8d8/`, `SEED` in main.py), with one new rule: all items of a slot with an effect that wowsims implements are candidates (`EFFECTS`, see below). The results below come from commit `3633d376a`.

## Rules (the same for each spec)

- **Item pool.** Uncommon, rare and epic items of item level 63 or lower, for level 60 or lower. Only content of the game start and Dire Maul. No Classic items with item ids 19000–23999. These items are from patch 1.6 or later: Zul'Gurub, Ahn'Qiraj and Naxxramas era items, dungeon set 2 and battleground rewards. No items that need Revered or Exalted reputation. Not Jewel of the Guard Captain (a battleground name, no source). No raid drops and no world boss drops (zone and NPC sources in the wowsims data and AtlasLoot). No PvP items, no PvP reputation items, and not the raid items of the earlier `GEARFIX` list. No items with random enchantments.
- **Class.** Each spec keeps its armor and weapon types and its weapon setup (two-handed weapon, two weapons, or weapon and off-hand item).
- **Search.** Start: the wowsims test set without the items outside the pool (Fury: the `prebis_fury` set). For each slot, the candidates are the best items for the stat values of the spec (measured in the sim). All items with an effect are also candidates. The search keeps the best item for each slot (1,000 iterations, fixed seed) and repeats until no slot changes (3 passes at most). Final value: 10,000 iterations.
- **Conditions.** The search runs with no enchants and no consumables. The class weapon items stay (oils, stones, poisons). The full wowsims test raid buffs and debuffs, the same for all specs (melee and caster buffs, totems, auras, all debuffs with Judgement of the Crusader). Level 63 boss, 2 min.
- **Enchants and consumables (second run).** The sets of the search, with enchants and consumables (`enchants_consumables.py`, see below).

## Results

| Spec | No enchants, no consumables | Enchants | Consumables | Both | Average item level | Epic items |
| --- | --- | --- | --- | --- | --- | --- |
| Fury Warrior | 704.0 | 787.9 | 856.5 | 946.2 | 59.1 | 5 |
| Demonology Warlock | 660.6 | 716.0 | 881.3 | 940.3 | 60.0 | 4 |
| Hunter | 757.3 | 814.6 | 858.8 | 919.8 | 61.0 | 3 |
| Fire Mage | 670.9 | 721.8 | 862.2 | 915.5 | 59.9 | 4 |
| Combat Rogue | 607.5 | 652.4 | 717.7 | 767.0 | 59.4 | 4 |
| Pure average | 680.1 | 738.5 | 835.3 | 897.8 | | |
| Retribution (live) | 618.5 (90.9%) | 661.8 (89.6%) | 795.8 (95.3%) | 843.5 (94.0%) | 59.3 | 4 |

Without the Rogue (both): 930.5, Retribution 90.7%. Retribution against Fury (both): 89.1%. wowsims links to each set: `links.md`.

- **Commit 3633d376a (11 November) against commit 9f254e8d8 (both).** Fury +8.7% (870.7 → 946.2), Combat Rogue +3.4% (742.1 → 767.0), Fire Mage +1.9% (898.7 → 915.5). Hunter +1.6% (905.4 → 919.8), Demonology Warlock +1.5% (926.0 → 940.3). Retribution does not change (843.5). Pure average 868.6 → 897.8, Retribution 97.1% → 94.0%. All the change comes from the new sets.
- **Set changes (11 November).** Fury: Ironfoe in the main hand and Flurry Axe in the off hand (+6.2% in the search, without enchants and consumables). Also Mark of Fordring, Truestrike Shoulders, Battleborn Armbraces and Windreaver Greaves. Combat Rogue: Mark of Fordring, Ironfoe and Talon of Tor'Rel. Hunter: Mark of Fordring, Truestrike Shoulders and Windreaver Greaves. Fire Mage: Eye of Flame, Burial Shawl, Sublime Wristguards, Omnicast Boots and Witchblade. Demonology Warlock: Eye of Flame, Royal Seal of Eldre'Thalas, Witchblade and Bonecreeper Stylus. All these items are new in the database, except Flurry Axe and Talon of Tor'Rel.
- **Retribution.** The search tested 28 two-handed weapons, all proc weapons that wowsims implements among them. No item is better than the set of 9 November. The log has the value of each candidate (`log_Retribution.txt`).
- **Proc items (`EFFECTS`).** The search keeps a list of candidates for each slot from the stat values. A proc weapon has low stat values, but the sim gives its full value. Before 11 November, the search took only the 8 items with an effect and the best stat values. In the weapon slots, it took 15, and in the trinket slots all items. Now, with `EFFECTS=<list>`, it takes all items of the slot with an effect that wowsims implements. The list comes from the sim (`core.HasItemEffect`, `../tank_gear/zzeffects_main.go`): 266 items on commit 3633d376a (`../tank_gear/effects_3633d376a.txt`). 77 Paladin pool items have an effect that wowsims implements, 23 of them weapons. For example, Flurry Axe and Ironfoe are in the list, but Destiny is not: its proc is not active in wowsims.

- **Commit 9f254e8d8 (9 November) against commit ae9b8c23a (both).** Retribution −9.9% (936.6 → 843.5). Combat Rogue +1.6% (730.4 → 742.1), Fire Mage +1.2% (888.2 → 898.7), Fury +0.8% (863.8 → 870.7), Demonology Warlock +0.5% (921.6 → 926.0), Hunter +0.4% (901.6 → 905.4). Pure average 861.1 → 868.6, Retribution 108.8% → 97.1%.
- **Two causes (9 November).** With the sets of 8 November on commit 9f254e8d8 (`ec_results_9f254e8d8_old_sets.json`), the Windfury Totem rule gives Retribution −9.9% and Fury −2.6%. The other specs do not change. The pure average is then 856.9, and Retribution 98.4%. The new items give the rest: Fury +3.5%, Combat Rogue +1.4%, Fire Mage +1.2%.
- **Windfury Totem.** In the Retribution test raid, Windfury gave +22% damage before this commit and +10% now (zzbatch with the buffs of each test, `own`). The Retribution set does not change: the search finds no better item.
- **Set changes (9 November).** Fury: Bloodmail Boots, Sword of Zeal and Satyr's Bow. Combat Rogue: Imperial Jewel, Flamebreak Talisman and Sword of Zeal. Hunter: Star of Mystaria, Bloodmail Boots, Flamebreak Talisman and Deep Jungle Rifle. Fire Mage: Star of Mystaria and Skyshroud Leggings. Demonology Warlock: Star of Mystaria and Mind Carver. All these items are new in the database.


- **Commit ae9b8c23a (8 November) against commit df57e2571 (both).** Fire Mage +8.9% (815.6 → 888.2), Demonology Warlock +6.9% (862.5 → 921.6), Fury +4.3% (828.5 → 863.8), Combat Rogue +3.4% (706.2 → 730.4), Hunter +3.3% (872.7 → 901.6). Retribution +3.1% (908.3 → 936.6). Pure average 817.1 → 861.1, Retribution 111.2% → 108.8%.
- **Two causes (8 November).** With the sets of 6 November on commit ae9b8c23a (`ec_results_ae9b8c23a_old_sets.json`), only the Hunter changes: +1.8% (872.7 → 888.5), from the ranged Attack Power. The pure average is then 820.4, and Retribution 110.7%. The new items give the rest.
- **Set changes (8 November).** Hand of Justice and Cape of the Black Baron: Fury, Combat Rogue, Hunter and Retribution. Fury also takes Sentimental Locket, Warpwood Bracers, Magni's Will and Mirah's Song. Combat Rogue: Blackstone Ring and Precisely Calibrated Boomstick. Hunter: Hermit's Pauldron and Tarnished Elven Ring. Fire Mage and Demonology Warlock: Crimson Felt Hat, Songstone of Ironforge, Maiden's Circle, Eye of the Beast, Second Wind, Arbiter's Blade and Lord Sakrasis' Scepter. The Fire Mage also takes Rotgrip Mantle and Magister's Leggings. Hermit's Pauldron and Magister's Leggings were in the pool before. All other items are new in the database.

- **Commit df57e2571 (6 November) against commit 9a8624af9 (both).** The Retribution set does not change: 908.3. Combat Rogue +5.2% (671.6 → 706.2), Hunter +2.0% (855.6 → 872.7), Demonology Warlock +0.7% (856.3 → 862.5), Fury −1.5% (840.7 → 828.5), Fire Mage −1.0% (823.9 → 815.6). Pure average 809.6 → 817.1, Retribution 112.2% → 111.2%.
- **Two causes.** With the sets of 4 November on commit df57e2571 (`ec_results_df57e2571_old_sets.json`), the flask change alone gives Fury −1.9%, Hunter −1.9% and Rogue −1.2%. The pure average is then 801.7, and Retribution 113.3%. The new sets give +1.9% to the pure average.
- **Set changes.** Fury: Timbermaw Tunic, Deepfury Bracers (new), Bagh Nakh, Skypierce Javelin (new). Combat Rogue: Bagh Nakh in the main hand (+5.6% without enchants and consumables). Hunter: Flawless Arcanite Rifle (+3.9%). Fire Mage: Lapidis Tankard of Tidesippe (new) and Red Mageweave Headband. Demonology Warlock: Lapidis Tankard of Tidesippe. Bagh Nakh, Flawless Arcanite Rifle, Timbermaw Tunic and Red Mageweave Headband were in the pool before. The first search did not find them, because it starts from the wowsims test set and keeps a local best set.
- **Fire Mage.** The search runs without enchants and consumables. Lapidis Tankard of Tidesippe is better there (+0.6%), but with both, the Fire Mage loses 1.0%. The rules keep the result of the search.
- **The sets and logs of 4 November** are in `sets_9a8624af9/`, their values in `ec_results_9a8624af9.json`.

- **Commit 9a8624af9 (evening of 4 November) against commit 8298ab833.** Fury +0.2% (839.2 → 840.7, base 611.4 → 612.6, enchants 685.1 → 685.6, consumables 763.0 → 765.3): one Reckless Swings before the pull. The other specs do not change. Pure average (both) 809.6, Retribution 112.2%, 108.0% of Fury (`ec_results_9a8624af9.json`). On commit 8298ab833, the pure average was 809.3 and Retribution 112.2% (`ec_results_8298ab833.json`).
- **Against commit 6ee3c30f35 (earlier on 4 November).** Hunter −3.5% (887.0 → 855.6), Demonology Warlock +1.4% (844.8 → 856.3), Combat Rogue +0.8% (666.4 → 671.6), Fury +0.3% (836.6 → 839.2), Mage 0%. Retribution +0.2% (906.5 → 908.3). The Warlock and Retribution changes come from the consumables: the shared elixir list takes the elixirs of the new Warlock preset. On commit 6ee3c30f35, the pure average was 811.7 and Retribution 111.7% (`ec_results_6ee3c30f35.json`).

- **Commit 6ee3c30f35 against commit d97252f2a (3 November).** The hotfix 113578 ports give Fury +6.2% (787.9 → 836.6), Combat Rogue +5.0% (634.4 → 666.4) and Hunter +16.5% (761.2 → 887.0). Mage, Warlock and Retribution do not change. On commit d97252f2a, the pure average was 770.4 and Retribution 117.7% (`ec_results_d97252f2a.json`).
- **Commit d97252f2a against commit 895cd67f9.** Retribution +3.7% (874.4 → 906.5): Vengeance 5 stacks and Holy damage on Two-Handed Weapon Specialization. The pure specs lose 0–5%. wowsims now uses the trainer ranks of Strength of Earth Totem and Grace of Air Totem in the raid buffs. It also uses the trainer ranks of the Hunter spells. On commit 895cd67f9, the pure average was 783.9 and Retribution 111.5% (`ec_results_895cd67f9.json`).

With the consumables of each wowsims preset as they are, Retribution was 116.3% (both, commit 895cd67f9). The presets are not equal: Retribution has 9 elixirs, the Rogue has none. Thus, the second run gives the same elixirs and extras to all specs.

`models/beta-30-oct/retribution_b2.py` uses the "Both" column. It puts the values on the scale of the Retribution start value (841, the item pool set with the Retribution test buffs, full buffs and consumables): each pure spec × 841 / 843.5.

**First pool (replaced).** The first search let in later items: Zul'Gurub, Ahn'Qiraj and Argent Dawn reputation items, dungeon set 2, battleground weapons and trinkets. With it, the pure average was 850.2 and Retribution 108.3% (both). The sets of that run are in `first_pool/`.

## Files

| File | What it holds |
| --- | --- |
| dump.patch | Patch to `sim/core/test_suite.go`: with `ZZDUMP=<dir>`, each spec test writes its request as JSON |
| zzbatch_main.go | Batch runner. Copy to `cmd/zzbatch/main.go`, build with `-tags with_db`. It reads the dumped requests from `/tmp/zzdump` (or from the `dir` of the job) |
| solo.py | Runs each zzbatch job in its own process: `python3 solo.py jobs.json out.json`. Use it for all final values (see below) |
| opt.py, main.py | Item pool and search: `python3 main.py <Spec>` (Hunter: `EPFULL=1`, see below). The run of 11 November: `SEED=sets_9f254e8d8/set_<Spec>.json EFFECTS=<zzeffects list> python3 main.py <Spec>` |
| set_*.json | The final set of each spec (item ids, slot order of wowsims) |
| log_*.txt | Stat values, slot changes and final DPS of each spec. Since 11 November, also the DPS of each candidate (lines `all:`) |
| enchants.json | Enchant ids by slot for each spec (wowsims presets; Mage and Warlock: Balance Druid caster enchants, 2504 on the weapon) |
| enchants_consumables.py | Second run: writes `/tmp/zzdump_u` (same elixirs and extras for each spec) and the zzbatch jobs |
| ec_results.json | DPS of the second run on commit 3633d376a (base, ench, cons, both). `ec_results_9f254e8d8.json`, `ec_results_ae9b8c23a.json`, `ec_results_df57e2571.json`, `ec_results_9a8624af9.json`, `ec_results_8298ab833.json`, `ec_results_6ee3c30f35.json`, `ec_results_d97252f2a.json` and `ec_results_895cd67f9.json`: the same on the earlier commits |
| links.md, zzlink_main.go | wowsims links to the final set of each spec, and the script that makes them |

- **One job for each process.** zzbatch runs its jobs in parallel in one process. In a batch of different specs and enchants, some results changed by up to 3%. All values in this folder and in Analysis, Damage come again from `solo.py`, one job for each process. They agree with the batch values.
- **Hunter.** In the first run, the stat values were all 0, because the start set had no ranged weapon in the pool (`first_pool/log_Hunter_first_run.txt`, 612.9). The final run measures the stat values on the full test set (`EPFULL=1`).
- **Limits.** Many Forever items have no source in the game data. They stay in the pool. The same rule applies to all specs. The search can stop at a local best set.
- **Fight length (`fight_length.json`, commit 895cd67f9).** The final sets with enchants and consumables at 2, 3 and 5 min, `solo.py`, 10,000 iterations. Retribution: 111.5%, 113.6% and 114.8% of the pure average. Without the Rogue: 106.8%, 108.3% and 109.0%.
- **Rogue talents (`rogue_talents.json`, commit 895cd67f9).** The six wowsims Rogue talent presets on the final Rogue set, with and without Backstab in the rotation, 5,000 iterations. The test preset (Combat SS) gives 645. The best is Combat Backstab with 657 (+2%).
- **Raid buffs (`raid_buffs.json`, commit 895cd67f9).** All six wowsims test presets have the same raid and party buffs. Only the debuffs are different: the Hunter preset has no Hunter's Mark (the Hunter casts it), and the Warlock preset has no Curse of the Elements. A run with the buffs and debuffs of each own preset (`"own": true` in zzbatch) gives the same six values.
