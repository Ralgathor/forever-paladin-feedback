# Retribution: best damage build and stat weights

This file gives the best damage builds on one target. It uses the live trees and the proposed trees of calculator version 6. It also gives the stat weights. All values come from wowsims Forever (see [README](README.md)).

## Summary

| Trees | Case | Build | Points | Code | DPS |
| --- | --- | --- | --- | --- | --- |
| Live | Raid | RB1 | 14/6/31 | [`b2050250002-501-05233011201301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2050250002-501-05233011201301351) | 910 |
| Proposed | Raid | RB1 | 14/6/31 | [`v6p050250002-501-05233011201301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p050250002-501-05233011201301351) | 910 |
| Live | Fresh 60 | RB1 | 14/6/31 | [`b2050250002-501-05233011201301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2050250002-501-05233011201301351) | 303 |
| Proposed | Fresh 60 | RB1 | 14/6/31 | [`v6p050250002-501-05233011201301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p050250002-501-05233011201301351) | 315 |

- **RB1 is the best build in all four cases.** It is the wowsims default build of 1 November and RB1 of Analysis, Builds. The talent search found raid builds with at most +0.6%. These builds are 2–5% worse at fresh 60 (part 2).
- **"Raid"** is full raid buffs and debuffs, with consumables. **"Fresh 60"** is no buffs, no debuffs and no consumables.
- **Proposed against live.** Only Reverence 50% (C-H1) changes Retribution damage: +4.1% at fresh 60 (more mana), and 0% in a raid.
- **Stat weights.** In a raid, Expertise rating is the best stat for each point (2.1 Strength). Crit rating and Haste rating are about 1 Strength. At fresh 60, Haste rating and Intellect have more value (part 3).

## 1. Method

- **Sim.** wowsims Forever, master of 1 November 2026 (commit 895cd67f9), with `models/wowsims-b2/patches/talents.patch`. The proposed trees use the flag REV50 (Reverence 25/50%). The other kept proposals do not change Retribution damage. The talent search ran with earlier flags: Reverence 30% and the Holy Strike Seal trigger (C1, withdrawn on 2 November 2026). The builds and stat weights then ran again with REV50 only.
- **910 against 906.** This file uses 3 min fights: 910 DPS in a raid. Analysis, Damage uses the 2 min wowsims test run: 906 DPS. Both use the default set and master of 1 November. Build 70755 (3 November 2026) gives 981 DPS in the 2 min run (Beta test results).
- **Fight.** 3 min, one level 63 boss, 3,000 iterations, the same random seed for all runs.
- **Gear and rotation.** The default Retribution gear set and the default rotation of wowsims Forever. This folder has no gear search.
- **Talent search.** A hill climb (`models/wowsims-b2/search.py`). Each step tests all moves of 1 point into a talent with damage value, at 1,000 iterations. It keeps the best move. A round with moves of 2 points then tests the best moves at 250 iterations, and the 6 best again at 2,000. The best builds then run at 3,000 iterations. The logs are `search_ret-*.log`.
- **Starts.** RB1 and the earlier wowsims build (14/5/32, [`b2050250002-5-05233301101301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2050250002-5-05233301101301351)) for the raid. RB1 and the best raid builds for fresh 60.

## 2. Builds

### RB1

[`v6p050250002-501-05233011201301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p050250002-501-05233011201301351) (14/6/31).

- Holy: Divine Strength 5, Reverence 2, Improved Seals 5, Holy Conduit 2.
- Protection: Divine Intellect 5, Precision 1.
- Retribution: Benediction 5, Improved Judgement 2, Conviction 3, Sanctified Judgement 3, Unyielding Faith 1, Seal of Command, Pursuit of Justice 2, Sacred Arbiter, Two-Handed Weapon Specialization 3, Repentance, Vengeance 3, Champion of the Light 5, Unsealed Wrath.

### Search builds

| Build | Trees | Code | Raid | Fresh 60 | Change against RB1 |
| --- | --- | --- | --- | --- | --- |
| RS1, 12/8/31 | Live | [`b2050150001-503-15233011101301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2050150001-503-15233011101301351) | 916 (+0.6%) | 288 (−5.0%) | Reverence 1, Holy Conduit 1, Pursuit of Justice 1, Precision 3, Deflection 1 |
| RS2, 13/7/31 | Proposed | [`v6p050150002-502-05233011201301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p050150002-502-05233011201301351) | 913 (+0.2%) | — | Reverence 1, Precision 2 |
| RS3, 12/8/31 | Proposed | [`v6p050050002-503-15233011101301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p050050002-503-15233011101301351) | — | 296 (−6.2%) | Reverence 0, Pursuit of Justice 1, Precision 3, Deflection 1 |

- **Precision is the only gain in a raid.** The raid buffs fill the mana. Thus, the search moves Reverence points to Precision 3.
- **At fresh 60, Reverence has value.** With no buffs, RB1 has no mana for 69 sec of the 3 min fight. RS1 has no mana for 88 sec.
- **The gain is small.** +0.6% is 5 DPS. A tank or a boss with more armor can change the order. Thus, RB1 stays the main build.
- Unyielding Faith 1 and Pursuit of Justice give no damage. They fill the rows to Unsealed Wrath (Analysis, Builds, part 4).

## 3. Stat weights

Each stat + a small amount (20 Strength, Agility or Intellect, 40 spell damage or Attack Power, 10 rating). DPS gain for each point, divided by the gain of 1 Strength. Build RB1.

| Stat | Live, raid | Proposed, raid | Live, fresh 60 |
| --- | --- | --- | --- |
| DPS for 1 Strength | 0.50 | 0.50 | 0.23 |
| Strength | 1.00 | 1.00 | 1.00 |
| Agility | 0.73 | 0.74 | 0.64 |
| Intellect | 0.61 | 0.61 | 1.49 |
| Spell damage | 0.80 | 0.80 | 0.82 |
| Attack Power | 0.41 | 0.41 | 0.44 |
| Hit rating | 0.48 | 0.44 | 0.22 |
| Crit rating | 1.03 | 1.03 | 0.93 |
| Haste rating | 1.13 | 1.13 | 2.22 |
| Expertise rating | 2.06 | 2.06 | 1.02 |

- **Expertise rating** has the most value for each point in a raid: 2.1 Strength.
- **Spell damage is 0.8 Strength.** Seals, Judgements, Holy Strike and Consecration use spell damage.
- **Hit rating has a low value with the default gear.** Each point gives less than half of 1 Strength.
- **At fresh 60, mana limits the damage.** Intellect is 1.5 Strength and Haste rating is 2.2 Strength.

## 4. Limits

- The values come from wowsims, not from combat logs. The wowsims rotation is the rotation of RB1.
- The talent search is a hill climb. It gives a good build, not a proven best build.
- The stat weights are for the default gear. A change of gear changes them.
- The earlier values (trees of 18 October, with a gear search) are in the history of the repository.
