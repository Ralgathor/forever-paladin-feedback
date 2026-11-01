# Holy: best healing build, talent values and stat weights

This file gives the best healing build on the trees of 30 October 2026, the value of each healing talent and the stat weights. All values come from the healing model of the beta of 30 October (`models/beta-30-oct/healing_b2.py`). The script is `models/beta-30-oct/holy_builds_b2.py`.

## Summary

| Trees | Build | Points | Code | Raid, 3 / 5 / 10 min | One tank, 3 / 5 / 10 min |
| --- | --- | --- | --- | --- | --- |
| Proposed | HB2 | 31/12/8 | `v6p50320115202101251-50122000000000002-0503` | 596 / 506 / 427 | 695 / 601 / 507 |
| Beta | HB1 | 38/5/8 | `b250325115202121251-5-0503` | 596 / 506 / 427 | 695 / 601 / 507 |

- Healing each sec after overhealing, 715 healing power, 200% critical heals (Holy Power 5/5, main hypothesis).
- In both trees, all healing talents fit in 51 points. Thus, the best healing build takes all of them. The other points give only utility.
- The proposed trees have no Holy talent change. Thus, HB1 and HB2 heal the same. HB2 takes Devoted Sacrifice (C-P11) and Protection saves in place of Improved Seals and Consecrated Ground.
- **Stat weights.** MP5 is the best stat for each point in all fight lengths (2.3–3.3 healing power). Intellect is about 1 healing power, crit rating 1.3–1.5 (part 3).

## 1. Builds

### Proposed: HB2

`v6p50320115202101251-50122000000000002-0503` (31/12/8). This is HB2 of Analysis, Builds.

- Holy: Spiritual Focus 5, Healing Light 3, Reverence 2, Purifying Power 1, Divine Favor, Illumination 5, Holy Conduit 2, Infusion of Light 2, Oath of Light, Holy Shock, Boundless Light 2, Holy Power 5, Light's Vigil.
- Protection: Divine Intellect 5, Precision 1, Guardian's Favor 2, Sacred Duty 2, Devoted Sacrifice 2.
- Retribution: Benediction 5, Conviction 3.

### Beta: HB1

`b250325115202121251-5-0503` (38/5/8). This is HB1 of Analysis, Builds. It takes Improved Seals 5 and Consecrated Ground 2 in place of the Protection saves.

### Points that the rows force

- Light's Vigil (row 7) needs 30 Holy points in rows 1–6. Holy Conduit 2/2 fills rows 1–5. It gives only cheaper Consecration, Holy Wrath, Exorcism and Hammer of Wrath.
- The 3 Retribution points after Benediction go to Conviction 3/3: +6% critical chance, also more Illumination mana.

## 2. Value of each talent

The healing without the talent, 5 min fight, against HB1/HB2.

| Talent | Raid | One tank |
| --- | --- | --- |
| Reverence 2/2 and Illumination 5/5 (Illumination needs Reverence) | −20.8% | −20.8% |
| Illumination 5/5 | −11.9% | −11.9% |
| Holy Power 5/5 (200% critical heals) | −10.8% | −10.8% |
| Healing Light 3/3 | −10.7% | −10.7% |
| Conviction 3/3 | −6.9% | −6.9% |
| Divine Intellect 5/5 | −2.6% | −2.6% |
| Divine Favor | −2.3% | −2.4% |
| Benediction 5/5 | 0% | 0% |
| Boundless Light 2/2 | 0% | 0% |
| Light's Vigil | 0% | 0% |

- **Mana talents give the most.** Reverence and Illumination together give 21% of the healing. Holy Power gives 11% (15% at 225%).
- **Holy Shock, Boundless Light and Light's Vigil give 0%.** The best spell plan does not cast them: they heal the least for each mana point. Holy Shock has value when you move.
- **Benediction gives 0%** because the plan casts no instant spell. It has value with Holy Shock and Seals.

## 3. Stat weights

Each stat + a small amount (40 healing power, Intellect or Spirit, 10 MP5, 14 crit rating). Healing each sec after overhealing, divided by the gain of 1 healing power. The model has no haste.

| Stat | Raid, 3 min | Raid, 5 min | Raid, 10 min | One tank, 5 min |
| --- | --- | --- | --- | --- |
| Healing each sec for 1 healing power | 0.349 | 0.340 | 0.287 | 0.340 |
| Healing power | 1.00 | 1.00 | 1.00 | 1.00 |
| Intellect | 1.33 | 0.90 | 0.71 | 0.98 |
| Spirit | 0.34 | 0.38 | 0.61 | 0.42 |
| MP5 | 2.30 | 2.47 | 3.32 | 2.66 |
| Crit rating | 1.54 | 1.26 | 1.26 | 1.49 |

- **MP5 has the most value in all cases.** Its value increases with the fight length.
- **Intellect** gives mana and critical chance. In a short fight, the critical chance has more value.
- **Spirit** has little value: Reverence keeps only 30% of the Spirit regeneration during casts.
- **Crit rating** gives larger heals (200%) and Illumination mana.

## 4. Gear

This folder has no new gear search for Holy. wowsims Forever has no Holy healing sim (the Holy page is a gear planner). Use the stat weights of part 3 with the default Holy set of wowsims Forever.

## 5. Limits

- The values come from a model, not from combat logs. The model uses fixed overhealing for each spell.
- The model uses 200% critical heals (Holy Power 5/5, decision of 1 November). The beta test of Holy Power can change these values (see Open items).
- The earlier values (trees of 18 October) are in the history of the repository.
