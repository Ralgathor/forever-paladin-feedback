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
| Protection | Threat each sec | 1,208 | 1,154 | +4.7% |
| Protection | Damage taken each sec | 283 | 308 | −8% |
| Protection | TMI (lower is better) | 41.5 | 49.3 | −16% |
| Retribution | DPS, raid | 837 | 837 | 0% |
| Retribution | DPS, fresh 60 | 308 | 309 | −0.5% |
| Shockadin | DPS, raid | 816 | 816 | 0% |
| Shockadin | DPS, fresh 60 | 289 | 283 | +2.1% |

- **Holy.** Light's Vigil (C-H7) gives the raid healing. Oath of Light 30% (C-H8) gives the one-tank healing. Reverence 50% (C-H1) gives +5–9% healing, more in long fights. HB2 takes Devoted Sacrifice (C-P11) with the free points.
- **Protection.** Redoubt (C-P1) removes almost all crushing blows and adds threat with more Holy Shield blocks. Since commit 3633d376a (11 November), wowsims applies the block proc of Argent Defender only on a proc. Thus, the live builds have less block than on 9 November, and the gain is larger. Righteous Fury (C25) multiplies all threat by 1.42.
- **Retribution.** Reverence 50% (C-H1) gives −0.5% at fresh 60 with the item pool set of 12 November, evening, on commit 8c7b5a5f5 (all three judgements ranged: −0.2%; 129fcd89e: +0.1%; set of 12 November, 52471a100: +1.0%; set of 11 November: −0.9%). In a raid, the proposed and live trees give the same damage. The 837 DPS use 3 min fights. Analysis, Damage gives 831 DPS with the 2 min wowsims test run.

  The ranged Judgement of Righteousness and Judgement of Fury (hotfixes of 11 November) and the Two-Handed Weapon Specialization fix give RB1 −0.7 to −0.9%. Judgement of Command is melee again (late hotfix of 13 November). With all three judgements ranged, the loss was −1.5%. The Hand of Justice change of commit 129fcd89e gives RB1 −2%. The new Windfury Totem rule of 9 November gives RB1 −11% in a raid.
- **Shockadin.** SB1 is 97% of RB1 in a raid, with the item pool Shockadin set (8 November: 89%). Reverence 50% (C-H1) gives +2.1% at fresh 60 with the set of 11 November on commit 8c7b5a5f5 (129fcd89e: +0.3%; set of 9 November: +8.0%). Light's Vigil (C-H7) gives a build with 31 Holy points +9.4%, but this build stays 10% below SB1.

## Common rules

- **Codes.** All build codes load with 51 points. The level-up codes show the points at a lower level. A code that starts with `v6p` opens the proposed trees. A code that starts with `b2` opens the live trees.
- **Sim.** wowsims Forever, master of 13 November 2026 (commit 8c7b5a5f5, hotfixes of 13 November, client 1.60.1.70938). Judgement of Righteousness and Judgement of Fury are ranged attacks, as in the hotfixes of 11 November. Judgement of Command is a melee attack again, as in the late hotfix of 13 November (`models/wowsims-b2/patches/judgement-ranged.patch`). The proposals are flags (`models/wowsims-b2`). 3 min, one level 63 boss, 3,000 iterations.
- **Gear.** The item pool sets, the same item pool as Analysis, Damage and Threat (no raid, PvP, Zul'Gurub, Ahn'Qiraj or Revered and Exalted reputation items, item level 63 or lower): [Protection Paladin](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-pool-protection-paladin.html), [Retribution](https://ralgathor.github.io/forever-paladin-feedback/sets/build-retribution.html) and [Shockadin](https://ralgathor.github.io/forever-paladin-feedback/sets/build-shockadin.html). The talent search ran with the wowsims default sets. Level-up uses leveling gear (level-up.md).
- **Holy.** wowsims Forever has no Holy healing sim. The Holy values come from the healing model (`models/beta-30-oct/healing_b2.py`), with 175% critical heals (Holy Power 5/5, main hypothesis).
- **Stat weights.** Each stat changes by a small amount, with the same random seed for all runs. The reference stat is 1.00: healing power for Holy, Strength for Retribution, spell damage for the Shockadin. For Protection, the table gives the change for each point.
- **Talent search.** A hill climb in wowsims (`models/wowsims-b2/search.py`). It gives a good build, not a proven best build.

## Sources

- Damage and tank: talent search in wowsims Forever (commit 895cd67f9, default sets), builds and stat weights again on commit 8c7b5a5f5 with the item pool sets. Scripts and logs in `models/wowsims-b2` (`search.py`, `finals.py`, `logs/finals.log`).
- Shockadin: talent search in wowsims Forever (commit 6ee3c30f35, wowsims Holy Shock set). The builds and stat weights ran again on commit 8c7b5a5f5, with the item pool set and the Light's Vigil flag CH7 (`search.py`, `finals.py shock`, `logs/finals_shock.log`).
- Healer: healing model and stat weights (`models/beta-30-oct/holy_builds_b2.py`).
- Level-up: wowsims Forever (commit 895cd67f9), live talents (`models/wowsims-b2/levelup.py`).
- The earlier files (trees of 18 October, calculator version 5) are in the history of the repository.
