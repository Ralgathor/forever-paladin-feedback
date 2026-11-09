# Crushing blows

**Question.** Why does the Paladin tank take crushing blows, and how does Redoubt (C-P1) stop them?

## Short answer

- **The problem.** In the live version, a raid boss hits the Paladin with a crushing blow on 5.6% of its swings (11.9% before Argent Defender, part 3). A crushing blow does 150% damage. The Warrior takes crushing blows on only 1.1% of the swings.
- **The fix.** With Redoubt (C-P1), each Holy Shield cast also starts Redoubt. The two block buffs are then active together. Crushing blows decrease to 1.0%, the same as the Warrior (1.1%).
- **The tank takes 7% less damage** with C-P1. With the item pool tank sets and the same tank consumables as the Warrior, it then takes 4% less damage than the Warrior (293 against 306 each sec). Its TMI is also lower (40.2 against 43). With the survival sets, it takes the same damage as the Warrior, and its TMI is lower (38.8 against 41).
- **Keep Redoubt at 6–30% block.** At 4–20%, the crushing blows stay near C-P1 on a normal boss (1.2%). Fast bosses and bosses with two weapons then give 1.3–2.7 points more.
- **Fast bosses and bosses with two weapons** give both tanks more crushing blows. With C-P1, the Paladin stays 1.2–1.7 points below the Warrior. At 4–20%, it is 0.1–1.0 points above.

## 1. Why crushing blows occur

- A raid boss is level 63, 3 levels above the player.
- A level 63 boss has a 15% chance to hit for a crushing blow.
- The boss attack table has 100% in total. Miss, dodge, parry and block come first. Then crushing blows fill the next 15%.
- Thus, a tank stops crushing blows only with miss + dodge + parry + block = 100%.

Each tank handles crushing blows in a different way:

| Tank | Method | Result |
| --- | --- | --- |
| Warrior | Shield Block gives +75% block for 2 blocks, each 5 sec | Almost no crushing blows |
| Druid | No shield. High armor and health | Many crushing blows, but the Druid survives them |
| Paladin, live | Holy Shield gives +30% block for 4 blocks, each 10 sec. Redoubt gives +30% block, but it starts only on 10% of the hits | Many crushing blows, and no extra armor or health |

Redoubt (C-P1) uses the Warrior method. It removes crushing blows with block. The Protection tree already gives block.

## 2. How Redoubt (C-P1) works

- **In the live version,** Redoubt starts on only 10% of the melee hits. Thus, it is off for most of the fight.
- **With C-P1,** each Holy Shield cast starts Redoubt. Holy Shield has a 10 sec cooldown. Thus, both buffs are active for the full fight.
- **The charges are enough.** The boss swings each 2.3 sec: about 4.4 swings in 10 sec. About 2.7 of them are blocks. Redoubt has 5 blocks and Holy Shield has 4.
- **The first swing.** Cast Holy Shield before the pull. Then it covers the first swing.
- **Holy Shield stays at +30%.** With C-P1, this is already enough to match the Warrior.

## 3. Results in wowsims

Item pool threat set of each class (Analysis, Threat, part 6), tank consumables, full buffs, one level 63 boss, 3 min fight. The Paladin has Holy Shield rank 4 (build 70755) and the consumables of the Warrior test, with Greater Arcane Elixir and Brilliant Wizard Oil.

| Tank | Block | Crushing blows | Damage taken each sec | TMI |
| --- | --- | --- | --- | --- |
| Paladin, live | 55.0% | 5.6% | 316 | 47.1 |
| **Paladin, Redoubt (C-P1)** | **61.9%** | **1.0%** | **293 (−7%)** | **40.2** |
| Paladin, C-P1 with Redoubt 4–20% | 61.6% | 1.2% | 293 (−7%) | 40.3 |
| Paladin, Redoubt 4–20% without C-P1 | 54.9% | 5.7% | 317 (+0%) | 47.3 |
| Warrior | 53.1% | 1.1% | 306 | 43 |
| Druid | 0% | 15.0% | 359 | 38.2 |

- **Argent Defender halves the live crushing blows.** The item pool set of 8 November has Argent Defender, a shield of the hotfixes of 7 and 8 November. After a hit, it can increase the block chance. The live block goes from 41.0% to 55.0%, and the crushing blows from 11.9% to 6.6%. The set of 9 November gives 5.6% (Analysis, Threat, part 6).
- **C-P1 puts the Paladin at the Warrior level for crushing blows:** 1.0% against 1.1%.
- **With C-P1, the Paladin takes 4% less damage than the Warrior** (293 against 306 each sec). Its TMI is also lower (40.2 against 43). The live Paladin takes 3% more damage. The Warrior dodges more: 21.5% against 14.5%. The boss has 0.3% critical hits on the Paladin with C-P1.
- **Consumables are important.** Without consumables (Demonic Rune only, the runs before 4 November evening), the Paladin with C-P1 took 13% more damage than the Warrior (339 each sec, TMI 55.3), and the live Paladin 28% more.
- **5 min fights give the same result.** Live 5.7%, C-P1 1.0%, C-P1 with 4–20% 1.3%, Warrior 1.1%.
- **The Druid takes the most crushing blows,** but its armor and health keep it safe.

**Survival sets.** The same runs with the item pool survival set of each class (Analysis, Threat, part 6).

| Tank | Block | Crushing blows | Damage taken each sec | TMI |
| --- | --- | --- | --- | --- |
| Paladin, live | 54.9% | 5.7% | 317 | 45.5 |
| **Paladin, Redoubt (C-P1)** | **62.0%** | **0.9%** | **292 (−8%)** | **38.8** |
| Paladin, C-P1 with Redoubt 4–20% | 61.7% | 1.2% | 293 (−8%) | 38.9 |
| Paladin, Redoubt 4–20% without C-P1 | 54.8% | 5.8% | 317 (+0%) | 45.5 |
| Warrior | 52.2% | 0.9% | 293 | 41 |
| Druid | 0% | 15.0% | 345 | 35.8 |

- **The crushing blows do not change much with the set.** C-P1 gives 0.9% (Warrior: 0.9%).
- **The Paladin TMI decreases:** 38.8 with C-P1 (threat set: 40.2). The Warrior goes from 43 to 41.
- **With C-P1, the Paladin takes the same damage as the Warrior** (292 against 293 each sec; live: 8% more).
- **Fast bosses and bosses with two weapons** give the same result as the table below. C-P1 is 0.7–1.4 points below the Warrior. With 4–20%, the Paladin is 0.5–1.3 points above.

**Fast bosses and bosses with two weapons.** The same tanks and 3 min fight. "Fast" is a swing each 1.2 sec with 60% damage, thus the same damage each sec. "Two weapons" adds a second weapon. The Paladin uses the wowsims default tank build (12/32/7), with Toughness removal (C-P13) in the C-P1 columns.

| Boss | Warrior | Paladin, C-P1 | Paladin, C-P1 with 4–20% | Paladin, live |
| --- | --- | --- | --- | --- |
| Normal (2.0 sec) | 1.1% | 1.0% | 1.2% | 5.6% |
| Fast (1.2 sec) | 3.5% | 2.3% | 3.6% | 5.8% |
| Two weapons | 4.4% | 3.2% | 5.1% | 6.2% |
| Fast, two weapons | 7.8% | 6.1% | 8.8% | 8.0% |

| Boss | Damage taken each sec: Warrior | Paladin, C-P1 | Paladin, C-P1 with 4–20% | Paladin, live |
| --- | --- | --- | --- | --- |
| Normal | 306 | 298 | 299 | 316 |
| Fast | 296 | 278 | 282 | 291 |
| Two weapons | 458 | 447 | 456 | 461 |
| Fast, two weapons | 456 | 432 | 445 | 438 |

- **More swings use the charges faster.** Both tanks then have gaps. The Warrior reaches 3.5–7.8% crushing blows, the Paladin with C-P1 2.3–6.1%.
- **C-P1 follows the Warrior.** It is 0.1–1.7 points below the Warrior with each boss. Against a boss with two weapons, it takes 2–5% less damage than the Warrior. Against a boss with one weapon, it takes 3–6% less.
- **4–20% is worse against faster bosses.** On a normal boss, it is near C-P1 (1.2% against 1.0%), because Argent Defender adds block. Against fast bosses and bosses with two weapons, it is 1.3–2.7 points above C-P1, and 0.1–1.0 points above the Warrior.
- **Against fast bosses with two weapons,** C-P1 gives a small gain: 8.0% → 6.1%. The charges are empty too soon. The Warrior has 7.8%.

## 4. Stat targets for the tank

A tank needs two targets against a level 63 boss.

**Target 1: 440 Defense, for no critical hits.** The boss has 5.6% critical hit chance. Each Defense point removes 0.04%. Anticipation 5/5 gives 20 Defense. Thus, gear and enchants must give 120 Defense.

**Target 2: miss + dodge + parry + block = 100%, for no crushing blows.** At 440 Defense, each of the four values increases by 5%.

With 440 Defense, Deflection 5/5, Holy Shield and Redoubt 5/5:

| Result | Sources | Total |
| --- | --- | --- |
| Miss | 5% base, 5% Defense | 10% |
| Dodge | About 0.7% base, 5% Defense, 1% for each 20 Agility | 5.7% + Agility ÷ 20 |
| Parry | 5% base, 5% Deflection, 5% Defense | 15% |
| Block | 5% base, 5% Defense, 30% Holy Shield, 30% Redoubt | 70% |
| **Total** | | **100.7% + Agility ÷ 20** |

- **With both buffs, Target 2 is automatic** after Target 1.
- **The 1.0% in wowsims comes from short gaps.** For example, Holy Shield comes late, or Redoubt has no blocks left. Fast bosses and bosses with two weapons use the charges faster.
- **With Holy Shield only,** the total is 70.7% + Agility ÷ 20. Then up to 15% of the swings are crushing blows.
- **With Redoubt at 4–20%,** the total is 90.7% + Agility ÷ 20. With 100 Agility, about 4.3% of the swings are crushing blows. wowsims gives 1.2%, because Argent Defender adds block (part 3). With the set of 4 November, it gave 5.6%.

## 5. Paladin against Warrior

Both tanks have 440 Defense and 100 Agility. The boss swings each 2 sec. Shield Block (Wowhead tooltip): "Increases chance to block by 75% for 7 sec, but will only block 2 attacks", 10 rage, 5 sec cooldown.

| Tank | Swings that the buffs cover | Crushing blow chance on the other swings | Crushing blows in total |
| --- | --- | --- | --- |
| Warrior | About 80% (2 of 2.5 swings each 5 sec) | 15% | About 3% |
| Paladin with C-P1 | About 100% | 0% at 440 Defense | Only in gaps |

- wowsims gives the Warrior 1.1% and the Paladin 1.0%. Thus, the two tanks are equal for crushing blows.
- The Warrior gaps depend on the swing speed of the boss. The Paladin gaps depend on when Holy Shield is cast. With fast bosses or two weapons, both tanks have more gaps (part 3).

## 6. Method and limits

- **Sim.** wowsims Forever, master commit 9f254e8d8 (hotfix push 113823), with the proposals as flags (`models/wowsims-b2`). The item pool tank set of each class (`models/wowsims-b2/tank_gear`), tank consumables, full buffs, one level 63 boss, 3,000 iterations, 3 min. Logs: `logs/checks_9f254e8d8_pool.log` and `logs/checks_9f254e8d8_pool_surv.log`. The runs of 8 November: `logs/checks_ae9b8c23a_pool.log` and `logs/checks_ae9b8c23a_pool_surv.log`. The runs of 4 and 6 November (set without Argent Defender): `logs/checks_9a8624af9_pool.log`, `logs/checks_9a8624af9_pool_surv.log` and `logs/checks_df57e2571_pool.log`.
- **Gear.** The item pool tank sets are pre-raid sets. They do not reach 440 Defense. Thus, the boss still has 0.3% critical hits on the Paladin with C-P1.
- **Boss.** The main tables use a boss with one weapon and a 2 sec swing. Part 3 also gives fast bosses and bosses with two weapons (`FEEDBACK_BOSS` in `models/wowsims-b2`).
- **Talents.** The values use the live talents. A change to Holy Shield or Redoubt changes all values.
