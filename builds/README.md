# Best builds, gear and stat weights

This folder gives the best build, the pre-raid gear and the stat weights of each spec, for the beta trees and for the proposed trees. The values come from wowsims Forever with the proposals patch (`models/wowsims/proposals.patch`). This folder is a reference. It does not change a proposal.

| Spec | File | Best proposed build | Best beta build |
| --- | --- | --- | --- |
| Holy (healer) | [holy.md](holy.md) | P1: `v6p53201132251010512-30200000000000502-0005` | B1: `05320113225101051-500250002-05` |
| Protection (tank) | [protection.md](protection.md) | PT3: `v6p0003-53030321301551-5215200001` | BT4b: `50003-5230513021301351-50201` |
| Retribution (damage), raid | [retribution.md](retribution.md) | RB6 5/8/38: `v6p2003-030000000000005-021533120133032153` | Holy Shock 23/0/28: `551030032001012--052152310012303` |
| Retribution (damage), fresh 60 | [retribution.md](retribution.md) | Ret 9/8/34: `v6p3003003-030000000000005-02253310013303215` | 22/0/29: `550031031101002--052251310013303` |
| Level-up (beta only) | [level-up.md](level-up.md) | — | 12/3/36: `52003002-3-5122533120133032` |

## Main results

| Spec | Measure | Proposed | Beta | Proposed against beta |
| --- | --- | --- | --- | --- |
| Holy | Healing per sec, pre-raid gear, 3 min | 625 | 519 | +20% |
| Holy | Healing per sec, raid gear, 3 min | 853 | 742 | +15% |
| Protection | Threat per sec (TPS), raid | 1,190 | 994 | +20% |
| Protection | TMI, raid (lower is better) | 21.8 | 28.8 | −24% |
| Retribution | DPS, raid, best build | 881 | 873 | +1% |
| Retribution | DPS, fresh 60, best build | 353 | 311 | +14% |

## Common rules

- **Codes.** All proposed codes load in calculator version 6 with 51 points. A code with only digits opens the beta trees.
- **Gear.** Pre-raid gear for all specs. Holy also has a raid set (Naxxramas). The gear search changes one slot at a time and keeps the best item in the sim. Thus, it gives a good set, not a proven best set.
- **Item list.** On 28 October 2026, wowsims rebuilt its item list from the live Forever game cache. Some items left the list (for example Hand of Edward the Odd and Arcanoweave Cloak). All sets of this folder use only items of the new list.
- **Pre-raid rules.** No raid drops and no items made from raid materials (for example Signet Ring of the Bronze Dragonflight, Fist of Cenarius and Dragonslayer's Signet).
- **Shields.** Some shield block values in wowsims are not the Wowhead Forever values. The tank sims use the Wowhead values (for example 66 for The Immovable Object).
- **wowsims links.** Each link loads the gear and the talents in wowsims. The live wowsims has no proposals. Thus, a proposed build loads in the beta tree order, and the site gives beta values for it. The values of this folder come from the sim with the proposals.
- **Stat weights.** Each stat changes by a small amount, with the same random seed for all runs. The reference stat is 1.00: healing power for Holy, Strength (and spell damage) for Protection, Strength for Retribution.

## Sources

- Tank: build search and gear path in wowsims Forever (commit a10f483, 30 October 2026). Holy Shield (C-P9) at 100% of block value.
- Healer: healing model search (`models/healing`), with a wowsims check. Gear search and stat weights in wowsims Forever (commit 47b3c01). On commit a10f483, the Holy sets give the same healing per sec.
- Damage: build search and gear path in wowsims Forever (commit a10f483).
- Level-up: wowsims Forever (commit 69e0e5b), beta talents.
