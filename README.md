# Forever Paladin feedback

This project gives player feedback for the Paladin in **World of Warcraft: Forever**. It is not an official project. It is not related to Blizzard Entertainment.

## Contents

- **Proposals:** 21 changes (C1–C19, C21 and C22) and 5 moves (M1, M4–M6 and M8) for the Holy, Protection and Retribution trees. Three changes are new talents.
- **Talent calculator:** you can try the proposals and compare them with the beta trees.
- **Analysis:** crushing blows, threat, PvP burst, mana, healing, damage, builds and tree balance, each with its model and limits.
- **Builds:** the best builds for each spec and role (raid, dungeon, PvP), with calculator codes. Also the builds that use a different tree for a role.

## IDs

- **C (change):** the proposal changes what a talent does, adds a talent or removes a talent. C16, C18 and C19 change baseline spells.
- **M (move):** the proposal moves a talent to a different row. The talent text does not change.

## Changes and moves

**Holy**

- **C1 Reverence:** 17/33/50% mana regeneration while casting (beta: 10/20/30%). It moves from row 3 to row 2. Protection and Retribution can get it with 8 Holy points.
- **C2 Lingering Light (new):** a critical heal adds a heal over time of 10/20% of the heal.
- **C3 Infusion of Light:** all Holy Shock, Flash of Light and Holy Strike hits make the next Holy Light faster (beta: critical hits only). It moves from row 4 to row 2.
- **C4 Healing Light:** 3 ranks, 10/20/30% (beta: 4/8/12%), with C19. It moves from row 2 to row 6.
- **C5 Improved Seals:** it moves from row 2 to row 1. It keeps 3 ranks, 5/10/15%.
- **M1 Consecrated Ground:** row 5 → row 3.

**Protection**

- **C6 Redoubt:** each Holy Shield cast also starts it. The block chance stays high. Most crushing blows stop.
- **C7 Iron Creed:** −2–10% damage taken while Righteous Fury is active (beta: for 6 sec after Holy Strike).
- **C8 Toughness and Divine Strength:** removed. Precision and Guardian's Favor go to Protection row 1, Holy Conduit to Protection row 2. Vindication goes to Retribution row 2 with 5 ranks (+1–5% Attack Power). Unyielding Faith goes to Holy row 1. Each point in rows 1 and 2 then has a use for its spec.
- **C9 Improved Righteous Fury:** removed. Iron Creed alone gives −10% damage taken.
- **C10 Shoulder the Burden (new) replaces Improved Seal of Fury:** 50% of the threat of an ally moves to you. 5 min cooldown (4 min with Sacred Duty 2/2). It has no effect in PvP.
- **C11 Reckoning:** block, dodge and parry also give charges (once each 4 sec). Holy Strike releases up to 2 charges.
- **C12 Fury's Reach (new):** Judgement range +5/10 yards while Seal of Fury is active.
- **C13 Shield Specialization:** mana return once each 2 sec (beta: 3 sec).
- **C14 Holy Shield:** each block also does 200% of your block value as Holy damage. Paladin threat then increases with gear, as Warrior and Druid threat does.
- **M4 Improved Hammer of Justice:** row 4 → row 3.
- **M5 Swift Judgement:** row 4 → row 3, with no requirement.
- **C22 Guardian's Favor:** Lay on Hands drains only 75/50% of your remaining mana (beta: all of it). The talent keeps its Blessing of Protection and Blessing of Freedom effects. Alternative C22a: the spell drains 50% for all Paladins. C8 moves the talent to row 1.

**Retribution**

- **C15 Conviction:** +1–5% critical hit chance with attacks and spells (beta: melee only).
- **C16 Holy Strike (spell change):** Holy Strike triggers your active Seal and Echo the same as a melee attack, for all specs (beta: only Seal of Light, Justice and Wisdom).
- **C17 Twist of Light:** the Echo applies to all melee attacks for 10 sec (beta: the next melee attack only).
- **M6 Two-Handed Weapon Specialization:** row 5 → row 4 (20 → 15 points).
- **M8 Conviction and Benediction:** they change rows. Conviction goes to row 1, as all other +5% critical hit talents. A Holy Paladin gets it for 5 points.
- **C21 Benediction:** 3 ranks, 3/6/9% (beta: 5 ranks, 2/4/6/8/10%). With M8, it is in row 2. The dips into Retribution cost 2 points less. Retribution has 42 points.

**Judgements and Blessings**

- **C18 Judgement of the Crusader:** a personal debuff. It does not count against the one-Judgement limit. C18a and C18b are alternatives.
- **C19 Blessing of Light:** removed. Healing Light (C4) gives 10/20/30%. Thus, Holy healing does not change with the number of Paladins in the raid. C19a and C19b are alternatives.

## Read and try

- **[Proposals](proposals/README.md).** The full document, in one file for each part. For each proposal, it gives the beta text, the proposed text, the reason and the model talent from another class. It also gives the analysis, the test results and the open questions.
- **[Talent calculator](calculator/index.html).** Live version: https://ralgathor.github.io/forever-paladin-feedback/calculator/
  - The calculator opens with the proposed trees. Push **Beta** to see the beta trees.
  - **Versions.** Use the Version list to open an earlier version of the proposed trees. Version 2 (23 October 2026) is the current version. Its build codes start with `v2p`. A version 1 code (it starts with `p`) opens on the version 1 page: https://ralgathor.github.io/forever-paladin-feedback/calculator/v1/
  - A purple tag (C) shows a changed talent. A blue tag (M) shows a talent that only moves.
  - A build code that starts with `v2p` opens a proposed build. A build code with only digits opens a beta build.

The talent icons come from the Wowhead icon server (wow.zamimg.com). If the icons do not load, the calculator shows drawn icons. This project does not keep game files.

## Method

- **Data.** Forever client build 1.60.1.70450, with the server hotfixes of 18 October 2026. The talent text comes from [wowforevertalents.com](https://wowforevertalents.com/). Player tests give the talent behavior.
- **Models.** Each proposal uses a talent from another class in the same beta as a model (Warrior, Druid, Priest, Shaman, Hunter, Mage).
- **Rules.** The combat and mana values use Classic 1.12 rules when no test gives a different rule.
- **Estimates.** The burst values are estimates. The Reckoning, threat, mana, healing and damage values come from simple models, not combat logs. Each estimate gives its assumptions and limits.
- **Other classes.** The healing comparison uses the DoubleZug sheets for the four Forever healers, with the spell values of the Forever spellbook ([model](models/healing/)). The damage comparison uses the ratios of one external simulation ([MythicSim](https://mythicsim.com/wow-forever/tier-list)) and a same-gear model check.

## Feedback

Open an issue to send corrections, test results or other proposals.
