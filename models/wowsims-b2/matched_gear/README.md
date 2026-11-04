# Pure damage specs with the same item pool (2 November 2026)

This run gives the pure average of Analysis, Damage (parts 1, 3 and 7).

The item search ran on wowsims Forever, master commit `895cd67f9` (1 November 2026). On 3 November 2026, the same sets ran again on master commit `d97252f2a` (game files of client 1.60.1.70755), and on 4 November on master commit `6ee3c30f35` (the hotfix 113578 ports of the Warrior, Rogue and Hunter). The results below come from commit `6ee3c30f35`.

## Rules (the same for each spec)

- **Item pool.** Uncommon, rare and epic items of item level 63 or lower, for level 60 or lower. Only content of the game start and Dire Maul. No Classic items with item ids 19000–23999. These items are from patch 1.6 or later: Zul'Gurub, Ahn'Qiraj and Naxxramas era items, dungeon set 2 and battleground rewards. No items that need Revered or Exalted reputation. Not Jewel of the Guard Captain (a battleground name, no source). No raid drops and no world boss drops (zone and NPC sources in the wowsims data and AtlasLoot). No PvP items, no PvP reputation items, and not the raid items of the earlier `GEARFIX` list. No items with random enchantments.
- **Class.** Each spec keeps its armor and weapon types and its weapon setup (two-handed weapon, two weapons, or weapon and off-hand item).
- **Search.** Start: the wowsims test set without the items outside the pool (Fury: the `prebis_fury` set). For each slot, the candidates are the best items for the stat values of the spec (measured in the sim). All items with an effect are also candidates. The search keeps the best item for each slot (1,000 iterations, fixed seed) and repeats until no slot changes (3 passes at most). Final value: 10,000 iterations.
- **Conditions.** The search runs with no enchants and no consumables. The class weapon items stay (oils, stones, poisons). The full wowsims test raid buffs and debuffs, the same for all specs (melee and caster buffs, totems, auras, all debuffs with Judgement of the Crusader). Level 63 boss, 2 min.
- **Enchants and consumables (second run).** The sets of the search, with enchants and consumables (`enchants_consumables.py`, see below).

## Results

| Spec | No enchants, no consumables | Enchants | Consumables | Both | Average item level | Epic items |
| --- | --- | --- | --- | --- | --- | --- |
| Fury Warrior | 613.1 | 686.2 | 761.9 | 836.6 | 58.6 | 5 |
| Hunter | 706.2 | 763.7 | 822.2 | 887.0 | 59.2 | 4 |
| Fire Mage | 583.5 | 632.4 | 772.1 | 823.9 | 57.6 | 3 |
| Demonology Warlock | 588.4 | 642.0 | 787.7 | 844.8 | 57.0 | 3 |
| Combat Rogue | 527.3 | 562.8 | 630.3 | 666.4 | 58.5 | 3 |
| Pure average | 603.7 | 657.4 | 754.8 | 811.7 | | |
| Retribution (live) | 667.1 (110.5%) | 715.5 (108.8%) | 853.3 (113.0%) | 906.5 (111.7%) | 59.1 | 5 |

Without the Rogue (both): 848.1, Retribution 106.9%. Retribution against Fury (both): 108.4%.

- **Against commit d97252f2a (3 November).** The hotfix 113578 ports give Fury +6.2% (787.9 → 836.6), Combat Rogue +5.0% (634.4 → 666.4) and Hunter +16.5% (761.2 → 887.0). Mage, Warlock and Retribution do not change. On commit d97252f2a, the pure average was 770.4 and Retribution 117.7% (`ec_results_d97252f2a.json`).
- **Commit d97252f2a against commit 895cd67f9.** Retribution +3.7% (874.4 → 906.5): Vengeance 5 stacks and Holy damage on Two-Handed Weapon Specialization. The pure specs lose 0–5%. wowsims now uses the trainer ranks of Strength of Earth Totem and Grace of Air Totem in the raid buffs. It also uses the trainer ranks of the Hunter spells. On commit 895cd67f9, the pure average was 783.9 and Retribution 111.5% (`ec_results_895cd67f9.json`).

With the consumables of each wowsims preset as they are, Retribution was 116.3% (both, commit 895cd67f9). The presets are not equal: Retribution has 9 elixirs, the Rogue has none. Thus, the second run gives the same elixirs and extras to all specs.

`models/beta-30-oct/retribution_b2.py` uses the "Both" column. It puts the values on the scale of the Retribution start value (938, full buffs and consumables): each pure spec × 938 / 906.5.

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
| ec_results.json | DPS of the second run on commit 6ee3c30f35 (base, ench, cons, both). `ec_results_d97252f2a.json` and `ec_results_895cd67f9.json`: the same on commits d97252f2a and 895cd67f9 |
| links.md, zzlink_main.go | wowsims links to the final set of each spec, and the script that makes them |

- **One job for each process.** zzbatch runs its jobs in parallel in one process. In a batch of different specs and enchants, some results changed by up to 3%. All values in this folder and in Analysis, Damage come again from `solo.py`, one job for each process. They agree with the batch values.
- **Hunter.** In the first run, the stat values were all 0, because the start set had no ranged weapon in the pool (`first_pool/log_Hunter_first_run.txt`, 612.9). The final run measures the stat values on the full test set (`EPFULL=1`).
- **Limits.** Many Forever items have no source in the game data. They stay in the pool. The same rule applies to all specs. The search can stop at a local best set.
- **Fight length (`fight_length.json`, commit 895cd67f9).** The final sets with enchants and consumables at 2, 3 and 5 min, `solo.py`, 10,000 iterations. Retribution: 111.5%, 113.6% and 114.8% of the pure average. Without the Rogue: 106.8%, 108.3% and 109.0%.
- **Rogue talents (`rogue_talents.json`, commit 895cd67f9).** The six wowsims Rogue talent presets on the final Rogue set, with and without Backstab in the rotation, 5,000 iterations. The test preset (Combat SS) gives 645. The best is Combat Backstab with 657 (+2%).
- **Raid buffs (`raid_buffs.json`, commit 895cd67f9).** All six wowsims test presets have the same raid and party buffs. Only the debuffs are different: the Hunter preset has no Hunter's Mark (the Hunter casts it), and the Warlock preset has no Curse of the Elements. A run with the buffs and debuffs of each own preset (`"own": true` in zzbatch) gives the same six values.
