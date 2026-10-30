# Tree balance

Three rules:

1. Rows 1 and 2 must give something to the other specs.
2. Row 3 is an investment choice. Another spec puts 10 points or more in the tree for it.
3. Talents must be in parity with the talents of other classes, not equal. A Paladin talent can be stronger when this is a strength of the class.

The comparison uses rows 1–3 of the 24 trees of the other classes (build 70450). The sources do not give the columns of the other classes.

## How the other classes use rows 1–3

| Row | Usual content | Examples |
| --- | --- | --- |
| 1 | A main stat, or +5% critical hit or hit, for all specs of the class | Cruelty, Malice, Lethal Attacks, Thundering Strikes (+5% critical hit). Elemental Precision, Shadow Focus, Suppression (+5% hit). Ancestral Knowledge, Heart of the Wild (+10% stat). Deflection (parry) |
| 2 | Efficiency, utility, more stats. Sometimes the healer mana talent | Precision (Rogue), Mental Strength (Priest), Mindfulness (Shaman), Nature's Majesty (+4% critical hit), Anticipation (Warrior), Elusiveness (Rogue) |
| 3 | A 1-point signature talent, and investment talents | Anger Management, Last Stand, Riposte, Pyroblast, Ice Lance, Inner Focus, Holy Nova, Water Shield, Feral Charge. Healer mana: Meditation, Reflection |

Healer dips of other classes:

- **Restoration Shaman** puts 10 points in Enhancement row 1: Ancestral Knowledge (+10% Intellect) and Thundering Strikes (+5% critical hit).
- **Restoration Druid** puts 5 points in Feral row 1: Heart of the Wild.
- **Holy Priest** receives Twin Disciplines (row 1), Mental Strength (row 2) and Meditation (row 3) from Discipline.

## Rule 1: rows 1 and 2 give something to the other specs

This table uses the proposed trees with Conviction (M-R2) and Toughness and Divine Strength removal (C-P3), in calculator version 5.

| Tree | Rows 1–2 | Retribution receives | Protection receives | Holy receives |
| --- | --- | --- | --- | --- |
| Holy | Improved Seals, Unyielding Faith, Divine Intellect · Infusion of Light, Reverence, Spiritual Focus | Seal damage, −30% Fear, regeneration during casts, a fast Holy Light (7–10 points) | Seal damage, −30% Fear, regeneration (8 points) | — |
| Retribution | Deflection, Conviction · Improved Judgement, Holy Conduit, Vindication | — | Parry, critical hit, Judgement −2 sec, cheaper Consecration, a debuff on the boss (5–10 points) | +5% critical heal chance (5 points) |
| Protection | Benediction, Redoubt · Precision, Guardian's Favor, Anticipation | Instant spells −10%, +3% hit (8 points) | — | Instant spells −10%: Holy Shock, Cleanse. Guardian's Favor: saves (7 points). Redoubt for PvP, and to open row 3 |

**Protection for Holy is a mana and saves dip.** Benediction makes Holy Shock and Cleanse 10% cheaper. Guardian's Favor gives more saves: Hand of Protection each 3 min and Hand of Freedom +6 sec. With Redoubt 3, Holy opens row 3 and takes Devoted Sacrifice (C-P11): Lay on Hands drains only 50% of the mana. Thus, Holy healers in raids also take 12 Protection points. Redoubt gives Holy only a small defense in PvP. Other classes also use a defensive tree for PvP: Iron Will (Warrior), Frost Warding (Mage), Deflection (Hunter).

Redoubt in PvP (block value 44, from the gear profile):

| Attacker | Redoubt active | More blocks | Melee damage removed |
| --- | --- | --- | --- |
| Rogue with two weapons, from the front | About 77% of the time | About 15% of the hits | About 2% |
| Rogue from behind | — | None: you cannot block from behind | 0% |
| Warrior with a two-handed weapon | About 34% of the time | About 7% of the hits | About 0.5% |

**The points must fit in a Holy build.** A Holy healer uses about 35 Holy points. Thus, 16 points are free.

| Build | Retribution | Protection | Result |
| --- | --- | --- | --- |
| Beta layout | Benediction 5 + Conviction 5 = 10 | Redoubt 5 + Guardian's Favor 2 = 7 | 17 points: does not fit |
| With Conviction (M-R2) and Toughness and Divine Strength removal (C-P3) | Conviction 5 | Benediction 5 + Guardian's Favor 2 = 7 | 12 points: fits, with 4 more points (35/11/5 with Redoubt 4) |
| With Devoted Sacrifice (C-P11) | Conviction 5 | Benediction 5 + Guardian's Favor 2 + Redoubt 3 + Devoted Sacrifice 2 = 12 | 17 points: fits with 34 Holy points (HB1, 34/12/5) |

Without Conviction (M-R2), Holy must choose between +5% critical heal chance and Guardian's Favor. Thus, Conviction (M-R2) is necessary for rule 1.

## Rule 2: row 3 is an investment

| Tree | Row 3 | Who puts 10 points or more |
| --- | --- | --- |
| Holy | Voice of Truth (1-point signature), Purifying Power, Lingering Light (C-H2) | Retribution: Exorcism and Holy Wrath cooldowns. Holy Shock builds: the 20 points for row 5 (Holy Shock, Holy Power). All specs in PvP: Voice of Truth |
| Protection | Shoulder the Burden (1-point signature, C-P5), Devoted Sacrifice (C-P11), Shield Specialization, Sacred Duty | Holy healers: Lay on Hands drains only 50% (12 points). All specs in PvP: Divine Shield −60 sec, and the way to Hammer of Justice each 45 sec and Swift Judgement in row 4 |
| Retribution | Seal of Command (1-point signature), Sanctified Judgement, Pursuit of Justice | Holy: Pursuit of Justice. Protection: Sanctified Judgement (mana) |

Each row 3 has a 1-point signature talent, as in the other classes. Each also has a reason for another spec to invest. The strong PvP dips are on the watch list (W1, W2, W9).

## Rule 3: parity with other classes

| Paladin talent | Comparable talents | Result |
| --- | --- | --- |
| Divine Intellect (+10% Intellect, row 1) | Ancestral Knowledge (row 1), Mental Strength (row 2) | Equal |
| Deflection (+5% parry, row 1) | Deflection (Warrior, Hunter, row 1) | Equal |
| Conviction (+5% critical hit, row 1 with the Conviction move, M-R2) | Cruelty, Malice, Lethal Attacks, Thundering Strikes (all row 1) | Equal with Conviction (M-R2). In the beta, it is one row deeper |
| Benediction (instant spells −10%, 5 points, Protection row 1 with the Benediction move, M-P1) | Convection (−10%, 5 points, row 1), Cataclysm (−10%, 3 points) | Equal: more spells, but Paladin instant spells cost less |
| Precision (+3% hit, Protection row 2) | Elemental Precision, Shadow Focus, Arcane Focus (row 1), Precision (Rogue, row 2) | Equal |
| Anticipation (+20 Defense, row 2) | Anticipation (Warrior, row 2) | Equal |
| Reverence (50%, row 2, C-H1) | Mindfulness (row 2), Meditation and Reflection (row 3) | Equal |
| Improved Seals (+15% Seals and Judgements, 3 points, row 1) | Concussion (+5%), Improved Eviscerate (+20%) | Parity. Strong for each point, but the beta value |
| Unyielding Faith (−30% Fear and Disorient, 2 points, Holy row 1 with the Unyielding Faith move, M-H2) | Iron Will (−15% stun and fear, 5 points, Warrior row 1), Silent Resolve (−15%, 3 points) | Stronger. Resistance to fear is a Paladin strength. If PvP shows a problem: −10/20% |
| Holy Conduit (−40% on 4 spells, 2 points, Retribution row 2) | Moonglow (−25%, 3 points, row 2), Cataclysm (−10%, 3 points) | Stronger for each point, but on few spells (W4) |
| Vindication (+6% Attack Power, 3 points, Retribution row 2 with Toughness and Divine Strength removal, C-P3) | Demoralizing Shout, Demoralizing Roar (baseline Attack Power debuffs) | Equal. The stack with these debuffs is not known (Open questions) |
| Improved Judgement (−2 sec, 2 points) | Improved Mind Blast (−2.5 sec, 5 points), Reverberation (−1 sec, 5 points) | Stronger for each point. It is the Classic value |
| Guardian's Favor (Protection row 2), Sacred Duty, Improved Hammer of Justice | Endurance, Elusiveness, Brutal Impact (row 2). Frost Warding, Earth's Grasp (row 1 utility) | Stronger on saves |
| Two-Handed Weapon Specialization (+6%, row 4 with the Two-Handed Weapon Specialization move, M-R1) | Two-Handed Weapon Specialization (Warrior, +3%, row 4) | Stronger, intentional. Retribution is the two-handed spec of the class. The 3% difference gives Retribution about +10 DPS (+3%). See Analysis, Damage, part 8 |

## Paladin strengths

These talents are stronger than, or different from, the talents of other classes. This is intentional:

- A fast emergency heal for hybrids (Infusion of Light, C-H3).
- More saves (Guardian's Favor, Sacred Duty).
- Resistance to fear (Unyielding Faith).
- Seal and Judgement damage as a dip from Holy (Improved Seals).
- Two-handed weapon damage (Two-Handed Weapon Specialization 6%, Warrior 3%). It also increases Seal and Judgement damage. Retribution judges with a two-handed weapon and Seals (design rule 5). The Warrior has other damage multipliers: Impale, Weaponmaster, Deep Wounds and Death Wish.

**Row 1 of the other classes.** Each row 1 has 10 points or more. 17 of the 24 trees have two 5-point talents in row 1. Fire, Frost (Mage) and the three Rogue trees have 5 + 3 + 2. The proposed Holy row 1 has the same (Toughness and Divine Strength removal, C-P3). Arms (Warrior) and Holy (Priest) have 5 + 3 + 3. Row 2 has 7–15 points (Affliction 7, Survival 15).

## Points in each tree

Source: the talent data of wowsims/forever (25 October 2026) for all nine classes. The proposed values use calculator version 5, with Merciful Light (C-H5), Divine Grace (C-H6), Burning Zeal (C-R4) and Measure for Measure (C-R5).

| Class | Tree 1 | Tree 2 | Tree 3 | Total | Talents |
| --- | --- | --- | --- | --- | --- |
| Warrior | Arms 47 | Fury 53 | Protection 50 | 150 | 52 |
| Druid | Balance 46 | Feral Combat 51 | Restoration 51 | 148 | 52 |
| Hunter | Beast Mastery 44 | Marksmanship 52 | Survival 52 | 148 | 50 |
| Priest | Discipline 51 | Holy 48 | Shadow 49 | 148 | 52 |
| Shaman | Elemental 46 | Enhancement 51 | Restoration 51 | 148 | 50 |
| Warlock | Affliction 46 | Demonology 50 | Destruction 50 | 146 | 52 |
| Mage | Arcane 49 | Fire 46 | Frost 48 | 143 | 54 |
| Rogue | Assassination 48 | Combat 44 | Subtlety 47 | 139 | 53 |
| **Paladin, beta** | Holy 46 | Protection 48 | Retribution 44 | **138** | 50 |
| **Paladin, proposed** | Holy 47 | Protection 49 | Retribution 47 | **143** | 54 |

- The other classes have 139–150 points (mean 146, or 48.75 for each tree). Their smallest trees are Beast Mastery and Combat (44).
- In the beta, the Paladin is the smallest class, 1 point below the Rogue. Retribution (44) is equal to Beast Mastery and Combat.
- With the proposals, the Paladin has 143 points: 4 points above the Rogue and 3 points below the mean. Holy (47) and Retribution (47) are in the range of the other trees. Without the four new talents of 29 October, Retribution (39) and Holy (43) are the two smallest of the 27 trees.
- wowforevertalents.com gives Frost 53 points. wowsims gives 48. The table uses the wowsims value.

**Cause: ranks, not talents.**

- The Paladin had 49–50 talents. The other classes have 50–54. Thus, the difference was in the ranks. With the four new talents, the Paladin has 54.
- Toughness and Divine Strength removal (C-P3) deletes Divine Strength (5) and Toughness (5). Improved Righteous Fury removal (C-P4) deletes its 3 ranks. Lingering Light, Reach of Law and Devoted Sacrifice (C-P11) add 6. Vindication keeps its 3 beta ranks (C-P3). Merciful Light (C-H5), Divine Grace (C-H6), Burning Zeal (C-R4) and Measure for Measure (C-R5) add 12 (Burning Zeal has 5 ranks). The net change is +5 (138 to 143).
- All tank builds skipped Toughness and Divine Strength (see Analysis, Builds, part 3).

**Thin rows.**

| Tree | Rows 1–7 | Rows 1–3 | Rows 4–6 |
| --- | --- | --- | --- |
| Holy, calculator version 4 | 10 / 7 / 3 / 6 / 8 / 8 / 1 | **20** (other trees: 23–35) | 22 |
| Holy, with Lingering Light (C-H2) in row 3, Holy Power (M-H3) and Consecrated Ground (M-H4) | 10 / 7 / 5 / 6 / 9 / 5 / 1 | 22 | 20 |
| Holy, with Merciful Light (C-H5), Divine Grace (C-H6) and Divine Precision in row 4 (M-H5) | 10 / 7 / 5 / 11 / 8 / 5 / 1 | 22 | 24 |
| Protection, proposed | 10 / 10 / 8 / 7 / 8 / 5 / 1 | 28 | 20 |
| Retribution, calculator version 5 | 10 / 9 / 6 / 6 / 4 / 5 / 1 | 25 | **15** (other trees: 15–25) |
| Retribution, with Burning Zeal (C-R4) and Measure for Measure (C-R5) | 10 / 9 / 6 / 6 / 9 / 5 / 1 | 25 | 20 |
| Retribution, calculator version 6 (Burning Zeal with 5 ranks in row 3, M-R4, M-R5, Vindication with 3 ranks) | 10 / 7 / 11 / 6 / 7 / 5 / 1 | 28 | 18 |
| Mean of the other 24 trees | — | 28.6 | 19.1 |

- In version 4, Holy row 3 has 3 points. Each other tree has 4 points or more in row 3. Holy rows 1–3 (20 points) are the lowest of the 27 trees.
- This causes 2 points of filler for the Holy healer. Row 4 needs 15 points in rows 1–3, and only 14 of these points help a healer. Row 6 needs 25 points in rows 1–5, and only 23 help a healer.
- **The fix: one new talent and two moves in Holy.** Lingering Light (C-H2) is a new talent in row 3. Holy Power goes to row 5 (M-H3). Consecrated Ground goes to row 6 (M-H4). Rows 1–3 then hold 16 healer points, and rows 1–5 hold 28. The Holy healer has no filler.
- After the moves, each Holy row is in the range of the other trees. Rows 1–3 (22) are 1 point below the lowest other tree.
- In calculator version 5, Retribution rows 4–6 (15 points) were equal to the lowest other tree (Discipline). A deep Retribution build took almost all of them. With Burning Zeal (C-R4) and Measure for Measure (C-R5), rows 4–6 have 20 points. In calculator version 6, Burning Zeal (5 ranks) goes to row 3, and Vindication has 3 ranks (C-P3): rows 1–3 have 28 points and rows 4–6 have 18. Both values are in the range of the other trees. A deep build chooses between Measure for Measure, Eye for an Eye and Repentance.

**What the smaller trees change.**

| Effect | Result |
| --- | --- |
| Choices in the main tree | In calculator version 5, a deep build left 8 points of Retribution, 11 points of Holy (healer: 32 points) and 14 points of Protection. With the four new talents, Holy healing needs 36 points. RB6 (38 Retribution points) leaves 9 points of Retribution |
| Forced filler | It comes from thin rows, not from the total. Holy healer: 2 points in version 4, none with the three moves. Main Protection and Retribution builds: none |
| Points for the other trees | Smaller trees free more points: up to 19 for Holy (HB1, 34/12/5, uses 17) and 18 for Retribution (RB1, 10/8/33). Rule 1 needs these dips |
| The 52-point hybrids | The tree size does not cause them. Holy Shock with Twist of Light or Holy Shield needs 52 of the 51 points |

**Result.** Do not add ranks to reach the totals of the other classes. New ranks become stat filler again, as Toughness and Divine Strength were (Toughness and Divine Strength removal, C-P3). Devoted Sacrifice (C-P11) adds 2 ranks to Protection, but for an effect, not for stats. The talent count is already in the range of the other classes. Holy rows were the one weak point. One new talent and two moves fix them: Lingering Light (C-H2) in row 3, Holy Power (M-H3) and Consecrated Ground (M-H4). These three changes keep all build codes valid. Shock-Retribution changes to 26/0/25 (see Builds, part 5).

**New talents of 29 October 2026.** Each new talent has an effect, not a stat. Merciful Light (C-H5) gives Holy the burst after a large hit. Divine Grace (C-H6) gives the tank armor after a large hit. Burning Zeal (C-R4) and Measure for Measure (C-R5) give Retribution new choices. In calculator version 6, Burning Zeal is in row 3 and Measure for Measure is in row 5. The new talents go at the end of the build code of each tree. Thus, all version 5 codes stay valid.
