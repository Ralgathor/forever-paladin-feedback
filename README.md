# Forever Paladin feedback

This project gives player feedback for the Paladin in **World of Warcraft: Forever**. It is not an official project. It is not related to Blizzard Entertainment.

## Contents

- **Proposals:** 18 changes (C1–C18) and 7 moves (M1–M7) for the Holy, Protection and Retribution trees. Three changes are new talents.
- **Talent calculator:** you can try the proposals and compare them with the beta trees.

## IDs

- **C (change):** the proposal changes what a talent does, adds a talent or removes a talent.
- **M (move):** the proposal moves a talent to a different row or column. The talent text does not change.

## Changes and moves

**Holy**

- **C1 Reverence:** 17/33/50% mana regeneration while casting (beta: 10/20/30%). It moves from row 3 to row 2. Protection and Retribution can get it with 8 Holy points.
- **C2 Lingering Light (new):** a critical heal adds a heal over time of 15/30% of the heal.
- **C3 Infusion of Light:** Holy Strike critical hits also make the next Holy Light faster. It moves from row 4 to row 2.
- **C4 Healing Light:** 2 ranks, 6/12% (beta: 3 ranks, 4/8/12%). It moves from row 2 to row 6.
- **C5 Improved Seals:** 5 ranks, 3/6/9/12/15% (beta: 3 ranks). It moves from row 2 to row 1 and replaces Divine Strength.
- **M1 Consecrated Ground:** row 5 → row 3.
- **M2 Spiritual Focus:** row 2 → row 4.
- **M3 Unyielding Faith:** row 2, column 4 → column 3.

**Protection**

- **C6 Redoubt:** each Holy Shield cast also starts it. The block chance stays high. Most crushing blows stop.
- **C7 Iron Creed:** −2–10% damage taken while Righteous Fury is active (beta: for 6 sec after Holy Strike).
- **C8 Divine Strength replaces Toughness:** +2–10% Strength, from Holy row 1.
- **C9 Improved Righteous Fury:** removed. Iron Creed alone gives −10% damage taken.
- **C10 Righteous Defense (new) replaces Improved Seal of Fury:** your Blessing of Protection also makes up to 3 enemies that attack the target attack you for 6 sec. Row 3. It requires Guardian's Favor.
- **C11 Reckoning:** block, dodge and parry also give charges (once each 4 sec). Holy Strike releases up to 2 charges.
- **C12 Fury's Reach (new):** Judgement range +5/10 yards while Seal of Fury is active. Row 4, column 2. It requires Swift Judgement. One-Handed Weapon Specialization moves to column 3.
- **C13 Shield Specialization:** mana return once each 2 sec (beta: 3 sec).
- **C14 Holy Shield:** each block also does 200% of your block value as Holy damage. Paladin threat then increases with gear, as Warrior and Druid threat does.
- **M4 Improved Hammer of Justice:** row 4, column 3 → row 3, column 1.
- **M5 Swift Judgement:** stays in row 4, column 1. It has no requirement now (C10 removes Improved Seal of Fury).

**Retribution**

- **C15 Conviction:** +1–5% critical hit chance with attacks and spells (beta: melee only).
- **C16 Sacred Arbiter:** Holy Strike always triggers your active Seal (beta: +20% Holy Strike damage). It moves from row 4 to row 5.
- **C17 Twist of Light:** the Echo applies to all melee attacks for 10 sec (beta: the next melee attack only).
- **M6 Two-Handed Weapon Specialization:** row 5 → row 4 (20 → 15 points).
- **M7 Repentance:** row 5 → row 4 (20 → 15 points).

**Judgements**

- **C18 Judgement of the Crusader:** a personal debuff. It does not count against the one-Judgement limit. C18a and C18b are alternatives.

## Read and try

- **[Proposals](proposals.md).** The full document. For each proposal, it gives the beta text, the proposed text, the reason and the model talent from another class. It also gives the analysis, the test results and the open questions.
- **[Talent calculator](calculator/index.html).** Live version: https://ralgathor.github.io/forever-paladin-feedback/calculator/
  - The calculator opens with the proposed trees. Push **Beta** to see the beta trees.
  - A purple tag (C) shows a changed talent. A blue tag (M) shows a talent that only moves.
  - A build code that starts with `p` opens a proposed build. A build code without `p` opens a beta build.

The talent icons come from the Wowhead icon server (wow.zamimg.com). If the icons do not load, the calculator shows drawn icons. This project does not keep game files.

## Method

- **Data.** Forever client build 1.60.1.70450, with the server hotfixes of 18 October 2026. The talent text comes from [wowforevertalents.com](https://wowforevertalents.com/). Player tests give the talent behavior.
- **Models.** Each proposal uses a talent from another class in the same beta as a model (Warrior, Druid, Priest, Shaman, Hunter, Mage).
- **Rules.** The combat and mana values use Classic 1.12 rules when no test gives a different rule.
- **Estimates.** The burst values are estimates. The Reckoning, threat and mana values come from simple models. Each estimate gives its assumptions.

## Feedback

Open an issue to send corrections, test results or other proposals.
