# Mana

**Question.** How long does the mana of a Protection or a Retribution Paladin last, in the live version and with the proposals?

The unit is mana each sec (MPS). A positive value means that the mana increases. A negative value means that the mana decreases. For Holy mana, see Healing, part 4.

## Short answer

- **A tank that the boss hits has enough mana, if it does not use Consecration.** The tank receives +6.5 MPS at fresh 60 and +28.9 MPS in Naxxramas. With Blessing of Wisdom, +14.5 and +36.9 MPS.
- **Blocks give the tank its mana.** Shield Specialization returns 4% of maximum mana on a block. With Shieldsworn, Holy Strike also gives the return.
- **Redoubt (C-P1) gives the tank more mana:** +4.9 to +8.3 MPS, because the tank blocks more.
- **Consecration on cooldown empties the mana fast:** in 59 sec at fresh 60, and in about 3 min in Naxxramas (with Blessing of Wisdom). Use it against groups, not all the time.
- **A tank that the boss does not hit loses mana at fresh 60:** −2.7 MPS with Blessing of Wisdom.
- **Retribution loses mana because it changes Seals often.** The wowsims rotation (plan 1 + 3) empties the mana in 3 min 43 sec at fresh 60. In a 5 min fight, plan 3 + 3 costs 2.5% damage, but the mana lasts 8 min 45 sec.
- **Sanctified Judgement (C-R3) does not change the total at 3/3.** It gives more mana only at ranks 1 and 2.

## 1. Why mana is a problem

- **Spirit regeneration stops after each cast.** It gives 15 + Spirit ÷ 5 mana each 2 sec, but it stops for 5 sec after a cast. In combat, it is almost zero.
- **Reverence keeps only 30% of it.** The healer talents of the other classes keep 50%. Reverence 2/2 gives 6.1 MPS at 130 Spirit.
- **Protection receives mana mainly when it is hit,** from Shield Specialization. Sanctified Judgement is the other source.
- **Retribution loses mana because of Seal changes,** not because of low regeneration.

## 2. Protection

**Mana in and out (the boss hits the tank, no Consecration, no Blessing of Wisdom)**

| Source | Fresh 60, live | Fresh 60, Redoubt (C-P1) | Naxxramas, live | Naxxramas, Redoubt (C-P1) |
| --- | --- | --- | --- | --- |
| Shield Specialization, blocks | 17.2 | 22.1 | 29.1 | 37.4 |
| Shield Specialization, Holy Strike | 12.6 | 12.6 | 21.2 | 21.2 |
| Sanctified Judgement 3/3 | 17.0 | 17.0 | 17.0 | 17.0 |
| MP5 from gear | 0.6 | 0.6 | 2.4 | 2.4 |
| Cost: Holy Shield, Holy Strike, Judgement, Seal of Fury | −40.8 | −40.8 | −40.8 | −40.8 |
| **Result** | **+6.5** | **+11.4** | **+28.9** | **+37.2** |

Consecration on cooldown adds 63.6 MPS of cost.

**Result at each gear level (the boss hits the tank, no Consecration)**

| Gear level (maximum mana) | Live | Redoubt (C-P1) | Redoubt (C-P1), flatter gear | Live, Blessing of Wisdom | Redoubt (C-P1), Blessing of Wisdom |
| --- | --- | --- | --- | --- | --- |
| Fresh 60 (2,897) | +6.5 | +11.4 | +11.4 | +14.5 | +19.4 |
| Pre-raid best (3,400) | +12.1 | +17.8 | +17.8 | +20.1 | +25.8 |
| Molten Core (3,900) | +17.8 | +24.4 | +21.1 | +25.8 | +32.4 |
| Blackwing Lair (4,400) | +23.4 | +30.8 | +24.3 | +31.4 | +38.8 |
| Naxxramas (4,900) | +28.9 | +37.2 | +27.5 | +36.9 | +45.2 |

The tank receives more mana with better gear: 4% of a larger mana pool is a larger return. "Flatter gear" is the slower gear of Threat, part 3.

**Other cases: MPS, and the time until the mana is empty**

| Case | Fresh 60, live | Fresh 60, Redoubt (C-P1) | Naxxramas, live | Naxxramas, Redoubt (C-P1) |
| --- | --- | --- | --- | --- |
| Consecration on cooldown | −57.0: 50 sec | −52.2: 55 sec | −34.6: 2 min 21 sec | −26.4: 3 min 5 sec |
| Consecration on cooldown, Blessing of Wisdom | −49.0: 59 sec | −44.2: 1 min 5 sec | −26.6: 3 min 3 sec | −18.4: 4 min 26 sec |
| Not hit | −10.7: 4 min 31 sec | −10.7: 4 min 31 sec | −0.2: more than 1 hour | −0.2: more than 1 hour |
| Not hit, Blessing of Wisdom | −2.7: 17 min 59 sec | −2.7: 17 min 59 sec | +7.8 | +7.8 |
| Not hit, Consecration on cooldown | −74.2: 39 sec | −74.2: 39 sec | −63.8: 1 min 16 sec | −63.8: 1 min 16 sec |

**Value of each mana talent (the boss hits the tank, no Consecration)**

| Case | Fresh 60, live | Fresh 60, Redoubt (C-P1) | Naxxramas, live | Naxxramas, Redoubt (C-P1) |
| --- | --- | --- | --- | --- |
| Tank build 0/38/13 | +6.5 | +11.4 | +28.9 | +37.2 |
| No Shieldsworn | −4.8 | 0.0 | +8.9 | +17.1 |
| No Sanctified Judgement | −10.5 | −5.6 | +11.9 | +20.2 |
| No Benediction | +2.0 | +6.9 | +24.4 | +32.6 |

- **Shieldsworn** gives 11–20 MPS: the Shield Specialization return on Holy Strike.
- **Sanctified Judgement** gives 17.0 MPS, also when the boss does not hit the tank.
- **Benediction** saves 4.5 MPS.

**Sanctified Judgement by rank (C-R3).** 8.5 Judgements each min with Seal of Fury.

| Rank | Live | With C-R3 |
| --- | --- | --- |
| 1/3 | 1.9 | 5.7 |
| 2/3 | 7.6 | 11.3 |
| 3/3 | 17.0 | 17.0 |

In the live version, each rank increases the chance (33/66/100%) and the return (20/40/60%). With C-R3, the return occurs on each Judgement. Tank and Retribution builds take 3/3. Thus, C-R3 does not change the other tables.

**Lay on Hands at full mana (the boss hits the tank, Blessing of Wisdom)**

| Gear level (mana income) | Live: mana lost, time until it is back | Devoted Sacrifice (C-P11) 2/2: mana lost, time until it is back |
| --- | --- | --- |
| Fresh 60 (+14.5 MPS) | 2,897: 3 min 19 sec | 1,449: 1 min 39 sec |
| Naxxramas (+36.9 MPS) | 4,900: 2 min 12 sec | 2,450: 1 min 6 sec |

## 3. Retribution

The wowsims default Retribution build (14/6/31) at fresh 60, with Blessing of Wisdom. The wowsims rotation uses plan 1 + 3: 1 swing with Seal of Righteousness, then 3 swings with Seal of Command.

- **Mana pool:** 3,029. **Cost:** 27.8 MPS. **Income:** 6.2 MPS, plus 8 MPS from Blessing of Wisdom.
- **The mana is empty after** 3 min 43 sec (2 min 20 sec without Blessing of Wisdom).

**Seal plans.** "1 + 3" is 1 swing with Seal of Righteousness, then 3 swings with Seal of Command.

| Plan | DPS (model) | Mana each sec | Time until the mana is empty |
| --- | --- | --- | --- |
| Seal of Command only | 285 (−14%) | 10.2 | — |
| 1 + 3 (wowsims rotation) | 332 | 27.8 | 3 min 43 sec |
| 1 + 2 | 330 (−0.8%) | 35.6 | 2 min 21 sec |
| 1 + 1 | 324 (−2.5%) | 51.2 | 1 min 21 sec |
| 3 + 3 | 324 (−2.5%) | 19.9 | 8 min 45 sec |
| 3 + 1 | 316 (−5.1%) | 27.8 | 3 min 43 sec |

- **The best plan depends on the fight length.** 2 and 3 min fights: plan 1 + 3 at all gear levels. 5 min fights: plan 3 + 3 before raids, plan 1 + 3 from Molten Core.
- **Unsealed Wrath has no Seal cost decrease (W29).** With −20% Seal cost, plan 1 + 3 lasts 5 min 40 sec. The damage in a 5 min fight increases by 2.6% at fresh 60 (see Damage).
- **Reverence** needs 7 Holy points for 2/2. It gives 6.1 MPS at 130 Spirit.

## 4. What the results mean

- **Intellect is a tank stat for the Paladin.** It gives a larger mana pool and a larger Shield Specialization return.
- **Consecration is for groups of enemies.** On cooldown, it empties the mana in 50 sec to 4 min 26 sec.
- **Retribution chooses between damage and mana only in long fights.** Plan 1 + 3 gives the most damage. In a 5 min fight at fresh 60, plan 3 + 3 costs 2.5% damage, but the mana lasts 2.4 times longer.

## 5. Inputs

**Gear.** Maximum mana and MP5 come from the gear levels of Threat, part 2. Fresh 60: 2,897 mana and 3 MP5. Naxxramas: 4,900 mana and 12 MP5. Tank gear has little Spirit: all levels use 130 Spirit.

**Combat (wowsims, default tank gear, 3 min)**

- The boss swings each 2.0 sec. The tank blocks 42.3% of the swings in the live version, 61.6% with Redoubt (C-P1).
- Shield Specialization gives a return at most once each 3 sec from blocks. Thus, the returns each sec are block ÷ (2 × (1 + block)).
- With Shieldsworn, 0.65 of each Holy Strike gives a return. The Holy Strike must land while Holy Shield is active.

**Tank build 0/38/13 (only the mana talents)**

- Shield Specialization 2/2: returns 4% of maximum mana on a block (once each 3 sec), and on each Holy Strike that lands (no limit).
- Shieldsworn: Holy Strike has a 6 sec cooldown.
- Benediction 5/5: −10% cost of instant spells.
- Improved Judgement 2/2 and Swift Judgement: 8.5 Judgements each min.
- Sanctified Judgement 3/3: returns 60% of the base Seal cost on each Judgement. Seal of Fury rank 7 costs 200, thus the return is 120 mana.

**Spell costs at level 60**

| Spell | Cost |
| --- | --- |
| Holy Shield rank 3 | 240 mana, each 10 sec |
| Holy Strike | 20 mana, each 6 sec |
| Judgement | 91 mana (6% of base mana 1,512), each 8 sec |
| Seal of Fury rank 7 | 200 mana, each 30 sec |
| Consecration rank 5 | 565 mana, each 8 sec |

**wowsims check.** The model gives 5% more Shield Specialization returns than wowsims: 15.4 against 14.7 each min (live), 17.9 against 17.0 (Redoubt). The model rules agree with the sim.

## 6. Method and limits

- **Scripts.** `models/beta-30-oct/mana_tables_b2.py` (Protection) and `models/beta-30-oct/retribution_b2.py` (Retribution).
- **Block rate.** It comes from wowsims with the default tank gear. More Defense or block from gear changes it.
- **Holy Shield rank 4** has no cost yet. The model uses 240 mana (rank 3).
- **Base mana** 1,512 is the Classic value. It is not confirmed for Forever.
- **Spirit regeneration** uses the Classic 1.12 formula. Forever did not publish a formula.
- **Blessing of Wisdom** gives 8 MPS. Judgement of Wisdom on the boss is not in the tables.
- The earlier version of this tab (trees of 18 October) is in the history of the repository.
