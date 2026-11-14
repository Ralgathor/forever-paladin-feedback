# wowsims links of the tank and builds sets (13 November 2026)

The `sets/` pages at the root of the repository open these sets in wowsims Forever: https://ralgathor.github.io/forever-paladin-feedback/sets/

| Page | Sim | Check on commit 8c7b5a5f5 |
| --- | --- | --- |
| tank-pool-protection-paladin.html | feedback_prot_test.go, `FEEDBACK_DUR=180`, `FEEDBACK_ITEMS` of ../tank_gear/set_prot.json | 1,138.9 threat per sec |
| tank-pool-protection-warrior.html | feedback_warrior_test.go, `FEEDBACK_DUR=180`, `FEEDBACK_ITEMS` of ../tank_gear/set_war.json | 1,525.0 threat per sec |
| tank-pool-bear-druid.html | feedback_bear_test.go, `FEEDBACK_DUR=180`, `FEEDBACK_ITEMS` of ../tank_gear/set_bear.json | 2,276.8 threat per sec |
| tank-surv-protection-paladin.html | feedback_prot_test.go, `FEEDBACK_DUR=180`, `FEEDBACK_ITEMS` of ../tank_gear/set_prot_surv.json | 1,089.7 threat per sec |
| tank-surv-protection-warrior.html | feedback_warrior_test.go, `FEEDBACK_DUR=180`, `FEEDBACK_ITEMS` of ../tank_gear/set_war_surv.json | 1,385.9 threat per sec |
| tank-surv-bear-druid.html | feedback_bear_test.go, `FEEDBACK_DUR=180`, `FEEDBACK_ITEMS` of ../tank_gear/set_bear_surv.json | 2,162.9 threat per sec |
| tank-protection-paladin.html | feedback_prot_test.go, `FEEDBACK_DUR=180` | 1,037.5 threat per sec |
| tank-protection-warrior.html | feedback_warrior_test.go, `FEEDBACK_DUR=180` | 1,470.4 threat per sec |
| tank-bear-druid.html | feedback_bear_test.go, `FEEDBACK_DUR=180` | 2,503.1 threat per sec |
| build-retribution.html | feedback_run_test.go, `FEEDBACK_DUR=180 FEEDBACK_BUFFS=full`, `FEEDBACK_ITEMS` of ../matched_gear/set_Retribution.json | 837.2 DPS (RB1) |
| build-shockadin.html | feedback_run_test.go, `FEEDBACK_DUR=180 FEEDBACK_BUFFS=full FEEDBACK_SHOCK=1`, `FEEDBACK_ITEMS` of ../tank_gear/set_shock.json | 815.5 DPS (SB1) |

Steps:

1. Set up wowsims as in `../run.sh`, on master commit 8c7b5a5f5 (Go 1.27) with `../patches/talents-9a8624af9.patch` and `../patches/judgement-ranged.patch` (see `../tank_gear/run_pool.sh`).
2. Run each test of the table with `FEEDBACK_DUMP=<dir>/<file>.json` and no `PROPOSE` flag. For the item pool sets, also set `FEEDBACK_ITEMS`. The file names are in `jobs.json`.
3. Copy `zzsets_main.go` to `cmd/zzsets/main.go` and run `go run -tags with_db ./cmd/zzsets <dir> jobs.json`. It prints the links. It also decodes each link and runs it again: the values of the table come from these runs.

On 6 November 2026, the Warrior item pool set changed (Scarlet Kris, `../tank_gear/README.md`). On 8 November 2026, the searches on master commit ae9b8c23a changed the Paladin, Druid, Retribution and Shockadin sets. On 9 November 2026, the searches on master commit 9f254e8d8 changed the Paladin threat set and the Druid survival set. wowsims also changed the default Warrior set.

On 11 November 2026, the searches on master commit 3633d376a changed five sets. These are the Paladin survival set, both Warrior sets, the Druid threat set and the Shockadin set. wowsims also changed the default Paladin set.

On 12 November 2026, the searches on master commit 52471a100 changed both Warrior sets and the Retribution set (Warblade of Caer Darrow). The Druid threat values increase by 43%, because this commit gives Lacerate 10/3 threat for each point of damage. Later on 12 November 2026, master commit 129fcd89e decreases the Hand of Justice and Ironfoe procs. The searches on this commit changed the Warrior survival set (Hammer of the Vesper) and the Retribution set (Demonshear).

The Warrior loses 3.0% threat and the Druid 1.1%. On 13 November 2026, master commit 8c7b5a5f5 adds 46 items, and the runs use the ranged judgements. The searches on this commit changed four sets: the Paladin threat and survival sets, the Warrior threat set and the Druid survival set. All four have The Lion Horn of Stormwind. All links come again from commit 8c7b5a5f5 with the same steps.

The links have the live talents and no proposal. Since commit 9a8624af9, wowsims gives the Warrior and the Druid the threat multipliers of the hotfixes of 4 November (Defensive Stance +80%, Defiance 20%, Bear Form +115%). The Paladin links have the tank consumables of `feedbackConsumables` (`../go/feedback_prot_test.go`).
