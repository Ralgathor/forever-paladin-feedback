# Forever Paladin feedback

This project gives player feedback for the Paladin in **World of Warcraft: Forever**. It is not an official project. It is not related to Blizzard Entertainment.

## Contents

- **Proposals:** 18 changes (C1–C18) and 7 moves (M1–M7) for the Holy, Protection and Retribution trees. Three changes are new talents.
- **Talent calculator:** you can try the proposals and compare them with the beta trees.

## IDs

- **C (change):** the proposal changes what a talent does, adds a talent or removes a talent.
- **M (move):** the proposal moves a talent to a different row or column. The talent text does not change.

## Main changes

- **Protection: crushing blows (C6).** Each Holy Shield cast also starts Redoubt. The block chance stays high. Most crushing blows stop.
- **Protection: threat (C14).** Holy Shield damage increases with block value. Paladin threat then increases with gear, as Warrior and Druid threat does.
- **Protection: Reckoning (C11).** Block, dodge and parry also give charges. Holy Strike releases up to 2 charges.
- **Holy: mana and layout (C1, C4, M1–M3).** Reverence gives 17/33/50% mana regeneration while casting. It moves to row 2. Protection and Retribution can get it with 8 Holy points. Healing Light moves to row 6.

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
