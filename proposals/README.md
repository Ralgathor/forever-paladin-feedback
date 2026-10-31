# Forever Paladin Talent Proposals

This document gives talent proposals for the WoW Forever Paladin. It has 9 changes. The proposals use the beta trees of 30 October 2026. That beta adopts 6 earlier proposals, and makes 20 others unnecessary. The proposals follow the rules that Forever uses for the other classes. Each proposal uses a talent from another class in the same beta build as a model.

**Contents**

- **This page:** [How to read this document](#how-to-read-this-document) · [Summary](#summary) · [Design rules](#design-rules)
- **Proposals:** [Holy](holy.md) · [Protection](protection.md) · [Retribution](retribution.md) · [Judgements and Blessings](judgements-and-blessings.md)
- **Analysis:** [Analysis](analysis/README.md): [Crushing blows](analysis/crushing-blows.md) · [Threat](analysis/threat.md) · [PvP burst check](analysis/pvp-burst-check.md) · [Mana](analysis/mana.md) · [Healing](analysis/healing.md) · [Damage](analysis/damage.md) · [Builds](analysis/builds.md) · [Tree balance](analysis/tree-balance.md)
- **Tests and open items:** [Beta test results](beta-test-results.md) · [Open items](open-items.md) · [Withdrawn ideas](withdrawn-ideas.md) · [Sources](sources.md)

## How to read this document

- **C1 to C5 (spell change).** These change baseline spells, not talents.
- **C-H, C-P and C-R (talent change).** These change what a talent does, add a talent or remove a talent. The letter after C gives the tree: H (Holy), P (Protection), R (Retribution). A change can also move the talent. The text then gives the new row.
- **M-H, M-P and M-R (move).** These move a talent to a different row. The talent text does not change. No move proposal is open now.
- **New IDs.** A new proposal takes the next free number of its series. A new proposal never takes the number of a withdrawn proposal.
- **Names.** The text gives the name first and the ID in parentheses, for example Sanctified Judgement (C-R3).
- **C2a** is the alternative to Personal Judgement of the Crusader (C2). **C-P11a** is the alternative to the Lay on Hands part of Devoted Sacrifice (C-P11).
- **Withdrawn ideas** have no ID. They are in [Withdrawn ideas](withdrawn-ideas.md) only. A withdrawn proposal shows its earlier ID there, because the Analysis tabs still use it.
- **Data.** Forever client build 1.60.1.70707, hotfix push 113554 (beta of 30 October 2026), from the game files in wowsims Forever. Player tests from 19 October 2026 and later. The text tells you when a value comes from an in-game tooltip.
- **Analysis values.** Most values in the Analysis tabs use the beta of 18 October 2026. Beta test results gives the first model results for the beta of 30 October. A proposal says when its values must be modeled again.
- **Limits.** These are design proposals. No player has tested them in the game. The combat and mana values use Classic 1.12 rules when no test gives a different rule. Each estimate gives its assumptions.
- **Calculator.** You can try all proposals in the talent calculator. Use the Beta/Proposed button to compare.

## Summary

**Changes**

| ID | Talent | Tree and row | Beta | Proposed |
| --- | --- | --- | --- | --- |
| C1 | Holy Strike | Baseline spell | Triggers only Seal of Light, Justice and Wisdom | Triggers your active Seal the same as a melee attack |
| C2 | Judgement of the Crusader | Baseline spell | Uses the one Judgement of the Paladin | Personal debuff. It does not count against the one-Judgement limit |
| C4 | Hand of Sacrifice | Baseline spell | Blessing of Sacrifice: 55 damage for each hit moves to you. No cooldown | Up to 825 damage moves to you. Lasts 30 sec, 15 sec cooldown |
| C5 | Hands: Sacrifice, Protection and Freedom | Baseline spells | Blessings of Sacrifice, Protection and Freedom use a Blessing slot | The spells take the name Hand of. No Blessing slot. One Hand from each Paladin on a target |
| C-P1 | Redoubt | Protection, row 1 | 10% chance when you are hit: +6–30% block | The same. Each Holy Shield cast also starts it |
| C-P5 | Shoulder the Burden (new) | Protection, row 5 | — | 50% of the threat of an ally moves to you, 3 min cooldown |
| C-P11 | Devoted Sacrifice (new) | Protection, row 4 | — | 2 ranks: Lay on Hands drains only 75/50% of your current mana, and you take 20/40% less damage from your Hand of Sacrifice. Alternative C-P11a: the spell drains 50% for all Paladins |
| C-R3 | Sanctified Judgement | Retribution, row 2 | 33/66/100% chance to return 20/40/60% of the Seal cost | 100% chance at all ranks. The return is 20/40/60% of the Seal cost |
| C-R4 | Burning Zeal (new) | Retribution, row 5 | — | 2 ranks: +10/20% critical damage bonus for Seals, Judgements and Holy Strike |

**Adopted in the beta of 30 October 2026**

| ID | Proposal | What the beta does |
| --- | --- | --- |
| C3 | Blessing of Light: removed | Blessing of Light and Greater Blessing of Light are removed. Oath of Light (new Holy talent) gives their bonus on one ally |
| C-H1 (move) | Reverence to Holy row 2 | Reverence is in row 2. Its values are 15/30% |
| C-P5 (removal) | Improved Seal of Fury: removed | Improved Seal of Fury is removed |
| C-R1 | Conviction: attacks and spells | Conviction gives 2/4/6% critical chance with all spells and attacks |
| M-H5 | Divine Precision: row 4, no requirement | Divine Precision is in row 4 with no requirement |
| M-R1 | Two-Handed Weapon Specialization: row 4 | Two-Handed Weapon Specialization is in row 4 |

## Design rules

Forever uses five rules for its talent trees. All proposals follow these rules.

1. **No talents that improve a buff.** Buffs such as Blessing of Kings come from the trainer.
2. **Rows 1 and 2 are for all specs.** The first talents must give the other two specs a reason to put points in the tree.
3. **Shared stats are for melee and spells.** Precision gives hit for both. Thundering Strikes (Shaman) gives critical hit for both.
4. **Each tree has 1-point signature talents** in rows 3 and 4. Each tree ends with a 1-point talent at 30 points.
5. **The class identity stays.** Holy heals with the Light and is the best single-target healer. It does not need to be the best raid healer. Protection holds the enemy with a shield. Retribution judges with a two-handed weapon and Seals.

### What the other classes have

| Pattern | Other classes | Paladin beta |
| --- | --- | --- |
| Mana regeneration during casts (healers) | Meditation (Priest), Reflection (Druid), Mindfulness (Shaman): 50% | Reverence: 30% |
| Mana regeneration during casts (damage and hybrid specs) | 50% at about 20 points: Bestial Discipline, Resourcefulness (Hunter), Improved Stormstrike (Shaman), Spirit Tap (Priest) | None for Protection or Retribution |
| Healing bonus deep in the tree | Spiritual Healing (Priest, 25 points), Purification (Shaman, 25 points) | Healing Light (+12%) at 5 points. Oath of Light (flat bonus, one ally) at 15 points |
| Shared critical hit | Thundering Strikes (Shaman, row 1): all spells and attacks | Conviction (row 2): all spells and attacks |
| Two-handed weapon talent | Warrior: 15 points | 15 points |
| Stun cooldown talent | Brutal Impact (Druid): 2 ranks, −15/−30 sec on Bash | Improved Hammer of Justice: 3 ranks, −5/−10/−15 sec |
| Area taunt | Challenging Shout (Warrior), Challenging Roar (Druid): 10 yards, 6 sec, 10 min | None |
