# Level-up: best beta talent order from level 10 to 60

This file gives the fastest talent order to level a Paladin in the beta trees, with 1 point for each level. The proposed trees are not in this check.

## Summary

Go deep in Retribution. Take Seal of Command at level 20 and Pursuit of Justice at levels 22–23. At 35 Retribution points (level 44), go to Holy for Divine Strength and Improved Seals. The level 60 build is 12/3/36: `52003002-3-5122533120133032`.

## 1. Point order

| Level | Talent | Rank |
| --- | --- | --- |
| 10–14 | Deflection | 1–5/5 |
| 15 | Improved Judgement | 1/2 |
| 16–18 | Conviction | 1–3/5 |
| 19 | Holy Conduit | 1/2 |
| 20 | Seal of Command | 1/1 |
| 21 | Holy Conduit | 2/2 |
| 22–23 | Pursuit of Justice | 1–2/2 |
| 24–25 | Sanctified Judgement | 1–2/3 |
| 26 | Sacred Arbiter | 1/1 |
| 27 | Sanctified Judgement | 3/3 |
| 28–29 | Conviction | 4–5/5 |
| 30–32 | Two-Handed Weapon Specialization | 1–3/3 |
| 33–34 | Vengeance | 1–2/3 |
| 35–37 | Champion of the Light | 1–3/3 |
| 38 | Vengeance | 3/3 |
| 39–41 | Vindication | 1–3/3 |
| 42 | Improved Judgement | 2/2 |
| 43–44 | Instrument of Law | 1–2/2 (Hammer of Wrath comes at level 44) |
| 45–49 | Divine Strength | 1–5/5 |
| 50–52 | Improved Seals | 1–3/3 |
| 53–55 | Toughness | 1–3/5 |
| 56–57 | Divine Intellect | 1–2/5 |
| 58 | Reverence | 1/3 |
| 59 | Benediction | 1/5 |
| 60 | Reverence | 2/3 (or Twist of Light, see part 3) |

## 2. Codes for each level

Set the level select of the calculator to the level, or read "Required level". Paste the code into the code box and click "Load code".

| Level | Points | Code |
| --- | --- | --- |
| 20 | 0/0/11 | `--50113001` |
| 30 | 0/0/21 | `--501250312011` |
| 40 | 0/0/31 | `--501252312013303` |
| 50 | 6/0/35 | `50001--5022533120133032` |
| 60 | 12/3/36 | `52003002-3-5122533120133032` |
| 60, Twist of Light | 11/3/37 | `52003001-3-51225331201330321` |

## 3. Why this order

- **Levels 10–19.** No talent in rows 1–2 changes the kill speed much. Deflection decreases the damage that you take, and thus the time that you eat after a fight. Divine Strength 5/5 gives about the same result, but it puts the points in Holy.
- **Level 20.** Seal of Command is the largest step of the path: 18% more damage and 12% less time for each kill. Holy Conduit 1/2 at level 19 opens row 3 one level early. It also makes Consecration and Exorcism cheaper.
- **Levels 22–23.** Pursuit of Justice gives 15% more speed, also on a mount. The model gives 10 sec of travel for each kill. Thus, 2 points save about 1.3 sec for each kill, more than most damage talents.
- **Levels 24–27.** Sanctified Judgement 3/3 returns 60% of the Seal cost on each Judgement. It also opens Vengeance in row 5. Ranks 1–2 give little alone (7% and 26% return on average).
- **Levels 30–44.** Two-Handed Weapon Specialization, Vengeance and Champion of the Light give the most damage. Instrument of Law makes Hammer of Wrath faster from level 44.
- **Levels 45–60.** At 35 Retribution points, Divine Strength 5/5 and Improved Seals 3/3 give more than the other Retribution talents.

**Twist of Light at level 60.** In the beta, the Echo lasts for one swing. Thus, you must change Seals before almost each swing, and the mana cost increases.

| Build at level 60 | Time for each kill, health limits the rest | Time for each kill, mana limits the rest |
| --- | --- | --- |
| This order, Reverence 2/3 (`52003002-3-5122533120133032`) | 32.6 sec | **28.1 sec** |
| This order, Twist of Light (`52003001-3-51225331201330321`) | **31.6 sec** | 29.4 sec |
| Raid Twist of Light preset (`55003003--05225331101330321`) | 33.4 sec | 29.0 sec |
| Best fresh level 60 boss build (`550031031101002--052251310013303`) | 37.6 sec | 30.8 sec |

Take Twist of Light only if you change Seals before each swing and the rest is for health, not for mana. Otherwise, Reverence 2/3 is 4.5% faster and you use one Seal.

## 4. Method

- **Sim.** wowsims Forever commit 69e0e5b, beta talents (no proposal flags). One level 60 enemy with 3,000 armor that attacks you (2.0 sec swing). Fights of 15 sec ±25%, from 20 yards. No buffs, no consumables. Retribution preset gear. 80% humanoid and 20% undead enemies (Exorcism).
- **Rotations.** The default Retribution APL with no assigned Judgement, and the same APL with no Consecration. The model keeps the faster of the two for each build. Below level 20, the APL has no Consecration and no Exorcism. Below level 44, it has no Hammer of Wrath.
- **Time for each kill.** Enemy health 5,000. Rest = the longer of mana / 120 per sec (water) and damage taken / 80 per sec (food). Travel = 10 sec for each kill, divided by 1.15 with Pursuit of Justice 2/2.
- **Search.** First, a hill climb found the best 51-point build. Then a beam search (8 paths) found the order. Its score is the sum over levels 10–60 of level × time for each kill. The weight gives more value to the slow, high levels.
- **Two cases.** With the full enemy damage, health limits the rest. With half the enemy damage, mana limits the rest. The order above comes from the half damage case. In the full damage case, it is 0.5% slower than the best order of that case. In the half damage case, it is 3.9% faster than that order.

## 5. Limits

- The sim works only at level 60. Thus, each level uses level 60 gear, spell ranks and enemies. The model removes only the spells that a lower level does not have yet. The order of talents with almost the same value can change at low levels.
- Close choices: Deflection or Divine Strength at levels 10–14, and Toughness, Divine Intellect, Reverence or Benediction at levels 53–59. Each choice changes the time for each kill by less than 1%.
- The model does not include pulls of 2 or more enemies, Seal of Wisdom, Blessing of Wisdom or heals on yourself.
- A Protection path (Holy Shield, Seal of Fury) is not in the model, because the Retribution APL does not use those spells.
