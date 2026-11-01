# Level-up: talent order from level 10 to 60

This file gives a fast talent order to level a Paladin in the beta trees of 30 October 2026, with 1 point for each level. The order ends at the raid build RB1 (Analysis, Builds). The proposed trees have the same Retribution talents, thus the order is also valid for them.

## Summary

Go deep in Retribution first. Take Seal of Command at level 20, Pursuit of Justice at levels 21–22 and Unsealed Wrath at level 40. Then take the Holy talents (Divine Strength, Improved Seals, Holy Conduit) and Divine Intellect. The level 60 build is RB1, 14/6/31: `050250002-501-05233011201301351`.

## 1. Point order

| Level | Talent | Rank |
| --- | --- | --- |
| 10–14 | Benediction | 1–5/5 |
| 15–17 | Conviction | 1–3/3 |
| 18–19 | Improved Judgement | 1–2/2 |
| 20 | Seal of Command | 1/1 |
| 21–22 | Pursuit of Justice | 1–2/2 |
| 23–24 | Sanctified Judgement | 1–2/3 |
| 25 | Sacred Arbiter | 1/1 |
| 26–28 | Two-Handed Weapon Specialization | 1–3/3 |
| 29 | Sanctified Judgement | 3/3 |
| 30–32 | Vengeance | 1–3/3 |
| 33 | Unyielding Faith | 1/2 |
| 34 | Repentance | 1/1 |
| 35–39 | Champion of the Light | 1–5/5 |
| 40 | Unsealed Wrath | 1/1 |
| 41–45 | Divine Strength | 1–5/5 |
| 46–50 | Improved Seals | 1–5/5 |
| 51–52 | Holy Conduit | 1–2/2 |
| 53–57 | Divine Intellect | 1–5/5 |
| 58–59 | Reverence | 1–2/2 |
| 60 | Precision | 1/3 |

## 2. Codes for each level

Paste the code into the code box of the calculator and click "Load code". A code that starts with "b2" opens the beta trees.

| Level | Points | Code |
| --- | --- | --- |
| 20 | 0/0/11 | `b2--05230001` |
| 30 | 0/0/21 | `b2--052330012013001` |
| 40 | 0/0/31 | `b2--05233011201301351` |
| 50 | 10/0/31 | `b205005--05233011201301351` |
| 60 | 14/6/31 | `b2050250002-501-05233011201301351` |

## 3. Time for each kill

| Level | Points | Time for each kill (average of the two cases) |
| --- | --- | --- |
| 9 | No talents | 56.2 sec |
| 20 | Seal of Command | 52.0 sec |
| 30 | Vengeance 1 | 47.0 sec |
| 39 | Champion of the Light 5/5 | 41.2 sec |
| 40 | Unsealed Wrath | 39.8 sec |
| 50 | Improved Seals 5/5 | 38.3 sec |
| 60 | RB1 | 37.1 sec |

- **Levels 10–19.** Benediction makes each Seal cheaper, thus the rest for mana is shorter. Conviction and Improved Judgement give the first damage.
- **Level 20.** Seal of Command gives the largest step before level 35.
- **Levels 21–22.** Pursuit of Justice gives 15% more speed. The model gives 10 sec of travel for each kill. Thus, 2 points save about 1.3 sec for each kill.
- **Levels 35–40.** Champion of the Light 5/5 makes Hammer of Wrath instant. Unsealed Wrath gives both Seals to each swing. These two steps save 4.4 sec for each kill.
- **Levels 41–60.** The Holy and Protection points give less: 2.7 sec for each kill in total. Divine Intellect, Reverence and Precision give almost nothing alone.

## 4. Method

- **Sim.** wowsims Forever, master of 1 November 2026 (commit 895cd67f9), beta talents, no proposal flags. Test TestFeedbackLevelUp (models/wowsims-b2). One level 60 humanoid with 3,000 armor that attacks you (2.0 sec swing). Fights of 15 sec ±25%. No buffs, no consumables. Default Retribution gear and rotation. 1,000 iterations.
- **Time for each kill.** Enemy health 5,000. Rest = the longer of mana / 120 per sec (water) and damage taken / 80 per sec (food). Travel = 10 sec for each kill, divided by 1.15 with Pursuit of Justice 2/2.
- **Two cases.** The enemy hits for 400 (health limits the rest) or for 200 (mana limits the rest more often). The score is the average of the two cases.
- **Search.** A beam search (30 paths) for the order of the 51 points of RB1. Its score is the sum over levels 10–60 of level × time for each kill. The weight gives more value to the slow, high levels. The script is models/wowsims-b2/levelup.py.
- **Other level 60 builds.** A free greedy search from 0 points ends in Holy or in Eye for an Eye. These builds are slower on average than RB1: 38.6 sec (Eye for an Eye build) and 44.2 sec (Holy build), against 37.1 sec.

## 5. Limits

- The sim works only at level 60. Thus, each level uses level 60 gear, spell ranks and enemies. The order of talents with almost the same value can change at low levels.
- The model does not remove the spells that a lower level does not have yet. Hammer of Wrath (level 44) and Consecration (level 20) are in the sim at all levels.
- The model does not include pulls of 2 or more enemies, Seal of Wisdom, Blessing of Wisdom or heals on yourself.
- A Protection path (Holy Shield, Seal of Fury) is not in the model, because the Retribution rotation does not use those spells.
