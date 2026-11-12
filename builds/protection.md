# Protection: best tank build and stat weights

This file gives the best tank builds for the live trees and for the proposed trees of calculator version 6. It also gives the stat weights. All values come from wowsims Forever (see [README](README.md)).

## Summary

| Trees | Build | Points | Code | Threat each sec | With Righteous Fury (C25) | Damage taken each sec | TMI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Proposed | PT1 | 0/34/17 | [`v6p-3530110213501531-54233`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p-3530110213501531-54233) | 1,195 | 1,702 | 295 | 41.1 |
| Proposed | PS1 | 0/34/17 | [`v6p-3530110213501531-53233000001`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p-3530110213501531-53233000001) | 1,219 | 1,735 | 295 | 41.1 |
| Proposed | PI1 | 10/31/10 | [`v6p05005-3530110213201531-5023`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p05005-3530110213201531-5023) | 1,255 | 1,787 | 301 | 41.5 |
| Live | BS2 | 0/35/16 | [`b2-05302102313501531-52233000001`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2-05302102313501531-52233000001) | 1,147 | — | 328 | 49.9 |
| Live | BT1 | 12/32/7 | [`b2050050002-05302102213301531-502`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2050050002-05302102213301531-502) | 1,133 | — | 336 | 51.0 |
| Live | BS1 | 10/31/10 | [`b205005-05302102213201531-5023`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b205005-05302102213201531-5023) | 1,171 | — | 338 | 51.2 |

- **Righteous Fury (C25)** is a baseline spell change, not a talent. It multiplies all threat by 1.42 in wowsims (1.9 ÷ 1.33 on the threat multiplier). In the C25 run of Analysis, Threat, part 6, on commit 52471a100, it is 1,720 ÷ 1,208. Thus, the build order and the stat order do not change. The C25 column uses this multiplier.
- **Proposed: PS1 is PT1 with Sacred Arbiter.** One Benediction point goes to Sacred Arbiter: +2.0% threat, the same damage taken and the same TMI. PT1 is the tank of Analysis, Builds.
- **Proposed: PI1 is the threat choice.** Divine Strength and Improved Seals give +3.0% threat against PS1, but 2.0% more damage taken and a 1.0% worse TMI.
- **Live: BS2 is the tank build.** It takes Sacred Arbiter and Sanctified Judgement 3. Against the wowsims default build BT1, it has +1.2% threat, 2.5% less damage taken and a 2.0% better TMI.
- **Live: BS1 is the threat choice.** It has +2.1% threat against BS2, but 3.0% more damage taken and a 2.4% worse TMI.
- **Proposed against live.** PT1 has +4.2% threat against BS2, 10% less damage taken and an 18% better TMI. PS1 has +6.3% threat. With Righteous Fury (C25), PT1 has +48% threat against BS2. Redoubt (C-P1) removes almost all crushing blows: 1.2% against 11.9%. Since commit 3633d376a (11 November), wowsims applies the block proc of Argent Defender only on a proc, as the item text tells. Before, the sim applied it all the time, by error. Thus, the live builds have 4.5% less threat and 6–7% more damage taken than on 9 November, and the gap is larger.
- **Stat weights.** For threat, Expertise rating is the best stat for each point, then Hit rating and spell damage. For survival, Stamina, Defense rating and Block value (proposed trees) are the best (part 3).

**Survival set.** The table above uses the item pool threat set. The same builds with the item pool survival set ([wowsims link](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-surv-protection-paladin.html), Analysis, Threat, part 6):

| Trees | Build | Threat each sec | With Righteous Fury (C25) | Damage taken each sec | TMI |
| --- | --- | --- | --- | --- | --- |
| Proposed | PT1 | 1,142 | 1,625 | 283 | 36.5 |
| Proposed | PS1 | 1,164 | 1,657 | 283 | 36.5 |
| Proposed | PI1 | 1,190 | 1,695 | 287 | 36.9 |
| Live | BS2 | 1,095 | — | 316 | 44.6 |
| Live | BT1 | 1,082 | — | 323 | 45.7 |
| Live | BS1 | 1,093 | — | 325 | 45.8 |

- **The build order of the proposed trees does not change.** All builds have 4–7% less threat, 4% less damage taken and a 10–11% better TMI than with the threat set. In the live trees, BS2 has more threat than BS1 with this set (+0.2%).
- **PI1 against PS1:** +2.3% threat, 1.6% more damage taken and a 1.2% worse TMI.
- **PT1 against BS2:** +4.2% threat, 10% less damage taken and an 18% better TMI.
- **Stat weights** with the survival set, on commit ae9b8c23a (`models/wowsims-b2/logs/finals_surv_ae9b8c23a.log`). For threat, Expertise rating is still the best stat, then Hit rating. For survival, Stamina and Defense rating stay the best.

## 1. Method

- **Sim.** wowsims Forever, master of 12 November 2026 (commit 52471a100, hotfixes of 11 and 12 November, client 1.60.1.70888, Holy Shield rank 4). It has the patches of `models/wowsims-b2/patches`. The proposed trees use the flags of all kept proposals: Redoubt (C-P1) and Toughness removal (C-P13). The talent search ran on master of 1 November (commit 895cd67f9), with the Holy Strike Seal trigger (C1), withdrawn on 2 November 2026. The builds and stat weights then ran again on commit 52471a100 without it, with the item pool sets of 11 November and tank consumables. The search of 12 November keeps the Paladin sets. The values do not change.
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
- **Deflection 5, not Benediction 5.** After Improved Judgement, Conviction and Sanctified Judgement, 9 points stay for Deflection and Benediction. One point in Deflection gives 1.5% less damage taken. One point in Benediction gives 0.3% more threat. With Benediction 5 and Deflection 4, PT1 has 1,200 threat each sec, 300 damage taken each sec and a TMI of 41.4.
- **Improved Seals (PI1, threat choice).** Divine Strength 5 and Improved Seals 5 cost 10 points. The best points to give up, against PS1: 3 Anticipation points, Benediction 3, Sanctified Judgement 3 and Sacred Arbiter. PI1 is 10/31/10, [`v6p05005-3530110213201531-5023`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p05005-3530110213201531-5023). Against PS1, it has +3.0% threat (1,255 each sec), but 2.0% more damage taken (301) and a 1.0% worse TMI (41.5). It is the same trade as BS1 in the live trees. On 1 November (Holy Shield rank 3, default set), other places cost more. Anticipation 3 gave 1,020 / 300 / 46.1, and Retribution 7 (Deflection 5, Improved Judgement 2) gave 990 / 296 / 45.8.

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
- **The tank build of the Analysis model** (B2T, 0/38/13, [`b2-25301102513501531-05233`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2-25301102513501531-05233)) gives 1,129 threat each sec and 345 damage taken each sec. Its TMI is 50.5.

## 3. Stat weights

Each stat + a small amount (20 Strength, Agility or Stamina, 40 spell damage, 10 rating, 20 Block value, 200 armor). The table gives the change for each point. A negative change of damage taken or TMI is better.

| Stat | BS2 threat | BS2 damage taken | BS2 TMI (10 points) | PT1 threat | PT1 damage taken | PT1 TMI (10 points) |
| --- | --- | --- | --- | --- | --- | --- |
| Strength | +0.33 | −0.01 | −0.01 | +0.32 | −0.01 | −0.02 |
| Agility | +0.20 | −0.35 | −0.31 | +0.08 | −0.37 | −0.36 |
| Stamina | +0.02 | +0.01 | −1.13 | −0.01 | −0.01 | −0.88 |
| Spell damage | +0.79 | −0.02 | −0.02 | +0.79 | −0.02 | −0.03 |
| Hit rating | +0.79 | −0.09 | −0.05 | +0.74 | −0.01 | −0.13 |
| Expertise rating | +1.57 | −0.08 | −0.27 | +1.46 | −0.24 | −0.44 |
| Defense rating | −0.14 | −0.71 | −0.89 | −0.51 | −0.66 | −0.63 |
| Block rating | +0.61 | −0.03 | −0.19 | +0.01 | −0.03 | −0.06 |
| Block value | +0.01 | −0.23 | −0.27 | 0 | −0.34 | −0.54 |
| Dodge rating | −0.19 | −0.41 | −0.29 | −0.40 | −0.46 | −0.40 |
| Parry rating | −0.14 | −0.39 | −0.33 | −0.31 | −0.37 | −0.31 |
| Armor | 0 | −0.02 | −0.05 | 0 | −0.02 | −0.04 |

- **Threat.** Expertise rating gives the most threat for each point. Hit rating and spell damage give 2.3–2.5 times the threat of Strength.
- **Survival.** Stamina gives the best TMI for each point, with and without Redoubt. Defense rating gives the largest decrease of damage taken.
- **Block rating has almost no value with Redoubt (C-P1).** With Redoubt, about 61% of the boss swings are blocks. Misses, dodges, parries and blocks fill almost all of the attack table.
- **Dodge and parry cost threat with Redoubt.** Each dodge or parry takes the place of a block. Holy Shield and Reckoning need the blocks.
- **Block value has more value with Redoubt:** about 61% of the swings are blocks, without Redoubt about 41%.
- **Block rating has value without Redoubt.** Without Redoubt, only about 41% of the swings are blocks. Each point of Block rating gives +0.61 threat each sec and a small TMI gain. The BT1 weights are in `models/wowsims-b2/logs/finals.log`.

## 4. Limits

- The values come from wowsims, not from combat logs. wowsims does not model Lay on Hands.
- The talent search is a hill climb. It gives a good build, not a proven best build.
- The stat weights are for the item pool set. A change of gear changes them.
- One boss only. Dungeon enemies cannot hit with crushing blows. Thus, a dungeon tank has other choices (Analysis, Builds).
- The earlier values (trees of 18 October, with a gear search) are in the history of the repository.
