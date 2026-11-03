# Holy: best healing build, talent values and stat weights

This file gives the best healing build on the live trees, the value of each healing talent and the stat weights. All values come from the healing model of the live trees (`models/beta-30-oct/healing_b2.py`). The script is `models/beta-30-oct/holy_builds_b2.py`.

## Summary

| Trees | Build | Points | Code | Raid, 3 / 5 / 10 min | One tank, 3 / 5 / 10 min |
| --- | --- | --- | --- | --- | --- |
| Proposed | HB2 | 31/12/8 | [`v6p50320115202101251-50122000000000002-0503`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p50320115202101251-50122000000000002-0503) | 814 / 728 / 647 | 755 / 658 / 571 |
| Live | HB1 | 38/5/8 | [`b250325115202121251-5-0503`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b250325115202121251-5-0503) | 563 / 479 / 404 | 658 / 568 / 480 |

- Healing each sec after overhealing, 715 healing power, 175% critical heals (Holy Power 5/5, main hypothesis since 3 November).
- In both trees, all healing talents fit in 51 points. Thus, the best healing build takes all of them. The other points give only utility.
- HB2 heals 45–60% more than HB1 in raids, with Light's Vigil (C-H7) and Reverence 50% (C-H1). On one tank, it heals 15–19% more, with Oath of Light 30% (C-H8) and Reverence 50%. The gain increases with the fight length. HB2 also takes Devoted Sacrifice (C-P11) and Protection saves in place of Improved Seals and Consecrated Ground.
- **Stat weights.** MP5 is the best stat for each point in all fight lengths (2.3–3.3 healing power). Intellect is 0.7–1.3 healing power, crit rating 1.1–1.4 (part 3).

## 1. Builds

### Proposed: HB2

[`v6p50320115202101251-50122000000000002-0503`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p50320115202101251-50122000000000002-0503) (31/12/8). This is HB2 of Analysis, Builds.

- Holy: Spiritual Focus 5, Healing Light 3, Reverence 2, Purifying Power 1, Divine Favor, Illumination 5, Infusion of Light 2, Oath of Light, Holy Shock, Boundless Light 2, Holy Conduit 2, Holy Power 5, Light's Vigil.
- Protection: Divine Intellect 5, Precision 1, Guardian's Favor 2, Sacred Duty 2, Devoted Sacrifice 2.
- Retribution: Benediction 5, Conviction 3.

### Live: HB1

[`b250325115202121251-5-0503`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b250325115202121251-5-0503) (38/5/8). This is HB1 of Analysis, Builds. It takes Improved Seals 5 and Consecrated Ground 2 in place of the Protection saves.

### Points that the rows force

- Light's Vigil (row 7) needs 30 Holy points in rows 1–6. In both trees, Holy Conduit 2/2 fills rows 1–5. It gives only cheaper Consecration, Holy Wrath, Exorcism and Hammer of Wrath.
- The 3 Retribution points after Benediction go to Conviction 3/3: +6% critical chance, also more Illumination mana.

## 2. Value of each talent

The healing without the talent, 5 min fight, against HB1. Reverence 50% and Oath of Light 30%: against HB2.

| Talent | Raid | One tank |
| --- | --- | --- |
| Reverence 50% in place of 30% (C-H1, HB2 only) | −6.1% | −5.6% |
| Oath of Light 30% (C-H8, HB2 only) | 0% | −23.1% |
| Oath of Light (live: +400 / +115 / +229) | 0% | −15.8% |
| Reverence 2/2 and Illumination 5/5 (Illumination needs Reverence) | −21.0% | −21.0% |
| Illumination 5/5 | −12.0% | −12.0% |
| Healing Light 3/3 | −10.7% | −10.7% |
| Conviction 3/3 | −6.0% | −6.0% |
| Holy Power 5/5 (175% critical heals) | −5.7% | −5.7% |
| Divine Intellect 5/5 | −2.6% | −2.6% |
| Divine Favor | −1.9% | −2.0% |
| Benediction 5/5 | 0% | 0% |
| Boundless Light 2/2 | 0% | 0% |
| Light's Vigil | 0% | 0% |

- **Oath of Light gives the most on one tank,** and nothing in raids. It helps only one ally (model: `models/beta-30-oct/oath_light_ch8.py`).
- **Mana talents give the most.** Reverence and Illumination together give 21% of the healing. Holy Power gives 6% (15% at 225%).
- **Holy Shock, Boundless Light and Light's Vigil give 0%.** The best spell plan does not cast them: they heal the least for each mana point. Holy Shock has value when you move. In the proposed trees, Light's Vigil (C-H7) gives HB1 +44% in raids at 5 min (479 → 692).
- **Benediction gives 0%** because the plan casts no instant spell. It has value with Holy Shock and Seals.

## 3. Stat weights

Each stat + a small amount (40 healing power, Intellect or Spirit, 10 MP5, 14 crit rating). Healing each sec after overhealing, divided by the gain of 1 healing power. The model has no haste.

| Stat | Raid, 3 min | Raid, 5 min | Raid, 10 min | One tank, 5 min |
| --- | --- | --- | --- | --- |
| Healing each sec for 1 healing power | 0.331 | 0.322 | 0.272 | 0.322 |
| Healing power | 1.00 | 1.00 | 1.00 | 1.00 |
| Intellect | 1.28 | 0.86 | 0.67 | 0.94 |
| Spirit | 0.34 | 0.38 | 0.61 | 0.42 |
| MP5 | 2.28 | 2.45 | 3.33 | 2.66 |
| Crit rating | 1.35 | 1.09 | 1.09 | 1.29 |

- **MP5 has the most value in all cases.** Its value increases with the fight length.
- **Intellect** gives mana and critical chance. In a short fight, the critical chance has more value.
- **Spirit** has little value: Reverence keeps only 30% of the Spirit regeneration during casts. With Reverence 50% (HB2), Spirit has more value.
- **Crit rating** gives larger heals (175%) and Illumination mana.

## 4. Gear

This folder has no new gear search for Holy. wowsims Forever has no Holy healing sim (the Holy page is a gear planner). Use the stat weights of part 3 with the default Holy set of wowsims Forever.

## 5. Limits

- The values come from a model, not from combat logs. The model uses fixed overhealing for each spell.
- The model uses 175% critical heals (Holy Power 5/5, decision of 3 November). The live test of Holy Power can change these values (see Open items).
- The earlier values (trees of 18 October) are in the history of the repository.
