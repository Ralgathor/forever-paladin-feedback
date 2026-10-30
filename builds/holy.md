# Holy: best healing build, gear and stat weights

This file gives the best healing build for the beta trees and for the proposed trees. It also gives the pre-raid and raid gear and the stat weights of each build. The build search uses the healing model (`models/healing`). The gear and the stat weights come from wowsims Forever (see [README](README.md)).

## Summary

| Trees | Build | Points | Code | Raid, 3 / 10 min (model, 715 healing power) | Pre-raid gear, 3 min (wowsims) | Raid gear, 3 min (wowsims) |
| --- | --- | --- | --- | --- | --- | --- |
| Proposed | P1 (= HB1) | 34/12/5 | `v6p53201132251010512-30200000000000502-0005` | 694 / 526 | 625 | 853 |
| Beta | B1 | 32/14/5 | `05320113225101051-500250002-05` | 616 / 449 | 519 | 742 |

- In both trees, all healing talents fit in 51 points. Thus, the best healing build takes all of them. The other points give only utility.
- The proposed healer heals 13% more than the beta healer in the model. In wowsims, it heals 20% more with pre-raid gear and 15% more with raid gear.
- **Stat weights.** In a long fight, the healer goes out of mana, and MP5 and Intellect have the most value. In a short fight, the mana lasts, and haste, crit and healing power have the most value (part 4).

## 1. Method

- **Build search.** The healing model examined all legal talent sets down to 8 points below the full healing set. That is 7,103 beta sets and 26,629 proposed sets. The best sets then ran at full precision: 3, 5 and 10 min, 715 and 900 healing power, recovery after 3 and 6 sec.
- **wowsims check.** wowsims gives the same build order. The value of each talent is within about 2 percentage points of the model.
- **Gear search.** wowsims Forever commit 47b3c01 with `models/wowsims/proposals.patch`. Slot by slot, 12 candidates for each slot (24 for rings and trinkets). The sim keeps the set with the most healing per sec. 3 min, raid buffs, no consumables, no enchants, Alliance.
- **Gear tiers.** Pre-raid: item level 65 or lower, no raid drops. Raid: all items up to item level 92 (Naxxramas).
- **Sim rules.** The heal targets the caster. The sim has no overhealing: the values are raw healing.
- **Codes.** All codes load in calculator version 6 with 51 points.

## 2. Best builds

### Proposed: P1

`v6p53201132251010512-30200000000000502-0005` (34/12/5). This is HB1 of Analysis, Builds.

- Holy: Divine Intellect 5, Healing Light 3, Spiritual Focus 2, Unyielding Faith 1, Voice of Truth, Reverence 3, Purifying Power 2, Infusion of Light 2, Illumination 5, Divine Favor, Holy Shock, Holy Power 5, Light's Vigil, Lingering Light 2.
- Protection: Redoubt 3, Guardian's Favor 2, Benediction 5, Devoted Sacrifice 2.
- Retribution: Conviction 5.

### Beta: B1

`05320113225101051-500250002-05` (32/14/5)

- Holy: Divine Intellect 5, Healing Light 3, Spiritual Focus 2, Unyielding Faith 1, Voice of Truth, Reverence 3, Purifying Power 2, Infusion of Light 2, Illumination 5, Divine Favor, Holy Shock, Holy Power 5, Light's Vigil.
- Protection: Toughness 5, Guardian's Favor 2, Anticipation 5, Sacred Duty 2.
- Retribution: Benediction 5.

### Other builds

| Trees | Build | Code | Healing against the best build | Use |
| --- | --- | --- | --- | --- |
| Proposed | P2 (= HB2) | `v6p53200032251010512-30200020000000502-0005` | The same | Sacred Duty 2/2 in place of Unyielding Faith and Voice of Truth |
| Proposed | P3, PvP | `v6p53201030251000502-30201020030000502-0004` | −0.9% (model), −1.1% (wowsims) | Improved Hammer of Justice 3/3. No Holy Shock or Light's Vigil, Conviction 4 |
| Beta | B2, PvP | `05320203125101051-530230002003-02` | −0.03% (model), 0% (wowsims) | Improved Hammer of Justice 3/3, Benediction 2 |

### Value of each talent (model, raid, 3 min)

| Talent | Beta | Proposed |
| --- | --- | --- |
| Reverence and Illumination (Illumination needs Reverence 3/3) | −16.4% | −21.8% |
| Healing Light | −10.7% | −19.5% (−23.1% one tank) |
| Illumination | −8.9% | −10.6% |
| Lingering Light | — | −5.1% |
| Holy Power | −3.8% | −4.6% |
| Conviction (spells, C-R1) | — | −4.6% |
| Divine Favor | −2.5% | −3.0% |
| Divine Intellect | −2.5% | −2.5% |
| Infusion of Light | −1.9% | −1.8% (−3.0% one tank) |
| Benediction | −0.04% | −0.04% |
| Holy Shock and Light's Vigil | 0% | 0% (recovery −1%) |

- The best spell plan never casts Holy Shock or Light's Vigil. They heal the least for each mana point. Holy Shock has value when you move.
- Light's Vigil helps only in a short burst with no mana limit and 5 injured party members (about +19% in the model). In wowsims, it lowers the healing in all gear sets, also in 60 sec fights.

## 3. Gear

| Slot | Pre-raid, proposed (P1) | Pre-raid, beta (B1) | Raid, proposed (P1) | Raid, beta (B1) |
| --- | --- | --- | --- | --- |
| Head | Living Crown | Virtuous Crown | Redemption Headpiece | Redemption Headpiece |
| Neck | Wavefront Necklace | Wavefront Necklace | Gem of Trapped Innocents | Pendant of Forgotten Names |
| Shoulders | Wildheart Spaulders | Ironfeather Shoulders | Redemption Spaulders | Redemption Spaulders |
| Back | Drape of Recovery | Deep Woodlands Cloak | Cloak of Clarity | Cloak of Clarity |
| Chest | Breastplate of Salvation | Breastplate of Salvation | Redemption Tunic | Redemption Tunic |
| Wrist | Bracers of Hope | Bracers of Hope | Bracelets of Royal Redemption | Bracelets of Royal Redemption |
| Hands | Theramore Handwraps | Theramore Handwraps | Redemption Handguards | Redemption Handguards |
| Waist | Belt of the Archmage | Girdle of Insight | Grasp of the Old God | Redemption Girdle |
| Legs | Martyr's Legplates | Martyr's Legplates | Redemption Legguards | Redemption Legguards |
| Feet | Virtuous Sandals | Virtuous Sandals | Redemption Boots | Redemption Boots |
| Finger 1 | Band of Piety | Band of Piety | Ring of Redemption | Ring of Redemption |
| Finger 2 | Warden's Signet of Resolve | Warden's Signet of Resolve | Band of Unanswered Prayers | Band of Unanswered Prayers |
| Trinket 1 | Serenity Field | Serenity Field | Rejuvenating Gem | Rejuvenating Gem |
| Trinket 2 | Weakness Analyzer | Jewel of the Guard Captain | Eye of the Dead | Eye of the Dead |
| Main hand | Simone's Cultivating Hammer | Simone's Cultivating Hammer | Scepter of the False Prophet | Scepter of the False Prophet |
| Off hand | Earthcalm Orb | Earthcalm Orb | Wormscale Blocker | Wormscale Blocker |
| Libram | Libram of Economy | Libram of Economy | Libram of Economy | Libram of Economy |
| Healing power | 615 | 510 | 916 | 882 |
| Intellect | 163 | 180 | 255 | 276 |
| MP5 | 31 | 33 | 82 | 87 |
| Crit rating | 14 | 21 | 98 | 70 |

- The beta sets take more Intellect and MP5. Holy Light spam, the best beta plan in the search, uses more mana.
- The raid sets are mostly the Redemption set (8 pieces). The proposed set takes Grasp of the Old God in place of the Redemption Girdle.

wowsims links (gear and talents, no enchants):

- [Pre-raid, proposed (P1)](https://wowsims.com/forever/paladin/holy/#eJzjkuFgFGCUYFRg1GBMYMxgLGBsYGTsYGRcwMi4gpFRSAQsywSStWB0YPRgDGCMYJTazsjBIsAklcbFwjFxKz+QPLuQEUieawKRcy8IAMmXS0Hi3RtBIifPgESe9oPYL8DiR9aA2DPBsv1vQLLbwbq2gck360DiB5eCyC0XBJx4EE50YFzFyLCLScLA1NjIwNDQ2MjI1NDA0MDUUFfXwNTAwPQEE8sFJqYXTCkfmIwamRnAwNJhFjNbQE5iZWqR0j8mTrBYQ5qD5KyZIHDSXjENDK7ZGz1gkmBXsNfawcQwIKDEgS7WqK2lmT2WYDJoiYMjVMAhAZSYZjJCeA/snZCSmwFSkgIlvArGCiYAyB1JZA==)
- [Pre-raid, beta (B1)](https://wowsims.com/forever/paladin/holy/#eJzjkuFgFGCUYFRg1GBMYMxgLGBsYGTsYGRcwMi4gpFRSAQsywSStWB0YPRgDGCMYJTaw8jBIsAklcrFwnFgDSOQPLuQkYuZ43YpkLlxKkjg5VJ+INm9EcQ+eUYASJ6YAGK/AIsfAWuaCZbtfwOS3X4BRE7cDyLfrAOJH1wKIrdcEHDiQbjQgXEVI8MuJjkDU2MjA0NDYyMjU0MDQwNTQ11TAwMjIDYw0jUwPcHEcoGJ6QVTygcmo0ZmBjCwdJjFzBaQk1iZWqT0j4kTLNaQ5iA5ayYInLRXTAODa/ZGD5gk2BXstXYwMQwIKHGgizVqa2lmjyWYDFri4AgVcEgApaiZjBDeA3snpDRngJSuQKmvgrGCCQDls0ol)
- [Raid, proposed (P1)](https://wowsims.com/forever/paladin/holy/#eJzjkuFgFGCUYFRg1GBMYMxgLGBsYGTsYGRcwMi4gpFRSAQsywSStWB0YPRgDGCMYJTazsjBIsAklcbFwjFnPSOQnLgFRM4Fs8+vAJEzwewnYPYsMPscmD0bzJ4HJmeBdc3eDCIPTweR7WCR86tA5Cuw+i0XBJx4EE50YFzFyLCLScLA1NjIwNDQ2MjI1NDA0MDUUFfXwNTAwPQEE8sFJqYXTCkfmIwamRnAwNJhFjNbQE5iZWqR0j8mTrBYQ5qD5KyZIHDSXjENDK7ZGz1gkmBXsNfawcQwIKDEgS7WqK2lmT2WYDJoiYMjVMAhAZSYZjJCeA/snZCSmwFSkgIlvArGCiYA9ZRHlQ==)
- [Raid, beta (B1)](https://wowsims.com/forever/paladin/holy/#eJzjkuFgFGCUYFRg1GBMYMxgLGBsYGTsYGRcwMi4gpFRSAQsywSStWB0YPRgDGCMYJTay8jBIsAklcbFwjFnPSOQXLwZRM4Fs8+vAJEzwewnYPYsMHs+mJwNJueByVlbwCJgvYeng8h2sMj5VSDyFVjvlgsCTjwIJzowrmJk2MUkZ2BqbGRgaGhsZGRqaGBoYGqoa2pgYATEBka6BqYnmFguMDG9YEr5wGTUyMwABpYOs5jZAnISK1OLlP4xcYLFGtIcJGfNBIGT9oppYHDN3ugBkwS7gr3WDiaGAQElDnSxRm0tzeyxBJNBSxwcoQIOCaAkNZMRwntg74SU6AyQEhYo+VUwVjABANoRSLM=)

The live wowsims has no Holy sim: the Holy page is a gear planner. The links load the gear, the talents and the stats of a Human Paladin. The proposed talents load in the beta tree order, thus the page shows beta talents. These links were made from the wowsims code. They were not opened in a browser.

## 4. Stat weights

Method: each stat + and − a small amount (40 healing power, Intellect or Spirit, 10 MP5, 14 crit rating, 10 haste rating). 10,000 iterations, the same random seed for all runs. Raid buffs, no consumables. EP = healing per sec for each point, divided by the healing per sec for each point of healing power.

The weights change with the mana. Thus, this part gives two cases: a long fight where the healer goes out of mana, and a short fight where the mana lasts.

### 3 min fight: mana is the limit

Spell plan: the best plan of each case. Proposed: "Divine Favor, Flash of Light then Holy Light". Beta, pre-raid: "Divine Favor, Holy Light". Beta, raid: "Divine Favor, Flash of Light, Holy Light on Infusion".

| Stat | Pre-raid, proposed | Pre-raid, beta | Raid, proposed | Raid, beta |
| --- | --- | --- | --- | --- |
| Healing per sec for each point of healing power | 0.260 | 0.151 | 0.316 | 0.301 |
| Healing power | 1.00 | 1.00 | 1.00 | 1.00 |
| Intellect | 2.77 | 3.64 | 2.95 | 2.58 |
| Spirit | 1.80 | 1.95 | 2.05 | 0.75 |
| MP5 | 4.22 | 5.53 | 4.01 | 2.68 |
| Crit rating | 1.93 | 1.97 | 2.16 | 1.41 |
| Haste rating | 0.20 | 0.75 | 0.76 | 0.81 |
| Healing per sec | 624 | 519 | 849 | 742 |
| Seconds out of mana | 103 | 105 | 91 | 48 |

### 60 sec fight: the mana lasts

Spell plan: "Divine Favor, Flash of Light, Holy Light on Infusion" for all cases.

| Stat | Pre-raid, proposed | Pre-raid, beta | Raid, proposed | Raid, beta |
| --- | --- | --- | --- | --- |
| Healing per sec for each point of healing power | 0.467 | 0.390 | 0.570 | 0.405 |
| Healing power | 1.00 | 1.00 | 1.00 | 1.00 |
| Intellect | 4.16 | 0.75 | 1.14 | 0.51 |
| Spirit | 0.88 | 0.02 | 0.16 | 0.00 |
| MP5 | 2.23 | 0.09 | 0.41 | 0.00 |
| Crit rating | 1.76 | 1.84 | 1.26 | 1.83 |
| Haste rating | 0.37 | 2.01 | 1.90 | 2.53 |
| Healing per sec | 977 | 784 | 1,362 | 988 |
| Seconds out of mana | 9 | 0 | 0 | 0 |

### What the weights show

- **Long fights: mana is the best stat.** The sim heals all the time with no overhealing and no consumables. Thus, the healer is out of mana before the end of a 3 min fight. Then MP5 and Intellect give more healing than healing power: MP5 is 2.7–5.5 and Intellect 2.6–3.8 healing power.
- **Short fights: healing power, crit and haste.** When the mana lasts, Intellect, Spirit and MP5 have little value. Haste rating is about 2 healing power and crit rating about 1.3–1.8.
- **The proposed pre-raid set goes out of mana also in 60 sec** (9 sec). Thus, its Intellect stays high (4.16).
- **Crit rating has value in all cases** (1.3–2.2). Each critical heal heals more and, with Illumination, returns mana.
- **The value of healing power changes with the spell plan.** With Holy Light spam (beta, pre-raid), each point gives 0.151 healing per sec. With a Flash of Light plan, each point gives 0.26–0.32 in a 3 min fight.
- **Limit.** In a raid, heals have overhealing and the healer does not heal all the time. Then mana has less value than in the 3 min table. Most raid fights are between the two cases. The healing model (`models/healing`) gives the overhealing case.
