# Crushing blows

Values on the beta of 30 October 2026. Redoubt gives 6–30% block (5 ranks). Holy Shield gives +30% block with 4 charges for 10 sec, in row 5.

## Summary

- The beta Paladin takes a crushing blow on 11.9% of the boss attacks. The Warrior takes 1.0%.
- With Redoubt (C-P1), Holy Shield also starts Redoubt. Then crushing blows decrease to 1.0%, the same as the Warrior.
- Keep Redoubt at 6–30%. At 4–20% with the trigger, 4.9% of the attacks are still crushing blows.

## 1. wowsims results

wowsims Forever with the proposals as flags (models/wowsims-b2). The default tank set of each class, full buffs, a level 63 boss, 3,000 iterations, 3 min.

| Case | Block | Crushing blows | Damage taken each sec | TMI |
| --- | --- | --- | --- | --- |
| Paladin, beta | 42.3% | 11.9% | 333 | 57.1 |
| Paladin, Redoubt (C-P1) | 61.6% | 1.0% | 288 (−13%) | 44.0 |
| Paladin, C-P1 with Redoubt 4–20% | 55.3% | 4.9% | 313 (−6%) | 52.8 |
| Paladin, Redoubt 4–20% without C-P1 | 40.8% | 12.9% | 340 (+2%) | 58.7 |
| Warrior | 49.2% | 1.0% | 281 | 47 |
| Druid | 0% | 15.0% | 379 | 39.7 |

- **5 min fights.** The results are almost the same. Beta: 11.9% crushing blows. C-P1: 1.1%. C-P1 with 4–20%: 5.1%. Warrior: 1.0%.
- **Damage taken.** With Redoubt (C-P1), the Paladin takes 2% more damage than the Warrior and has a better TMI.
- **The Druid.** The Druid takes the most crushing blows. Armor and health make the Druid safe (see part 2).

## 2. The problem

- A raid boss is 3 levels above the player.
- With Classic rules, the boss has a 15% chance to hit with a crushing blow (150% damage).
- Crushing blows stop only when miss + dodge + parry + block = 100% against the boss.
- A tank can remove crushing blows from the attack table (Warrior). Or the tank can survive them with armor and health (Druid).

| Tank | How the tank handles crushing blows | Result |
| --- | --- | --- |
| Warrior | Shield Block: +75% block, 2 blocks, 7 sec, 5 sec cooldown. Shield Specialization: +5% block | Removes crushing blows with average gear. Some crushing blows come after the 2 blocks |
| Druid | No shield. Thick Hide armor increases with Defense. Bear Form gives up to +20% Stamina | Crushing blows always occur. The Druid has the armor and health to survive them |
| Paladin (beta) | Holy Shield: +30% block, 4 charges, 10 sec, 10 sec cooldown. Redoubt: +30% block, but only 10% of melee hits start it | Crushing blows occur, as for the Druid, but without the Druid armor and health |

Redoubt (C-P1) uses the Warrior method: it removes crushing blows with block. The Protection tree already gives block.

## 3. How Redoubt (C-P1) fixes the problem

- **Redoubt in the beta** gives +6–30% block for 10 sec or 5 blocks. Only 10% of melee hits start it. Thus, it is not active for most of the fight.
- **With Redoubt (C-P1),** each Holy Shield cast (each 10 sec) starts Redoubt again. Thus, the two buffs are active together.
- **The charges are sufficient.** In wowsims, the boss swings each 2.3 sec, thus about 4.4 times in 10 sec. With 61.6% block, about 2.7 of these swings are blocked. Redoubt has 5 blocks and Holy Shield has 4 charges.
- **First hit.** Cast Holy Shield before the pull. Then it covers the first swing of the boss.
- **Holy Shield stays at +30%.** With the Redoubt trigger, +30% already gives the same result as the Warrior.

## 4. Stat targets

Against a level 63 boss (attack skill 315), with Classic rules.

- **No critical hits: 440 Defense.** The boss has 5.6% critical hit chance against a level 60 player. Each Defense point removes 0.04%. Anticipation 5/5 gives 20 Defense. Thus, gear and enchants must give +120 Defense.
- **No crushing blows: miss + dodge + parry + block = 100%.** At 440 Defense, each of these increases by 5%.

With Deflection 5/5, Holy Shield and Redoubt 5/5 active:

| Roll | Sources | Against the boss |
| --- | --- | --- |
| Miss | 5% base + 5% Defense | 10% |
| Dodge | About 0.7% base + 5% Defense + Agility ÷ 20 | 5.7% + Agility ÷ 20 |
| Parry | 5% base + 5% Deflection + 5% Defense | 15% |
| Block | 5% base + 5% Defense + 30% Holy Shield + 30% Redoubt | 70% |
| Total |  | 100.7% + Agility ÷ 20 |

- **No difference after the critical hit cap.** At 440 Defense, the two buffs remove all crushing blows from the table.
- **The 1.0% in wowsims comes from gaps.** A late Holy Shield or Redoubt with no blocks left gives a short gap. Fast bosses or bosses with two weapons can use all charges early.
- **Without Redoubt.** With Holy Shield only, the total is 70.7% + Agility ÷ 20. Then 15% of the swings can be crushing blows. Thus, Holy Shield alone does not fix the problem.
- **With Redoubt at 4–20%.** The total is 90.7% + Agility ÷ 20. With about 100 Agility, about 4.3% of the swings can be crushing blows. wowsims shows 4.9%.

## 5. Comparison with the Warrior

Both tanks have 440 Defense and about 100 Agility. The boss swings each 2 sec. Shield Block tooltip on Wowhead: "Increases chance to block by 75% for 7 sec, but will only block 2 attacks", 10 Rage, 5 sec cooldown.

|  | Swings covered | Crushing blow chance on other swings | Swings that can be crushing blows |
| --- | --- | --- | --- |
| Warrior | About 80% (2 of 2.5 swings each 5 sec) | 15% | About 3% |
| Paladin with Redoubt (C-P1) | About 100% | 0% at 440 Defense | Only in gaps |

- wowsims gives both tanks 1.0% crushing blows. Thus, the two tanks are equal.
- The Warrior gaps change with the swing speed of the boss. The Paladin gaps change with the cast time of Holy Shield.

## 6. Limits

- The wowsims tank sets are pre-raid sets. They do not reach 440 Defense (Paladin: 0.2% critical hits with C-P1).
- The sims use one boss with one weapon. Bosses with two weapons use the charges faster.
- The values use the beta talents of 30 October. A change to Holy Shield or Redoubt changes all values.
