# Pure damage specs with the same item pool (2 November 2026)

This run gives the pure average of Analysis, Damage (parts 1, 3 and 7). It replaces the MythicSim values of 22 October.

wowsims Forever, master commit `895cd67f9` (the same commit as the other wowsims checks of the beta of 30 October).

## Rules (the same for each spec)

- **Item pool.** Uncommon, rare and epic items of item level 63 or lower, for level 60 or lower. No raid drops and no world boss drops (zone and NPC sources in the wowsims data and AtlasLoot). No PvP items, no PvP reputation items, and not the raid items of the earlier `GEARFIX` list. No items with random enchantments.
- **Class.** Each spec keeps its armor and weapon types and its weapon setup (two-handed weapon, two weapons, or weapon and off-hand item).
- **Search.** Start: the wowsims test set without the items outside the pool (Fury: the `prebis_fury` set). For each slot, the candidates are the best items for the stat values of the spec (measured in the sim). All items with an effect are also candidates. The search keeps the best item for each slot (1,000 iterations, fixed seed) and repeats until no slot changes (3 passes at most). Final value: 10,000 iterations.
- **Conditions.** The search runs with no enchants and no consumables. The class weapon items stay (oils, stones, poisons). Retribution raid buffs and debuffs (with Judgement of the Crusader). Level 63 boss, 2 min.
- **Enchants and consumables (second run).** The sets of the search, with enchants and consumables (`enchants_consumables.py`, see below).

## Results

| Spec | No enchants, no consumables | Enchants | Consumables | Both | Average item level | Epic items |
| --- | --- | --- | --- | --- | --- | --- |
| Fury Warrior | 677.9 | 754.4 | 824.6 | 901.6 | 59.6 | 12 |
| Hunter | 673.7 | 719.8 | 778.8 | 828.7 | 59.8 | 7 |
| Fire Mage | 661.5 | 712.9 | 861.7 | 916.1 | 58.9 | 11 |
| Demonology Warlock | 655.1 | 709.7 | 861.2 | 919.3 | 59.0 | 8 |
| Combat Rogue | 545.1 | 578.3 | 648.4 | 685.2 | 59.4 | 9 |
| Pure average | 642.7 | 695.0 | 794.9 | 850.2 | | |
| Retribution (live) | 681.8 (106.1%) | 728.6 (104.8%) | 870.0 (109.4%) | 921.1 (108.3%) | 59.6 | 12 |

Without the Rogue (both): 891.4, Retribution 103.3%. Retribution against Fury (both): 102.2%.

With the consumables of each wowsims preset as they are, Retribution is 112.9% (both). The presets are not equal: Retribution has 9 elixirs, the Rogue has none. Thus, the second run gives the same elixirs and extras to all specs.

`models/beta-30-oct/retribution_b2.py` uses the "Both" column. It puts the values on the scale of the Retribution start value (906, full buffs and consumables): each pure spec × 906 / 921.1.

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

- **One job for each process.** zzbatch runs its jobs in parallel in one process. In a batch of different specs and enchants, some results changed by up to 5% (for example Grand Crusader). All values in this folder and in Analysis, Damage come again from `solo.py`, one job for each process. They agree with the batch values.
- **Hunter.** In the first run, the stat values were all 0, because the start set had no ranged weapon in the pool (`log_Hunter_first_run.txt`, 612.9). The final run measures the stat values on the full test set (`EPFULL=1`).
- **Limits.** Many Forever items have no source in the game data. Some reputation and crafted items from later content can stay in the pool. The same rule applies to all specs. The search can stop at a local best set.
