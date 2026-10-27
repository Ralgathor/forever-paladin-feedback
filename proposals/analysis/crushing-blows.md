# Crushing blows

## The problem

- A raid boss is 3 levels above the player.
- With Classic rules, the boss has a 15% chance to hit with a crushing blow (150% damage).
- Crushing blows stop only when miss + dodge + parry + block = 100% against the boss (about 102.4% on the character sheet).
- A tank can remove crushing blows from the attack table (Warrior). Or the tank can survive them with armor and health (Druid).

| Tank | How the tank handles crushing blows | Result |
| --- | --- | --- |
| Warrior | Shield Block: +75% block, 2 blocks, 7 sec, 5 sec cooldown. Shield Specialization: +5% block | Removes crushing blows with average gear. But some crushing blows come after the 2 blocks |
| Druid | No shield. Thick Hide armor increases with Defense. Bear Form gives up to +20% Stamina | Crushing blows always occur. The Druid has the armor and health to survive them |
| Paladin (beta) | Holy Shield: +30% block, 4 charges, 10 sec, 10 sec cooldown. Redoubt is a 10% proc | Needs about 72% avoidance from gear. Crushing blows occur, as for the Druid, but without the Druid armor and health |

Redoubt (C-P1) uses the Warrior method: it removes crushing blows with block. The Protection tree already gives block.

## How C-P1 fixes the problem

- **Redoubt in the beta** gives +4–20% block for 10 sec or 5 blocks. Only 10% of melee hits start it. Thus, it is active about half of the time.
- **With Redoubt (C-P1),** each Holy Shield cast (each 10 sec) starts Redoubt again. Thus, the two buffs are always active together.
- **The charges are sufficient.** A boss that swings each 2 sec swings 5 times in 10 sec. About 3 of these swings are blocked. Redoubt has 5 blocks and Holy Shield has 4 charges.
- **First hit.** Cast Holy Shield before the pull. Then it covers the first swing of the boss.
- **Holy Shield stays at +30%.** With the Redoubt trigger, +30% already gives the same result as the Warrior.

## Stat targets

Against a level 63 boss (attack skill 315), with Classic rules.

- **No critical hits: 440 Defense.** The boss has 5.6% critical hit chance against a level 60 player. Each Defense point removes 0.04%. Anticipation gives 20 Defense. Thus, gear and enchants must give +120 Defense.
- **No crushing blows: miss + dodge + parry + block = 100%.** At 440 Defense, each of these increases by 5%.

With Deflection 5/5, Holy Shield and Redoubt active:

| Roll | Sources | Against the boss |
| --- | --- | --- |
| Miss | 5% base + 5% Defense | 10% |
| Dodge | About 0.7% base + 5% Defense + Agility ÷ 20 | 5.7% + Agility ÷ 20 |
| Parry | 5% base + 5% Deflection + 5% Defense | 15% |
| Block | 5% base + 5% Defense + 30% Holy Shield + 20% Redoubt | 60% |
| Total |  | 90.7% + Agility ÷ 20 |

- **Difference after the critical hit cap: 9.3%.** This is about 186 Agility or 58 Defense above 440. Until the tank closes this difference, this difference is the crushing blow chance. With about 100 Agility, about 4.3% of the swings can be crushing blows. This is close to a Warrior between Shield Blocks.
- **Holy Shield is the full mechanism.** Without it, crushing blows occur at the full rate.
- **Gaps.** A late Holy Shield gives a short gap. Fast bosses or bosses with two weapons can use all charges early.

## Comparison with the Warrior

Both tanks have 440 Defense and about 100 Agility. The boss swings each 2 sec. Shield Block tooltip on Wowhead: "Increases chance to block by 75% for 7 sec, but will only block 2 attacks", 10 Rage, 5 sec cooldown.

|  | Swings covered | Crushing blow chance on other swings | Swings that can be crushing blows |
| --- | --- | --- | --- |
| Warrior | About 80% (2 of 2.5 swings each 5 sec) | 15% | About 3% |
| Paladin with Redoubt (C-P1) | About 100% | About 4.3% | About 4.3% |

The two tanks are equal. Gear closes the Paladin gap. The Warrior gaps change with the swing speed of the boss.
