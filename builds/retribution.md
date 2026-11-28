# Retribution: best damage build and stat weights

This file gives the best damage builds on one target. It uses the live trees and the proposed trees of calculator version 6. It also gives the stat weights. All values come from wowsims Forever (see [README](README.md)).

## Summary

| Trees | Case | Build | Points | Code | DPS |
| --- | --- | --- | --- | --- | --- |
| Live | Raid | RB1 | 14/6/31 | [`b2050250002-501-05233011201301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2050250002-501-05233011201301351) | 942 |
| Proposed | Raid | RB1 | 14/6/31 | [`v6p050250002-501-05233011201301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p050250002-501-05233011201301351) | 942 |
| Live | Fresh 60 | RB1 | 14/6/31 | [`b2050250002-501-05233011201301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2050250002-501-05233011201301351) | 323 |
| Proposed | Fresh 60 | RB1 | 14/6/31 | [`v6p050250002-501-05233011201301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p050250002-501-05233011201301351) | 340 |

- **RB1 is the main build in all four cases.** It is the wowsims default build of 1 November and RB1 of Analysis, Builds. The talent search found raid builds with at most +0.4%. At fresh 60, RS1 gives −1.7% in the live trees, and RS3 −6.9% in the proposed trees (part 2).
- **"Raid"** is full raid buffs and debuffs, with consumables. **"Fresh 60"** is no buffs, no debuffs and no consumables.
- **Proposed against live.** Only Reverence 50% (C-H1) changes Retribution damage. With the item pool set and the enchants of 28 November on commit dc09e002f0, it gives +5.3% at fresh 60. In a raid, it gives 0%. With the set of 18 November on commit ad6b13af8, it gave +3.9% at fresh 60 (without the enchants of 18 November evening: +4.0%). With the set of 15 November on commit 6084403a9, it gave −0.1% at fresh 60. On commit 8c7b5a5f5 with the set of 12 November, evening, it gave −0.5% at fresh 60. With all three judgements ranged, it gave −0.2%.

  On commit 129fcd89e, it gave +0.1% at fresh 60. With the set of 12 November (commit 52471a100), it gave +1.0% at fresh 60. The set of 11 November gave −0.9%, and the set of 4 November +0.4%. With the wowsims default set, it gave +4.2% at fresh 60.
- **Stat weights.** In a raid, Expertise rating is the best stat for each point (2.3 Strength), then Crit rating (1.1 Strength) and Haste rating (0.9 Strength). Hit rating is only 0.4 Strength. At fresh 60, Intellect has more value (part 3).

## 1. Method

- **Sim.** wowsims Forever, master of 27 November 2026 (commit dc09e002f0, client 1.60.1.71139, hotfixes up to push 114405), with `models/wowsims-b2/patches/talents.patch`. wowsims itself makes Judgement of Righteousness and Judgement of Fury ranged attacks, as in the hotfixes of 11 November. Thus, they no longer trigger melee weapon procs. Judgement of Command stays a melee attack, as in the late hotfix of 13 November. The Seals of Command, Fury and Righteousness also proc from the Windfury Totem strike. The proposed trees use the flag REV50 (Reverence 25/50%). The other kept proposals do not change Retribution damage.

  The talent search ran on master of 1 November (commit 895cd67f9). It used earlier flags: Reverence 30% and the Holy Strike Seal trigger (C1, withdrawn on 2 November 2026). The builds and stat weights then ran again on commit dc09e002f0 with REV50 only. They use the item pool set of 28 November (Destiny, three pieces of Justice Battlegear, Chained Essence of Eranikus) with the enchants of 28 November. The set of 8 November is the start of this search.
- **942 against 939.** This file uses 3 min fights: 942 DPS in a raid. Analysis, Damage uses the 2 min wowsims test run: 939 DPS. Both use the item pool set and the enchants of 28 November and commit dc09e002f0. With the set of 18 November on commit dc09e002f0, the values were 922 and 915. Judgement of Command now has one weapon proc roll for each hit (−0.8%), and the new set gives +2.6%. On commit ad6b13af8 with the set of 18 November, the values were 919 and 910. With the wowsims preset enchants, the values were 914 and 905. On commit 6084403a9 with the set of 15 November, the values were 890 and 882. Destiny and Soulforge Warboots give +3%. On commit 8c7b5a5f5 with the set of 12 November, evening, the values were 837 and 831. The Seal procs from the Windfury Totem strike give +6%. On commit 129fcd89e, the values were 843 and 838. The two ranged judgements and the Two-Handed Weapon Specialization fix give −0.7 to −0.9%. With all three judgements ranged, the values were 830 and 825.

  With the set of 12 November on commit 52471a100, the values were 854 and 848. The Hand of Justice change of commit 129fcd89e gives −2%. With the set of 11 November, the values were 847 and 841. On commit ae9b8c23a (8 November), the values were 949 and 939. The new Windfury Totem rule of commit 9f254e8d8 gives RB1 −11% in a raid: Holy Strike and Judgement of Command do not proc Windfury. With the wowsims default set (4 November), the values were 944 and 938.
- **Fight.** 3 min, one level 63 boss, 3,000 iterations, the same random seed for all runs.
- **Gear and rotation.** The item pool Retribution set of 28 November, Analysis, Damage, part 7 ([wowsims link](https://ralgathor.github.io/forever-paladin-feedback/sets/build-retribution.html)), and the default rotation of wowsims Forever. Enchants of 28 November: the same rules for all specs (Analysis, Damage, part 7). Superior Strength on the wrists and +15 Strength on the gloves replace Healing Power (Argent Dawn, Exalted) and Greater Agility. The talent search ran with the wowsims default set.
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
| RS1, 12/8/31 | Live | [`b2050150001-503-15233011101301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2050150001-503-15233011101301351) | 946 (+0.4%) | 318 (−1.7%) | Reverence 1, Holy Conduit 1, Pursuit of Justice 1, Precision 3, Deflection 1 |
| RS2, 13/7/31 | Proposed | [`v6p050150002-502-05233011201301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p050150002-502-05233011201301351) | 944 (+0.2%) | — | Reverence 1, Precision 2 |
| RS3, 12/8/31 | Proposed | [`v6p050050002-503-15233011101301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p050050002-503-15233011101301351) | — | 317 (−6.9%) | Reverence 0, Pursuit of Justice 1, Precision 3, Deflection 1 |

- **Precision is the only gain in a raid.** The raid buffs fill the mana. Thus, the search moves Reverence points to Precision 3.
- **At fresh 60, mana limits the damage.** With no buffs, RB1 has no mana for 80 sec of the 3 min fight, and RS1 for 89 sec. With Reverence 50% (proposed), RB1 has no mana for 74 sec, and RS3 (no Reverence) for 87 sec.
- **The gain is small.** In a raid, +0.4% is 4 DPS. At fresh 60, RB1 is now better than RS1. On commit ad6b13af8, RS1 gave +0.8% at fresh 60 (3 DPS). A tank or a boss with more armor can change the order. Thus, RB1 stays the main build.
- Unyielding Faith 1 and Pursuit of Justice give no damage. They fill the rows to Unsealed Wrath (Analysis, Builds, part 4).

## 3. Stat weights

Each stat + a small amount (20 Strength, Agility or Intellect, 40 spell damage or Attack Power, 10 rating). DPS gain for each point, divided by the gain of 1 Strength. Build RB1.

| Stat | Live, raid | Proposed, raid | Live, fresh 60 |
| --- | --- | --- | --- |
| DPS for 1 Strength | 0.51 | 0.51 | 0.21 |
| Strength | 1.00 | 1.00 | 1.00 |
| Agility | 0.74 | 0.73 | 0.76 |
| Intellect | 0.61 | 0.61 | 3.93 |
| Spell damage | 0.78 | 0.78 | 0.86 |
| Attack Power | 0.40 | 0.40 | 0.46 |
| Hit rating | 0.36 | 0.32 | 0.33 |
| Crit rating | 1.05 | 1.05 | 1.14 |
| Haste rating | 1.39 | 1.43 | 0.90 |
| Expertise rating | 2.22 | 2.18 | 1.33 |

- **Expertise rating** has the most value for each point in a raid: 2.2 Strength (18 November: 2.3).
- **Spell damage is 0.8 Strength.** Seals, Judgements, Holy Strike and Consecration use spell damage.
- **Haste rating is 1.4 Strength** (18 November: 0.9; 15 November: 1.4; 13 November: 1.0; all three judgements ranged: 0.7; 129fcd89e: 0.9; 52471a100: 1.3; 11 November: 1.8). More swings give more Windfury Totem strikes, and each Windfury strike procs the Seal (since commit 6084403a9). Since commit 9f254e8d8, Windfury Totem procs from auto attacks, not from Holy Strike.
- **Hit rating has little value in this set.** It is 0.3–0.4 Strength (18 November: 0.4; 15 November: 0.1; 13 November: 0.6; all three ranged: 0.2; 52471a100: 0.4; 11 November: 1.0). The value changes much from one commit and set to the next. The cause of this change is not known.
- **At fresh 60, mana limits the damage.** Intellect is 3.9 Strength (18 November: 2.0; 15 November: 1.3; 13 November: 1.2; 129fcd89e: 1.6) and Expertise rating 1.3 Strength. Hit rating is 0.3 Strength (18 November: 0.05). Haste rating is 0.9 Strength (18 November: −0.6; 15 November: 0.3; 13 November: 0.4; all three judgements ranged: 0.7; 52471a100: 0.9; 11 November: −0.27). The fresh 60 weights change much from one set to the next. With the wowsims default set, Haste rating was 2.3 Strength.

## 4. Limits

- The values come from wowsims, not from combat logs. The wowsims rotation is the rotation of RB1.
- The talent search is a hill climb. It gives a good build, not a proven best build.
- The stat weights are for the item pool set. A change of gear changes them.
- The earlier values (trees of 18 October, with a gear search) are in the history of the repository.
