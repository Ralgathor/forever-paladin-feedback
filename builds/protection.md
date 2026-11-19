# Protection: best tank build and stat weights

This file gives the best tank builds for the live trees and for the proposed trees of calculator version 6. It also gives the stat weights. All values come from wowsims Forever (see [README](README.md)).

## Summary

| Trees | Build | Points | Code | Threat each sec | With Righteous Fury (C25) | Damage taken each sec | TMI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Proposed | PT1 | 0/34/17 | [`v6p-3530110213501531-54233`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p-3530110213501531-54233) | 1,465 | 2,086 | 249 | 31.8 |
| Proposed | PS1 | 0/34/17 | [`v6p-3530110213501531-53233000001`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p-3530110213501531-53233000001) | 1,497 | 2,132 | 249 | 31.8 |
| Proposed | PI1 | 10/31/10 | [`v6p05005-3530110213201531-5023`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p05005-3530110213201531-5023) | 1,546 | 2,202 | 255 | 32.2 |
| Live | BS2 | 0/35/16 | [`b2-05302102313501531-52233000001`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2-05302102313501531-52233000001) | 1,451 | — | 272 | 37.7 |
| Live | BT1 | 12/32/7 | [`b2050050002-05302102213301531-502`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2050050002-05302102213301531-502) | 1,439 | — | 278 | 38.5 |
| Live | BS1 | 10/31/10 | [`b205005-05302102213201531-5023`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b205005-05302102213201531-5023) | 1,481 | — | 279 | 38.6 |

- **Righteous Fury (C25)** is a baseline spell change, not a talent. It multiplies all threat by 1.42 in wowsims (1.9 ÷ 1.33 on the threat multiplier). In the C25 run of Analysis, Threat, part 6, on commit ad6b13af8, it is 2,050 ÷ 1,439. Thus, the build order and the stat order do not change. The C25 column uses this multiplier.
- **Proposed: PS1 is PT1 with Sacred Arbiter.** One Benediction point goes to Sacred Arbiter: +2.2% threat, the same damage taken and the same TMI. PT1 is the tank of Analysis, Builds.
- **Proposed: PI1 is the threat choice.** Divine Strength and Improved Seals give +3.3% threat against PS1, but 2.2% more damage taken and a 1.1% worse TMI.
- **Live: BS2 is the tank build.** It takes Sacred Arbiter and Sanctified Judgement 3. Against the wowsims default build BT1, it has +0.8% threat, 2.1% less damage taken and a 2.1% better TMI.
- **Live: BS1 is the threat choice.** It has only +2.1% threat against BS2, but 2.8% more damage taken and a 2.4% worse TMI.
- **Proposed against live.** PT1 has +1.0% threat against BS2, 8% less damage taken and a 15% better TMI. PS1 has +3.1% threat. With Righteous Fury (C25), PT1 has +44% threat against BS2. Redoubt (C-P1) removes almost all crushing blows: 1.1% against 10.2%.

  Since commit 8c7b5a5f5 (13 November), each melee attack against the Paladin rolls the live Redoubt, avoided attacks included. Thus, with the same set, the live BT1 takes 2.4% less damage than on 12 November. The item pool set of 13 November (Draconian Deflector, The Lion Horn of Stormwind) takes 4% less damage again. Thus, the gap is smaller. Commit 6084403a9 (15 November) gives all builds about +1% threat, and the damage taken does not change. The open search set of 16 November gives all builds 1–3% more threat and 5% less damage taken. The full threat consumables of 17 November give all builds 18–19% more threat and 1–2% less damage taken (Flask of Supreme Power, Elixir of Holy Power and other spell power items). Commit ad6b13af8 (18 November) and its new item pool sets give all builds about 1% less threat, 2% less damage taken and a 5–6% better TMI. The enchants of 18 November evening give all builds 5–6% more threat, about 4% less damage taken and an 11–12% better TMI (Analysis, Threat, part 6). Before, the Paladin sets had no enchants. On 19 November, Crusader replaces Revelation on the weapon (no Protection ability procs Revelation in the game). All builds then have 1.5–2.2% less threat, and the damage taken and the TMI change by 1% or less. The runs with Revelation are in `models/wowsims-b2/logs/finals_full_revelation.log` and `finals_surv_full_revelation.log`.
- **Stat weights.** For threat, Expertise rating is the best stat for each point, then Hit rating and spell damage. Crit rating gives about 1.7–1.8 times the threat of Strength. For survival, Stamina, Defense rating and Block value (proposed trees) are the best (part 3).

**Survival set.** The table above uses the item pool threat set of 18 November, with the enchants of 18 November evening and Crusader on the weapon (19 November). The same builds with the item pool survival set of 19 November, with 5 pieces of Deathbone Guardian ([wowsims link](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-surv-protection-paladin.html), Analysis, Threat, part 6):

| Trees | Build | Threat each sec | With Righteous Fury (C25) | Damage taken each sec | TMI |
| --- | --- | --- | --- | --- | --- |
| Proposed | PT1 | 1,251 | 1,782 | 199 | 24.0 |
| Proposed | PS1 | 1,277 | 1,819 | 199 | 24.0 |
| Proposed | PI1 | 1,319 | 1,879 | 203 | 24.2 |
| Live | BS2 | 1,261 | — | 205 | 25.5 |
| Live | BT1 | 1,247 | — | 211 | 26.3 |
| Live | BS1 | 1,295 | — | 214 | 26.6 |

- **The build order of the proposed trees does not change.** All builds have 13–15% less threat, 20–25% less damage taken and a 25–32% better TMI than with the threat set. The survival set has Greater Stoneshield Potion (+2,000 armor). In the live trees, BS1 has 2.7% more threat than BS2 with this set too. Before 19 November, without Deathbone Guardian, all builds had 3–5% more threat and took 3–8% more damage.
- **PI1 against PS1:** +3.3% threat, 2.2% more damage taken and a 1.1% worse TMI.
- **PT1 against BS2:** −0.7% threat, 3% less damage taken and a 6% better TMI.
- **Stat weights** with the survival set, on commit ad6b13af8 (`models/wowsims-b2/logs/finals_surv_full.log`). For threat, Expertise rating and Hit rating are the best stats (PT1: +1.67 and +1.52 for each point). For survival, Stamina, Defense rating and Block value stay the best.

## 1. Method

- **Sim.** wowsims Forever, master of 18 November 2026 (commit ad6b13af8, hotfixes of 16 and 17 November, Holy Shield rank 4). It has the patches of `models/wowsims-b2/patches`. wowsims itself now has the ranged judgements of the hotfixes of 11 November. The proposed trees use the flags of all kept proposals: Redoubt (C-P1) and Toughness removal (C-P13). The talent search ran on master of 1 November (commit 895cd67f9), with the Holy Strike Seal trigger (C1), withdrawn on 2 November 2026. The builds and stat weights then ran again on commit ad6b13af8 without it. They use the item pool sets of the open search of 18 November, the full threat consumables of 17 November and the enchants of 18 November evening (Analysis, Threat, part 6). The runs without the enchants are in `models/wowsims-b2/logs/finals_full_no_enchants.log` and `finals_surv_full_no_enchants.log`. The runs on commit 6084403a9 are in `models/wowsims-b2/logs/finals_full_6084403a9.log` and `finals_surv_full_6084403a9.log`.
- **Fight.** 3 min, one level 63 boss that attacks the Paladin from the front. Full buffs. Full threat consumables of 17 November, for example Flask of Supreme Power, Lobster Stew and Elixir of Holy Power (Analysis, Threat, part 6). The runs with the consumables of 16 November are in `models/wowsims-b2/logs/finals.log` and `finals_surv.log`. 3,000 iterations, the same random seed for all runs.
- **Gear and rotation.** The item pool Protection set of Analysis, Threat, part 6 ([wowsims link](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-pool-protection-paladin.html)): no raid, PvP or high reputation items. The enchants obey the same rules. The default rotation of wowsims Forever. The talent search ran with the wowsims default set. This set has raid, PvP and reputation items. With the default set, PT1 had 1,056 threat each sec, 295 damage taken each sec and a TMI of 45.3, and BS2 had 1,006, 331 and 56.3. The build order does not change.
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
- **Deflection 5, not Benediction 5.** After Improved Judgement, Conviction and Sanctified Judgement, 9 points stay for Deflection and Benediction. One point in Deflection gives 1.5% less damage taken. One point in Benediction gives 0.3% more threat. With Benediction 5 and Deflection 4, PT1 had 1,217 threat each sec, 274 damage taken each sec and a TMI of 38.9 (consumables of 16 November).
- **Improved Seals (PI1, threat choice).** Divine Strength 5 and Improved Seals 5 cost 10 points. The best points to give up, against PS1: 3 Anticipation points, Benediction 3, Sanctified Judgement 3 and Sacred Arbiter. PI1 is 10/31/10, [`v6p05005-3530110213201531-5023`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p05005-3530110213201531-5023). Against PS1, it has +3.3% threat (1,546 each sec), but 2.2% more damage taken (255) and a 1.1% worse TMI (32.2).

  It is the same trade as BS1 in the live trees. On 1 November (Holy Shield rank 3, default set), other places cost more. Anticipation 3 gave 1,020 / 300 / 46.1, and Retribution 7 (Deflection 5, Improved Judgement 2) gave 990 / 296 / 45.8.

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
- **The tank build of the Analysis model** (B2T, 0/38/13, [`b2-25301102513501531-05233`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2-25301102513501531-05233)) gives 1,207 threat each sec and 293 damage taken each sec. Its TMI is 38.9.

## 3. Stat weights

Each stat + a small amount (20 Strength, Agility, Stamina or Intellect, 40 spell damage, 40 Attack power, 10 rating, 20 Block value, 200 armor). The table gives the change for each point. A negative change of damage taken or TMI is better.

| Stat | BS2 threat | BS2 damage taken | BS2 TMI (10 points) | PT1 threat | PT1 damage taken | PT1 TMI (10 points) |
| --- | --- | --- | --- | --- | --- | --- |
| Strength | +0.35 | −0.01 | −0.01 | +0.34 | −0.01 | −0.01 |
| Agility | +0.39 | −0.30 | −0.29 | +0.15 | −0.29 | −0.30 |
| Stamina | −0.01 | 0 | −0.78 | +0.01 | −0.01 | −0.63 |
| Intellect | 0 | 0 | 0 | 0 | 0 | +0.01 |
| Spell damage | +0.85 | −0.01 | −0.02 | +0.84 | −0.01 | −0.02 |
| Attack power | +0.16 | 0 | 0 | +0.15 | 0 | 0 |
| Hit rating | +1.27 | −0.08 | −0.16 | +1.25 | +0.04 | −0.01 |
| Crit rating | +0.61 | −0.01 | −0.02 | +0.61 | −0.01 | −0.01 |
| Expertise rating | +2.13 | −0.24 | −0.40 | +2.10 | −0.17 | −0.36 |
| Defense rating | −0.04 | −0.74 | −0.96 | −0.50 | −0.49 | −0.48 |
| Block rating | +0.62 | −0.20 | −0.44 | −0.02 | −0.03 | −0.03 |
| Block value | 0 | −0.24 | −0.28 | 0 | −0.30 | −0.44 |
| Dodge rating | −0.10 | −0.32 | −0.22 | −0.41 | −0.34 | −0.35 |
| Parry rating | −0.09 | −0.27 | −0.17 | −0.38 | −0.30 | −0.29 |
| Armor | 0 | −0.02 | −0.04 | 0 | −0.02 | −0.03 |

- **Threat.** Expertise rating gives the most threat for each point. Hit rating gives 3.6–3.7 times the threat of Strength, and spell damage 2.4–2.5 times. On commit 6084403a9, Hit rating gave 4.8–5.0 times.
- **Crit rating, Attack power and Intellect.** Crit rating gives +0.61 threat each sec for each point, about 1.7–1.8 times Strength, and almost no survival. Attack power gives +0.15–0.16 for each point, less than half of Strength. Intellect gives almost nothing in a 3 min fight.
- **Survival.** With Redoubt, Stamina gives the best TMI for each point. Without Redoubt (BS2), Defense rating gives the best TMI, then Stamina (−0.96 and −0.78). Defense rating gives the largest decrease of damage taken.
- **Block rating has almost no value with Redoubt (C-P1).** With Redoubt, about 54% of the boss swings are blocks. Misses, dodges, parries and blocks fill almost all of the attack table.
- **Dodge and parry cost threat with Redoubt.** Each dodge or parry takes the place of a block. Holy Shield and Reckoning need the blocks.
- **Block value has more value with Redoubt:** about 54% of the swings are blocks, without Redoubt about 43%.
- **Block rating has value without Redoubt.** Without Redoubt, only about 43% of the swings are blocks. Each point of Block rating gives +0.57–0.62 threat each sec (BT1 and BS2). The BT1 weights are in `models/wowsims-b2/logs/finals_full.log`.

## 4. Limits

- The values come from wowsims, not from combat logs. wowsims does not model Lay on Hands.
- The talent search is a hill climb. It gives a good build, not a proven best build.
- The stat weights are for the item pool set. A change of gear changes them.
- One boss only. Dungeon enemies cannot hit with crushing blows. Thus, a dungeon tank has other choices (Analysis, Builds).
- The earlier values (trees of 18 October, with a gear search) are in the history of the repository.
