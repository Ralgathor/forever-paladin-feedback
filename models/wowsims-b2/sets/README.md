# wowsims links of the tank and builds sets (19 November 2026)

The `sets/` pages at the root of the repository open these sets in wowsims Forever: https://ralgathor.github.io/forever-paladin-feedback/sets/

| Page | Sim | Check on commit ad6b13af8 |
| --- | --- | --- |
| tank-pool-protection-paladin.html | feedback_prot_test.go, `FEEDBACK_DUR=180`, `FEEDBACK_ITEMS` of ../tank_gear/set_prot.json | 1,439.3 threat per sec |
| tank-pool-protection-warrior.html | feedback_warrior_test.go, `FEEDBACK_DUR=180`, `FEEDBACK_ITEMS` of ../tank_gear/set_war.json | 1,931.5 threat per sec |
| tank-pool-bear-druid.html | feedback_bear_test.go, `FEEDBACK_DUR=180`, `FEEDBACK_ITEMS` of ../tank_gear/set_bear.json | 2,674.3 threat per sec |
| tank-surv-protection-paladin.html | feedback_prot_test.go, `FEEDBACK_DUR=180`, `FEEDBACK_ITEMS` of ../tank_gear/set_prot_surv.json | 1,246.9 threat per sec |
| tank-surv-protection-warrior.html | feedback_warrior_test.go, `FEEDBACK_DUR=180`, `FEEDBACK_ITEMS` of ../tank_gear/set_war_surv.json | 1,600.5 threat per sec |
| tank-surv-bear-druid.html | feedback_bear_test.go, `FEEDBACK_DUR=180`, `FEEDBACK_ITEMS` of ../tank_gear/set_bear_surv.json | 2,405.7 threat per sec |
| tank-protection-paladin.html | feedback_prot_test.go, `FEEDBACK_DUR=180` | 1,051.9 threat per sec |
| tank-protection-warrior.html | feedback_warrior_test.go, `FEEDBACK_DUR=180` | 1,730.6 threat per sec |
| tank-bear-druid.html | feedback_bear_test.go, `FEEDBACK_DUR=180` | 2,679.7 threat per sec |
| build-retribution.html | feedback_run_test.go, `FEEDBACK_DUR=180 FEEDBACK_BUFFS=full`, `FEEDBACK_ITEMS` of ../matched_gear/set_Retribution.json | 919.0 DPS (RB1) |
| build-shockadin.html | feedback_run_test.go, `FEEDBACK_DUR=180 FEEDBACK_BUFFS=full FEEDBACK_SHOCK=1`, `FEEDBACK_ITEMS` of ../tank_gear/set_shock.json | 817.6 DPS (SB1) |

Steps:

1. Set up wowsims as in `../run.sh`, on master commit ad6b13af8 (Go 1.27) with `../patches/talents-9a8624af9.patch` (see `../tank_gear/run_pool.sh`). On this commit, the patch applies only with `patch -p1 --fuzz=3`. Since this commit, wowsims makes the judgements ranged attacks itself: do not apply `../patches/judgement-ranged.patch`.
2. Run each test of the table with `FEEDBACK_DUMP=<dir>/<file>.json` and no `PROPOSE` flag. For the item pool sets, also set `FEEDBACK_ITEMS`. The file names are in `jobs.json`.
3. Copy `zzsets_main.go` to `cmd/zzsets/main.go` and run `go run -tags with_db ./cmd/zzsets <dir> jobs.json`. It prints the links. It also decodes each link and runs it again: the values of the table come from these runs.

On 6 November 2026, the Warrior item pool set changed (Scarlet Kris, `../tank_gear/README.md`). On 8 November 2026, the searches on master commit ae9b8c23a changed the Paladin, Druid, Retribution and Shockadin sets. On 9 November 2026, the searches on master commit 9f254e8d8 changed the Paladin threat set and the Druid survival set. wowsims also changed the default Warrior set.

On 11 November 2026, the searches on master commit 3633d376a changed five sets. These are the Paladin survival set, both Warrior sets, the Druid threat set and the Shockadin set. wowsims also changed the default Paladin set.

On 12 November 2026, the searches on master commit 52471a100 changed both Warrior sets and the Retribution set (Warblade of Caer Darrow). The Druid threat values increase by 43%, because this commit gives Lacerate 10/3 threat for each point of damage. Later on 12 November 2026, master commit 129fcd89e decreases the Hand of Justice and Ironfoe procs. The searches on this commit changed the Warrior survival set (Hammer of the Vesper) and the Retribution set (Demonshear).

The Warrior loses 3.0% threat and the Druid 1.1%. On 13 November 2026, master commit 8c7b5a5f5 adds 46 items, and the runs use the ranged judgements. The searches on this commit changed four sets: the Paladin threat and survival sets, the Warrior threat set and the Druid survival set. All four have The Lion Horn of Stormwind. All links come again from commit 8c7b5a5f5 with the same steps.

On 15 November 2026, master commit 6084403a9 adds 98 items and changes the Warrior and Druid presets, the rage rules and Windfury Totem. The searches on this commit changed three sets: both Warrior sets and the Druid threat set (`../tank_gear/README.md`). The Retribution set takes Counterattack Lodestone. Some other links change because the wowsims presets changed (for example the default Warrior and Druid sets).

On 16 November 2026, an open item search on the same commit (`../tank_gear/search_open.py`) changed all six item pool tank sets. The six tank pool links come again from commit 6084403a9 with the same steps. The other links do not change.

On 18 November 2026, master commit ad6b13af8 changes the proc rates of many items and adds the Destiny proc. The searches on this commit changed four tank sets: the Paladin threat and survival sets and the Druid threat and survival sets (`../tank_gear/README.md`). The Retribution set takes Destiny and Soulforge Warboots (`../matched_gear/README.md`). All links come again from commit ad6b13af8 with the same steps. The Warrior sets and the Shockadin set do not change.

On the evening of 18 November 2026, the six item pool tank links and the Retribution link come again from commit ad6b13af8 with the enchants of the same rules (`FEEDBACK_ENCHANTS`: `../tank_gear/enchants_*.json`, `../matched_gear/enchants_fair.json`). The tank links also have the full threat consumables (`FEEDBACK_CONSUMES=full`, `fullsurv` for the survival sets). The values of the table come from these runs. The default set links and the Shockadin link do not change.

On 19 November 2026, the two Paladin item pool tank links come again from commit ad6b13af8 with the same steps. The Paladin sets now have Crusader on the weapon (not Revelation) and Libram of Invocation (not Libram of Holy Alacrity). The other links do not change.

Later on 19 November 2026, the Paladin survival link comes again from commit ad6b13af8 with the same steps. The Paladin survival set now has the 5 pieces of Deathbone Guardian (`../tank_gear/search_sets.py`). The other links do not change.

The links have the live talents and no proposal. Since commit 9a8624af9, wowsims gives the Warrior and the Druid the threat multipliers of the hotfixes of 4 November (Defensive Stance +80%, Defiance 20%, Bear Form +115%). The Paladin default set link has the tank consumables of `feedbackConsumables` (`../go/feedback_prot_test.go`).
