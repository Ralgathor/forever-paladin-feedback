# Forever Paladin Talent Proposals

This document gives talent proposals for the WoW Forever Paladin. It has 20 changes and 9 moves. The proposals follow the rules that Forever uses for the other classes. Each proposal uses a talent from another class in the same beta build as a model.

**Contents**

- **This page:** [How to read this document](#how-to-read-this-document) · [Summary](#summary) · [Design rules](#design-rules)
- **Proposals:** [Holy](holy.md) · [Protection](protection.md) · [Retribution](retribution.md) · [Judgements and Blessings](judgements-and-blessings.md)
- **Analysis:** [Analysis](analysis/README.md): [Crushing blows](analysis/crushing-blows.md) · [Threat](analysis/threat.md) · [PvP burst check](analysis/pvp-burst-check.md) · [Mana](analysis/mana.md) · [Healing](analysis/healing.md) · [Damage](analysis/damage.md) · [Builds](analysis/builds.md) · [Tree balance](analysis/tree-balance.md)
- **Tests and open items:** [Beta test results](beta-test-results.md) · [Open items](open-items.md) · [Withdrawn ideas](withdrawn-ideas.md) · [Sources](sources.md)

## How to read this document

- **C (change).** C1 to C19, C22 and C23 change what a talent does, add a talent or remove a talent. C16, C18, C19 and C23 change baseline spells. A change can also move the talent. The text then gives the new row.
- **M (move).** M4 to M6 and M8 move a talent to a different row. The talent text does not change.
- **C18a and C18b** are the two alternatives to C18.
- **Withdrawn ideas** have no ID. They are in [Withdrawn ideas](withdrawn-ideas.md) only.
- **Data.** Forever client build 1.60.1.70450, with the server hotfixes of 18 October 2026, from wowforevertalents.com. Player tests from 19 October 2026 and later. The text tells you when a value comes from an in-game tooltip.
- **Limits.** These are design proposals. No player has tested them in the game. The combat and mana values use Classic 1.12 rules when no test gives a different rule. Each estimate gives its assumptions.
- **Calculator.** You can try all proposals in the talent calculator. Use the Beta/Proposed button to compare.

## Summary

**Changes**

| ID | Talent | Tree and row | Beta | Proposed |
| --- | --- | --- | --- | --- |
| C1 | Reverence | Holy, row 3 → row 2 | 10/20/30% of mana regeneration while casting | 17/33/50% |
| C2 | Lingering Light (new) | Holy, row 3 | — | 2 ranks: a critical heal adds a heal over time of 10/20% of the heal |
| C3 | Infusion of Light | Holy, row 4 → row 2 | Holy Shock and Flash of Light critical hits make the next Holy Light faster | All Holy Shock, Flash of Light and Holy Strike hits do this. No critical hit is necessary |
| C4 | Healing Light | Holy, row 2 → row 6 | 3 ranks: 4/8/12% | 3 ranks: 10/20/30% (with C19) |
| C6 | Redoubt | Protection, row 1 | 10% chance when you are hit: +4–20% block | The same. Each Holy Shield cast also starts it |
| C7 | Iron Creed | Protection, row 6 | −2–10% damage taken for 6 sec after Holy Strike | −2–10% damage taken while Righteous Fury is active |
| C8 | Toughness and Divine Strength: removed | Protection row 1, Retribution row 2, Holy row 1 | Toughness: +2–10% armor from items. Divine Strength: +2–10% Strength | Both removed. Vindication goes to Retribution row 2 with 5 ranks (+1–5% Attack Power). Benediction (M11) and Unyielding Faith (M10) fill row 1 of Protection and Holy |
| C9 | Improved Righteous Fury | Protection, row 3 | −2–6% damage taken with Righteous Fury | Removed |
| C10 | Shoulder the Burden (new) replaces Improved Seal of Fury | Protection, row 3 → row 4 | Improved Seal of Fury: mana when the Seal of Fury shield absorbs a hit | Shoulder the Burden: 50% of the threat of an ally moves to you, 5 min cooldown. Sacred Duty decreases the cooldown |
| C11 | Reckoning | Protection, row 5 | Extra attack after a block (40%) or a critical hit taken (100%). It hits with the next swing | Charge after a block, dodge or parry (once each 4 sec) or a critical hit taken. Holy Strike releases up to 2 charges |
| C12 | Fury's Reach (new) | Protection, row 4 | — | 2 ranks: Judgement range +5/10 yards while Seal of Fury is active |
| C13 | Shield Specialization | Protection, row 3 | Mana return once each 3 sec | Mana return once each 2 sec |
| C14 | Holy Shield | Protection, row 7 | 221 Holy damage for each block (rank 3) | 221 Holy damage plus 200% of your block value for each block |
| C15 | Conviction | Retribution, row 2 → row 1 (M8) | +1–5% critical hit chance with melee attacks | +1–5% critical hit chance with attacks and spells |
| C16 | Holy Strike | Spell, all specs | Triggers only Seal of Light, Justice and Wisdom | Triggers your active Seal and Echo the same as a melee attack |
| C17 | Twist of Light | Retribution, row 7 | The Echo applies to the next melee attack only | The Echo applies to all melee attacks for 10 sec |
| C18 | Judgement of the Crusader | Baseline spell | Uses the one Judgement of the Paladin | Personal debuff. It does not count against the one-Judgement limit |
| C19 | Blessing of Light | Baseline spell, and Healing Light (C4) | +400 Holy Light, +115 Flash of Light. Uses a Blessing slot | Removed. Healing Light gives 10/20/30% |
| C22 | Guardian's Favor | Protection, row 2 | Blessing of Protection −1/2 min, Blessing of Freedom +3/6 sec. Lay on Hands drains all your remaining mana | The same, and Lay on Hands drains only 75/50% of your remaining mana. Alternative C22a: the spell drains 50% for all Paladins |
| C23 | Blessing of Sacrifice, Protection and Freedom become Hands | Baseline spells | The three use a Blessing slot. Sacrifice: 55 damage for each hit moves to you, no cooldown | No Blessing slot. One Hand from each Paladin on a target. Hand of Sacrifice: up to 825 damage moves to you, 15 sec cooldown |

**Moves**

| ID | Talent | Tree | Beta | Proposed |
| --- | --- | --- | --- | --- |
| M4 | Improved Hammer of Justice | Protection | Row 4 | Row 3 |
| M5 | Swift Judgement | Protection | Row 4, requires Improved Seal of Fury | Row 3, no requirement |
| M6 | Two-Handed Weapon Specialization | Retribution | Row 5 (20 points) | Row 4 (15 points) |
| M8 | Conviction | Retribution | Row 2 | Row 1 |
| M9 | Improved Seals | Holy | Row 2 | Row 1 |
| M10 | Unyielding Faith | Holy | Row 2 | Row 1 |
| M11 | Benediction | Retribution → Protection | Retribution row 1 | Protection row 1 |
| M12 | Holy Power | Holy | Row 6 | Row 5 |
| M13 | Consecrated Ground | Holy | Row 5 | Row 6 |

## Design rules

Forever uses five rules for its talent trees. All proposals follow these rules.

1. **No talents that improve a buff.** Buffs such as Blessing of Kings come from the trainer. Iron Creed (C7) is the one exception. The text of C7 gives the reason.
2. **Rows 1 and 2 are for all specs.** The first talents must give the other two specs a reason to put points in the tree.
3. **Shared stats are for melee and spells.** Precision gives hit for both. Thundering Strikes (Shaman) gives critical hit for both.
4. **Each tree has 1-point signature talents** in rows 3 and 4. Each tree ends with a 1-point talent at 30 points.
5. **The class identity stays.** Holy heals with the Light. Protection holds the enemy with a shield. Retribution judges with a two-handed weapon and Seals.

### What the other classes have

| Pattern | Other classes | Paladin beta |
| --- | --- | --- |
| Mana regeneration while casting (healers) | Meditation (Priest), Reflection (Druid), Mindfulness (Shaman): 50% | Reverence: 30% |
| Mana regeneration while casting (damage and hybrid specs) | 50% at about 20 points: Bestial Discipline, Resourcefulness (Hunter), Improved Stormstrike (Shaman), Spirit Tap (Priest) | None for Protection or Retribution |
| Healing bonus deep in the tree | Spiritual Healing (Priest, 25 points), Purification (Shaman, 25 points) | Healing Light (+12%) at 5 points |
| Shared critical hit | Thundering Strikes (Shaman, row 1): all spells and attacks | Conviction: melee only |
| Two-handed weapon talent | Warrior: 15 points | 20 points |
| Stun cooldown talent | Brutal Impact (Druid): 2 ranks, −15/−30 sec on Bash | Improved Hammer of Justice: 3 ranks, −5/−10/−15 sec |
| Area taunt | Challenging Shout (Warrior), Challenging Roar (Druid): 10 yards, 6 sec, 10 min | None |
