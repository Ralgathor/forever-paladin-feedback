# wowsims check on the beta of 30 October

These files add the proposals to wowsims Forever, master branch (commit `895cd67f9`, 1 November 2026). They run the default Retribution set: default gear, rotation and consumables (with Major Mana Potion), build 14/6/31. The earlier runs used branch `paladin/hotfix-113554-port` (commit `db28d84a8`) with the build 14/5/32.

| File | What it does |
| --- | --- |
| proposals_sim.go | Flags in `PROPOSE`: `C1` (Holy Strike triggers your active Seal), `BZ` (Burning Zeal 2/2, withdrawn), `UW20` (Unsealed Wrath: Seal cost −20%), `CP1` (each Holy Shield cast starts Redoubt), `RD20` (Redoubt 4–20% in place of 6–30%), `CP6` (Reckoning C-P6: charges from blocks, dodges and parries, Holy Strike releases 2), `CP6R` (beta Reckoning triggers, Holy Strike releases 2), `RKB` (the beta block chance and limit also on dodges and parries), `CP6A` (C-P6 triggers with the beta release on the next auto attack), `RK100` (Reckoning block chance 100%), `RKICD4` (Reckoning block limit 4 sec), `NOTOUGH` (Toughness removal, C-P13: Toughness gives no armor) |
| talents.patch | Calls the flags after the talents, the Reckoning flags and the `NOTOUGH` flag |
| feedback_run_test.go | One Retribution sim: `FEEDBACK_DUR` (sec), `FEEDBACK_BUFFS` (`full` or `lean`), 3,000 iterations |
| feedback_prot_test.go | One Protection sim (default tank set, full buffs, level 63 boss in front): threat, damage taken, TMI (6 sec window) and the boss attack table |
| feedback_warrior_test.go | The same for the Protection Warrior (pre-raid set), for comparison |
| feedback_bear_test.go | The same for the Druid tank (default Bear set): threat, damage taken, TMI and crushing blows |
| feedback_warrior_dps_test.go | One Fury or Arms Warrior sim for Analysis, Damage, part 9: `FEEDBACK_SPEC` (`fury` or `arms`), `FEEDBACK_GEAR` (`prebis` or `p1`), full buffs |
| `FEEDBACK_MANA` | In the Paladin tank test: also print the mana sources (Analysis, Mana) |
| `FEEDBACK_TARGETS` | In the three tank tests: the number of targets. Each target hits for 1/3 of the boss. The tests then print the threat on each target |
| run.sh | All runs: `./run.sh <wowsims clone>` |

- **Full buffs.** The wowsims test buffs, with Mana Spring Totem, Mana Tide Totem and Atiesh.
- **Lean buffs.** Gift of the Wild, Battle Shout, Kings, Might and Wisdom only.
- The results are in Retribution, wowsims check, in Protection, wowsims check, in Analysis, Threat, parts 7 and 8, in Analysis, Crushing blows, and in Analysis, Damage, part 9.
- Protection, wowsims check still has the 2 min runs of commit db28d84a8. The 3 min runs of master give almost the same values (Analysis, Crushing blows).
