# Best builds and stat weights

This folder gives the best build and the stat weights of each spec. It uses the live trees and the proposed trees of calculator version 6. It also gives a talent order to level up. This folder is a reference. It does not change a proposal.

| Spec | File | Best proposed build | Best live build |
| --- | --- | --- | --- |
| Holy (healer) | [holy.md](holy.md) | HB2, 31/12/8: [`v6p50320115202101251-50122000000000002-0503`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p50320115202101251-50122000000000002-0503) | HB1, 38/5/8: [`b250325115202121251-5-0503`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b250325115202121251-5-0503) |
| Protection (tank) | [protection.md](protection.md) | PS1, 0/34/17: [`v6p-3530110213501531-53233000001`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p-3530110213501531-53233000001) | BS2, 0/35/16: [`b2-05302102313501531-52233000001`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2-05302102313501531-52233000001), or BS1 for more threat |
| Retribution (damage), raid and fresh 60 | [retribution.md](retribution.md) | RB1, 14/6/31: [`v6p050250002-501-05233011201301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p050250002-501-05233011201301351) | RB1, 14/6/31: [`b2050250002-501-05233011201301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2050250002-501-05233011201301351) |
| Shockadin (Holy Shock damage), raid and fresh 60 | [shockadin.md](shockadin.md) | SB1, 23/0/28: [`v6p05025210221021--0523330110130033`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p05025210221021--0523330110130033) | SB1, 23/0/28: [`b205025210221021--0523330110130033`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b205025210221021--0523330110130033) |
| Level-up (live) | [level-up.md](level-up.md) | — | Ends at RB1 |

## Main results

| Spec | Measure | Proposed | Live | Proposed against live |
| --- | --- | --- | --- | --- |
| Holy | Healing each sec, raid, 5 min | 728 | 479 | +52% |
| Holy | Healing each sec, one tank, 5 min | 658 | 568 | +16% |
| Protection | Threat each sec | 1,076 | 1,006 | +7.0% |
| Protection | Damage taken each sec | 295 | 331 | −11% |
| Protection | TMI (lower is better) | 45.3 | 56.3 | −19% |
| Retribution | DPS, raid | 944 | 944 | 0% |
| Retribution | DPS, fresh 60 | 328 | 315 | +4.2% |
| Shockadin | DPS, raid | 852 | 851 | 0% |
| Shockadin | DPS, fresh 60 | 304 | 290 | +4.9% |

- **Holy.** Light's Vigil (C-H7) gives the raid healing. Oath of Light 30% (C-H8) gives the one-tank healing. Reverence 50% (C-H1) gives +5–9% healing, more in long fights. HB2 takes Devoted Sacrifice (C-P11) with the free points.
- **Protection.** Redoubt (C-P1) removes almost all crushing blows and adds threat with more Holy Shield blocks. Righteous Fury (C25) multiplies all threat by 1.43.
- **Retribution.** Reverence 50% (C-H1) adds mana at fresh 60. In a raid, the proposed and live trees give the same damage. The 944 DPS use 3 min fights. Analysis, Damage gives 938 DPS with the 2 min wowsims test run.
- **Shockadin.** SB1 is 90% of RB1 in a raid, with the wowsims Holy Shock set. Reverence 50% (C-H1) adds mana at fresh 60. Light's Vigil (C-H7) gives a build with 31 Holy points +9.4%, but this build stays 11% below SB1.

## Common rules

- **Codes.** All build codes load with 51 points. The level-up codes show the points at a lower level. A code that starts with `v6p` opens the proposed trees. A code that starts with `b2` opens the live trees.
- **Sim.** wowsims Forever, master of 3 November 2026 (commit d97252f2a, game files of client 1.60.1.70755), with the proposals as flags (`models/wowsims-b2`). 3 min, one level 63 boss, 3,000 iterations.
- **Gear.** The default gear set of each spec in wowsims Forever: [Protection Paladin](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-protection-paladin.html) and [Retribution](https://ralgathor.github.io/forever-paladin-feedback/sets/build-retribution.html). The Shockadin uses the [wowsims Holy Shock set](https://ralgathor.github.io/forever-paladin-feedback/sets/build-shockadin.html). This folder has no gear search.
- **Holy.** wowsims Forever has no Holy healing sim. The Holy values come from the healing model (`models/beta-30-oct/healing_b2.py`), with 175% critical heals (Holy Power 5/5, main hypothesis).
- **Stat weights.** Each stat changes by a small amount, with the same random seed for all runs. The reference stat is 1.00: healing power for Holy, Strength for Retribution, spell damage for the Shockadin. For Protection, the table gives the change for each point.
- **Talent search.** A hill climb in wowsims (`models/wowsims-b2/search.py`). It gives a good build, not a proven best build.

## Sources

- Damage and tank: talent search in wowsims Forever (commit 895cd67f9), builds and stat weights again on commit d97252f2a (the same values on commit 6ee3c30f35 of 4 November). Scripts and logs in `models/wowsims-b2` (`search.py`, `finals.py`, `logs/finals.log`).
- Shockadin: talent search, builds and stat weights in wowsims Forever (commit 6ee3c30f35), with the Light's Vigil flag CH7 (`search.py`, `finals.py shock`, `logs/finals_shock.log`).
- Healer: healing model and stat weights (`models/beta-30-oct/holy_builds_b2.py`).
- Level-up: wowsims Forever (commit 895cd67f9), live talents (`models/wowsims-b2/levelup.py`).
- The earlier files (trees of 18 October, calculator version 5) are in the history of the repository.
