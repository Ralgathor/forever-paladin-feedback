# Protection: best tank build and stat weights

This file gives the best tank builds for the live trees and for the proposed trees of calculator version 6. It also gives the stat weights. All values come from wowsims Forever (see [README](README.md)).

## Summary

| Trees | Build | Points | Code | Threat each sec | Damage taken each sec | TMI |
| --- | --- | --- | --- | --- | --- | --- |
| Proposed | PT1 | 0/34/17 | [`v6p-3530110213501531-54233`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p-3530110213501531-54233) | 1,012 | 292 | 45.0 |
| Proposed | PS1 | 0/34/17 | [`v6p-3530110213501531-53233000001`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p-3530110213501531-53233000001) | 1,033 | 292 | 45.0 |
| Live | BS2 | 0/35/16 | [`b2-05302102313501531-52233000001`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2-05302102313501531-52233000001) | 953 | 325 | 55.5 |
| Live | BT1 | 12/32/7 | [`b2050050002-05302102213301531-502`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2050050002-05302102213301531-502) | 928 | 333 | 57.1 |
| Live | BS1 | 10/31/10 | [`b205005-05302102213201531-5023`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b205005-05302102213201531-5023) | 975 | 342 | 58.5 |

- **Proposed: PS1 is PT1 with Sacred Arbiter.** One Benediction point goes to Sacred Arbiter: +2.1% threat, the same damage taken and the same TMI. PT1 is the tank of Analysis, Builds.
- **Live: BS2 is the tank build.** It takes Sacred Arbiter (+2.2% threat) and Sanctified Judgement 3. Against the wowsims default build BT1, it has +2.7% threat, 2.4% less damage taken and a 2.7% better TMI.
- **Live: BS1 is the threat choice.** It has +2.3% threat against BS2, but 5.1% more damage taken and a 5.2% worse TMI.
- **Proposed against live.** PT1 has +6.1% threat, 10% less damage taken and a 19% better TMI than BS2. Redoubt (C-P1) removes almost all crushing blows: 1.0% against 11.9%.
- **Stat weights.** For threat, Expertise rating and Hit rating are the best stats for each point. For survival, Stamina, Defense rating and Block value (proposed trees) are the best (part 3).

## 1. Method

- **Sim.** wowsims Forever, master of 1 November 2026 (commit 895cd67f9), with `models/wowsims-b2/talents.patch`. The proposed trees use the flags of all kept proposals: the Holy Strike Seal trigger (C1), Redoubt (C-P1) and Toughness removal (C-P13). Reckoning (C-P12) was withdrawn on 2 November 2026: the values do not include it.
- **Fight.** 3 min, one level 63 boss that attacks the Paladin from the front. Full buffs and consumables. 3,000 iterations, the same random seed for all runs.
- **Gear and rotation.** The default Protection gear set and the default rotation of wowsims Forever. This folder has no gear search.
- **TMI.** The damage intake value of wowsims with a 6 sec window: less is better.
- **Talent search.** A hill climb (`models/wowsims-b2/search.py`) with moves of 1 point into a talent with tank value, at 1,000 iterations. The score is 40% threat, 20% damage, 20% damage taken and 20% TMI, each against the start build. The best builds then run at 3,000 iterations. The logs are `search_prot*.log`.
- **Starts.** BT1 and BS2 for the live trees. PT1 for the proposed trees.
- **Limit of the search.** A move of 1 or 2 points cannot reach a talent in a far row. Sacred Arbiter is in Retribution row 4 and needs 15 Retribution points first. Thus, BS2 is a hand-made start: the search from BS2 found no better move.

## 2. Builds

### Proposed: PT1 and PS1

[`v6p-3530110213501531-54233`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p-3530110213501531-54233) (0/34/17).

- Protection: Divine Intellect 3, Redoubt 5, Precision 3, Sacred Duty 1, Templar's Bulwark, Shield Specialization 2, Swift Judgement, Improved Righteous Fury 3, Anticipation 5, Holy Shield, Reckoning 5, Iron Creed 3, Shieldsworn.
- Retribution: Deflection 5, Benediction 4, Improved Judgement 2, Conviction 3, Sanctified Judgement 3.
- **Dungeon tank** ([`v6p-353011021350153102-52233`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p-353011021350153102-52233), 0/36/15): Reach of Law 2 in place of Benediction 2. Judgement and Swift Judgement then pull from 20 yards with Seal of Fury. wowsims does not model the pull, and the raid values do not change.
- **PS1** ([`v6p-3530110213501531-53233000001`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p-3530110213501531-53233000001)): Benediction 3 and Sacred Arbiter in place of Benediction 4.
- **Deflection 5, not Benediction 5.** After Improved Judgement, Conviction and Sanctified Judgement, 9 points stay for Deflection and Benediction. One point in Deflection gives 1.3% less damage taken. One point in Benediction gives 0.2% more threat. With Benediction 5 and Deflection 4, PT1 has 1,014 threat each sec, 295 damage taken each sec and a TMI of 45.2.
- **Without the Holy Strike Seal trigger (C1),** PT1 has 986 threat each sec and 291 damage taken each sec. Its TMI is 45.0 (Analysis, Builds).

### Live: BS2

[`b2-05302102313501531-52233000001`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2-05302102313501531-52233000001) (0/35/16).

- Protection: Redoubt 5, Precision 3, Sacred Duty 2, Templar's Bulwark, Shield Specialization 2, Toughness 3, Swift Judgement, Improved Righteous Fury 3, Anticipation 5, Holy Shield, Reckoning 5, Iron Creed 3, Shieldsworn.
- Retribution: Deflection 5, Benediction 2, Improved Judgement 2, Conviction 3, Sanctified Judgement 3, Sacred Arbiter.
- **Sacred Arbiter.** Holy Strike does +20% damage and refreshes the Judgements on the target. With Toughness 4 in its place, the build has 936 threat each sec, 326 damage taken each sec and a TMI of 55.7.
- **Sanctified Judgement, not Benediction.** With Benediction 5 in place of Benediction 2 and Sanctified Judgement 3, the build has 957 threat each sec, 329 damage taken each sec and a TMI of 56.4. Sanctified Judgement gives more mana, thus Holy Shield is active for a longer time.
- **No Holy points.** The 16 Retribution points leave no points for Holy. Divine Strength and Improved Seals give less than Sacred Arbiter and the Protection talents.

### Live: BT1 and BS1

[`b2050050002-05302102213301531-502`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2050050002-05302102213301531-502) (12/32/7).

- Holy: Divine Strength 5, Improved Seals 5, Holy Conduit 2.
- Protection: Redoubt 5, Precision 3, Sacred Duty 2, Templar's Bulwark, Shield Specialization 2, Toughness 2, Swift Judgement, Improved Righteous Fury 3, Anticipation 3, Holy Shield, Reckoning 5, Iron Creed 3, Shieldsworn.
- Retribution: Deflection 5, Improved Judgement 2.
- **BS1** ([`b205005-05302102213201531-5023`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b205005-05302102213201531-5023)): no Holy Conduit, Anticipation 2, and Conviction 3.
- **The tank build of the Analysis model** (B2T, 0/38/13, [`b2-25301102513501531-05233`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2-25301102513501531-05233)) gives 932 threat each sec and 340 damage taken each sec. Its TMI is 55.9.

## 3. Stat weights

Each stat + a small amount (20 Strength, Agility or Stamina, 40 spell damage, 10 rating, 20 Block value, 200 armor). The table gives the change for each point. A negative change of damage taken or TMI is better.

| Stat | BS2 threat | BS2 damage taken | BS2 TMI (10 points) | PT1 threat | PT1 damage taken | PT1 TMI (10 points) |
| --- | --- | --- | --- | --- | --- | --- |
| Strength | +0.33 | −0.01 | −0.01 | +0.32 | −0.02 | −0.03 |
| Agility | +0.19 | −0.33 | −0.28 | +0.17 | −0.31 | −0.33 |
| Stamina | 0 | 0 | −1.36 | 0 | 0 | −1.05 |
| Spell damage | +0.70 | −0.02 | −0.03 | +0.74 | −0.02 | −0.03 |
| Hit rating | +1.02 | −0.14 | −0.03 | +1.39 | +0.01 | +0.01 |
| Expertise rating | +1.32 | −0.16 | −0.18 | +1.34 | −0.18 | −0.33 |
| Defense rating | −0.23 | −0.72 | −0.87 | −0.38 | −0.58 | −0.55 |
| Block rating | +0.39 | −0.10 | +0.24 | +0.05 | +0.03 | +0.02 |
| Block value | −0.01 | −0.24 | −0.29 | −0.01 | −0.34 | −0.60 |
| Dodge rating | −0.13 | −0.38 | −0.19 | −0.32 | −0.42 | −0.33 |
| Parry rating | −0.15 | −0.35 | −0.20 | −0.17 | −0.30 | −0.26 |
| Armor | 0 | −0.03 | −0.06 | 0 | −0.02 | −0.04 |

- **Threat.** Expertise rating and Hit rating give the most threat for each point. Spell damage gives about twice the threat of Strength.
- **Survival.** Stamina gives the best TMI for each point. Defense rating gives the largest decrease of damage taken.
- **Block rating has no value with Redoubt (C-P1).** With PT1, the boss swings already have 60.9% blocks. Misses, dodges, parries and blocks fill 97% of the attack table.
- **Dodge and parry cost threat with Redoubt.** Each dodge or parry takes the place of a block. Holy Shield and Reckoning need the blocks.
- **Block value has more value with Redoubt:** PT1 blocks 60.9% of the swings, BS2 only 42.5%.
- **Block rating has value without Redoubt.** BS2 blocks only 42.5% of the swings. Each point of Block rating gives +0.39 threat each sec, but a worse TMI. The BT1 weights are in `models/wowsims-b2/finals.log`.

## 4. Limits

- The values come from wowsims, not from combat logs. wowsims does not model Lay on Hands.
- The talent search is a hill climb. It gives a good build, not a proven best build.
- The stat weights are for the default gear. A change of gear changes them.
- One boss only. Dungeon enemies cannot hit with crushing blows. Thus, a dungeon tank has other choices (Analysis, Builds).
- The earlier values (trees of 18 October, with a gear search) are in the history of the repository.
