# wowsims check on the beta of 30 October

These files add the Retribution proposals to wowsims Forever, branch `paladin/hotfix-113554-port` (commit `db28d84a8`), and run the default Retribution set (default gear, default rotation, Unsealed Wrath build 14/5/32, default consumables).

| File | What it does |
| --- | --- |
| proposals_sim.go | Flags in `PROPOSE`: `C1` (Holy Strike triggers your active Seal), `BZ` (Burning Zeal 2/2, withdrawn), `UW20` (Unsealed Wrath: Seal cost −20%), `CP1` (each Holy Shield cast starts Redoubt), `RD20` (Redoubt 4–20% in place of 6–30%), `CP6` (Reckoning C-P6: charges from blocks, dodges and parries, Holy Strike releases 2), `CP6R` (beta Reckoning triggers, Holy Strike releases 2), `RKB` (the beta block chance and limit also on dodges and parries) |
| talents.patch | Calls the flags after the talents, and the Reckoning flags |
| feedback_run_test.go | One Retribution sim: `FEEDBACK_DUR` (sec), `FEEDBACK_BUFFS` (`full` or `lean`), 3,000 iterations |
| feedback_prot_test.go | One Protection sim (default tank set, full buffs, level 63 boss in front): threat, damage taken and the boss attack table |
| feedback_warrior_test.go | The same for the Protection Warrior (pre-raid set), for comparison |
| run.sh | All runs: `./run.sh <wowsims clone>` |

- **Full buffs.** The wowsims test buffs, with Mana Spring Totem, Mana Tide Totem and Atiesh.
- **Lean buffs.** Gift of the Wild, Battle Shout, Kings, Might and Wisdom only.
- The results are in Retribution, wowsims check, and in Protection, wowsims check.
