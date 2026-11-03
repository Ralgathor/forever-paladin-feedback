# wowsims check on the beta of 30 October

These files add the proposals to wowsims Forever, master branch (commit `895cd67f9`, 1 November 2026). They run the default Retribution set: default gear, rotation and consumables (with Major Mana Potion), build 14/6/31. The earlier runs used branch `paladin/hotfix-113554-port` (commit `db28d84a8`) with the build 14/5/32. Build 70755 (3 November 2026, master commit `d97252f2a`) adds the two Retribution changes that `notes-2-november.patch` gives as flags.

The folders: `patches/` (the wowsims patches), `go/` (the sim flags and the test files), `apl/` (the rotations), `logs/` (the run logs). The scripts stay in this folder.

| File | What it does |
| --- | --- |
| go/proposals_sim.go | Flags in `PROPOSE`: `C1` (Holy Strike triggers your active Seal, withdrawn on 2 November 2026), `BZ` (Burning Zeal 2/2, withdrawn), `UW20` (Unsealed Wrath: Seal cost −20%), `CP1` (each Holy Shield cast starts Redoubt), `RD20` (Redoubt 4–20% in place of 6–30%), `CP6` (Reckoning C-P6: charges from blocks, dodges and parries, Holy Strike releases 2), `CP6R` (beta Reckoning triggers, Holy Strike releases 2), `RKB` (the beta block chance and limit also on dodges and parries), `CP6A` (C-P6 triggers with the beta release on the next auto attack), `RK100` (Reckoning block chance 100%), `RKICD4` (Reckoning block limit 4 sec), `NOTOUGH` (Toughness removal, C-P13: Toughness gives no armor), `REV50` (Reverence 25/50%, C-H1), `SA10` and `SA0` (Sacred Arbiter +10% or +0% in place of +20%), `C25` (Righteous Fury: all threat +90% in place of +33%; `RF_ALL` sets the multiplier, default 1.90) |
| patches/talents.patch | Calls the flags after the talents, the Reckoning flags and the `NOTOUGH` flag |
| go/feedback_run_test.go | One Retribution sim: `FEEDBACK_DUR` (sec), `FEEDBACK_BUFFS` (`full` or `lean`), 3,000 iterations |
| go/feedback_prot_test.go | One Protection sim (default tank set, full buffs, level 63 boss in front): threat, damage taken, TMI (6 sec window) and the boss attack table |
| go/feedback_warrior_test.go | The same for the Protection Warrior (pre-raid set), for comparison |
| go/feedback_bear_test.go | The same for the Druid tank (default Bear set): threat, damage taken, TMI and crushing blows |
| go/feedback_warrior_dps_test.go | One Fury or Arms Warrior sim for Analysis, Damage, part 9: `FEEDBACK_SPEC` (`fury` or `arms`), `FEEDBACK_GEAR` (`prebis` or `p1`), full buffs |
| `FEEDBACK_MANA` | In the Paladin tank test: also print the mana sources (Analysis, Mana) |
| `FEEDBACK_BOSS` | In the Paladin and Warrior tank tests: `fast` (a swing each 1.2 sec, 60% damage), `dw` (two weapons), or both |
| `FEEDBACK_TARGETS` | In the three tank tests: the number of targets. Each target hits for 1/3 of the boss. The tests then print the threat on each target |
| go/allspecs_main.go, logs/allspecs.log | All damage specs with pre-raid gear and the same buffs (Analysis, Damage, part 7). The file header gives the steps |
| matched_gear/ | The pure damage specs and Retribution with the same pre-raid item pool: the pure average of Analysis, Damage. See matched_gear/README.md |
| patches/notes-2-november.patch | Flags for the development notes of 2 November 2026: `N2H` (Two-Handed Weapon Specialization also increases Holy damage by 2/4/6%) and `V5` (Vengeance stacks up to 5 times). Apply after talents.patch. Result (default Retribution set, full buffs, 2 min): live 905.9 DPS, `N2H` 938.7, `V5` 946.3, both 980.8 |
| patches/threat-options.patch | Threat options for the gap after the notes of 2 November 2026 (Analysis, Threat), off by default. `PROPOSE=CP9`: Holy Shield adds block value × `CP9_BV` (default 2.0) to each hit (C-P9, withdrawn on 31 October). `HS_THREAT`: the Holy Shield threat multiplier (live 1.2). `CP6_ICD`: the C-P6 limit on blocks, dodges and parries in sec (default 4). Apply after talents.patch. Result (3 min, with `CP1`, Warrior 1,338 TPS after the notes): `CP1` 986, `CP9` at 1.0 1,089, at 2.0 1,192; `HS_THREAT` 2.0 1,120, 2.25 1,162, 2.5 1,203; `CP6A` with `CP6_ICD` 4 1,029, 2 1,108, 1 1,137; `HS_THREAT=2.0` with `CP9` at 1.0 1,292 |
| patches/burst-threat.patch | Analysis, Threat, part 8. A threat recorder in the core: with `FEEDBACK_BURST=<label>`, the three tank tests print the threat on the boss after 1.5, 3, 4.5, 6, 8, 10, 15, 20 and 30 sec (mean, 10% and 90% of the fights) and the best 3, 6 and 10 sec windows of the fight. The fight length is then fixed. Apply after threat-options.patch |
| apl/furyopen.apl.json, apl/furyopen1.apl.json | Paladin Fury openers for part 8 (`FEEDBACK_APL=furyopen`): Seal of Fury at −3 sec and Holy Shield at −1.5 sec, then Judgement of Fury, Swift Judgement and Holy Strike at 0 sec. `furyopen1`: Swift Judgement at 1.5 sec |
| apl/charge.apl.json | Warrior default rotation with Charge at −0.5 sec from 20 yards (`FEEDBACK_CHARGE=1`) |
| `FEEDBACK_NOENG` | In the Warrior tank test: no Engineering, thus no Goblin Sapper Charge |
| `FEEDBACK_LOG`, `FEEDBACK_SRC` | In the three tank tests: the combat log of one fight, or the threat of each spell |
| run.sh | All runs: `./run.sh <wowsims clone>` |

- **Full buffs.** The wowsims test buffs, with Mana Spring Totem, Mana Tide Totem and Atiesh.
- **Lean buffs.** Gift of the Wild, Battle Shout, Kings, Might and Wisdom only.
- The results are in Retribution and Protection (wowsims check). They are also in Analysis: Threat (parts 6 to 9), Crushing blows and Damage (part 9).
- Protection, wowsims check still has the 2 min runs of commit db28d84a8. The 3 min runs of master give almost the same values (Analysis, Crushing blows).
