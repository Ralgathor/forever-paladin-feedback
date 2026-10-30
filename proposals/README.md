# Forever Paladin Talent Proposals

This document gives talent proposals for the WoW Forever Paladin. It has 26 changes and 11 moves. The proposals follow the rules that Forever uses for the other classes. Each proposal uses a talent from another class in the same beta build as a model.

**Contents**

- **This page:** [How to read this document](#how-to-read-this-document) · [Summary](#summary) · [Design rules](#design-rules)
- **Proposals:** [Holy](holy.md) · [Protection](protection.md) · [Retribution](retribution.md) · [Judgements and Blessings](judgements-and-blessings.md)
- **Analysis:** [Analysis](analysis/README.md): [Crushing blows](analysis/crushing-blows.md) · [Threat](analysis/threat.md) · [PvP burst check](analysis/pvp-burst-check.md) · [Mana](analysis/mana.md) · [Healing](analysis/healing.md) · [Damage](analysis/damage.md) · [Builds](analysis/builds.md) · [Tree balance](analysis/tree-balance.md)
- **Tests and open items:** [Beta test results](beta-test-results.md) · [Open items](open-items.md) · [Withdrawn ideas](withdrawn-ideas.md) · [Sources](sources.md)

## How to read this document

- **C1 to C5 (spell change).** These change baseline spells, not talents.
- **C-H, C-P and C-R (talent change).** These change what a talent does, add a talent or remove a talent. The letter after C gives the tree: H (Holy), P (Protection), R (Retribution). A change can also move the talent. The text then gives the new row.
- **M-H, M-P and M-R (move).** These move a talent to a different row. The talent text does not change.
- **New IDs.** A new proposal takes the next free number of its series. A new proposal never takes the number of a withdrawn proposal.
- **Names.** The text gives the name first and the ID in parentheses, for example Twist of Light (C-R2).
- **C2a and C2b** are the two alternatives to Personal Judgement of the Crusader (C2).
- **Withdrawn ideas** have no ID. They are in [Withdrawn ideas](withdrawn-ideas.md) only.
- **Data.** Forever client build 1.60.1.70450, with the server hotfixes of 18 October 2026, from wowforevertalents.com. Player tests from 19 October 2026 and later. The text tells you when a value comes from an in-game tooltip.
- **Limits.** These are design proposals. No player has tested them in the game. The combat and mana values use Classic 1.12 rules when no test gives a different rule. Each estimate gives its assumptions.
- **Calculator.** You can try all proposals in the talent calculator. Use the Beta/Proposed button to compare.

## Summary

**Changes**

| ID | Talent | Tree and row | Beta | Proposed |
| --- | --- | --- | --- | --- |
| C1 | Holy Strike | Baseline spell | Triggers only Seal of Light, Justice and Wisdom | Triggers your active Seal and Echo the same as a melee attack |
| C2 | Judgement of the Crusader | Baseline spell | Uses the one Judgement of the Paladin | Personal debuff. It does not count against the one-Judgement limit |
| C3 | Blessing of Light | Baseline spell, and Healing Light (C-H4) | +400 Holy Light, +115 Flash of Light. Uses a Blessing slot | Removed. Healing Light gives 10/20/30% |
| C4 | Hand of Sacrifice | Baseline spell | Blessing of Sacrifice: 55 damage for each hit moves to you. No cooldown | Up to 825 damage moves to you. Lasts 30 sec, 15 sec cooldown |
| C5 | Hands: Sacrifice, Protection and Freedom | Baseline spells | Blessings of Sacrifice, Protection and Freedom use a Blessing slot | The spells take the name Hand of. No Blessing slot. One Hand from each Paladin on a target |
| C-H1 | Reverence | Holy, row 3 → row 2 | 10/20/30% of mana regeneration during casts | 17/33/50% |
| C-H2 | Lingering Light (new) | Holy, row 3 | — | 2 ranks: a critical heal adds a heal over time of 10/20% of the heal |
| C-H3 | Infusion of Light | Holy, row 4 → row 2 | Holy Shock and Flash of Light critical hits make the next Holy Light faster | All Holy Shock, Flash of Light and Holy Strike hits do this. No critical hit is necessary |
| C-H4 | Healing Light | Holy, row 2 → row 6 | 3 ranks: 4/8/12% | 3 ranks: 10/20/30% (with Blessing of Light removal, C3) |
| C-H5 | Merciful Light (new) | Holy, row 5 | — | 2 ranks: Holy Shock heals 50/100% more on targets at or below 35% health. Requires Holy Shock |
| C-H6 | Divine Grace (new) | Holy, row 4 | — | 2 ranks: a Flash of Light, Holy Light or Holy Shock heal while Divine Favor is active gives the target 15/30% armor from items for 15 sec. Requires Divine Favor |
| C-P1 | Redoubt | Protection, row 1 | 10% chance when you are hit: +4–20% block | The same. Each Holy Shield cast also starts it |
| C-P2 | Iron Creed | Protection, row 6 | −2–10% damage taken for 6 sec after Holy Strike | −2–10% damage taken while Righteous Fury is active |
| C-P3 | Toughness and Divine Strength: removed | Protection row 1, Retribution row 2, Holy row 1 | Toughness: +2–10% armor from items. Divine Strength: +2–10% Strength | Both removed. Vindication goes to Retribution row 2 with 5 ranks (+1–5% Attack Power). Benediction (M-P1) and Unyielding Faith (M-H2) fill row 1 of Protection and Holy |
| C-P4 | Improved Righteous Fury | Protection, row 3 | −2–6% damage taken with Righteous Fury | Removed |
| C-P5 | Shoulder the Burden (new) replaces Improved Seal of Fury | Protection, row 3 | Improved Seal of Fury: mana when the Seal of Fury shield absorbs a hit | Shoulder the Burden: 50% of the threat of an ally moves to you, 3 min cooldown. Swift Judgement keeps its row 4 place with no requirement |
| C-P6 | Reckoning | Protection, row 5 | Extra attack after a block (40%) or a critical hit taken (100%). It hits with the next swing | Charge after a block, dodge or parry (once each 4 sec) or a critical hit taken. Holy Strike releases up to 2 charges |
| C-P7 | Reach of Law (new) | Protection, row 5 | — | 2 ranks: Judgement range +5/10 yards while Seal of Fury is active |
| C-P8 | Shield Specialization | Protection, row 3 | 33/66/100% chance to restore 4% of maximum mana, once each 3 sec | Each block restores 2/4/6% of maximum mana, once each 2 sec |
| C-P9 | Holy Shield | Protection, row 7 | 221 Holy damage for each block (rank 3) | 221 Holy damage, increased by your block value (100%), for each block |
| C-P11 | Devoted Sacrifice (new) | Protection, row 3 | — | 2 ranks: Lay on Hands drains only 75/50% of your current mana, and you take 20/40% less damage from your Hand of Sacrifice. Alternative C-P11a: the spell drains 50% for all Paladins |
| C-R1 | Conviction | Retribution, row 2 → row 1 (Conviction, M-R2) | +1–5% critical hit chance with melee attacks | +1–5% critical hit chance with attacks and spells |
| C-R2 | Twist of Light | Retribution, row 7 | The Echo applies to the next melee attack only | The Echo applies to all melee attacks for 10 sec |
| C-R3 | Sanctified Judgement | Retribution, row 3 | 33/66/100% chance to return 20/40/60% of the Seal cost | 100% chance at all ranks. The return is 20/40/60% of the Seal cost |
| C-R4 | Burning Zeal (new) | Retribution, row 4, before Vengeance | — | 2 ranks: +10/20% critical damage bonus for Seals, Judgements and Holy Strike |
| C-R5 | Measure for Measure (new) | Retribution, row 5, column 1 | — | 3 ranks: when the target dodges or parries, the Judgement cooldown decreases by 1/2/3 sec |

**Moves**

| ID | Talent | Tree | Beta | Proposed |
| --- | --- | --- | --- | --- |
| M-H1 | Improved Seals | Holy | Row 2 | Row 1 |
| M-H2 | Unyielding Faith | Holy | Row 2 | Row 1 |
| M-H3 | Holy Power | Holy | Row 6 | Row 5 |
| M-H4 | Consecrated Ground | Holy | Row 5 | Row 6 |
| M-H5 | Divine Precision | Holy | Row 5, requires Holy Shock | Row 4, no requirement |
| M-P1 | Benediction | Retribution → Protection | Retribution row 1 | Protection row 1 |
| M-R1 | Two-Handed Weapon Specialization | Retribution | Row 5 (20 points) | Row 4, column 1 (15 points) |
| M-R2 | Conviction | Retribution | Row 2 | Row 1 |
| M-R3 | Eye for an Eye | Retribution | Row 4 (15 points) | Row 3, column 2 (10 points) |
| M-R4 | Sanctified Judgement | Retribution | Row 3, column 2 | Row 3, column 1, requires Improved Judgement 2/2 |
| M-R5 | Vengeance | Retribution | Requires Sanctified Judgement 3/3 | Requires Burning Zeal 2/2 |

## Design rules

Forever uses five rules for its talent trees. All proposals follow these rules.

1. **No talents that improve a buff.** Buffs such as Blessing of Kings come from the trainer. Iron Creed (C-P2) is the one exception. The text of Iron Creed (C-P2) gives the reason.
2. **Rows 1 and 2 are for all specs.** The first talents must give the other two specs a reason to put points in the tree.
3. **Shared stats are for melee and spells.** Precision gives hit for both. Thundering Strikes (Shaman) gives critical hit for both.
4. **Each tree has 1-point signature talents** in rows 3 and 4. Each tree ends with a 1-point talent at 30 points.
5. **The class identity stays.** Holy heals with the Light. Protection holds the enemy with a shield. Retribution judges with a two-handed weapon and Seals.

### What the other classes have

| Pattern | Other classes | Paladin beta |
| --- | --- | --- |
| Mana regeneration during casts (healers) | Meditation (Priest), Reflection (Druid), Mindfulness (Shaman): 50% | Reverence: 30% |
| Mana regeneration during casts (damage and hybrid specs) | 50% at about 20 points: Bestial Discipline, Resourcefulness (Hunter), Improved Stormstrike (Shaman), Spirit Tap (Priest) | None for Protection or Retribution |
| Healing bonus deep in the tree | Spiritual Healing (Priest, 25 points), Purification (Shaman, 25 points) | Healing Light (+12%) at 5 points |
| Shared critical hit | Thundering Strikes (Shaman, row 1): all spells and attacks | Conviction: melee only |
| Two-handed weapon talent | Warrior: 15 points | 20 points |
| Stun cooldown talent | Brutal Impact (Druid): 2 ranks, −15/−30 sec on Bash | Improved Hammer of Justice: 3 ranks, −5/−10/−15 sec |
| Area taunt | Challenging Shout (Warrior), Challenging Roar (Druid): 10 yards, 6 sec, 10 min | None |
