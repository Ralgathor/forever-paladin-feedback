# wowsims check on the beta of 30 October

These files add the Retribution proposals to wowsims Forever, branch `paladin/hotfix-113554-port` (commit `db28d84a8`), and run the default Retribution set (default gear, default rotation, Unsealed Wrath build 14/5/32, default consumables).

| File | What it does |
| --- | --- |
| proposals_sim.go | Flags in `PROPOSE`: `C1` (Holy Strike triggers your active Seal), `BZ` (Burning Zeal 2/2: +20% critical damage bonus of Seals, Judgements and Holy Strike), `UW20` (Unsealed Wrath: Seal cost −20%) |
| talents.patch | Calls the flags after the talents |
| feedback_run_test.go | One sim: `FEEDBACK_DUR` (sec), `FEEDBACK_BUFFS` (`full` or `lean`), 3,000 iterations |
| run.sh | All runs: `./run.sh <wowsims clone>` |

- **Full buffs.** The wowsims test buffs, with Mana Spring Totem, Mana Tide Totem and Atiesh.
- **Lean buffs.** Gift of the Wild, Battle Shout, Kings, Might and Wisdom only.
- The results are in Retribution, wowsims check.
