# Pure damage specs with the same item pool (2 November 2026)

This run gives the pure average of Analysis, Damage (parts 1, 3 and 7). It replaces the MythicSim values of 22 October.

wowsims Forever, master commit `895cd67f9` (the same commit as the other wowsims checks of the beta of 30 October).

## Rules (the same for each spec)

- **Item pool.** Uncommon, rare and epic items of item level 63 or lower, for level 60 or lower. No raid drops, no world boss drops (zone and NPC sources in the wowsims data and AtlasLoot), no PvP items, no PvP reputation items, and the raid items of the earlier `GEARFIX` list. No items with random enchantments.
- **Class.** Each spec keeps its armor and weapon types and its weapon setup (two-handed weapon, two weapons, or weapon and off-hand item).
- **Search.** Start: the wowsims test set without the items outside the pool (Fury: the `prebis_fury` set). For each slot, the candidates are the best items for the stat values of the spec (measured in the sim), and the items with an effect (all trinkets with an effect). The search keeps the best item for each slot (1,000 iterations, fixed seed) and repeats until no slot changes (3 passes at most). Final value: 10,000 iterations.
- **Conditions.** No enchants. The class weapon items stay (oils, stones, poisons). Retribution raid buffs and debuffs (with Judgement of the Crusader). No consumables. Level 63 boss, 2 min.

## Results

| Spec | DPS | Average item level | Epic items |
| --- | --- | --- | --- |
| Fury Warrior | 677.9 | 59.6 | 12 |
| Hunter | 673.7 | 59.8 | 7 |
| Fire Mage | 661.5 | 58.9 | 11 |
| Demonology Warlock | 655.1 | 59.0 | 8 |
| Combat Rogue | 545.1 | 59.4 | 9 |
| Retribution (live) | 681.8 | 59.6 | 12 |

Pure average 642.7. Retribution 106%. Without the Rogue: 667.1, Retribution 102%.

`models/beta-30-oct/retribution_b2.py` puts these values on the scale of the Retribution start value (906, full buffs and consumables): each pure spec × 906 / 681.8.

## Files

| File | What it holds |
| --- | --- |
| dump.patch | Patch to `sim/core/test_suite.go`: with `ZZDUMP=<dir>`, each spec test writes its request as JSON |
| zzbatch_main.go | Batch runner. Copy to `cmd/zzbatch/main.go`, build with `-tags with_db`. It reads the dumped requests from `/tmp/zzdump` |
| opt.py, main.py | Item pool and search: `python3 main.py <Spec>` (Hunter: `EPFULL=1`, see below) |
| set_*.json | The final set of each spec (item ids, slot order of wowsims) |
| log_*.txt | Stat values, slot changes and final DPS of each spec |

- **Hunter.** In the first run, the stat values were all 0, because the start set had no ranged weapon in the pool (`log_Hunter_first_run.txt`, 612.9). The final run measures the stat values on the full test set (`EPFULL=1`).
- **Limits.** Many Forever items have no source in the game data. Some reputation and crafted items from later content can stay in the pool. The same rule applies to all specs. The search can stop at a local best set.
