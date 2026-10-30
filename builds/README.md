# Best builds, gear and stat weights

This folder gives the best build, the pre-raid gear and the stat weights of each spec, for the beta trees and for the proposed trees. The values come from wowsims Forever with the proposals patch (`models/wowsims/proposals.patch`). This folder is a reference. It does not change a proposal.

| Spec | File | Best proposed build | Best beta build |
| --- | --- | --- | --- |
| Holy (healer) | [holy.md](holy.md) | P1: `v6p53201132251010512-30200000000000502-0005` | B1: `05320113225101051-500250002-05` |
| Protection (tank) | [protection.md](protection.md) | PT3: `v6p0003-53030321301551-5215200001` | BT4b: `50003-5230513021301351-50201` |
| Retribution (damage), raid | [retribution.md](retribution.md) | Holy Shock 21/0/30: `v5p50032032201010002--022553100133032`, or Ret 11/8/32: `v5p5003003-030000000000005-0215531201330321` (equal within 1%) | Holy Shock 23/0/28: `551030032001012--052152310012303` |
| Retribution (damage), fresh 60 | [retribution.md](retribution.md) | Ret 11/8/32: `v5p5003003-030000000000005-0225531201330311` | 22/0/29: `550031031101002--052251310013303` |
| Level-up (beta only) | [level-up.md](level-up.md) | — | 12/3/36: `52003002-3-5122533120133032` |

## Main results

| Spec | Measure | Proposed | Beta | Proposed against beta |
| --- | --- | --- | --- | --- |
| Holy | Healing per sec, pre-raid gear, 3 min | 625 | 519 | +20% |
| Holy | Healing per sec, raid gear, 3 min | 853 | 742 | +15% |
| Protection | Threat per sec (TPS), raid | 1,240 | 884 | +40% |
| Protection | TMI, raid (lower is better) | 22.5 | 26.0 | −13% |
| Retribution | DPS, raid, best build | 860 | 879 | −2% |
| Retribution | DPS, fresh 60, best build | 341 | 315 | +8% |

## Common rules

- **Codes.** The Holy and Protection codes load in calculator version 6 with 51 points. The proposed Retribution codes are version 5 codes (`v5p`): they open on the version 5 page. In version 6, Vengeance requires Burning Zeal 2/2. [retribution.md](retribution.md) gives the version 6 builds. A code with only digits opens the beta trees.
- **Gear.** Pre-raid gear for all specs. Holy also has a raid set (Naxxramas). The gear search changes one slot at a time and keeps the best item in the sim. Thus, it gives a good set, not a proven best set.
- **Item list.** On 28 October 2026, wowsims rebuilt its item list from the live Forever game cache. Some items left the list (for example Hand of Edward the Odd and Arcanoweave Cloak). All sets of this folder use only items of the new list.
- **wowsims links.** Each link loads the gear and the talents in wowsims. The live wowsims has no proposals. Thus, a proposed build loads in the beta tree order, and the site gives beta values for it. The values of this folder come from the sim with the proposals.
- **Stat weights.** Each stat changes by a small amount, with the same random seed for all runs. The reference stat is 1.00: healing power for Holy, Strength (and spell damage) for Protection, Strength for Retribution.

## Sources

- Tank: build search and gear path in wowsims Forever (commit 69e0e5b, item list of commit 47b3c01).
- Healer: healing model search (`models/healing`), with a wowsims check. Gear search and stat weights in wowsims Forever (commit 47b3c01).
- Damage: build search and gear path in wowsims Forever (commit 47b3c01).
- Level-up: wowsims Forever (commit 69e0e5b), beta talents.
