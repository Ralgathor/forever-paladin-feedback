# Shockadin: Holy Shock damage build and stat weights

This file gives the Holy Shock damage build ("Shockadin") on one target. It uses the live trees and the proposed trees of calculator version 6. It also gives the stat weights. All values come from wowsims Forever (see [README](README.md)).

## Summary

| Trees | Case | Build | Points | Code | DPS | % of RB1 |
| --- | --- | --- | --- | --- | --- | --- |
| Live | Raid | SB1 | 23/0/28 | [`b205025210221021--0523330110130033`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b205025210221021--0523330110130033) | 834 | 98% |
| Proposed | Raid | SB1 | 23/0/28 | [`v6p05025210221021--0523330110130033`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p05025210221021--0523330110130033) | 834 | 98% |
| Live | Fresh 60 | SB1 | 23/0/28 | [`b205025210221021--0523330110130033`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b205025210221021--0523330110130033) | 289 | 95% |
| Proposed | Fresh 60 | SB1 | 23/0/28 | [`v6p05025210221021--0523330110130033`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p05025210221021--0523330110130033) | 289 | 96% |

- **SB1 is the best Holy Shock build found.** It is the wowsims Holy Shock build (`HolyShockTalents`). In a raid, the talent search found no move of 1 point with more than +2 DPS. At fresh 60, the search removes Holy Shock (part 2).
- **SB1 is 98% of Retribution (RB1) in a raid.** RB1 has 847 DPS in a raid, 305 (live) and 303 (proposed) at fresh 60. On commit ae9b8c23a (8 November), SB1 was 89% of RB1. The proc items of 11 November (Storm Gauntlets and The Needler) give SB1 +1.3%. The new Windfury Totem rule decreases RB1 by 11% and SB1 by 3%. The two builds use sets from the same item pool, but with different items (part 1). Thus, the % is approximate.
- **Holy Shock gives +11% in a raid.** Without Holy Shock and with Champion of the Light 4 (SF1), the damage is 749 in a raid. At fresh 60, SF1 has more damage than SB1: Holy Shock costs too much mana without buffs (part 2).
- **Proposed against live.** Reverence 50% (C-H1) gives +0.1% at fresh 60 and 0% in a raid. With the Shockadin set of 9 November, it gave +8.0% at fresh 60. Storm Gauntlets cause the change (part 3). Light's Vigil (C-H7) gives a build with 31 Holy points +9.2%, but this build stays 11% below SB1 (part 2).
- **Stat weights.** Spell damage is the main stat. In a raid, Hit rating is the best stat for each point (1.9 spell damage). At fresh 60, Hit rating also has the most value (1.4 spell damage) (part 3).

## 1. Method

- **Sim.** wowsims Forever, master of 11 November 2026 (commit 3633d376a, hotfixes of 10 and 11 November, game files of client 1.60.1.70888), with `models/wowsims-b2/patches/talents.patch`. The proposed trees use the flags REV50 (Reverence 25/50%, C-H1) and CH7 (Light's Vigil, C-H7). The other kept proposals do not change the damage of this build.
- **CH7 flag.** Holy Shock, Judgement and Holy Strike give a stack of Light's Vigil for 30 sec, once each 6 sec, up to 3 stacks. A Holy Shock cast uses one stack and then incurs no cooldown. The sim starts each fight with no stack. The party heal is not in the damage sim.
- **Gear, rotation and consumables.** The sim uses the `shockadinSuite` of the wowsims Retribution test. The gear is the wowsims Holy Shock set (`holy_shock`: spell damage gear, and Manual Crowd Pummeler as a swap). It uses the item pool rules of Analysis, Damage, part 7 ([wowsims link](https://ralgathor.github.io/forever-paladin-feedback/sets/build-shockadin.html)). Five items are not in the pool: two rings, two trinkets and the libram. A search in wowsims replaced them with pool items (`models/wowsims-b2/tank_gear`, `search_tank.py shock`). On 8 November, the search takes Hand of Justice and Smolderweb's Eye as trinkets: +0.2% damage against the default set (4 November: −1.4%). The search of 9 November found no better set, thus this set stays: +0.3% against the default set on commit 9f254e8d8 (823.0 against 820.6). On 11 November, the search also tested all pool items with a proc effect in each slot. It takes Storm Gauntlets and The Needler (a proc dagger) in place of Gauntlets of Elements and Shin Blade: 833.8 DPS (was 823.0). The rotation is `holy_shock.apl.siml`. The consumables add Cerebral Cortex Compound and Frost Oil. The race is Human, as for RB1. RB1 uses the item pool Retribution set, thus the two sets are not the same. The talent search ran with the wowsims Holy Shock set.
- **Fight.** 3 min, one level 63 boss, 3,000 iterations, the same random seed for all runs. "Raid" is full raid buffs and debuffs, with consumables. "Fresh 60" is no buffs, no debuffs and no consumables.
- **Talent search.** A hill climb (`models/wowsims-b2/search.py`, cases `shock-raid` and `shock-fresh`, with `-prop` for the proposed trees). Each step tests all moves of 1 point into a talent with damage value, at 1,000 iterations. It keeps the best move. This search has no round with moves of 2 points. The best builds then run at 3,000 iterations (`finals.py shock`), with the item pool set. The logs are `search_shock-*.log` and `finals_shock.log`.
- **Starts.** SB1 for all four cases. For the proposed trees, also SB2 (31 Holy points with Light's Vigil).

## 2. Builds

### SB1

[`v6p05025210221021--0523330110130033`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p05025210221021--0523330110130033) (23/0/28).

- Holy: Divine Strength 5, Reverence 2, Improved Seals 5, Purifying Power 2, Divine Favor, Holy Conduit 2, Divine Precision 2, Infusion of Light 1, Consecrated Ground 2, Holy Shock.
- Retribution: Benediction 5, Improved Judgement 2, Conviction 3, Sanctified Judgement 3, Vindication 3, Seal of Command, Pursuit of Justice 1, Sacred Arbiter, Two-Handed Weapon Specialization 3, Vengeance 3, Champion of the Light 3.
- **Holy Shock needs 20 Holy points.** The 23 Holy points leave 28 for Retribution. Thus, the build has no Unsealed Wrath and only 3 points in Champion of the Light.
- **Mana.** In a raid, SB1 has mana for the full fight. At fresh 60, it has no mana for 111 sec of the 3 min fight (proposed trees: 111 sec).

### Other builds

| Build | Trees | Code | Raid | Fresh 60 | Change against SB1 |
| --- | --- | --- | --- | --- | --- |
| SB2, 31/0/20 | Live | [`b205025211222021051--052323010013`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b205025211222021051--052323010013) | 682 (−18%) | 223 (−23%) | Light's Vigil, Holy Power 5, Illumination 1, Infusion of Light 2. Retribution 20: no Vengeance, no Champion of the Light |
| SB2, 31/0/20 | Proposed | [`v6p05025211222021051--052323010013`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p05025211222021051--052323010013) | 745 (−11%) | 235 (−19%) | The same build, with Light's Vigil (C-H7) |
| SB3, 32/0/19 | Live | [`b215325210222121201--052330002013`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b215325210222121201--052330002013) | 683 (−18%) | 242 (−16%) | A hybrid healer: Light's Vigil, Oath of Light, Healing Light 3, Boundless Light 2, no Holy Power. Retribution 19: no Vengeance, no Champion of the Light |
| SB3, 32/0/19 | Proposed | [`v6p15325210222121201--052330002013`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p15325210222121201--052330002013) | 747 (−10%) | 253 (−12%) | The same build, with Light's Vigil (C-H7) |
| SF1, 22/0/29 | Live | [`b20502521022102--0523330110130034`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b20502521022102--0523330110130034) | 749 (−10%) | 310 (+7.5%) | No Holy Shock. Champion of the Light 4 |
| SF2, 22/0/29 | Proposed | [`v6p0502520122102--0523330110130034`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p0502520122102--0523330110130034) | 749 (−10%) | 321 (+11.1%) | No Holy Shock. Illumination 1 in place of Divine Favor, Champion of the Light 4 |

- **Light's Vigil (C-H7) adds damage, but not enough.** It gives SB2 +63 DPS in a raid (+9.2%): one Holy Shock each 6 sec, in place of each 10 sec. SB2 has no Vengeance and no Champion of the Light, thus it stays 11% below SB1. The talent search from SB2 at fresh 60 moved the Light's Vigil point to other talents at its second step.
- **In a raid, SB3 has the same damage as SB2.** Light's Vigil (C-H7) gives +9.3% in a raid. At fresh 60, it gives only +2.7%: with more Holy Shocks, the build has no mana for 123 sec of the 3 min fight. Reverence 50% (C-H1) gives +1.8% there. The heal talents of SB3 give no damage, and this sim has no heals.
- **At fresh 60, Holy Shock costs too much mana.** The search moved the Holy Shock point to Champion of the Light. SF1 is a Retribution build with the Holy Shock set, not a Shockadin. In the final runs, SB1 has no mana for 111 sec of the 3 min fight, and SF1 for 56 sec.
- **The search did not find a better Shockadin.** In a raid, no move of 1 point from SB1 gave more than +2 DPS, in the live and in the proposed trees.

## 3. Stat weights

Each stat + a small amount (20 Strength, Agility or Intellect, 40 spell damage or Attack Power, 10 rating). DPS gain for each point, divided by the gain of 1 spell damage. Build SB1, except the last column (SB2).

| Stat | Live, raid | Proposed, raid | Live, fresh 60 | SB2, proposed, raid |
| --- | --- | --- | --- | --- |
| DPS for 1 spell damage | 0.50 | 0.50 | 0.22 | 0.49 |
| Spell damage | 1.00 | 1.00 | 1.00 | 1.00 |
| Strength | 0.57 | 0.57 | 0.66 | 0.50 |
| Agility | 0.55 | 0.56 | 0.57 | 0.46 |
| Intellect | 0.44 | 0.44 | 0.11 | 0.04 |
| Attack Power | 0.23 | 0.23 | 0.30 | 0.21 |
| Hit rating | 1.88 | 1.94 | 1.36 | 1.72 |
| Crit rating | 0.88 | 0.88 | 0.91 | 0.78 |
| Haste rating | 0.78 | 0.74 | −0.23 | 0.88 |
| Expertise rating | 1.20 | 1.18 | 1.00 | 0.82 |

- **Spell damage is the main stat.** Holy Shock, Consecration, Exorcism, Judgements and Seals use spell damage. 1 spell damage is 1.8 Strength. For RB1, 1 spell damage is 0.9 Strength.
- **Hit rating has the most value for each point in a raid:** 1.9 spell damage. It increases melee and spell hits.
- **At fresh 60, Hit rating also has the most value:** 1.4 spell damage. With the Shockadin set of 11 November, Intellect has almost no value (0.1 spell damage), and Haste rating has a negative value. With the set of 9 November, Intellect was 2.8 spell damage. A test of each new item shows the cause: Storm Gauntlets. With The Needler and Gauntlets of Elements, Reverence 50% still gives +7.7% at fresh 60 (279.7 → 301.3). With Storm Gauntlets, the live and proposed trees have the same mana.
- **SB2 has mana in a raid.** Intellect then has almost no value.

## 4. Limits

- The values come from wowsims, not from combat logs. The wowsims Holy Shock rotation is the rotation of SB1.
- The talent search is a hill climb with moves of 1 point. It gives a good build, not a proven best build.
- The stat weights are for the item pool Shockadin set. A change of gear changes them.
- The CH7 flag starts each fight with no stack of Light's Vigil. A Paladin can start a fight with up to 3 stacks (see Holy, C-H7). Thus, the SB2 value with C-H7 is a low value for short fights.
- The sim has one target. The Shockadin has no heal in this sim, thus the value of Holy Shock heals and of the Light's Vigil party heal is not in this file.
