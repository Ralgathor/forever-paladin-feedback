# wowsims links of the tank and builds sets (11 November 2026)

The `sets/` pages at the root of the repository open these sets in wowsims Forever: https://ralgathor.github.io/forever-paladin-feedback/sets/

| Page | Sim | Check on commit 3633d376a |
| --- | --- | --- |
| tank-pool-protection-paladin.html | feedback_prot_test.go, `FEEDBACK_DUR=180`, `FEEDBACK_ITEMS` of ../tank_gear/set_prot.json | 1,133.4 threat per sec |
| tank-pool-protection-warrior.html | feedback_warrior_test.go, `FEEDBACK_DUR=180`, `FEEDBACK_ITEMS` of ../tank_gear/set_war.json | 1,632.4 threat per sec |
| tank-pool-bear-druid.html | feedback_bear_test.go, `FEEDBACK_DUR=180`, `FEEDBACK_ITEMS` of ../tank_gear/set_bear.json | 1,613.6 threat per sec |
| tank-surv-protection-paladin.html | feedback_prot_test.go, `FEEDBACK_DUR=180`, `FEEDBACK_ITEMS` of ../tank_gear/set_prot_surv.json | 1,082.3 threat per sec |
| tank-surv-protection-warrior.html | feedback_warrior_test.go, `FEEDBACK_DUR=180`, `FEEDBACK_ITEMS` of ../tank_gear/set_war_surv.json | 1,448.4 threat per sec |
| tank-surv-bear-druid.html | feedback_bear_test.go, `FEEDBACK_DUR=180`, `FEEDBACK_ITEMS` of ../tank_gear/set_bear_surv.json | 1,524.8 threat per sec |
| tank-protection-paladin.html | feedback_prot_test.go, `FEEDBACK_DUR=180` | 1,031.2 threat per sec |
| tank-protection-warrior.html | feedback_warrior_test.go, `FEEDBACK_DUR=180` | 1,483.5 threat per sec |
| tank-bear-druid.html | feedback_bear_test.go, `FEEDBACK_DUR=180` | 1,743.3 threat per sec |
| build-retribution.html | feedback_run_test.go, `FEEDBACK_DUR=180 FEEDBACK_BUFFS=full`, `FEEDBACK_ITEMS` of ../matched_gear/set_Retribution.json | 847.3 DPS (RB1) |
| build-shockadin.html | feedback_run_test.go, `FEEDBACK_DUR=180 FEEDBACK_BUFFS=full FEEDBACK_SHOCK=1`, `FEEDBACK_ITEMS` of ../tank_gear/set_shock.json | 833.8 DPS (SB1) |

Steps:

1. Set up wowsims as in `../run.sh`, on master commit 3633d376a (Go 1.27) with `../patches/talents-9a8624af9.patch` (see `../tank_gear/run_pool.sh`).
2. Run each test of the table with `FEEDBACK_DUMP=<dir>/<file>.json` and no `PROPOSE` flag. For the item pool sets, also set `FEEDBACK_ITEMS`. The file names are in `jobs.json`.
3. Copy `zzsets_main.go` to `cmd/zzsets/main.go` and run `go run -tags with_db ./cmd/zzsets <dir> jobs.json`. It prints the links. It also decodes each link and runs it again: the values of the table come from these runs.

On 6 November 2026, the Warrior item pool set changed (Scarlet Kris, `../tank_gear/README.md`). On 8 November 2026, the searches on master commit ae9b8c23a changed the Paladin, Druid, Retribution and Shockadin sets. On 9 November 2026, the searches on master commit 9f254e8d8 changed the Paladin threat set and the Druid survival set. wowsims also changed the default Warrior set. On 11 November 2026, the searches on master commit 3633d376a changed five sets. These are the Paladin survival set, both Warrior sets, the Druid threat set and the Shockadin set. wowsims also changed the default Paladin set. All links come again from commit 3633d376a with the same steps.

The links have the live talents and no proposal. Since commit 9a8624af9, wowsims gives the Warrior and the Druid the threat multipliers of the hotfixes of 4 November (Defensive Stance +80%, Defiance 20%, Bear Form +115%). The Paladin links have the tank consumables of `feedbackConsumables` (`../go/feedback_prot_test.go`).
