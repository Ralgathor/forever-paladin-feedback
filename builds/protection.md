# Protection: best tank build and stat weights

This file gives the best tank builds for the live trees and for the proposed trees of calculator version 6. It also gives the stat weights. All values come from wowsims Forever (see [README](README.md)).

## Summary

| Trees | Build | Points | Code | Threat each sec | With Righteous Fury (C25) | Damage taken each sec | TMI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Proposed | PT1 | 0/34/17 | [`v6p-3530110213501531-54233`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p-3530110213501531-54233) | 1,197 | 1,703 | 302 | 43.6 |
| Proposed | PS1 | 0/34/17 | [`v6p-3530110213501531-53233000001`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p-3530110213501531-53233000001) | 1,219 | 1,735 | 302 | 43.6 |
| Proposed | PI1 | 10/31/10 | [`v6p05005-3530110213201531-5023`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p05005-3530110213201531-5023) | 1,258 | 1,790 | 307 | 43.9 |
| Live | BS2 | 0/35/16 | [`b2-05302102313501531-52233000001`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2-05302102313501531-52233000001) | 1,150 | — | 335 | 53.1 |
| Live | BT1 | 12/32/7 | [`b2050050002-05302102213301531-502`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2050050002-05302102213301531-502) | 1,137 | — | 343 | 54.0 |
| Live | BS1 | 10/31/10 | [`b205005-05302102213201531-5023`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b205005-05302102213201531-5023) | 1,180 | — | 345 | 54.1 |

- **Righteous Fury (C25)** is a baseline spell change, not a talent. It multiplies all threat by 1.42 in wowsims (1.9 ÷ 1.33 on the threat multiplier, 1,722 ÷ 1,210 in the C25 run of Analysis, Threat, part 6). Thus, the build order and the stat order do not change. The C25 column uses this multiplier.
- **Proposed: PS1 is PT1 with Sacred Arbiter.** One Benediction point goes to Sacred Arbiter: +1.9% threat, the same damage taken and the same TMI. PT1 is the tank of Analysis, Builds.
- **Proposed: PI1 is the threat choice.** Divine Strength and Improved Seals give +3.2% threat against PS1, but 1.6% more damage taken and a 0.7% worse TMI.
- **Live: BS2 is the tank build.** It takes Sacred Arbiter and Sanctified Judgement 3. Against the wowsims default build BT1, it has +1.1% threat, 2.2% less damage taken and a 1.8% better TMI.
- **Live: BS1 is the threat choice.** It has +2.6% threat against BS2, but 2.9% more damage taken and a 2.0% worse TMI.
- **Proposed against live.** PT1 has +4.1% threat, 10% less damage taken and an 18% better TMI than BS2. PS1 has +6.0% threat. With Righteous Fury (C25), PT1 has +48% threat against BS2. Redoubt (C-P1) removes almost all crushing blows: 1.2% against 11.9%.
- **Stat weights.** For threat, Expertise rating is the best stat for each point, then spell damage. For survival, Stamina, Defense rating and Block value (proposed trees) are the best (part 3).

**Survival set.** The table above uses the item pool threat set. The same builds with the item pool survival set ([wowsims link](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-surv-protection-paladin.html), Analysis, Threat, part 6):

| Trees | Build | Threat each sec | With Righteous Fury (C25) | Damage taken each sec | TMI |
| --- | --- | --- | --- | --- | --- |
| Proposed | PT1 | 1,148 | 1,635 | 292 | 36.7 |
| Proposed | PS1 | 1,172 | 1,668 | 292 | 36.7 |
| Proposed | PI1 | 1,201 | 1,709 | 296 | 36.9 |
| Live | BS2 | 1,099 | — | 326 | 44.9 |
| Live | BT1 | 1,081 | — | 333 | 45.8 |
| Live | BS1 | 1,112 | — | 335 | 46.0 |

- **The build order does not change.** All builds have 4–6% less threat and a 15–16% better TMI than with the threat set.
- **PI1 against PS1:** +2.5% threat, 1.4% more damage taken and a 0.6% worse TMI.
- **PT1 against BS2:** +4.5% threat, 11% less damage taken and an 18% better TMI.
- **Stat weights** with the survival set (`models/wowsims-b2/logs/finals_surv.log`). For threat, Expertise rating is still the best stat, but Hit rating is second: the survival set has less Hit. For survival, Stamina and Defense rating stay the best.

## 1. Method

- **Sim.** wowsims Forever, master of 4 November 2026 (commit 9a8624af9, game files of client 1.60.1.70755 and the hotfixes of 4 November, Holy Shield rank 4), with `models/wowsims-b2/patches/talents-9a8624af9.patch`. The proposed trees use the flags of all kept proposals: Redoubt (C-P1) and Toughness removal (C-P13). The talent search ran on master of 1 November (commit 895cd67f9), with the Holy Strike Seal trigger (C1), withdrawn on 2 November 2026. The builds and stat weights then ran again on commit 9a8624af9 without it, with the item pool set and tank consumables.
- **Fight.** 3 min, one level 63 boss that attacks the Paladin from the front. Full buffs. Tank consumables: the consumables of the Warrior test of wowsims, with Greater Arcane Elixir and Brilliant Wizard Oil (Analysis, Threat, part 6). 3,000 iterations, the same random seed for all runs.
- **Gear and rotation.** The item pool Protection set of Analysis, Threat, part 6 ([wowsims link](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-pool-protection-paladin.html)): no raid, PvP or high reputation items. The default rotation of wowsims Forever. The talent search ran with the wowsims default set, which has raid, PvP and reputation items. With the default set, PT1 had 1,056 threat each sec, 295 damage taken each sec and a TMI of 45.3, and BS2 had 1,006, 331 and 56.3. The build order does not change.
- **TMI.** The damage intake value of wowsims with a 6 sec window: less is better.
- **Talent search.** A hill climb (`models/wowsims-b2/search.py`) with moves of 1 point into a talent with tank value, at 1,000 iterations. The score is 40% threat, 20% damage, 20% damage taken and 20% TMI, each against the start build. The best builds then run at 3,000 iterations. The logs are `search_prot*.log`.
- **Starts.** BT1 and BS2 for the live trees. PT1 for the proposed trees.
- **Limit of the search.** A move of 1 or 2 points cannot reach a talent in a far row. Sacred Arbiter is in Retribution row 4 and needs 15 Retribution points first. Thus, BS2 is a hand-made start: the search from BS2 found no better move. Improved Seals needs 5 Holy points first, thus the search does not find a Holy dip. PI1 is a hand-made check (part 2).

## 2. Builds

### Proposed: PT1, PS1 and PI1

[`v6p-3530110213501531-54233`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p-3530110213501531-54233) (0/34/17).

- Protection: Divine Intellect 3, Redoubt 5, Precision 3, Sacred Duty 1, Templar's Bulwark, Shield Specialization 2, Swift Judgement, Improved Righteous Fury 3, Anticipation 5, Holy Shield, Reckoning 5, Iron Creed 3, Shieldsworn.
- Retribution: Deflection 5, Benediction 4, Improved Judgement 2, Conviction 3, Sanctified Judgement 3.
- **Dungeon tank** ([`v6p-353011021350153102-52233`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p-353011021350153102-52233), 0/36/15): Reach of Law 2 in place of Benediction 2. Judgement and Swift Judgement then pull from 20 yards with Seal of Fury. wowsims does not model the pull, and the raid values do not change.
- **PS1** ([`v6p-3530110213501531-53233000001`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p-3530110213501531-53233000001)): Benediction 3 and Sacred Arbiter in place of Benediction 4.
- **Deflection 5, not Benediction 5.** After Improved Judgement, Conviction and Sanctified Judgement, 9 points stay for Deflection and Benediction. One point in Deflection gives 1.5% less damage taken. One point in Benediction gives 0.3% more threat. With Benediction 5 and Deflection 4, PT1 has 1,200 threat each sec, 306 damage taken each sec and a TMI of 43.9.
- **Improved Seals (PI1, threat choice).** Divine Strength 5 and Improved Seals 5 cost 10 points. The best points to give up, against PS1: 3 Anticipation points, Benediction 3, Sanctified Judgement 3 and Sacred Arbiter. PI1 is 10/31/10, [`v6p05005-3530110213201531-5023`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p05005-3530110213201531-5023). Against PS1, it has +3.2% threat (1,258 each sec), but 1.6% more damage taken (307) and a 0.7% worse TMI (43.9). It is the same trade as BS1 in the live trees. On 1 November (Holy Shield rank 3, default set), other places cost more. Anticipation 3 gave 1,020 / 300 / 46.1, and Retribution 7 (Deflection 5, Improved Judgement 2) gave 990 / 296 / 45.8.

### Live: BS2

[`b2-05302102313501531-52233000001`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2-05302102313501531-52233000001) (0/35/16).

- Protection: Redoubt 5, Precision 3, Sacred Duty 2, Templar's Bulwark, Shield Specialization 2, Toughness 3, Swift Judgement, Improved Righteous Fury 3, Anticipation 5, Holy Shield, Reckoning 5, Iron Creed 3, Shieldsworn.
- Retribution: Deflection 5, Benediction 2, Improved Judgement 2, Conviction 3, Sanctified Judgement 3, Sacred Arbiter.
- **Sacred Arbiter.** Holy Strike does +20% damage and refreshes the Judgements on the target. On 1 November (Holy Shield rank 3, default set), Toughness 4 in its place gave 936 threat each sec, 326 damage taken each sec and a TMI of 55.7.
- **Sanctified Judgement, not Benediction.** The build with Benediction 5 in place of Benediction 2 and Sanctified Judgement 3 was tested. On 1 November (Holy Shield rank 3, default set), it had 957 threat each sec, 329 damage taken each sec and a TMI of 56.4. Sanctified Judgement gives more mana, thus Holy Shield is active for a longer time.
- **No Holy points.** The 16 Retribution points leave no points for Holy. Divine Strength and Improved Seals give less than Sacred Arbiter and the Protection talents.

### Live: BT1 and BS1

[`b2050050002-05302102213301531-502`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2050050002-05302102213301531-502) (12/32/7).

- Holy: Divine Strength 5, Improved Seals 5, Holy Conduit 2.
- Protection: Redoubt 5, Precision 3, Sacred Duty 2, Templar's Bulwark, Shield Specialization 2, Toughness 2, Swift Judgement, Improved Righteous Fury 3, Anticipation 3, Holy Shield, Reckoning 5, Iron Creed 3, Shieldsworn.
- Retribution: Deflection 5, Improved Judgement 2.
- **BS1** ([`b205005-05302102213201531-5023`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b205005-05302102213201531-5023)): no Holy Conduit, Anticipation 2, and Conviction 3.
- **The tank build of the Analysis model** (B2T, 0/38/13, [`b2-25301102513501531-05233`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2-25301102513501531-05233)) gives 1,132 threat each sec and 354 damage taken each sec. Its TMI is 53.9.

## 3. Stat weights

Each stat + a small amount (20 Strength, Agility or Stamina, 40 spell damage, 10 rating, 20 Block value, 200 armor). The table gives the change for each point. A negative change of damage taken or TMI is better.

| Stat | BS2 threat | BS2 damage taken | BS2 TMI (10 points) | PT1 threat | PT1 damage taken | PT1 TMI (10 points) |
| --- | --- | --- | --- | --- | --- | --- |
| Strength | +0.34 | −0.01 | −0.01 | +0.33 | −0.01 | −0.02 |
| Agility | +0.16 | −0.31 | −0.25 | +0.23 | −0.30 | −0.32 |
| Stamina | +0.01 | 0 | −1.23 | 0 | 0 | −0.96 |
| Spell damage | +0.80 | −0.02 | −0.03 | +0.81 | −0.02 | −0.03 |
| Hit rating | +0.53 | −0.03 | −0.13 | +0.74 | +0.07 | +0.04 |
| Expertise rating | +1.50 | −0.25 | −0.42 | +1.70 | −0.21 | −0.38 |
| Defense rating | −0.20 | −0.72 | −1.11 | −0.31 | −0.57 | −0.59 |
| Block rating | +0.57 | −0.08 | −0.13 | +0.05 | +0.03 | +0.06 |
| Block value | −0.01 | −0.23 | −0.28 | 0 | −0.34 | −0.55 |
| Dodge rating | −0.22 | −0.36 | −0.32 | −0.21 | −0.39 | −0.39 |
| Parry rating | −0.14 | −0.33 | −0.17 | −0.16 | −0.32 | −0.28 |
| Armor | 0 | −0.03 | −0.05 | 0 | −0.02 | −0.04 |

- **Threat.** Expertise rating gives the most threat for each point. Spell damage gives about 2.4 times the threat of Strength, and Hit rating about 1.6 times (PT1: 2.2 times).
- **Survival.** Stamina gives the best TMI for each point. Defense rating gives the largest decrease of damage taken.
- **Block rating has almost no value with Redoubt (C-P1).** With Redoubt, about 61% of the boss swings are blocks. Misses, dodges, parries and blocks fill almost all of the attack table.
- **Dodge and parry cost threat with Redoubt.** Each dodge or parry takes the place of a block. Holy Shield and Reckoning need the blocks.
- **Block value has more value with Redoubt:** about 61% of the swings are blocks, without Redoubt about 41%.
- **Block rating has value without Redoubt.** Without Redoubt, only about 41% of the swings are blocks. Each point of Block rating gives +0.57 threat each sec and a small TMI gain. The BT1 weights are in `models/wowsims-b2/logs/finals.log`.

## 4. Limits

- The values come from wowsims, not from combat logs. wowsims does not model Lay on Hands.
- The talent search is a hill climb. It gives a good build, not a proven best build.
- The stat weights are for the item pool set. A change of gear changes them.
- One boss only. Dungeon enemies cannot hit with crushing blows. Thus, a dungeon tank has other choices (Analysis, Builds).
- The earlier values (trees of 18 October, with a gear search) are in the history of the repository.
