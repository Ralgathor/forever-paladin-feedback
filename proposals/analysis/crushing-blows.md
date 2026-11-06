# Crushing blows

**Question.** Why does the Paladin tank take crushing blows, and how does Redoubt (C-P1) stop them?

## Short answer

- **The problem.** In the live version, a raid boss hits the Paladin with a crushing blow on 11.9% of its swings. A crushing blow does 150% damage. The Warrior takes crushing blows on only 1.1% of the swings.
- **The fix.** With Redoubt (C-P1), each Holy Shield cast also starts Redoubt. The two block buffs are then active together. Crushing blows decrease to 1.2%, almost the same as the Warrior (1.1%).
- **The tank takes 13% less damage** with C-P1. With the item pool tank sets and the same tank consumables as the Warrior, it then takes 2% less damage than the Warrior (300 against 306 each sec). Its TMI is also lower (42.8 against 43). With the survival sets, it takes 1% less damage than the Warrior, and its TMI is lower (36.0 against 41).
- **Keep Redoubt at 6–30% block.** At 4–20%, 5.6% of the swings are still crushing blows.
- **Fast bosses and bosses with two weapons** give both tanks more crushing blows. With C-P1, the Paladin stays 0.1–1.0 points above the Warrior. At 4–20%, it is 2.4–4.5 points above.

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
| Paladin, live | 41.0% | 11.9% | 343 | 54.0 |
| **Paladin, Redoubt (C-P1)** | **60.9%** | **1.2%** | **300 (−13%)** | **42.8** |
| Paladin, C-P1 with Redoubt 4–20% | 53.6% | 5.6% | 327 (−5%) | 51.3 |
| Paladin, Redoubt 4–20% without C-P1 | 39.2% | 13.0% | 349 (+2%) | 55.7 |
| Warrior | 53.0% | 1.1% | 306 | 43 |
| Druid | 0% | 15.1% | 393 | 43.9 |

- **C-P1 puts the Paladin at the Warrior level for crushing blows:** 1.2% against 1.1%.
- **With C-P1, the Paladin takes 2% less damage than the Warrior** (300 against 306 each sec). Its TMI is also lower (42.8 against 43). The live Paladin takes 12% more damage. The Warrior dodges more: 21.4% against 14.2%. The boss has 0.2% critical hits on the Paladin with C-P1.
- **Consumables are important.** Without consumables (Demonic Rune only, the runs before 4 November evening), the Paladin with C-P1 took 13% more damage than the Warrior (339 each sec, TMI 55.3), and the live Paladin 28% more.
- **5 min fights give the same result.** Live 12.0%, C-P1 1.4%, C-P1 with 4–20% 5.7%, Warrior 1.1%.
- **The Druid takes the most crushing blows,** but its armor and health keep it safe.

**Survival sets.** The same runs with the item pool survival set of each class (Analysis, Threat, part 6).

| Tank | Block | Crushing blows | Damage taken each sec | TMI |
| --- | --- | --- | --- | --- |
| Paladin, live | 41.2% | 11.8% | 333 | 45.8 |
| **Paladin, Redoubt (C-P1)** | **61.7%** | **1.1%** | **289 (−13%)** | **36.0** |
| Paladin, C-P1 with Redoubt 4–20% | 53.5% | 6.3% | 320 (−4%) | 43.9 |
| Paladin, Redoubt 4–20% without C-P1 | 39.1% | 13.0% | 340 (+2%) | 47.1 |
| Warrior | 52.2% | 0.9% | 292 | 41 |
| Druid | 0% | 15.1% | 393 | 42.7 |

- **The crushing blows do not change with the set.** C-P1 gives 1.1% (Warrior: 0.9%).
- **The Paladin TMI decreases:** 36.0 with C-P1 (threat set: 42.8). The Warrior stays at 41.
- **With C-P1, the Paladin takes 1% less damage than the Warrior** (live: 14% more).
- **Fast bosses and bosses with two weapons** give the same result as the table below. C-P1 is 0.2–1.4 points above the Warrior. With 4–20%, the Paladin is 3.0–5.4 points above.

**Fast bosses and bosses with two weapons.** The same tanks and 3 min fight. "Fast" is a swing each 1.2 sec with 60% damage, thus the same damage each sec. "Two weapons" adds a second weapon. The Paladin uses the wowsims default tank build (12/32/7), with Toughness removal (C-P13) in the C-P1 columns.

| Boss | Warrior | Paladin, C-P1 | Paladin, C-P1 with 4–20% | Paladin, live |
| --- | --- | --- | --- | --- |
| Normal (2.0 sec) | 1.1% | 1.2% | 5.6% | 11.9% |
| Fast (1.2 sec) | 3.5% | 3.7% | 6.9% | 11.0% |
| Two weapons | 4.5% | 5.1% | 7.7% | 11.0% |
| Fast, two weapons | 7.8% | 8.8% | 10.2% | 11.7% |

| Boss | Damage taken each sec: Warrior | Paladin, C-P1 | Paladin, C-P1 with 4–20% | Paladin, live |
| --- | --- | --- | --- | --- |
| Normal | 306 | 305 | 333 | 343 |
| Fast | 294 | 290 | 311 | 314 |
| Two weapons | 459 | 467 | 495 | 494 |
| Fast, two weapons | 456 | 459 | 478 | 470 |

- **More swings use the charges faster.** Both tanks then have gaps. The Warrior reaches 3.5–7.8% crushing blows, the Paladin with C-P1 3.7–8.8%.
- **C-P1 follows the Warrior.** It is 0.1–1.0 points above the Warrior with each boss. Against a boss with two weapons, it takes 1–2% more damage than the Warrior. Against a boss with one weapon, it takes 0–1% less.
- **4–20% is always worse.** It is 2.4–4.5 points above the Warrior, and 4.5 points above on a normal boss.
- **Against fast bosses with two weapons,** C-P1 gives a small gain: 11.7% → 9.0%. The charges are empty too soon. The Warrior also has 7.8%.

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
- **With Redoubt at 4–20%,** the total is 90.7% + Agility ÷ 20. With 100 Agility, about 4.3% of the swings are crushing blows. wowsims gives 5.6%, because the item pool set has less Defense.

## 5. Paladin against Warrior

Both tanks have 440 Defense and 100 Agility. The boss swings each 2 sec. Shield Block (Wowhead tooltip): "Increases chance to block by 75% for 7 sec, but will only block 2 attacks", 10 rage, 5 sec cooldown.

| Tank | Swings that the buffs cover | Crushing blow chance on the other swings | Crushing blows in total |
| --- | --- | --- | --- |
| Warrior | About 80% (2 of 2.5 swings each 5 sec) | 15% | About 3% |
| Paladin with C-P1 | About 100% | 0% at 440 Defense | Only in gaps |

- wowsims gives the Warrior 1.1% and the Paladin 1.2%. Thus, the two tanks are almost equal for crushing blows.
- The Warrior gaps depend on the swing speed of the boss. The Paladin gaps depend on when Holy Shield is cast. With fast bosses or two weapons, both tanks have more gaps (part 3).

## 6. Method and limits

- **Sim.** wowsims Forever, master commit 9a8624af9 (game files of client 1.60.1.70755 and the hotfixes of 4 November), with the proposals as flags (`models/wowsims-b2`). The item pool tank set of each class (`models/wowsims-b2/tank_gear`), tank consumables, full buffs, one level 63 boss, 3,000 iterations, 3 min. The Warrior threat set runs on master commit df57e2571 (6 November, hotfix push 113693), with Scarlet Kris, a new item of this commit. Logs: `logs/checks_9a8624af9_pool.log`, `logs/checks_9a8624af9_pool_surv.log` and `logs/checks_df57e2571_pool.log` (Warrior).
- **Gear.** The item pool tank sets are pre-raid sets. They do not reach 440 Defense. Thus, the boss still has 0.2% critical hits on the Paladin with C-P1.
- **Boss.** The main tables use a boss with one weapon and a 2 sec swing. Part 3 also gives fast bosses and bosses with two weapons (`FEEDBACK_BOSS` in `models/wowsims-b2`).
- **Talents.** The values use the live talents. A change to Holy Shield or Redoubt changes all values.
