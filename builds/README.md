# Best builds and stat weights

This folder gives the best build and the stat weights of each spec. It uses the live trees and the proposed trees of calculator version 6. It also gives a talent order to level up. This folder is a reference. It does not change a proposal.

| Spec | File | Best proposed build | Best live build |
| --- | --- | --- | --- |
| Holy (healer) | [holy.md](holy.md) | HB2, 31/12/8: [`v6p50320115202101251-50122000000000002-0503`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p50320115202101251-50122000000000002-0503) | HB1, 38/5/8: [`b250325115202121251-5-0503`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b250325115202121251-5-0503) |
| Protection (tank) | [protection.md](protection.md) | PS1, 0/34/17: [`v6p-3530110213501531-53233000001`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p-3530110213501531-53233000001) | BS2, 0/35/16: [`b2-05302102313501531-52233000001`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2-05302102313501531-52233000001), or BS1 for more threat |
| Retribution (damage), raid and fresh 60 | [retribution.md](retribution.md) | RB1, 14/6/31: [`v6p050250002-501-05233011201301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p050250002-501-05233011201301351) | RB1, 14/6/31: [`b2050250002-501-05233011201301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2050250002-501-05233011201301351) |
| Level-up (live) | [level-up.md](level-up.md) | — | Ends at RB1 |

## Main results

| Spec | Measure | Proposed | Live | Proposed against live |
| --- | --- | --- | --- | --- |
| Holy | Healing each sec, raid, 5 min | 568 | 533 | +6.6% |
| Holy | Healing each sec, one tank, 5 min | 670 | 633 | +5.8% |
| Protection | Threat each sec | 1,007 | 953 | +5.7% |
| Protection | Damage taken each sec | 291 | 325 | −10% |
| Protection | TMI (lower is better) | 45.0 | 55.5 | −19% |
| Retribution | DPS, raid | 910 | 910 | 0% |
| Retribution | DPS, fresh 60 | 315 | 303 | +4.1% |

- **Holy.** Reverence 50% (C-H1) gives +5–9% healing, more in long fights. HB2 takes Devoted Sacrifice (C-P11) with the free points.
- **Protection.** Redoubt (C-P1) removes almost all crushing blows and adds threat with more Holy Shield blocks. Righteous Fury (C25) multiplies all threat by 1.42.
- **Retribution.** Reverence 50% (C-H1) adds mana at fresh 60. In a raid, the proposed and live trees give the same damage.

## Common rules

- **Codes.** All build codes load with 51 points. The level-up codes show the points at a lower level. A code that starts with `v6p` opens the proposed trees. A code that starts with `b2` opens the live trees.
- **Sim.** wowsims Forever, master of 1 November 2026 (commit 895cd67f9), with the proposals as flags (`models/wowsims-b2`). 3 min, one level 63 boss, 3,000 iterations.
- **Gear.** The default gear set of each spec in wowsims Forever. This folder has no gear search.
- **Holy.** wowsims Forever has no Holy healing sim. The Holy values come from the healing model (`models/beta-30-oct/healing_b2.py`), with 175% critical heals (Holy Power 5/5, main hypothesis).
- **Stat weights.** Each stat changes by a small amount, with the same random seed for all runs. The reference stat is 1.00: healing power for Holy, Strength for Retribution. For Protection, the table gives the change for each point.
- **Talent search.** A hill climb in wowsims (`models/wowsims-b2/search.py`). It gives a good build, not a proven best build.

## Sources

- Damage and tank: talent search and stat weights in wowsims Forever (commit 895cd67f9). Scripts and logs in `models/wowsims-b2` (`search.py`, `finals.py`, `finals.log`).
- Healer: healing model and stat weights (`models/beta-30-oct/holy_builds_b2.py`).
- Level-up: wowsims Forever (commit 895cd67f9), live talents (`models/wowsims-b2/levelup.py`).
- The earlier files (trees of 18 October, calculator version 5) are in the history of the repository.
