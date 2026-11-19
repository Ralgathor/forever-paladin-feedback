# Crushing blows

**Question.** Why does the Paladin tank take crushing blows, and how does Redoubt (C-P1) stop them?

## Short answer

- **The problem.** In the live version, a raid boss hits the Paladin with a crushing blow on 10.3% of its swings (part 3). A crushing blow does 150% damage. The Warrior takes crushing blows on only 1.0% of the swings.
- **The fix.** With Redoubt (C-P1), each Holy Shield cast also starts Redoubt. The two block buffs are then active together. Crushing blows decrease to 1.1%, the Warrior level (1.0%).
- **The tank takes 11% less damage** with C-P1. The tanks have the item pool tank sets, the full threat consumables and the enchants (the same rules for all tanks). The Paladin then takes 15% less damage than the Warrior (248 against 291 each sec), but its TMI is a little higher (31.3 against 30). With the survival sets, the Paladin takes 16% less damage than the Warrior (199 against 237), but its TMI is a little higher (23.7 against 23).
- **Keep Redoubt at 6–30% block.** With the item pool set and the enchants of 18 November, 4–20% gives the same crushing blows and damage taken on a normal boss (1.1%, 253 each sec without Toughness). Fast bosses and bosses with two weapons give up to 1% more damage taken. Without the enchants, 4–20% gave 2% more damage taken on a normal boss.
- **Fast bosses and bosses with two weapons** give both tanks more crushing blows. With C-P1, the Paladin is 0.3–0.9 points below the Warrior. At 4–20%, it is 0.4–0.9 points below.

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

Item pool threat set of each class (Analysis, Threat, part 6), full threat consumables of 17 November, enchants of 18 November evening (Paladin weapon enchant and libram of 19 November), master ad6b13af8 (18 November), full buffs, one level 63 boss, 3 min fight. The Paladin has Holy Shield rank 4 (build 70755).

| Tank | Block | Crushing blows | Damage taken each sec | TMI |
| --- | --- | --- | --- | --- |
| Paladin, live | 42.5% | 10.3% | 278 | 38.5 |
| **Paladin, Redoubt (C-P1)** | **54.1%** | **1.1%** | **248 (−11%)** | **31.3** |
| Paladin, C-P1 with Redoubt 4–20% | 53.8% | 1.1% | 248 (−11%) | 31.3 |
| Paladin, Redoubt 4–20% without C-P1 | 42.4% | 10.2% | 278 (+0%) | 38.4 |
| Warrior | 57.9% | 1.0% | 291 | 30 |
| Druid | 0% | 14.9% | 328 | 25.3 |

- **Argent Defender (correction).** The item pool set has Argent Defender, a shield of the hotfixes of 7 and 8 November. From 8 to 10 November, wowsims applied its proc buff (+18% block) all the time, by error. The live block was then 55.0%, and the crushing blows 5.6%. wowsims master 3633d376a (11 November) fixes this error. Masters 52471a100 and 129fcd89e (12 November) do not change the Paladin values. On 11 and 12 November, the live block was 41.2%, and the crushing blows 12.0%.
- **Redoubt fix and new set (13 November).** Master 8c7b5a5f5 makes each melee swing or ability against the Paladin roll the 10% Redoubt chance, avoided attacks included. Thus, the live Redoubt is active more often. The new item pool set has Draconian Deflector in place of Argent Defender. The live block was then 44.0%, and the crushing blows 10.1%.
- **New commit (15 November).** Master 6084403a9 does not change the Paladin values: 44.0% block and 10.2% crushing blows with the set of 13 November.
- **Open search sets (16 November).** The new Paladin threat set has Soulforge Chestguards and the Warder's pieces. It has more dodge (18.5% against 15.5%) and takes 5% less damage (300 against 317). The live block is 43.1%, and the crushing blows 10.1%. The new Warrior threat set blocks 57.7% and takes 1.1% crushing blows.
- **Full threat consumables (17 November).** The Paladin now has spell power consumables, for example Flask of Supreme Power, and all tanks have the same consumable rules (Analysis, Threat, part 6). The live block is 42.7%, the crushing blows 10.2%, and the damage taken decreases by 1% (300 → 296). The Warrior damage taken does not change (294 → 293), but its TMI decreases (37 → 31).
- **New commit and new set (18 November).** On master ad6b13af8, the new Paladin threat set has Vigorsteel Vambraces, Warder's Gloves and Frozen Heart of the Mountain. The live block is 43.1%, and the crushing blows 10.0%. The Paladin takes 2% less damage (296 → 291), and its TMI decreases (46.4 → 43.5).
- **Enchants (18 November evening).** The three tanks have enchants with the same rules (Analysis, Threat, part 6). Before, the Paladin sets had no enchants. The live block is 42.9%, and the crushing blows 10.1%. The Paladin takes 5% less damage (291 → 278), and its TMI decreases (43.5 → 38.2). The Warrior takes 1% less damage (293 → 291).
- **Weapon enchant and libram (19 November).** The Paladin sets have Crusader in place of Revelation and Libram of Invocation in place of Libram of Holy Alacrity (Analysis, Threat, part 6). The live block is 42.5%, and the crushing blows 10.3%. The damage taken does not change (278), and the TMI goes from 38.2 to 38.5.
- **C-P1 puts the Paladin at the Warrior level for crushing blows:** 1.1% against 1.0%. The live Redoubt fix does not close this gap: the live Paladin still has 10.3%.
- **With C-P1, the Paladin takes 15% less damage than the Warrior** (248 against 291 each sec). Its TMI is a little higher (31.3 against 30). The live Paladin takes 5% less damage. The two tanks dodge almost the same (19.3% and 18.8%). The boss has 0.1% critical hits on the Paladin with C-P1.
- **Consumables are important.** Without consumables (Demonic Rune only, the runs before 4 November evening), the Paladin with C-P1 took 13% more damage than the Warrior (339 each sec, TMI 55.3), and the live Paladin 28% more.
- **5 min fights give the same result.** Live 10.2%, C-P1 1.2%, C-P1 with 4–20% 1.2%, Warrior 1.0%.
- **The Druid takes the most crushing blows,** but its armor and health keep it safe.

**Survival sets.** The same runs with the item pool survival set of each class (Analysis, Threat, part 6). All three tanks have Greater Stoneshield Potion.

| Tank | Block | Crushing blows | Damage taken each sec | TMI |
| --- | --- | --- | --- | --- |
| Paladin, live | 43.7% | 6.1% | 211 | 26.3 |
| **Paladin, Redoubt (C-P1)** | **49.1%** | **0.9%** | **199 (−6%)** | **23.7** |
| Paladin, C-P1 with Redoubt 4–20% | 48.9% | 1.0% | 199 (−6%) | 23.8 |
| Paladin, Redoubt 4–20% without C-P1 | 43.5% | 6.2% | 211 (+0%) | 26.4 |
| Warrior | 49.6% | 0.9% | 237 | 23 |
| Druid | 0% | 15.1% | 276 | 20.1 |

- **The crushing blows do not change much with the set.** C-P1 gives 0.9% (Warrior: 0.9%). The live Paladin has 6.1%, because the Deathbone Guardian set gives more Defense and more dodge (20.7% against 19.5%; 19 November, before: 8.6%).
- **The TMI decreases:** 23.7 for the Paladin with C-P1 (threat set: 31.3). The Warrior goes from 30 to 23.
- **With C-P1, the Paladin takes 16% less damage than the Warrior** (199 against 237 each sec; live: 11% less). Before 19 November, without Deathbone Guardian, it took 13% less. The Warrior survival set dodges more (25.5% against 20.6%), but the Paladin blocks more. Before 18 November evening, only the Druid had Greater Stoneshield Potion, and the Paladin with C-P1 took 2% more damage than the Warrior. With the first survival sets of 15 November, it took 4% less.
- **Fast bosses and bosses with two weapons.** C-P1 is 0.5 points below the Warrior. With 4–20%, the Paladin is between 0.3 points below and 0.4 points above.

**Fast bosses and bosses with two weapons.** The same tanks and 3 min fight. "Fast" is a swing each 1.2 sec with 60% damage, thus the same damage each sec. "Two weapons" adds a second weapon. The Paladin uses the wowsims default tank build (12/32/7), with Toughness removal (C-P13) in the C-P1 columns.

| Boss | Warrior | Paladin, C-P1 | Paladin, C-P1 with 4–20% | Paladin, live |
| --- | --- | --- | --- | --- |
| Normal (2.0 sec) | 1.0% | 1.1% | 1.1% | 10.3% |
| Fast (1.2 sec) | 3.8% | 2.9% | 2.9% | 8.8% |
| Two weapons | 4.7% | 4.1% | 4.0% | 8.6% |
| Fast, two weapons | 8.3% | 8.0% | 7.9% | 10.0% |

| Boss | Damage taken each sec: Warrior | Paladin, C-P1 | Paladin, C-P1 with 4–20% | Paladin, live |
| --- | --- | --- | --- | --- |
| Normal | 291 | 253 | 253 | 278 |
| Fast | 281 | 232 | 232 | 248 |
| Two weapons | 443 | 376 | 377 | 393 |
| Fast, two weapons | 444 | 365 | 367 | 369 |

- **More swings use the charges faster.** Both tanks then have gaps. The Warrior reaches 3.8–8.3% crushing blows, the Paladin with C-P1 2.9–8.0%.
- **C-P1 follows the Warrior.** It is between 0.1 points above and 0.9 points below the Warrior with each boss. Its damage taken is 13–18% below the damage taken of the Warrior threat set with each boss.
- **4–20% gives the same or a little more damage taken with each boss.** With the item pool set and the enchants of 18 November, it gives the same or 0.1 points fewer crushing blows than C-P1. The Paladin takes 0–1% more damage. Without the enchants, the boss had more critical hits with 4–20%, and the Paladin took 1–2% more damage. With the first set of 15 November, 4–20% gave 3.1% crushing blows on a normal boss (C-P1: 1.2%).
- **Against fast bosses with two weapons,** C-P1 gives a smaller gain: 10.0% → 8.0%. The charges are empty too soon. The Warrior has 8.3%.

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
- **The 1.1% in wowsims comes from short gaps.** For example, Holy Shield comes late, or Redoubt has no blocks left. Fast bosses and bosses with two weapons use the charges faster.
- **With Holy Shield only,** the total is 70.7% + Agility ÷ 20. Then up to 15% of the swings are crushing blows.
- **With Redoubt at 4–20%,** the total is 90.7% + Agility ÷ 20. With 100 Agility, about 4.3% of the swings are crushing blows. wowsims gives 1.1% with the item pool set of 18 November (part 3), because this set has more dodge. With the first set of 15 November, it gave 3.1%.

## 5. Paladin against Warrior

Both tanks have 440 Defense and 100 Agility. The boss swings each 2 sec. Shield Block (Wowhead tooltip): "Increases chance to block by 75% for 7 sec, but will only block 2 attacks", 10 rage, 5 sec cooldown.

| Tank | Swings that the buffs cover | Crushing blow chance on the other swings | Crushing blows in total |
| --- | --- | --- | --- |
| Warrior | About 80% (2 of 2.5 swings each 5 sec) | 15% | About 3% |
| Paladin with C-P1 | About 100% | 0% at 440 Defense | Only in gaps |

- wowsims gives the Warrior 1.0% and the Paladin 1.1%. Thus, the two tanks are equal for crushing blows.
- The Warrior gaps depend on the swing speed of the boss. The Paladin gaps depend on when Holy Shield is cast. With fast bosses or two weapons, both tanks have more gaps (part 3).

## 6. Method and limits

- **Sim.** wowsims Forever, master commit ad6b13af8 (hotfixes of 16 and 17 November), with the proposals as flags (`models/wowsims-b2`). The item pool tank set of each class (`models/wowsims-b2/tank_gear`), full threat consumables of 17 November, enchants of 18 November evening, full buffs, one level 63 boss, 3,000 iterations, 3 min. Logs: `logs/checks_ad6b13af8_pool_full.log` and `logs/checks_ad6b13af8_pool_surv_full.log`, with the tank sets of 18 November. The runs without enchants: `logs/checks_ad6b13af8_pool_full_no_enchants.log` and `logs/checks_ad6b13af8_pool_surv_full_no_enchants.log`. The runs of 17 November (6084403a9): `logs/checks_6084403a9_pool_full.log` and `logs/checks_6084403a9_pool_surv_full.log`. The runs with the consumables of 16 November: `logs/checks_6084403a9_pool.log` and `logs/checks_6084403a9_pool_surv.log`. The runs with the first sets of 15 November: `logs/checks_6084403a9_pool_6084403a9_first.log` and `logs/checks_6084403a9_pool_surv_6084403a9_first.log`. The runs of 13 November (8c7b5a5f5, with `patches/judgement-ranged.patch`): `logs/checks_8c7b5a5f5_pool.log` and `logs/checks_8c7b5a5f5_pool_surv.log`. The runs of 12 November, evening (129fcd89e): `logs/checks_129fcd89e_pool.log` and `logs/checks_129fcd89e_pool_surv.log`.

  The runs of 12 November (52471a100): `logs/checks_52471a100_pool.log` and `logs/checks_52471a100_pool_surv.log`. The runs of 11 November: `logs/checks_3633d376a_pool.log` and `logs/checks_3633d376a_pool_surv.log`. The runs of 9 November (with the Argent Defender error): `logs/checks_9f254e8d8_pool.log` and `logs/checks_9f254e8d8_pool_surv.log`. The runs of 8 November: `logs/checks_ae9b8c23a_pool.log` and `logs/checks_ae9b8c23a_pool_surv.log`. The runs of 4 and 6 November (set without Argent Defender): `logs/checks_9a8624af9_pool.log`, `logs/checks_9a8624af9_pool_surv.log` and `logs/checks_df57e2571_pool.log`.
- **Gear.** The item pool tank sets are pre-raid sets. They do not reach 440 Defense. Thus, the boss still has 0.1% critical hits on the Paladin with C-P1.
- **Boss.** The main tables use a boss with one weapon and a 2 sec swing. Part 3 also gives fast bosses and bosses with two weapons (`FEEDBACK_BOSS` in `models/wowsims-b2`).
- **Talents.** The values use the live talents. A change to Holy Shield or Redoubt changes all values.
