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
- **Holy Priest** gets Twin Disciplines (row 1), Mental Strength (row 2) and Meditation (row 3) from Discipline.

## Rule 1: rows 1 and 2 give something to the other specs

This table uses the proposed trees with M8 and C8 (calculator version 4).

| Tree | Rows 1–2 | Retribution gets | Protection gets | Holy gets |
| --- | --- | --- | --- | --- |
| Holy | Improved Seals, Unyielding Faith, Divine Intellect · Infusion of Light, Reverence, Spiritual Focus | Seal damage, −30% Fear, regeneration while casting, a fast Holy Light (7–10 points) | Seal damage, −30% Fear, regeneration (8 points) | — |
| Retribution | Deflection, Conviction · Improved Judgement, Holy Conduit, Vindication | — | Parry, critical hit, Judgement −2 sec, cheaper Consecration, a debuff on the boss (5–10 points) | +5% critical heal chance (5 points) |
| Protection | Benediction, Redoubt · Precision, Guardian's Favor, Anticipation | Instant spells −10%, +3% hit (8 points) | — | Instant spells −10%: Holy Shock, Cleanse. Guardian's Favor: saves, and Lay on Hands drains only 50% of the mana (C22) (7 points). Redoubt for PvP |

**Protection for Holy is a mana and saves dip.** Benediction makes Holy Shock and Cleanse 10% cheaper. Guardian's Favor gives more saves: Blessing of Protection each 3 min, Blessing of Freedom +6 sec, and a Lay on Hands that drains only 50% of the mana (C22). Thus, Holy healers in raids also take it. Redoubt gives Holy only a small defense in PvP. Other classes also use a defensive tree for PvP: Iron Will (Warrior), Frost Warding (Mage), Deflection (Hunter).

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
| With M8 and C8 | Conviction 5 | Benediction 5 + Guardian's Favor 2 = 7 | 12 points: fits, with 4 more points (35/11/5 with Redoubt 4) |

Without M8, Holy must choose between +5% critical heal chance and Guardian's Favor. Thus, M8 is necessary for rule 1.

## Rule 2: row 3 is an investment

| Tree | Row 3 | Who puts 10 points or more |
| --- | --- | --- |
| Holy | Voice of Truth (1-point signature), Purifying Power | Retribution: Exorcism and Holy Wrath cooldowns. Holy Shock builds: the 20 points for row 5 (Holy Shock, Consecrated Ground). All specs in PvP: Voice of Truth |
| Protection | Swift Judgement (1-point signature), Improved Hammer of Justice, Shield Specialization, Sacred Duty | All specs in PvP: Hammer of Justice each 45 sec, Divine Shield −60 sec. Retribution: a Judgement reset |
| Retribution | Seal of Command (1-point signature), Sanctified Judgement, Pursuit of Justice | Holy: Pursuit of Justice. Protection: Sanctified Judgement (mana) |

Each row 3 has a 1-point signature talent, as in the other classes. Each also has a reason for another spec to invest. The strong PvP dips are on the watch list (W1, W2, W9).

## Rule 3: parity with other classes

| Paladin talent | Comparable talents | Result |
| --- | --- | --- |
| Divine Intellect (+10% Intellect, row 1) | Ancestral Knowledge (row 1), Mental Strength (row 2) | Equal |
| Deflection (+5% parry, row 1) | Deflection (Warrior, Hunter, row 1) | Equal |
| Conviction (+5% critical hit, row 1 with M8) | Cruelty, Malice, Lethal Attacks, Thundering Strikes (all row 1) | Equal with M8. In the beta, it is one row deeper |
| Benediction (instant spells −10%, 5 points, Protection row 1 with C8) | Convection (−10%, 5 points, row 1), Cataclysm (−10%, 3 points) | Equal: more spells, but Paladin instant spells cost less |
| Precision (+3% hit, Protection row 2) | Elemental Precision, Shadow Focus, Arcane Focus (row 1), Precision (Rogue, row 2) | Equal |
| Anticipation (+20 Defense, row 2) | Anticipation (Warrior, row 2) | Equal |
| Reverence (50%, row 2, C1) | Mindfulness (row 2), Meditation and Reflection (row 3) | Equal |
| Improved Seals (+15% Seals and Judgements, 3 points, row 1) | Concussion (+5%), Improved Eviscerate (+20%) | Parity. Strong for each point, but the beta value |
| Unyielding Faith (−30% Fear and Disorient, 2 points, Holy row 1 with C8) | Iron Will (−15% stun and fear, 5 points, Warrior row 1), Silent Resolve (−15%, 3 points) | Stronger. Resistance to fear is a Paladin strength. If PvP shows a problem: −10/20% |
| Holy Conduit (−40% on 4 spells, 2 points, Retribution row 2) | Moonglow (−25%, 3 points, row 2), Cataclysm (−10%, 3 points) | Stronger for each point, but on few spells (W4) |
| Vindication (+5% Attack Power, 5 points, Retribution row 2 with C8) | Demoralizing Shout, Demoralizing Roar (baseline Attack Power debuffs) | Equal. The stack with these debuffs is not known (Open questions) |
| Improved Judgement (−2 sec, 2 points) | Improved Mind Blast (−2.5 sec, 5 points), Reverberation (−1 sec, 5 points) | Stronger for each point. It is the Classic value |
| Guardian's Favor (Protection row 2), Sacred Duty, Improved Hammer of Justice | Endurance, Elusiveness, Brutal Impact (row 2). Frost Warding, Earth's Grasp (row 1 utility) | Stronger on saves |
| Two-Handed Weapon Specialization (+6%, row 4 with M6) | Two-Handed Weapon Specialization (Warrior, +3%, row 4) | Stronger, intentional. Retribution is the two-handed spec of the class. The 3% difference gives Retribution about +10 DPS (+3%). See Analysis, Damage, part 8 |

## Paladin strengths

These talents are stronger than, or different from, the talents of other classes. This is intentional:

- A fast emergency heal for hybrids (Infusion of Light, C3).
- More saves (Guardian's Favor, Sacred Duty).
- Resistance to fear (Unyielding Faith).
- Seal and Judgement damage as a dip from Holy (Improved Seals).
- Two-handed weapon damage (Two-Handed Weapon Specialization 6%, Warrior 3%). It also increases Seal and Judgement damage. Retribution judges with a two-handed weapon and Seals (design rule 5). The Warrior has other damage multipliers: Impale, Weaponmaster, Deep Wounds and Death Wish.

**Points in each tree.** Beta: Holy 46, Protection 48, Retribution 44. Proposed: Holy 43, Protection 47, Retribution 41 (total 131).

**Other classes (wowforevertalents.com, build 70450).** Warrior 47/53/50, Druid 46/51/51, Priest 51/48/49, Shaman 46/51/51, Hunter 44/57/52, Mage 49/46/53. Their totals are 148–153. The smallest tree is Beast Mastery (44). The Paladin is the smallest class in the beta too (138). Each build in Analysis, Builds still has useful talents for all 51 points.

**Row 1 of the other classes.** Each row 1 has 10 points or more. 15 of 18 rows have two 5-point talents. Fire (Mage) has 5 + 3 + 2, the same as Holy with C8. Row 2 has 7–10 points (Balance 7, Fire 10).
