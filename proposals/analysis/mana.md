# Mana

This section compares the mana of the Paladin in the beta and with the proposals. The unit is mana per second (MPS). A positive value means that the mana increases. A negative value means that the mana decreases.

## Summary

- Sanctified Judgement (Retribution row 3) is the best mana talent for a tank. It returns 120 mana for each Judgement: 14 MPS, or 17 MPS with Improved Judgement 2/2. Reverence gives 10.3 MPS.
- The tank builds PB1, PB3 and PB4 (3/35/13, see Builds) have Sanctified Judgement, Improved Judgement and Holy Conduit. PB2 has no Holy Conduit. With Consecration on cooldown, the mana lasts 1 min 25 sec at fresh level 60 and 9 min 56 sec in Naxxramas. With Blessing of Wisdom, the Naxxramas tank almost does not lose mana.
- Reverence (C-H1) stays the main mana talent for Holy. Retribution takes it without raid buffs (+4% DPS at fresh level 60). In a raid, Twist of Light (C-R2) and Sanctified Judgement give the mana of Retribution. Tanks receive their mana from Sanctified Judgement.
- PB1 receives +8.3 MPS while it tanks at fresh level 60 without Consecration, and +34.2 MPS in Naxxramas.
- **Below Blackwing Lair, PB1 has less mana than in the beta** (fresh level 60: +8.3 MPS, beta +16.2). Shoulder the Burden (C-P5) removes Improved Seal of Fury (23.3 MPS). Redoubt (C-P1) and Shield Specialization (C-P8) return only a part of it at low maximum mana. With the 8/35/8 tank, Reverence (10.3 MPS) hid this loss.
- Shield Specialization (C-P8, once each 2 sec) is necessary. Without Shield Specialization (C-P8), a fresh level 60 PB1 tank loses about 7 MPS.
- Consecration uses much mana. Use it against groups of enemies, not all the time.
- Benediction (M-P1) moves to Protection row 1. PB1 with Benediction and Consecration on cooldown has mana for 2 min 2 sec at fresh level 60. In Naxxramas, its mana lasts all the fight (part 4).
- Twist of Light (C-R2) fixes the mana of Retribution.

## 1. Problems in the beta

- **Spirit regeneration stops when you cast.** It gives 15 + Spirit ÷ 5 mana each 2 sec. It stops for 5 sec after each cast. In combat, it is almost zero.
- **Protection and Retribution have no talent for regeneration during casts.** Other classes give 50% to their damage and hybrid specs at about 20 points (see What the other classes have).
- **Protection receives mana mainly when it is hit.** Shield Specialization and Improved Seal of Fury give this mana. The other source is Sanctified Judgement in Retribution row 3. A tank needs 13 Retribution points for it.
- **Retribution loses mana because of Seal swaps.** The cause is not the regeneration.

## 2. Fixes

| Fix | Effect |
| --- | --- |
| Reverence in row 2 at 50% (C-H1) | Holy has 50%, as the other healers. Retribution takes it without raid buffs: +4% DPS at fresh level 60 (part 5). In a raid, Twist of Light (C-R2) and Sanctified Judgement give its mana. For a tank, Sanctified Judgement gives more (part 4) |
| Shield Specialization once each 2 sec (C-P8) | It stays the main mana source of the tank. Water Shield (Shaman) is the Forever precedent |
| Improved Seal of Fury removed (C-P5) | One talent for "mana when you are hit" is sufficient |
| Echo of 10 sec (Twist of Light, C-R2) | Retribution changes Seals one time each 10 sec, not before each swing |

## 3. Inputs

**Gear**

- Maximum mana and mp5 come from the gear tiers (see Threat, part 2).
- Fresh level 60 uses the real gear profile: 2,897 mana, 3 mp5.
- Tank gear does not give much Spirit. All tiers use 130 Spirit.

**Combat**

- The boss swings each 2.0 sec.
- One-handed weapon: 2.7 sec.
- Block: 50% in the beta, 60% with Redoubt (C-P1).

**Spell costs at level 60 (Forever spellbook)**

| Spell | Cost |
| --- | --- |
| Holy Shield rank 3 | 240 mana, each 10 sec |
| Holy Strike | 20 mana, each 10 sec |
| Judgement | 91 mana (6% of base mana 1,512), each 10 sec |
| Seal of Fury rank 7 | 200 mana, each 30 sec |
| Seal of Command | 210 mana |
| Consecration rank 5 | 565 mana, each 8 sec |

- Base mana 1,512 is the Classic value. It is not confirmed for Forever.
- Holy Conduit (Consecration ×0.60) is in Retribution row 2, as in the beta. A tank takes it with Deflection 5 (7 points).
- Benediction 5/5 (all costs ×0.90) is in Protection row 1 (M-P1). In the beta, it is in Retribution row 1. The beta columns use the same talents from a Retribution dip.
- Sanctified Judgement 3/3 returns 60% of the base cost of the Seal for each Judgement. Seal of Fury rank 7 costs 200: the return is 120 mana. The free Judgement of Swift Judgement also gives the return (wowsims Forever).
- Improved Judgement 2/2 (Retribution row 2) decreases the Judgement cooldown to 8 sec. The tank then uses 8.5 Judgements each min, not 7.
- Raid buffs are not in the model. Blessing of Wisdom gives 8 MPS. Judgement of Wisdom on the boss gives more.

## 4. Protection results

The tables use the raid tank PB1 (3/35/13, see Builds, part 3): Sanctified Judgement 3/3, Improved Judgement 2/2 and Holy Conduit 2/2, no Benediction. The beta columns use the same talents in the beta tree, with Improved Seal of Fury and the beta Shield Specialization. The script models/mana/mana_model.py gives all values.

**Mana income of the tank**

| Source | Beta | Proposed | Calculation |
| --- | --- | --- | --- |
| Shield Specialization | Maximum mana × 4% ÷ 6 sec | Maximum mana × 4% × 60% ÷ 2 sec | Beta: the 3 sec limit skips the next swing. 50% block. Proposed: each block counts (Shield Specialization, C-P8). 60% block (Redoubt, C-P1) |
| Improved Seal of Fury | 23.3 | 0 (Shoulder the Burden, C-P5) | 87 mana for each shield that a boss hit uses |
| Sanctified Judgement 3/3 | 17.0 | 17.0 | 120 mana for each Judgement, 8.5 Judgements each min (Improved Judgement 2/2 and Swift Judgement) |
| mp5 from gear | 0.6–2.4 | 0.6–2.4 | 3–12 mp5 |

**Mana used**

| Case | MPS |
| --- | --- |
| Tank, no Consecration | 41.7 |
| Tank, Consecration on cooldown | 112.4 |
| Tank, Consecration on cooldown, Holy Conduit | 84.1 |
| Tank, no Consecration, Benediction (M-P1) | 37.6 |
| Tank, Consecration on cooldown, Benediction (M-P1) | 101.2 |
| Tank, Consecration on cooldown, Benediction (M-P1) and Holy Conduit | 75.7 |
| **PB1:** tank, no Consecration (Improved Judgement 2/2) | 44.0 |
| **PB1:** tank, Consecration on cooldown | 114.7 |
| **PB1:** tank, Consecration on cooldown, Holy Conduit | 86.4 |

The costs do not change with gear.

**PB1: income and result for each gear tier (tank, no Consecration)**

| Tier (maximum mana) | Income, beta | Income, proposed | Result, beta | Result, proposed | Result, proposed, flatter gear |
| --- | --- | --- | --- | --- | --- |
| Fresh level 60 (2,897) | 60.2 | 52.4 | +16.2 | +8.3 | +8.3 |
| Pre-raid best in slot (3,400) | 64.0 | 58.8 | +19.9 | +14.8 | +14.8 |
| Molten Core (3,900) | 67.9 | 65.4 | +23.9 | +21.4 | +18.2 |
| Blackwing Lair (4,400) | 71.6 | 71.8 | +27.6 | +27.8 | +21.4 |
| Naxxramas (4,900) | 75.4 | 78.2 | +31.3 | +34.2 | +24.5 |

"Flatter gear" uses the model of Threat, part 3.

**PB1: other cases, MPS and time until the mana is zero**

| Case | Fresh level 60, beta | Fresh level 60, proposed | Naxxramas, beta | Naxxramas, proposed |
| --- | --- | --- | --- | --- |
| Tank, Consecration on cooldown, no Holy Conduit | −54.5: 53 sec | −62.3: 46 sec | −39.3: 2 min 4 sec | −36.5: 2 min 14 sec |
| Tank, Consecration on cooldown, Holy Conduit | −26.2: 1 min 50 sec | −34.1: 1 min 25 sec | −11.0: 7 min 23 sec | −8.2: 9 min 56 sec |
| Tank, Consecration on cooldown, Holy Conduit, Benediction (M-P1) | −15.9: 3 min 2 sec | −23.7: 2 min 2 sec | −0.7: more than 1 hour | +2.1: all the fight |
| Not hit, no Consecration | −26.4: 1 min 49 sec | −26.4: 1 min 49 sec | −24.6: 3 min 18 sec | −24.6: 3 min 18 sec |
| Not hit, Consecration on cooldown, Holy Conduit | −68.8: 42 sec | −68.8: 42 sec | −67.0: 1 min 13 sec | −67.0: 1 min 13 sec |

The Benediction row needs 5 Protection points from other PB1 talents.

**Tank builds: Sanctified Judgement against Reverence**

Each cell gives the MPS and the time until the mana is zero.

| Build | Fresh level 60, no Consecration | Fresh level 60, Consecration on cooldown | Naxxramas, no Consecration | Naxxramas, Consecration on cooldown |
| --- | --- | --- | --- | --- |
| PB1, PB3, PB4 (3/35/13: Sanctified Judgement, Improved Judgement, Holy Conduit) | +8.3 | −34.1: 1 min 25 sec | +34.2 | −8.2: 9 min 56 sec |
| PB1, PB3, PB4, Blessing of Wisdom | +16.3 | −26.1: 1 min 51 sec | +42.2 | −0.2: more than 1 hour |
| PB2 (3/35/13, no Holy Conduit) | +8.3 | −62.3: 46 sec | +34.2 | −36.5: 2 min 14 sec |
| 8/35/8 tank with Reverence | +3.9 | −66.8: 43 sec | +29.8 | −41.0: 1 min 59 sec |
| 8/35/8 tank with Reverence and Holy Conduit | +3.9 | −38.5: 1 min 15 sec | +29.8 | −12.6: 6 min 29 sec |
| 8/35/8 tank with Reverence and Holy Conduit, Blessing of Wisdom | +11.9 | −30.5: 1 min 35 sec | +37.8 | −4.6: 17 min 35 sec |

- **Sanctified Judgement** gives 14.0 MPS with 7 Judgements each min. Improved Judgement 2/2 adds 1.5 Judgements each min: +3.0 MPS of return and 2.3 MPS of cost. It also gives +19 threat per sec (see Builds).
- **Thus, the 3/35/13 tank has 4.4 MPS more** than the 8/35/8 tank, with or without Consecration.
- **Sanctified Judgement by rank (C-R3).** With Sanctified Judgement (C-R3), the return occurs on each Judgement. Each rank gives 40 mana for each Judgement with Seal of Fury: 5.7/11.3/17.0 MPS. The beta gives 1.9/7.5/17.0 MPS. At 3/3, the two are the same. Thus, the tables of this part do not change.
- **When the boss does not hit the tank,** Sanctified Judgement is better than Reverence also: PB1 loses 26.4 MPS, the 8/35/8 tank 30.9 MPS.
- Blessing of Wisdom (8 MPS) is not in the other tables of this part.

## 5. Retribution results

One target. Sanctified Judgement returns 126 mana (60% of the base cost of the Seal) for each Judgement. Tests show this.

| Case | Mana used | Time until zero, no regeneration (2,897 → 4,900 mana) | Time until zero, with Reverence 50% (9.75 MPS) |
| --- | --- | --- | --- |
| Beta: about 3 Seals each 10 sec | 41.6 MPS | 1 min 10 sec → 1 min 58 sec | 1 min 31 sec → 2 min 34 sec |
| Twist of Light (C-R2): one Seal each 10 sec | 11.4 MPS | 4 min 14 sec → 7 min 10 sec | 29 min → 49 min |

**wowsims check (27 October 2026).** RB1 with Reverence (C-H1), Twist of Light (C-R2) and Sanctified Judgement (C-R3), in a 3 min fight. Divine Intellect 3 replaces Reverence 3 in the second column. wowsims has only 3 ranks of Vindication, thus RB1 has Vindication 3.

| Case | RB1 with Reverence | RB1 without Reverence |
| --- | --- | --- |
| Raid buffs, Judgement of Wisdom | 849 DPS, the mana lasts all the fight | 853 DPS, the mana lasts all the fight |
| Raid buffs, no Judgement of Wisdom, no mana consumables | 850 DPS, the mana lasts all the fight | 853 DPS, the mana lasts all the fight |
| Fresh level 60, no buffs | 361 DPS | 348 DPS (−4%) |
| Without Twist of Light (C-R2), raid buffs, no Judgement of Wisdom, no mana consumables | 775 DPS | 739 DPS (−5%) |

- With Twist of Light (C-R2), Retribution does not need Reverence in a raid. Twist of Light (C-R2) and Sanctified Judgement give the mana.
- Without raid buffs, Reverence gives Retribution +4% DPS. Thus, it stays a Retribution talent while it levels and at fresh level 60. Without Twist of Light (C-R2), Reverence gives Retribution about 12 MPS.

## 6. What the results mean

- **The tank receives more mana with gear.** Shield Specialization returns 4% of maximum mana for each block. More mana gives a larger return.
- **At fresh level 60, PB1 receives +8.3 MPS** with the proposals. Without Shield Specialization (C-P8), it loses about 7 MPS.
- **In raids, the tank does not lose mana without Consecration.** PB1 receives +15 to +34 MPS (beta: +20 to +31).
- **The proposals give PB1 less mana than the beta up to Molten Core** (−7.9 MPS at fresh level 60, −2.5 in Molten Core). From Blackwing Lair, they give more (+2.9 in Naxxramas). The cause is Shoulder the Burden (C-P5): Improved Seal of Fury gave 23.3 MPS at all gear levels. Redoubt (C-P1) and Shield Specialization (C-P8) give more with more maximum mana.
- **Consecration on cooldown uses all mana quickly** without Holy Conduit: PB2 has mana for 46 sec at fresh level 60 and 2 min 14 sec in Naxxramas.
- **Holy Conduit gives the large decrease with Consecration.** With Benediction, it saves about 25 mana per sec (W4).
- **Sanctified Judgement is the best mana talent for a tank.** It gives 14–17 MPS, also when the boss does not hit the tank. Reverence gives 10.3 MPS. It stays the mana talent for Holy, and for Retribution without raid buffs.
- **Sanctified Judgement (C-R3) does not change the total return.** It changes only ranks 1 and 2. Each point now gives the same mana.
- **The 3/35/13 tank can use Consecration on cooldown for a long time.** With Holy Conduit, its mana lasts 1 min 25 sec at fresh level 60 and almost 10 min in Naxxramas.
- **Flatter gear gives less mana.** In late raids, PB1 receives +18 to +25 MPS. Shield Specialization (C-P8) is then more important.
- **Intellect is a tank stat for the Paladin.** It gives more mana. It also increases the Shield Specialization return.
- **Retribution with Twist of Light (C-R2) almost does not lose mana.** Sanctified Judgement pays for most of the Seal cost. Reverence adds no damage in a raid. It adds about 4% at fresh level 60. Thus, Retribution takes it without raid buffs (wowsims check, 27 October 2026).
