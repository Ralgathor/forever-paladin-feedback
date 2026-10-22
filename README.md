# Forever Paladin feedback

This project gives player feedback for the Paladin in **World of Warcraft: Forever**. It is not an official project. It is not related to Blizzard Entertainment.

## Contents

- **Proposals:** 20 changes (C1–C20) and 8 moves (M1–M8) for the Holy, Protection and Retribution trees. Three changes are new talents.
- **Talent calculator:** you can try the proposals and compare them with the beta trees.

## IDs

- **C (change):** the proposal changes what a talent does, adds a talent or removes a talent.
- **M (move):** the proposal moves a talent to a different row or column. The talent text does not change.

## Changes and moves

**Holy**

- **C1 Reverence:** 17/33/50% mana regeneration while casting (beta: 10/20/30%). It moves from row 3 to row 2. Protection and Retribution can get it with 8 Holy points.
- **C2 Lingering Light (new):** a critical heal adds a heal over time of 10/20% of the heal.
- **C3 Infusion of Light:** all Holy Shock, Flash of Light and Holy Strike hits make the next Holy Light faster (beta: critical hits only). It moves from row 4 to row 2.
- **C4 Healing Light:** 3 ranks, 10/20/30% (beta: 4/8/12%), with C19. It moves from row 2 to row 6, column 3. Holy Power moves to column 1.
- **C5 Improved Seals:** 5 ranks, 3/6/9/12/15% (beta: 3 ranks). It moves from row 2 to row 1 and replaces Divine Strength.
- **C20 Illumination:** critical heals return 75% of the base cost (beta: 50%, Classic: 100%). Thus, Holy keeps more healing than the other healers in long fights.
- **M1 Consecrated Ground:** row 5 → row 3.
- **M2 Spiritual Focus:** row 2 → row 4.
- **M3 Unyielding Faith:** row 2, column 4 → column 3.

**Protection**

- **C6 Redoubt:** each Holy Shield cast also starts it. The block chance stays high. Most crushing blows stop.
- **C7 Iron Creed:** −2–10% damage taken while Righteous Fury is active (beta: for 6 sec after Holy Strike).
- **C8 Divine Strength replaces Toughness:** +2–10% Strength, from Holy row 1.
- **C9 Improved Righteous Fury:** removed. Iron Creed alone gives −10% damage taken.
- **C10 Shoulder the Burden (new) replaces Improved Seal of Fury:** 50% of the threat of an ally moves to you. 5 min cooldown (4 min with Sacred Duty 2/2). It has no effect in PvP.
- **C11 Reckoning:** block, dodge and parry also give charges (once each 4 sec). Holy Strike releases up to 2 charges.
- **C12 Fury's Reach (new):** Judgement range +5/10 yards while Seal of Fury is active.
- **C13 Shield Specialization:** mana return once each 2 sec (beta: 3 sec).
- **C14 Holy Shield:** each block also does 200% of your block value as Holy damage. Paladin threat then increases with gear, as Warrior and Druid threat does.
- **M4 Improved Hammer of Justice:** row 4 → row 3.
- **M5 Swift Judgement:** row 4 → row 3, with no requirement.

**Retribution**

- **C15 Conviction:** +1–5% critical hit chance with attacks and spells (beta: melee only).
- **C16 Holy Strike and Sacred Arbiter:** Holy Strike triggers your active Seal and Echo the same as a melee attack, for all specs. Sacred Arbiter gives +10% Holy Strike damage (beta: +20%) and keeps the Judgement refresh. It moves from row 4 to row 5.
- **C17 Twist of Light:** the Echo applies to all melee attacks for 10 sec (beta: the next melee attack only).
- **M6 Two-Handed Weapon Specialization:** row 5 → row 4 (20 → 15 points).
- **M7 Repentance:** row 5 → row 4 (20 → 15 points).
- **M8 Conviction and Benediction:** they change rows. Conviction goes to row 1, as all other +5% critical hit talents. A Holy Paladin gets it for 5 points.

**Judgements and Blessings**

- **C18 Judgement of the Crusader:** a personal debuff. It does not count against the one-Judgement limit. C18a and C18b are alternatives.
- **C19 Blessing of Light:** removed. Healing Light (C4) gives 10/20/30%. Thus, Holy healing does not change with the number of Paladins in the raid. C19a and C19b are alternatives.

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
