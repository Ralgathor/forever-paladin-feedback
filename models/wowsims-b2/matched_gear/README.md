# Pure damage specs with the same item pool (2 November 2026)

This run gives the pure average of Analysis, Damage (parts 1, 3 and 7). It replaces the MythicSim values of 22 October.

wowsims Forever, master commit `895cd67f9` (the same commit as the other wowsims checks of the beta of 30 October).

## Rules (the same for each spec)

- **Item pool.** Uncommon, rare and epic items of item level 63 or lower, for level 60 or lower. Only content of the game start and Dire Maul: no Classic items with item ids 19000–23999 (patch 1.6 or later: Zul'Gurub, Ahn'Qiraj and Naxxramas era items, dungeon set 2, battleground rewards). No items that need Revered or Exalted reputation. Not Jewel of the Guard Captain (a battleground name, no source). No raid drops and no world boss drops (zone and NPC sources in the wowsims data and AtlasLoot). No PvP items, no PvP reputation items, and not the raid items of the earlier `GEARFIX` list. No items with random enchantments.
- **Class.** Each spec keeps its armor and weapon types and its weapon setup (two-handed weapon, two weapons, or weapon and off-hand item).
- **Search.** Start: the wowsims test set without the items outside the pool (Fury: the `prebis_fury` set). For each slot, the candidates are the best items for the stat values of the spec (measured in the sim). All items with an effect are also candidates. The search keeps the best item for each slot (1,000 iterations, fixed seed) and repeats until no slot changes (3 passes at most). Final value: 10,000 iterations.
- **Conditions.** The search runs with no enchants and no consumables. The class weapon items stay (oils, stones, poisons). Retribution raid buffs and debuffs (with Judgement of the Crusader). Level 63 boss, 2 min.
- **Enchants and consumables (second run).** The sets of the search, with enchants and consumables (`enchants_consumables.py`, see below).

## Results

| Spec | No enchants, no consumables | Enchants | Consumables | Both | Average item level | Epic items |
| --- | --- | --- | --- | --- | --- | --- |
| Fury Warrior | 592.9 | 662.7 | 735.7 | 804.8 | 58.6 | 5 |
| Hunter | 651.8 | 703.9 | 745.0 | 799.6 | 59.2 | 4 |
| Fire Mage | 580.7 | 629.3 | 772.1 | 824.0 | 57.6 | 3 |
| Demonology Warlock | 589.1 | 642.7 | 788.5 | 845.6 | 57.0 | 3 |
| Combat Rogue | 514.1 | 546.2 | 614.6 | 645.6 | 58.5 | 3 |
| Pure average | 585.7 | 637.0 | 731.2 | 783.9 | | |
| Retribution (live) | 645.7 (110.2%) | 691.9 (108.6%) | 823.5 (112.6%) | 874.4 (111.5%) | 59.1 | 5 |

Without the Rogue (both): 818.5, Retribution 106.8%. Retribution against Fury (both): 108.6%.

With the consumables of each wowsims preset as they are, Retribution is 116.3% (both). The presets are not equal: Retribution has 9 elixirs, the Rogue has none. Thus, the second run gives the same elixirs and extras to all specs.

`models/beta-30-oct/retribution_b2.py` uses the "Both" column. It puts the values on the scale of the Retribution start value (906, full buffs and consumables): each pure spec × 906 / 874.4.

**First pool (replaced).** The first search let in later items: Zul'Gurub, Ahn'Qiraj and Argent Dawn reputation items, dungeon set 2, battleground weapons and trinkets. With it, the pure average was 850.2 and Retribution 108.3% (both). The sets of that run are in `first_pool/`.

## Files

| File | What it holds |
| --- | --- |
| dump.patch | Patch to `sim/core/test_suite.go`: with `ZZDUMP=<dir>`, each spec test writes its request as JSON |
| zzbatch_main.go | Batch runner. Copy to `cmd/zzbatch/main.go`, build with `-tags with_db`. It reads the dumped requests from `/tmp/zzdump` (or from the `dir` of the job) |
| solo.py | Runs each zzbatch job in its own process: `python3 solo.py jobs.json out.json`. Use it for all final values (see below) |
| opt.py, main.py | Item pool and search: `python3 main.py <Spec>` (Hunter: `EPFULL=1`, see below) |
| set_*.json | The final set of each spec (item ids, slot order of wowsims) |
| log_*.txt | Stat values, slot changes and final DPS of each spec |
| enchants.json | Enchant ids by slot for each spec (wowsims presets; Mage and Warlock: Balance Druid caster enchants, 2504 on the weapon) |
| enchants_consumables.py | Second run: writes `/tmp/zzdump_u` (same elixirs and extras for each spec) and the zzbatch jobs |
| ec_results.json | DPS of the second run (base, ench, cons, both) |
| links.md, zzlink_main.go | wowsims links to the final set of each spec, and the script that makes them |

- **One job for each process.** zzbatch runs its jobs in parallel in one process. In a batch of different specs and enchants, some results changed by up to 3%. All values in this folder and in Analysis, Damage come again from `solo.py`, one job for each process. They agree with the batch values.
- **Hunter.** In the first run, the stat values were all 0, because the start set had no ranged weapon in the pool (`first_pool/log_Hunter_first_run.txt`, 612.9). The final run measures the stat values on the full test set (`EPFULL=1`).
- **Limits.** Many Forever items have no source in the game data. They stay in the pool. The same rule applies to all specs. The search can stop at a local best set.
