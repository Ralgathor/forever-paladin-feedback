# Forever Paladin feedback

This project gives player feedback for the Paladin in **World of Warcraft: Forever**. It is not an official project. It is not related to Blizzard Entertainment.

## Contents

- **Proposals:** 11 changes and 1 move for the live trees. 3 changes are baseline spell changes (C2, C4, C5). Shoulder the Burden (C-P5) is a new baseline spell. 7 changes are talent changes (C-H1, C-P1, C-P7, C-P11, C-P13, C-P14, C-R3). Devoted Sacrifice (C-P11) and Reach of Law (C-P7) are new talents. One move: Stoicism to row 4, column 4 (M-P2).
- **Adopted proposals:** the live version of 4 November 2026 adopts 6 earlier proposals (C3, the C-H1 move, the C-P5 removal, C-R1, M-H5 and M-R1).
- **Talent calculator:** you can try the proposals and compare them with the live trees.
- **Analysis:** crushing blows, threat, PvP burst, mana, healing, damage, builds and tree balance, each with its model and limits.
- **Builds:** the main builds for each spec and role (raid, dungeon, PvP), with calculator version 6 codes (Analysis, Builds).
- **Best builds, gear and stat weights:** the best build, pre-raid gear and stat weights of each spec in wowsims Forever ([builds](builds/README.md)). This folder uses the trees of 18 October 2026 and calculator version 5.

## IDs

- **C2 to C5 (spell change):** the proposal changes a baseline spell, not a talent. Shoulder the Burden (C-P5) is also a new baseline spell.
- **C-H, C-P and C-R (talent change):** the proposal changes what a talent does, adds a talent or removes a talent. The letter after C gives the tree: H (Holy), P (Protection), R (Retribution).
- **M-H, M-P and M-R (move):** the proposal moves a talent to a different row. The talent text does not change.
- **Alternatives.** C2a is the alternative to C2. C-P11a is the alternative to the Lay on Hands part of C-P11.
- **New IDs.** A new proposal takes the next free number of its series. A new proposal never takes the number of a withdrawn proposal.
- **Names.** The text gives the name first and the ID in parentheses, for example Sanctified Judgement (C-R3).

## Changes

**Spell changes**

- **C2 Judgement of the Crusader:** a personal debuff. It does not count against the one-Judgement limit. C2a is the alternative.
- **C4 Hand of Sacrifice:** up to 825 damage moves to you (live: Blessing of Sacrifice, 55 damage for each hit, no cooldown). Lasts 30 sec, 15 sec cooldown.
- **C5 Hands:** Blessing of Sacrifice, Protection and Freedom become Hand of Sacrifice, Protection and Freedom. They use no Blessing slot. Each Paladin can have one Hand on a target.
- **C-P5 Shoulder the Burden (new baseline spell):** 50% of the threat of an ally moves to you. 5 min cooldown. All Paladins can learn it. It has no effect in PvP.

**Holy**

- **C-H1 Reverence 25/50% (live: 15/30%, row 2):** more mana regeneration during casts, as the healer talents of the other classes (50%). Holy heals 5–9% more, most in long fights. On one tank, the Paladin is 12–17% above the Druid (225% critical heal), below the 20% limit. It has no link to critical heals, thus it does not depend on the Holy Power test. Retribution also takes it: +4–5% damage at fresh level 60 without buffs (wowsims), 0% with raid buffs.

**Protection**

- **C-P1 Redoubt:** each Holy Shield cast also starts it. In wowsims, crushing blows decrease from 12.0% to 0.9% of the boss attacks (Warrior: 1.1%).
- **C-P7 Reach of Law (new, row 5, requires Swift Judgement):** +5/10 yards Judgement range with Seal of Fury, for a 20 yard pull in dungeons. Stoicism moves to row 4, column 4 (M-P2).
- **C-P11 Devoted Sacrifice (new, row 3):** Lay on Hands drains only 75/50% of your current mana (live: all of it). You also take 20/40% less damage from your Hand of Sacrifice. Alternative C-P11a: the spell drains 50% for all Paladins.
- **C-P13 Toughness:** removed. Devoted Sacrifice (C-P11) takes its place in row 3. With Reach of Law (C-P7), Protection has 48 points (live: 49).
- **C-P14 Swift Judgement:** no longer requires Templar's Bulwark. The two talents have different uses.

**Retribution**

- **C-R3 Sanctified Judgement:** each Judgement returns 20/40/60% of the Seal cost (live: a 33/66/100% chance).

**Adopted in the live version (4 November 2026)**

| ID | Proposal | What the live version does |
| --- | --- | --- |
| C3 | Blessing of Light: removed | Blessing of Light and Greater Blessing of Light are removed. Oath of Light (new Holy talent) gives their bonus on one ally |
| C-H1 (move) | Reverence to Holy row 2 | Reverence is in row 2. Its values are 15/30%. The 25/50% part is a proposal (C-H1) |
| C-P5 (removal) | Improved Seal of Fury: removed | Improved Seal of Fury is removed |
| C-R1 | Conviction: attacks and spells | Conviction gives 2/4/6% critical chance with all spells and attacks |
| M-H5 | Divine Precision: row 4, no requirement | Divine Precision is in row 4 with no requirement |
| M-R1 | Two-Handed Weapon Specialization: row 4 | Two-Handed Weapon Specialization is in row 4 |

## Read and try

- **[Proposals](proposals/README.md).** The full document, in one file for each part. For each proposal, it gives the live text, the proposed text, the reason and the model talent from another class. It also gives the analysis, the test results and the open questions.
- **[Talent calculator](calculator/index.html).** Live version: https://ralgathor.github.io/forever-paladin-feedback/calculator/
  - The calculator opens with the proposed trees of version 6 (31 October 2026). These trees change the live trees. Push **Live** to see the live trees.
  - A purple tag (C-P1, C-P11…) shows a changed or new talent.
  - **Build codes.** A code that starts with `v6p` opens a proposed build. A code that starts with `b2` opens a build in the live trees. A code with only digits is a build in the beta trees of 18 October 2026. It opens on the page of that beta: https://ralgathor.github.io/forever-paladin-feedback/calculator/beta1/
  - **Versions.** Use the Version list to open an earlier version of the proposed trees. Versions 1 to 5 use the beta trees of 18 October 2026. Each earlier version has a frozen page. A code of an earlier version opens on its page.

| Version | Date | Code starts with | Page |
| --- | --- | --- | --- |
| 6 (current) | 31 October 2026 | `v6p` | https://ralgathor.github.io/forever-paladin-feedback/calculator/ |
| 5 | 26 and 29 October 2026 | `v5p` | https://ralgathor.github.io/forever-paladin-feedback/calculator/v5/ |
| 4 | 24 October 2026 | `v4p` | https://ralgathor.github.io/forever-paladin-feedback/calculator/v4/ |
| 3 | 24 October 2026 | `v3p` | https://ralgathor.github.io/forever-paladin-feedback/calculator/v3/ |
| 2 | 23 October 2026 | `v2p` | https://ralgathor.github.io/forever-paladin-feedback/calculator/v2/ |
| 1 | Before 23 October 2026 | `p` | https://ralgathor.github.io/forever-paladin-feedback/calculator/v1/ |

The talent icons come from the Wowhead icon server (wow.zamimg.com). If the icons do not load, the calculator shows drawn icons. This project does not keep game files.

## Method

- **Data.** Forever client build 1.60.1.70707, hotfix push 113554 (live version). The talent data comes from the game files in wowsims Forever (branch `paladin/hotfix-113554-port`). Player tests give the talent behavior.
- **Earlier data.** The Analysis tabs use the live trees. The values of the beta of 18 October 2026 (client build 1.60.1.70450) are in Beta test results and in the history of the repository.
- **Model talents.** Each proposal uses a talent from another class in the same game version as a model (Warrior, Druid, Priest, Shaman, Hunter, Mage).
- **Rules.** The combat and mana values use Classic 1.12 rules when no test gives a different rule.
- **Estimates.** The burst values are estimates. The Reckoning, threat, mana, healing and damage values come from simple models, not combat logs. Each estimate gives its assumptions and limits.
- **Other classes.** The healing comparison uses the DoubleZug sheets for the four Forever healers, with the spell values of the Forever spellbook ([model](models/healing/)). The damage comparison uses the ratios of one external simulation ([MythicSim](https://mythicsim.com/wow-forever/tier-list)) and a same-gear model check.

## Models

| Folder | What it holds | Trees |
| --- | --- | --- |
| [models/healing](models/healing/) | Healing model (linear program) and recovery after a large hit (Monte Carlo) | Beta (18 October) |
| [models/threat](models/threat/) | Threat model, one enemy and groups of enemies | Beta (18 October) |
| [models/damage](models/damage/) | Retribution damage model | Beta (18 October) |
| [models/mana](models/mana/) | Protection mana model, one boss | Beta (18 October) |
| [models/wowsims](models/wowsims/) | wowsims Forever check of the proposals (calculator version 5) | Beta (18 October) |
| [models/beta-30-oct](models/beta-30-oct/) | The models of the Analysis tabs on the new trees | Live (30 October) |
| [models/wowsims-b2](models/wowsims-b2/) | wowsims Forever check of the kept proposals | Live (30 October) |

## Feedback

Open an issue to send corrections, test results or other proposals.
