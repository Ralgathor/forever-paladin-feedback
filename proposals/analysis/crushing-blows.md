# Crushing blows

**Question.** Why does the Paladin tank take crushing blows, and how does Redoubt (C-P1) stop them?

## Short answer

- **The problem.** In the live version, a raid boss hits the Paladin with a crushing blow on 11.9% of its swings. A crushing blow does 150% damage. The Warrior takes crushing blows on only 1.0% of the swings.
- **The fix.** With Redoubt (C-P1), each Holy Shield cast also starts Redoubt. The two block buffs are then active together. Crushing blows decrease to 1.0%, the same as the Warrior.
- **The tank takes 13% less damage** with C-P1, and its TMI is better than the Warrior TMI.
- **Keep Redoubt at 6–30% block.** At 4–20%, 4.9% of the swings are still crushing blows.

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

Default tank gear of each class, full buffs, one level 63 boss, 3 min fight.

| Tank | Block | Crushing blows | Damage taken each sec | TMI |
| --- | --- | --- | --- | --- |
| Paladin, live | 42.3% | 11.9% | 333 | 57.1 |
| **Paladin, Redoubt (C-P1)** | **61.6%** | **1.0%** | **288 (−13%)** | **44.0** |
| Paladin, C-P1 with Redoubt 4–20% | 55.3% | 4.9% | 313 (−6%) | 52.8 |
| Paladin, Redoubt 4–20% without C-P1 | 40.8% | 12.9% | 340 (+2%) | 58.7 |
| Warrior | 49.2% | 1.0% | 281 | 47 |
| Druid | 0% | 15.0% | 379 | 39.7 |

- **C-P1 puts the Paladin at the Warrior level.** Both have 1.0% crushing blows. The Paladin takes 2% more damage than the Warrior, but its TMI is better.
- **5 min fights give the same result.** Live 11.9%, C-P1 1.1%, C-P1 with 4–20% 5.1%, Warrior 1.0%.
- **The Druid takes the most crushing blows,** but its armor and health keep it safe.

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
- **With Redoubt at 4–20%,** the total is 90.7% + Agility ÷ 20. With 100 Agility, about 4.3% of the swings are crushing blows. wowsims gives 4.9%.

## 5. Paladin against Warrior

Both tanks have 440 Defense and 100 Agility. The boss swings each 2 sec. Shield Block (Wowhead tooltip): "Increases chance to block by 75% for 7 sec, but will only block 2 attacks", 10 rage, 5 sec cooldown.

| Tank | Swings that the buffs cover | Crushing blow chance on the other swings | Crushing blows in total |
| --- | --- | --- | --- |
| Warrior | About 80% (2 of 2.5 swings each 5 sec) | 15% | About 3% |
| Paladin with C-P1 | About 100% | 0% at 440 Defense | Only in gaps |

- wowsims gives both tanks 1.0%. Thus, the two tanks are equal.
- The Warrior gaps depend on the swing speed of the boss. The Paladin gaps depend on when Holy Shield is cast.

## 6. Method and limits

- **Sim.** wowsims Forever with the proposals as flags (`models/wowsims-b2`). The default tank gear of each class, full buffs, one level 63 boss, 3,000 iterations, 3 min.
- **Gear.** The wowsims tank sets are pre-raid sets. They do not reach 440 Defense. Thus, the Paladin with C-P1 still has 0.2% critical hits.
- **One weapon.** The sims use a boss with one weapon. A boss with two weapons uses the charges faster.
- **Talents.** The values use the live talents. A change to Holy Shield or Redoubt changes all values.
