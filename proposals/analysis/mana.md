# Mana

This section gives the mana of the Paladin on the beta trees of 30 October 2026, in the beta and with the proposals. The unit is mana per second (MPS). A positive value means that the mana increases. A negative value means that the mana decreases.

The script models/beta-30-oct/mana_tables_b2.py gives the Protection values. It uses the spell costs and the gear tiers of models/mana/mana_model.py. The script models/beta-30-oct/retribution_b2.py gives the Retribution values. Analysis, Healing, part 2, gives the Holy values.

## Summary

- **A tank that is hit has mana without Consecration.** The tank build 0/38/13 receives +6.5 MPS at fresh level 60 and +28.9 MPS in Naxxramas. With Blessing of Wisdom, it receives +14.5 and +36.9 MPS.
- **Shield Specialization is the main mana source.** It gives 4% of maximum mana on a block, once each 3 sec. With Shieldsworn, each Holy Strike that lands with Holy Shield active also gives 4%. Sanctified Judgement gives 17.0 MPS.
- **Redoubt (C-P1) gives the tank +4.9 to +8.3 MPS.** More blocks give more Shield Specialization returns.
- **Consecration on cooldown empties the mana quickly.** With Blessing of Wisdom, the beta tank has mana for 59 sec at fresh level 60. In Naxxramas, it has mana for 3 min 3 sec. Use Consecration against groups of enemies, not all the time.
- **A tank that is not hit loses mana at fresh level 60.** With Blessing of Wisdom, it loses 2.7 MPS. In Naxxramas, it receives +7.8 MPS.
- **Holy has the least mana of the four healers.** Reverence keeps only 30% of the Spirit regeneration during casts (see Analysis, Healing, part 2).
- **Retribution loses mana because of Seal changes.** The wowsims rotation changes the Seal after each swing: 51.2 MPS. With Blessing of Wisdom, the mana is empty after 1 min 21 sec. A plan with fewer Seal changes costs 1.8–2.6% damage, and the mana lasts 1.7–2.8 times longer.
- **Sanctified Judgement (C-R3) does not change the total return.** At 3/3, it gives 17.0 MPS in the beta and with the proposal. It gives more at ranks 1 and 2.

## 1. Problems in the beta

- **Spirit regeneration stops when you cast.** It gives 15 + Spirit ÷ 5 mana each 2 sec. It stops for 5 sec after each cast. In combat, it is almost zero.
- **Reverence keeps only 30%.** Reverence (Holy row 2, 2 ranks) keeps 15/30% of the regeneration during casts. Meditation (Priest), Reflection (Druid) and Mindfulness (Shaman) keep 50%. Reverence 2/2 gives 6.1 MPS at 130 Spirit.
- **Protection receives mana mainly when it is hit.** Shield Specialization gives this mana. The beta of 30 October removes Improved Seal of Fury. Shieldsworn adds a return on each Holy Strike. Sanctified Judgement (Retribution row 2) is the other source.
- **Retribution loses mana because of Seal changes.** The cause is not the regeneration.

## 2. Inputs

**Gear**

- Maximum mana and mp5 come from the gear tiers (see Threat, part 2). Fresh level 60: 2,897 mana and 3 mp5. Naxxramas: 4,900 mana and 12 mp5.
- Tank gear does not give much Spirit. All tiers use 130 Spirit.

**Combat (wowsims Forever, default tank set, 3 min)**

- The boss swings each 2.0 sec.
- Blocks: 42.3% of the boss swings in the beta, 61.6% with Redoubt (C-P1).
- The 3 sec limit of Shield Specialization skips the next swing after a return. Thus, the returns from blocks each sec are block ÷ (2 × (1 + block)).
- Holy Strike with Shieldsworn: 0.65 returns for each Holy Strike cast. The Holy Strike must land while Holy Shield is active. In wowsims, about 17 of 26.9 Holy Strikes in 3 min give a return.

**Tank build 0/38/13 (only the talents that change mana)**

- Shield Specialization 2/2: a 100% chance to return 4% of maximum mana on a block, once each 3 sec. With Shieldsworn, the same chance on each Holy Strike that lands, with no limit.
- Shieldsworn: Holy Strike has a 6 sec cooldown.
- Benediction 5/5: −10% cost of instant spells.
- Improved Judgement 2/2: the Judgement cooldown is 8 sec. With Swift Judgement, the tank uses 8.5 Judgements each min.
- Sanctified Judgement 3/3: 60% of the base cost of the Seal on each Judgement. Seal of Fury rank 7 costs 200: the return is 120 mana. The free Judgement of Swift Judgement also gives the return (wowsims Forever).

**Spell costs at level 60 (Forever spellbook)**

| Spell | Cost |
| --- | --- |
| Holy Shield rank 3 | 240 mana, each 10 sec |
| Holy Strike | 20 mana, each 6 sec (Shieldsworn) |
| Judgement | 91 mana (6% of base mana 1,512), each 8 sec |
| Seal of Fury rank 7 | 200 mana, each 30 sec |
| Consecration rank 5 | 565 mana, each 8 sec |

- Base mana 1,512 is the Classic value. It is not confirmed for Forever.
- Holy Shield rank 4 has no cost yet in the game files. The model uses the cost of rank 3.
- Holy Conduit (Consecration ×0.60) is now in the Holy tree. A tank does not take it.
- Blessing of Wisdom gives 8 MPS. Judgement of Wisdom on the boss gives more. They are not in the tables, except where a column says so.

## 3. Protection results

**Mana income and cost of the tank (hit, no Consecration, no Blessing of Wisdom)**

| Source | Fresh level 60, beta | Fresh level 60, Redoubt (C-P1) | Naxxramas, beta | Naxxramas, Redoubt (C-P1) |
| --- | --- | --- | --- | --- |
| Shield Specialization, blocks | 17.2 | 22.1 | 29.1 | 37.4 |
| Shield Specialization, Holy Strike (Shieldsworn) | 12.6 | 12.6 | 21.2 | 21.2 |
| Sanctified Judgement 3/3 | 17.0 | 17.0 | 17.0 | 17.0 |
| mp5 from gear | 0.6 | 0.6 | 2.4 | 2.4 |
| Cost: Holy Shield, Holy Strike, Judgement, Seal of Fury | −40.8 | −40.8 | −40.8 | −40.8 |
| **Result** | **+6.5** | **+11.4** | **+28.9** | **+37.2** |

- Consecration on cooldown adds 63.6 MPS of cost (104.4 in all).
- Sanctified Judgement returns 60% of the base cost of the Seal, before talent cost decreases (Beta test results): 120 mana for each Judgement.

**Result for each gear tier (hit, no Consecration)**

| Tier (maximum mana) | Beta | Redoubt (C-P1) | Redoubt (C-P1), flatter gear | Beta, Blessing of Wisdom | Redoubt (C-P1), Blessing of Wisdom |
| --- | --- | --- | --- | --- | --- |
| Fresh level 60 (2,897) | +6.5 | +11.4 | +11.4 | +14.5 | +19.4 |
| Pre-raid best in slot (3,400) | +12.1 | +17.8 | +17.8 | +20.1 | +25.8 |
| Molten Core (3,900) | +17.8 | +24.4 | +21.1 | +25.8 | +32.4 |
| Blackwing Lair (4,400) | +23.4 | +30.8 | +24.3 | +31.4 | +38.8 |
| Naxxramas (4,900) | +28.9 | +37.2 | +27.5 | +36.9 | +45.2 |

"Flatter gear" uses the model of Threat, part 3.

**Other cases: MPS and time until the mana is zero**

| Case | Fresh level 60, beta | Fresh level 60, Redoubt (C-P1) | Naxxramas, beta | Naxxramas, Redoubt (C-P1) |
| --- | --- | --- | --- | --- |
| Consecration on cooldown | −57.0: 50 sec | −52.2: 55 sec | −34.6: 2 min 21 sec | −26.4: 3 min 5 sec |
| Consecration on cooldown, Blessing of Wisdom | −49.0: 59 sec | −44.2: 1 min 5 sec | −26.6: 3 min 3 sec | −18.4: 4 min 26 sec |
| Not hit | −10.7: 4 min 31 sec | −10.7: 4 min 31 sec | −0.2: more than 1 hour | −0.2: more than 1 hour |
| Not hit, Blessing of Wisdom | −2.7: 17 min 59 sec | −2.7: 17 min 59 sec | +7.8 | +7.8 |
| Not hit, Consecration on cooldown | −74.2: 39 sec | −74.2: 39 sec | −63.8: 1 min 16 sec | −63.8: 1 min 16 sec |

**Value of each mana talent (hit, no Consecration)**

| Case | Fresh level 60, beta | Fresh level 60, Redoubt (C-P1) | Naxxramas, beta | Naxxramas, Redoubt (C-P1) |
| --- | --- | --- | --- | --- |
| Tank build 0/38/13 | +6.5 | +11.4 | +28.9 | +37.2 |
| No Shieldsworn | −4.8: 10 min 1 sec | 0.0 | +8.9 | +17.1 |
| No Sanctified Judgement | −10.5: 4 min 36 sec | −5.6: 8 min 37 sec | +11.9 | +20.2 |
| No Benediction | +2.0 | +6.9 | +24.4 | +32.6 |

- **Shieldsworn** gives 11–20 MPS of mana: the Shield Specialization return on Holy Strike. It also costs 1.2 MPS: Holy Strike each 6 sec, not 10 sec.
- **Sanctified Judgement** gives 17.0 MPS at all tiers, also when the boss does not hit the tank.
- **Benediction** saves 4.5 MPS.

**Sanctified Judgement by rank (C-R3)**

8.5 Judgements each min with Seal of Fury (Improved Judgement 2/2 and Swift Judgement), no Benediction.

| Rank | Beta | Sanctified Judgement (C-R3) |
| --- | --- | --- |
| 1/3 | 1.9 | 5.7 |
| 2/3 | 7.6 | 11.3 |
| 3/3 | 17.0 | 17.0 |

- In the beta, each rank increases the chance (33/66/100%) and the return (20/40/60%). With Sanctified Judgement (C-R3), the return occurs on each Judgement.
- Tank and Retribution builds use 3/3. Thus, Sanctified Judgement (C-R3) does not change the tables of this part.

**Lay on Hands at full mana (hit, Blessing of Wisdom)**

| Tier (mana income) | Beta: all the mana, time until it is back | Devoted Sacrifice (C-P11) 2/2: drain, time until it is back |
| --- | --- | --- |
| Fresh level 60 (+14.5 MPS) | 2,897: 3 min 19 sec | 1,449: 1 min 39 sec |
| Naxxramas (+36.9 MPS) | 4,900: 2 min 12 sec | 2,450: 1 min 6 sec |

**wowsims check (default tank set, 3 min, full buffs)**

| Case | Shield Specialization returns each min, wowsims | Model |
| --- | --- | --- |
| Beta | 14.7 | 15.4 (+5%) |
| Redoubt (C-P1) | 17.0 | 17.9 (+5%) |

- The model gives 5% more returns than wowsims. The model rules for the 3 sec limit and for Shieldsworn agree with the sim.
- The wowsims tank has full buffs, Judgement of Wisdom on the boss and consumables. Thus, the sim result is not the result of the model tables.

## 4. Retribution results

The wowsims default Retribution build of 1 November (14/6/31) at fresh level 60. The wowsims rotation changes the Seal after each swing: Seal of Righteousness, then Seal of Command.

- **Mana.** Pool 3,029. Cost 51.2 MPS (0.25 Seals each sec). Income 6.2 MPS, and 8 MPS from Blessing of Wisdom.
- **Time until the mana is zero.** 1 min 21 sec with Blessing of Wisdom, 1 min 7 sec without.

**Seal plans** (n swings with Seal of Righteousness, then 1 with Seal of Command, Blessing of Wisdom)

| Plan | DPS (model) | Mana used | Time until the mana is zero |
| --- | --- | --- | --- |
| Seal of Command only | 285 (−12%) | — | — |
| n = 1 (wowsims rotation) | 324 | 51.2 | 1 min 21 sec |
| n = 2 | 318 (−1.8%) | 35.6 | 2 min 21 sec |
| n = 3 | 316 (−2.6%) | 27.8 | 3 min 43 sec |
| n = 4 | 306 (−5.5%) | 23.1 | 5 min 40 sec |
| n = 6 | 295 (−8.9%) | 17.7 | 14 min 17 sec |

- The best plan changes with the fight length. In fights of 2 min, n = 2 is best before raids, and n = 1 from Molten Core. In fights of 3 min, n = 3 is best before raids, and n = 2 from Molten Core. In fights of 5 min, n = 3 is best at all tiers.
- **Unsealed Wrath.** The talent has no Seal cost decrease (W29). With a −20% Seal cost, n = 1 lasts 1 min 49 sec and n = 3 lasts 5 min 40 sec. The best damage in the fight increases by 0.7–2.6% at fresh level 60. See Analysis, Damage.
- **Reverence.** Reverence is in Holy row 2. A Retribution Paladin needs 7 Holy points for Reverence 2/2. It gives 6.1 MPS at 130 Spirit.

## 5. What the results mean

- **The tank receives more mana with gear.** Shield Specialization returns 4% of maximum mana. More mana gives a larger return.
- **The tank has mana without Consecration.** At fresh level 60, the margin is small: +6.5 MPS without Blessing of Wisdom.
- **Consecration is for groups of enemies.** On cooldown, it empties the mana in 1–5 min (50 sec to 4 min 26 sec).
- **Redoubt (C-P1) gives more mana.** It adds 4.9 MPS at fresh level 60 and 8.3 MPS in Naxxramas. More blocks give more returns.
- **Intellect is a tank stat for the Paladin.** It gives more mana. It also increases the Shield Specialization return.
- **Retribution chooses between damage and mana.** Fewer Seal changes cost 1.7–8.8% damage, but the mana lasts 1.7–11 times longer.

## 6. Limits

- **Block rate.** The block rates come from wowsims with the default tank set. More Defense or block from gear changes them.
- **Holy Shield.** The cost of rank 4 is not known. The model uses 240 mana (rank 3).
- **Base mana.** 1,512 is the Classic value.
- **Spirit regeneration.** The model uses the Classic 1.12 formula. Forever did not publish a formula.
- **The beta of 18 October.** The earlier version of this tab used the trees of 18 October. It is in the history of the repository.
