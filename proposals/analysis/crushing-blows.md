# Crushing blows

**Question.** Why does the Paladin tank take crushing blows, and how does Redoubt (C-P1) stop them?

## Short answer

- **The problem.** In the live version, a raid boss hits the Paladin with a crushing blow on 10.2% of its swings (part 3). A crushing blow does 150% damage. The Warrior takes crushing blows on only 1.4% of the swings.
- **The fix.** With Redoubt (C-P1), each Holy Shield cast also starts Redoubt. The two block buffs are then active together. Crushing blows decrease to 1.2%, the Warrior level (1.4%).
- **The tank takes 11% less damage** with C-P1. The tanks have the item pool tank sets and the same tank consumables. The Paladin then takes 5% less damage than the Warrior (281 against 296 each sec), and its TMI is a little higher (40.8 against 38). The Warrior threat set of 15 November takes 10% more damage than its set of 13 November, but it has 7% more threat. With the survival sets, the Paladin takes 4% less damage than the Warrior, and its TMI is about the same (35.9 against 36).
- **Keep Redoubt at 6–30% block.** At 4–20%, the crushing blows go to 3.1% on a normal boss (C-P1: 1.2%). Fast bosses and bosses with two weapons then give 0.4–1.3 points more.
- **Fast bosses and bosses with two weapons** give both tanks more crushing blows. With C-P1, the Paladin is between 0.4 points below and 0.4 points above the Warrior. At 4–20%, it is 0.8–1.1 points above.

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
| Paladin, live | Holy Shield gives +30% block for 4 blocks, each 10 sec. Redoubt gives +30% block, but it starts only on 10% of the melee attacks | Many crushing blows, and no extra armor or health |

Redoubt (C-P1) uses the Warrior method. It removes crushing blows with block. The Protection tree already gives block.

## 2. How Redoubt (C-P1) works

- **In the live version,** Redoubt starts on only 10% of the melee attacks against the Paladin. Since wowsims master 8c7b5a5f5 (13 November), avoided attacks also roll this chance (before: only hits). Thus, it is still off for most of the fight.
- **With C-P1,** each Holy Shield cast starts Redoubt. Holy Shield has a 10 sec cooldown. Thus, both buffs are active for the full fight.
- **The charges are enough.** The boss swings each 2.3 sec: about 4.4 swings in 10 sec. About 2.7 of them are blocks. Redoubt has 5 blocks and Holy Shield has 4.
- **The first swing.** Cast Holy Shield before the pull. Then it covers the first swing.
- **Holy Shield stays at +30%.** With C-P1, this is already enough to match the Warrior.

## 3. Results in wowsims

Item pool threat set of each class (Analysis, Threat, part 6), tank consumables, full buffs, one level 63 boss, 3 min fight. The Paladin has Holy Shield rank 4 (build 70755) and the consumables of the Warrior test, with Greater Arcane Elixir and Brilliant Wizard Oil.

| Tank | Block | Crushing blows | Damage taken each sec | TMI |
| --- | --- | --- | --- | --- |
| Paladin, live | 44.0% | 10.2% | 317 | 50.5 |
| **Paladin, Redoubt (C-P1)** | **58.7%** | **1.2%** | **281 (−11%)** | **40.8** |
| Paladin, C-P1 with Redoubt 4–20% | 54.4% | 3.1% | 300 (−5%) | 47.1 |
| Paladin, Redoubt 4–20% without C-P1 | 42.4% | 10.9% | 323 (+2%) | 52.0 |
| Warrior | 54.9% | 1.4% | 296 | 38 |
| Druid | 0% | 15.0% | 355 | 37.1 |

- **Argent Defender (correction).** The item pool set has Argent Defender, a shield of the hotfixes of 7 and 8 November. From 8 to 10 November, wowsims applied its proc buff (+18% block) all the time, by error. The live block was then 55.0%, and the crushing blows 5.6%. wowsims master 3633d376a (11 November) fixes this error. Masters 52471a100 and 129fcd89e (12 November) do not change the Paladin values. On 11 and 12 November, the live block was 41.2%, and the crushing blows 12.0%.
- **Redoubt fix and new set (13 November).** Master 8c7b5a5f5 makes each melee swing or ability against the Paladin roll the 10% Redoubt chance, avoided attacks included. Thus, the live Redoubt is active more often. The new item pool set has Draconian Deflector in place of Argent Defender. The live block was then 44.0%, and the crushing blows 10.1%.
- **New commit (15 November).** Master 6084403a9 does not change the Paladin values: 44.0% block and 10.2% crushing blows. The new Warrior threat set blocks more (54.9%) but takes 1.4% crushing blows.
- **C-P1 puts the Paladin at the Warrior level for crushing blows:** 1.2% against 1.4%. The live Redoubt fix does not close this gap: the live Paladin still has 10.2%.
- **With C-P1, the Paladin takes 5% less damage than the Warrior** (281 against 296 each sec). Its TMI is a little higher (40.8 against 38). The live Paladin takes 7% more damage. The Warrior dodges more: 17.7% against 15.7%. The boss has 0.2% critical hits on the Paladin with C-P1.
- **Consumables are important.** Without consumables (Demonic Rune only, the runs before 4 November evening), the Paladin with C-P1 took 13% more damage than the Warrior (339 each sec, TMI 55.3), and the live Paladin 28% more.
- **5 min fights give the same result.** Live 10.2%, C-P1 1.3%, C-P1 with 4–20% 3.3%, Warrior 1.4%.
- **The Druid takes the most crushing blows,** but its armor and health keep it safe.

**Survival sets.** The same runs with the item pool survival set of each class (Analysis, Threat, part 6).

| Tank | Block | Crushing blows | Damage taken each sec | TMI |
| --- | --- | --- | --- | --- |
| Paladin, live | 43.7% | 10.2% | 302 | 44.0 |
| **Paladin, Redoubt (C-P1)** | **57.4%** | **1.2%** | **270 (−11%)** | **35.9** |
| Paladin, C-P1 with Redoubt 4–20% | 54.8% | 1.8% | 282 (−7%) | 39.7 |
| Paladin, Redoubt 4–20% without C-P1 | 42.7% | 10.3% | 305 (+1%) | 44.6 |
| Warrior | 52.6% | 1.3% | 282 | 36 |
| Druid | 0% | 15.0% | 337 | 35.3 |

- **The crushing blows do not change much with the set.** C-P1 gives 1.2% (Warrior: 1.3%).
- **The Paladin TMI decreases:** 35.9 with C-P1 (threat set: 40.8). The Warrior goes from 38 to 36.
- **With C-P1, the Paladin takes 4% less damage than the Warrior** (270 against 282 each sec; live: 7% more).
- **Fast bosses and bosses with two weapons** give the same result as the table below. C-P1 is between 0.4 points below and 0.5 points above the Warrior. With 4–20%, the Paladin is between 0.1 points below and 0.5 points above.

**Fast bosses and bosses with two weapons.** The same tanks and 3 min fight. "Fast" is a swing each 1.2 sec with 60% damage, thus the same damage each sec. "Two weapons" adds a second weapon. The Paladin uses the wowsims default tank build (12/32/7), with Toughness removal (C-P13) in the C-P1 columns.

| Boss | Warrior | Paladin, C-P1 | Paladin, C-P1 with 4–20% | Paladin, live |
| --- | --- | --- | --- | --- |
| Normal (2.0 sec) | 1.4% | 1.2% | 3.1% | 10.2% |
| Fast (1.2 sec) | 3.8% | 3.4% | 4.7% | 9.0% |
| Two weapons | 4.7% | 4.8% | 5.8% | 9.0% |
| Fast, two weapons | 8.2% | 8.6% | 9.0% | 10.4% |

| Boss | Damage taken each sec: Warrior | Paladin, C-P1 | Paladin, C-P1 with 4–20% | Paladin, live |
| --- | --- | --- | --- | --- |
| Normal | 296 | 286 | 305 | 317 |
| Fast | 283 | 268 | 283 | 285 |
| Two weapons | 440 | 434 | 454 | 450 |
| Fast, two weapons | 435 | 422 | 436 | 426 |

- **More swings use the charges faster.** Both tanks then have gaps. The Warrior reaches 3.8–8.2% crushing blows, the Paladin with C-P1 3.4–8.6%.
- **C-P1 follows the Warrior.** It is between 0.4 points below and 0.4 points above the Warrior with each boss. Its damage taken is 1–5% below the damage taken of the Warrior threat set of 15 November with each boss.
- **4–20% is worse with each boss.** On a normal boss, it gives 3.1% (C-P1: 1.2%). Against fast bosses and bosses with two weapons, it is 0.4–1.3 points above C-P1, and 0.8–1.1 points above the Warrior.
- **Against fast bosses with two weapons,** C-P1 gives a smaller gain: 10.4% → 8.6%. The charges are empty too soon. The Warrior has 8.2%.

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
- **The 1.2% in wowsims comes from short gaps.** For example, Holy Shield comes late, or Redoubt has no blocks left. Fast bosses and bosses with two weapons use the charges faster.
- **With Holy Shield only,** the total is 70.7% + Agility ÷ 20. Then up to 15% of the swings are crushing blows.
- **With Redoubt at 4–20%,** the total is 90.7% + Agility ÷ 20. With 100 Agility, about 4.3% of the swings are crushing blows. wowsims gives 3.1% (part 3). On 9 November, with the Argent Defender error, it gave 1.2%.

## 5. Paladin against Warrior

Both tanks have 440 Defense and 100 Agility. The boss swings each 2 sec. Shield Block (Wowhead tooltip): "Increases chance to block by 75% for 7 sec, but will only block 2 attacks", 10 rage, 5 sec cooldown.

| Tank | Swings that the buffs cover | Crushing blow chance on the other swings | Crushing blows in total |
| --- | --- | --- | --- |
| Warrior | About 80% (2 of 2.5 swings each 5 sec) | 15% | About 3% |
| Paladin with C-P1 | About 100% | 0% at 440 Defense | Only in gaps |

- wowsims gives the Warrior 1.4% and the Paladin 1.2%. Thus, the two tanks are almost equal for crushing blows.
- The Warrior gaps depend on the swing speed of the boss. The Paladin gaps depend on when Holy Shield is cast. With fast bosses or two weapons, both tanks have more gaps (part 3).

## 6. Method and limits

- **Sim.** wowsims Forever, master commit 6084403a9 (hotfixes of 15 November, with the ranged judgements in wowsims itself), with the proposals as flags (`models/wowsims-b2`). The item pool tank set of each class (`models/wowsims-b2/tank_gear`), tank consumables, full buffs, one level 63 boss, 3,000 iterations, 3 min. Logs: `logs/checks_6084403a9_pool.log` and `logs/checks_6084403a9_pool_surv.log`. The runs of 13 November (8c7b5a5f5, with `patches/judgement-ranged.patch`): `logs/checks_8c7b5a5f5_pool.log` and `logs/checks_8c7b5a5f5_pool_surv.log`. The runs of 12 November, evening (129fcd89e): `logs/checks_129fcd89e_pool.log` and `logs/checks_129fcd89e_pool_surv.log`.

  The runs of 12 November (52471a100): `logs/checks_52471a100_pool.log` and `logs/checks_52471a100_pool_surv.log`. The runs of 11 November: `logs/checks_3633d376a_pool.log` and `logs/checks_3633d376a_pool_surv.log`. The runs of 9 November (with the Argent Defender error): `logs/checks_9f254e8d8_pool.log` and `logs/checks_9f254e8d8_pool_surv.log`. The runs of 8 November: `logs/checks_ae9b8c23a_pool.log` and `logs/checks_ae9b8c23a_pool_surv.log`. The runs of 4 and 6 November (set without Argent Defender): `logs/checks_9a8624af9_pool.log`, `logs/checks_9a8624af9_pool_surv.log` and `logs/checks_df57e2571_pool.log`.
- **Gear.** The item pool tank sets are pre-raid sets. They do not reach 440 Defense. Thus, the boss still has 0.2% critical hits on the Paladin with C-P1.
- **Boss.** The main tables use a boss with one weapon and a 2 sec swing. Part 3 also gives fast bosses and bosses with two weapons (`FEEDBACK_BOSS` in `models/wowsims-b2`).
- **Talents.** The values use the live talents. A change to Holy Shield or Redoubt changes all values.
