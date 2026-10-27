# Forever Paladin feedback

This project gives player feedback for the Paladin in **World of Warcraft: Forever**. It is not an official project. It is not related to Blizzard Entertainment.

## Contents

- **Proposals:** 23 changes and 7 moves for the Holy, Protection and Retribution trees. 18 changes are talent changes (C-H1–C-H4, C-P1–C-P11, C-R1–C-R3), and four of them are new talents. 5 changes are baseline spell changes (C1–C5). The moves are M-H1–M-H4, M-P1, M-R1 and M-R2.
- **Talent calculator:** you can try the proposals and compare them with the beta trees.
- **Analysis:** crushing blows, threat, PvP burst, mana, healing, damage, builds and tree balance, each with its model and limits.
- **Builds:** the best builds for each spec and role (raid, dungeon, PvP), with calculator codes. Also the builds that use a different tree for a role.

## IDs

- **C-H, C-P and C-R (talent change):** the proposal changes what a talent does, adds a talent or removes a talent. The letter after C gives the tree: H (Holy), P (Protection), R (Retribution).
- **C1 to C5 (spell change):** the proposal changes a baseline spell, not a talent.
- **M-H, M-P and M-R (move):** the proposal moves a talent to a different row. The talent text does not change.
- **New IDs.** A new proposal takes the next free number of its series. A new proposal never takes the number of a withdrawn proposal.
- **Names.** The text gives the name first and the ID in parentheses, for example Twist of Light (C-R2).

## Changes and moves

**Holy**

- **C-H1 Reverence:** 17/33/50% mana regeneration during casts (beta: 10/20/30%). It moves from row 3 to row 2. Retribution can take it with 8 Holy points.
- **C-H2 Lingering Light (new, row 3):** a critical heal adds a heal over time of 10/20% of the heal.
- **C-H3 Infusion of Light:** all Holy Shock, Flash of Light and Holy Strike hits make the next Holy Light faster (beta: critical hits only). It moves from row 4 to row 2.
- **C-H4 Healing Light:** 3 ranks, 10/20/30% (beta: 4/8/12%), with Blessing of Light removal (C3). It moves from row 2 to row 6.
- **M-H1 Improved Seals:** row 2 → row 1. It keeps 3 ranks, 5/10/15%.
- **M-H2 Unyielding Faith:** row 2 → row 1, to fill the place of Divine Strength (Toughness and Divine Strength removal, C-P3).
- **M-H3 Holy Power:** row 6 → row 5. With Lingering Light (C-H2) in row 3, a Holy healer needs no filler.
- **M-H4 Consecrated Ground:** row 5 → row 6. Only deep Holy Shock builds take it.

**Protection**

- **C-P1 Redoubt:** each Holy Shield cast also starts it. The block chance stays high. Most crushing blows stop.
- **C-P2 Iron Creed:** −2–10% damage taken while Righteous Fury is active (beta: for 6 sec after Holy Strike).
- **C-P3 Toughness and Divine Strength:** removed. Vindication goes to Retribution row 2 with 5 ranks (+1–5% Attack Power). Benediction (M-P1) and Unyielding Faith (M-H2) fill row 1 of Protection and Holy. Precision, Guardian's Favor, Anticipation and Holy Conduit stay in their beta place. Each point in rows 1 and 2 then has a use for its spec.
- **C-P4 Improved Righteous Fury:** removed. Iron Creed alone gives −10% damage taken.
- **C-P5 Shoulder the Burden (new, row 3) replaces Improved Seal of Fury:** 50% of the threat of an ally moves to you. 5 min cooldown (4 min with Sacred Duty 2/2). It has no effect in PvP. Swift Judgement keeps its row 4 place with no requirement.
- **C-P6 Reckoning:** block, dodge and parry also give charges (once each 4 sec). Holy Strike releases up to 2 charges.
- **C-P7 Reach of Law (new, row 5):** Judgement range +5/10 yards while Seal of Fury is active.
- **C-P8 Shield Specialization:** mana return once each 2 sec (beta: 3 sec).
- **C-P9 Holy Shield:** each block also does 200% of your block value as Holy damage. Paladin threat then increases with gear, as Warrior and Druid threat does.
- **M-P1 Benediction:** Retribution row 1 → Protection row 1, with its 5 beta ranks (2–10%). It takes the place of Toughness (Toughness and Divine Strength removal, C-P3).
- **C-P10 Guardian's Favor:** it also reduces the cooldown of Hand of Sacrifice (C4) by 5/10 sec. The talent keeps its Hand of Protection and Hand of Freedom effects.
- **C-P11 Devoted Sacrifice (new, row 3):** Lay on Hands drains only 75/50% of your current mana (beta: all of it), and you take 10/20% less damage from your Hand of Sacrifice. Alternative C-P11a (Devoted Sacrifice): the spell drains 50% for all Paladins.

**Retribution**

- **C-R1 Conviction:** +1–5% critical hit chance with attacks and spells (beta: melee only).
- **C-R2 Twist of Light:** the Echo applies to all melee attacks for 10 sec (beta: the next melee attack only).
- **C-R3 Sanctified Judgement:** each Judgement returns 20/40/60% of the Seal cost (beta: a 33/66/100% chance).
- **M-R1 Two-Handed Weapon Specialization:** row 5 → row 4 (20 → 15 points).
- **M-R2 Conviction:** row 2 → row 1, as all other +5% critical hit talents. A Holy Paladin takes it for 5 points. Retribution has 41 points.

**Spell changes**

- **C1 Holy Strike:** Holy Strike triggers your active Seal and Echo the same as a melee attack, for all specs (beta: only Seal of Light, Justice and Wisdom).
- **C2 Judgement of the Crusader:** a personal debuff. It does not count against the one-Judgement limit. C2a and C2b are alternatives.
- **C3 Blessing of Light:** removed. Healing Light (C-H4) gives 10/20/30%. Thus, Holy healing does not change with the number of Paladins in the raid. C3a and C3b are alternatives.
- **C4 Hand of Sacrifice:** up to 825 damage moves to you (beta: 55 for each hit). 30 sec cooldown, 20 sec with Guardian's Favor (C-P10) 2/2.
- **C5 Hands:** Blessing of Sacrifice, Protection and Freedom become Hand of Sacrifice, Protection and Freedom. They use no Blessing slot. Each Paladin can have one Hand on a target.

## Read and try

- **[Proposals](proposals/README.md).** The full document, in one file for each part. For each proposal, it gives the beta text, the proposed text, the reason and the model talent from another class. It also gives the analysis, the test results and the open questions.
- **[Talent calculator](calculator/index.html).** Live version: https://ralgathor.github.io/forever-paladin-feedback/calculator/
  - The calculator opens with the proposed trees. Push **Beta** to see the beta trees.
  - **Versions.** Use the Version list to open an earlier version of the proposed trees. Version 5 (26 October 2026) is the current version. Its build codes start with `v5p`. A version 4 code (it starts with `v4p`) opens on the version 4 page: https://ralgathor.github.io/forever-paladin-feedback/calculator/v4/. A version 3 code (it starts with `v3p`) opens on the version 3 page: https://ralgathor.github.io/forever-paladin-feedback/calculator/v3/. A version 2 code (it starts with `v2p`) opens on the version 2 page: https://ralgathor.github.io/forever-paladin-feedback/calculator/v2/. A version 1 code (it starts with `p`) opens on the version 1 page: https://ralgathor.github.io/forever-paladin-feedback/calculator/v1/
  - A purple tag (C) shows a changed talent. A blue tag (M) shows a talent that only moves.
  - A build code that starts with `v5p` opens a proposed build. A build code with only digits opens a beta build.

The talent icons come from the Wowhead icon server (wow.zamimg.com). If the icons do not load, the calculator shows drawn icons. This project does not keep game files.

## Method

- **Data.** Forever client build 1.60.1.70450, with the server hotfixes of 18 October 2026. The talent text comes from [wowforevertalents.com](https://wowforevertalents.com/). Player tests give the talent behavior.
- **Models.** Each proposal uses a talent from another class in the same beta as a model (Warrior, Druid, Priest, Shaman, Hunter, Mage).
- **Rules.** The combat and mana values use Classic 1.12 rules when no test gives a different rule.
- **Estimates.** The burst values are estimates. The Reckoning, threat, mana, healing and damage values come from simple models, not combat logs. Each estimate gives its assumptions and limits.
- **Other classes.** The healing comparison uses the DoubleZug sheets for the four Forever healers, with the spell values of the Forever spellbook ([model](models/healing/)). The damage comparison uses the ratios of one external simulation ([MythicSim](https://mythicsim.com/wow-forever/tier-list)) and a same-gear model check.

## Feedback

Open an issue to send corrections, test results or other proposals.
