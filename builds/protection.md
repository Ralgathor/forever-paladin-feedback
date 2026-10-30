# Protection: best tank build, gear and stat weights

This file gives the best tank build for the beta trees and for the proposed trees. It also gives the pre-raid gear and the stat weights of each build. All values come from wowsims Forever (see [README](README.md)).

## Summary

| Trees | Build | Code | TPS | DPS | DTPS | TMI | Crushing blows |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Proposed | PT3 | `v6p0003-53030321301551-5215200001` | 1,190 | 673 | 214 | 21.8 | 0.5% |
| Beta | BT4b | `50003-5230513021301351-50201` | 994 | 555 | 230 | 28.8 | 9.4% |

- Values: raid with consumables, path gear with reputation items (part 3), 3 min fight, level 63 boss, 3,000 iterations. Holy Shield (C-P9) at 100% of block value. Shields use the Wowhead Forever block values.
- The proposed tank has 20% more threat than the beta tank, with 24% lower TMI. Redoubt (C-P1) and Holy Shield (C-P9) push crushing blows off the combat table.
- The beta tank keeps 7–11% crushing blows with all gear sets of this file. No beta build in the search removes them.
- Against the other tanks, see Analysis, Threat, part 7. With the player data threat values, the Druid has more threat than PT3.

## 1. Method

- **Sim.** wowsims Forever commit a10f483 (30 October 2026) with `models/wowsims/proposals.patch`.
- **Score.** The search uses a balanced score: 40% TPS, 20% DPS, 20% damage taken (DTPS), 20% TMI.
- **Talent search.** A hill climb from the best builds of Analysis, Builds (PT3, PB1, PT2) and random builds. It moves 1 to 3 points at a time, with the rules of calculator version 6, and keeps the best move.
- **Path.** Gear search and talent search in turns, until neither changes. The gear search changes one slot at a time. It tests the best pre-raid items for each slot, and all trinkets with an effect.
- **Gear rules.** Item level 66 or lower, no raid drops, no items made from raid materials, Alliance. Thus, Signet Ring of the Bronze Dragonflight is not in the sets. The enchants and the libram are the enchants and the libram of the reference tank (Libram of Fervor).
- **Shields.** wowsims gives epic shields about 32% more block than the Wowhead Forever tooltips. All runs use the Wowhead values (for example 66 for The Immovable Object).
- **Beta.** BT4b keeps its talents. The gear search runs again on the new sim.
- **Codes.** All codes load in calculator version 6 with 51 points.

## 2. Best builds

### Proposed: PT3

`v6p0003-53030321301551-5215200001` (3/32/16)

- Holy: Improved Seals 3.
- Protection: Redoubt 5, Precision 3, Anticipation 3, Shield Specialization 3, Sacred Duty 2, Swift Judgement, One-Handed Weapon Specialization 3, Templar's Bulwark, Reckoning 5, Iron Creed 5, Holy Shield.
- Retribution: Deflection 5, Improved Judgement 2, Holy Conduit 1, Conviction 5, Vindication 2, Sacred Arbiter.

With the path gear, PT3 has +1.6% TPS against the best PB1 of the version 6 search, with the same TMI. With Holy Strike Seal trigger (C1), Holy Strike also triggers Seal of Fury.

**Version 6 option.** `v6p0003-53030321301551-52050000010000003` (3/32/16) takes Burning Zeal 3/5 in place of Vindication 2 and Holy Conduit 1. It has +1.0% TPS against PT3 (1,202 against 1,190). Damage taken and TMI are almost the same. It has less mana (no Holy Conduit). Thus, PT3 stays the main build.

**Mana.** PT3 needs raid mana support (Judgement of Wisdom, Blessing of Wisdom). With no buffs and no consumables, PT3 is out of mana for 135 sec. PB1 keeps its mana longer (Sanctified Judgement 3, Holy Conduit 2). Thus, PB1 is the better tank at fresh level 60 with no mana support.

### Beta: BT4b

`50003-5230513021301351-50201` (8/35/8)

- Holy: Divine Strength 5, Improved Seals 3.
- Protection: Toughness 5, Redoubt 2, Precision 3, Anticipation 5, Improved Seal of Fury, Improved Righteous Fury 3, Sacred Duty 2, Swift Judgement, One-Handed Weapon Specialization 3, Templar's Bulwark, Reckoning 3, Iron Creed 5, Holy Shield.
- Retribution: Deflection 5, Improved Judgement 2, Conviction 1.

In the beta, each point of threat costs survival. Toughness, Sacred Duty and Improved Righteous Fury come first with this gear. Without consumables, BT4b is out of mana for about 50 sec.

### Other builds

| Trees | Build | Code | Use |
| --- | --- | --- | --- |
| Proposed | PT1 | `v6p0003-52040321301551-5205300001` | Best with the older gear (Precision 2, Anticipation 4, Conviction 5, Vindication 3). Not rerun on commit a10f483 |
| Proposed | PT2, maximum threat | `v6p0003-53040311301551-0225301201` | +2% TPS against PT1, but +9% damage taken. No Deflection. Version 6: Vindication 3 (+6% Attack Power) and Holy Conduit 2 in place of Vindication 5 (estimate, no new sim) |
| Proposed | PB1 | `v6p0003-53051321301551-522103` | Fresh level 60 with no mana support |
| Proposed | PB1, version 6 search | `v6p0003-53050321301551-52031000000000003` | PB1 with Burning Zeal 3/5. 1,171 TPS and TMI 21.7 with the path gear (part 3) |
| Beta | BT5 | `50003-5330513011301451-502` | Best beta build with the gear with no reputation items (part 3) |
| Beta | Maximum threat | `50003-0530511101301541-50205` | +3% TPS against the reference beta tank, but TMI +9% |

## 3. Gear

### With reputation items (main sets)

| Slot | Beta (BT4b) | Proposed (PT3) |
| --- | --- | --- |
| Head | Stalwart Helm | Enriched Thorium Helm |
| Neck | Horn of Ve'han | Amulet of the Darkmoon |
| Shoulders | Highlander's Plate Spaulders | Highlander's Plate Spaulders |
| Back | Shifting Cloak | Shifting Cloak |
| Chest | Enriched Thorium Breastplate | Darksoul Breastplate |
| Wrist | Warder's Wristguards | Berserker Bracers |
| Hands | Heavy Thorium Gauntlets | Theramore Gauntlets |
| Waist | Warder's Waistguard | Redeemer's Waistcord |
| Legs | Sentinel's Chain Leggings | Legplates of Valor |
| Feet | Warder's Sabatons | Depleted Thorium Sabatons |
| Finger 1 | Watcher's Signet of Vigilance | Watcher's Signet of Vigilance |
| Finger 2 | Warden's Signet of Vigilance | Warden's Signet of Vigilance |
| Trinket 1 | Adaptive Combat Assistant | Adaptive Combat Assistant |
| Trinket 2 | Defender's Grip Stabilizer | Defender's Grip Stabilizer |
| Main hand | Sageblade | Sageblade |
| Shield | Evergreen Shield | The Immovable Object |
| Libram | Libram of Fervor | Libram of Fervor |

The new gear search changed these items. Proposed: Enriched Thorium Helm, Watcher's Signet of Vigilance (in place of Signet Ring of the Bronze Dragonflight), Adaptive Combat Assistant and Sageblade. Beta: Stalwart Helm, Watcher's Signet of Vigilance, Adaptive Combat Assistant and Sageblade.

wowsims links:

- [Beta: BT4b and beta gear](https://wowsims.com/forever/paladin/protection/#eNrFVN1LFFEUn3NndvZ6N5vZcdNp8kEXqVGQZncbUl9mkqCgl6H6A9xQa8EHUR/KCDQ0JKxEQlJCq0kQKU1JMMkI+9IFyYcolDI1oqhgAyF87M6Mbh9IT0IH5vA7X79z7mXuITkYZMgDFSrgFNRCE8ANgAEAKQuDSEMqRBhH7p0zK0Dp5DEnIqUZiB9/6hfk71mEw9e+iFTPX3ecLztAfhSi4AONXjlIwRsKFrdTsNQadDwcnu0XqPl2BLyEJ14mh9u/OTwdrh6bc/Q41X6cGgK526RgkTK856nfHoNwmTidUFM12o8TJU9HgtalW9AD/q5jd+J9/TAI8uAAXE4s28KKLXy0hdZEeyJlC/O2sAQtiXLsnc2EUeAIIswEytU1TYsV69GYpkdiWpR+kZgeKda1qBaZRtwcQguIWUHPWRIiWHGGuD8DYUwoKo5p9WQHyVD8xIcnLdW37o7q9SSHBKYA0+yWNUtMB2h+NiEKtfCrXlD5dX9Eq5c4BZUxkopBKSCylE18SYQwkMCoy7LaSccmjFs5PAkqKxUpKsmVFJIR9v8j9+sFi+ZuU7yej22nkmL3HMO9kMad5y1pv6KTQmkPkYuyMSsFJsApedEHql/xTdEGLAks8L98aSTto0NrpEAJk2BYIJlJjlDGB82WhEQfyRyF30zvAElQufRQD+lQPimgeNf4zlJx2khaKp/Om7KdqlLaa5Mxn9HbxH+N6fnSSEIKI7OfUeUagmbW/beZkHmR3ZvhQu2mGezpdmTekPn8mCurRuHZ0NCh5carhvcamDmjh+WtmviZqrpwF+uVNlWbwQ2+nR7HjJFf7cprI5pCeUbROGL+izSYW8t3ZHO+3Xf/8N+e1Q9sVcdSV7fZ5gYj3Ue1g6vQGDgaT1TmHY/XnaxqaAPoBi+8ZJQhEcp3iev7TYMS+uAPg0U3XS2cdnbcT9JOy0I=)
- [Proposed: PT3 and proposed gear](https://wowsims.com/forever/paladin/protection/#eNrFVN1LFFEUn3Nndvd6N9vZcdNp6kEXqVGQZncbUl9mkqCgl6H6A9xQa8EHUR/KCFQ0JKxESlwJrSZBpLQkwSRDxEqXon2IQKn8ACGo2EAI66k7M+v2gfQkdB4Ov/M7n/dy7yF5GETIBxkq4SzUQTPALYAhACEHA09dMoQYSx5c1CtB6nVjjkdSCxAPXhv0iV9zCIfNXqB64aZFvu4C8WmAgi9xEK8doeBHL4gfdlIw+5K3GA7fSPLUfNeaDlhq9zt852ee6i5bjyctPWFHpkZAjOsUfO8BccltdRyHYDk/F5NTtcq306WzD/3GlTvQB56ek/eiA4MwDOLwEFyNrZi+VdO3ZvraY52xlOlbMH3L0BarwM7ZdBgDjiDCTKKgQiVSoqgRJUJBOBRRQqoaKlGVcEgNW87QHOKSCC0iZhU9Z0mAYMka5dE8BDGhqCSiNJBdJEvyEBeeMmRXmg6rDSSPeGcA0+i2DYPPOGh8LiEStfCbfpDdaT6kNAichMoZQcYgFRJRyCWuBEIYiHfMrrLeTYcnjJ05OgUyKxRLMtkrSCQr6PlH7KdLBo3dITk9p00rk2L7HKP9kMHdrYZwSFJJkbCfiMW5mBW8k2ClvBgA2SO5ZmgDlngX3b+4DBIO0qEVUigFiT/oI9kJjtCKj1sMAfEukj0Gv5nOARIgc5mhntChXIJXcq7xvSHjjJEwZHcmbsa0sspory3GfEZvE/81psNlkIAkRmQ/oqoNBC2s/cKZgH6ZPZBlQ+W27u+LW7Kgie6CiC3rWtGFwMjRlabrmvMnmKTWx7qN2uj56vpgD+ukNtfo/s16u50a81pBjS1vtXAK5WvFE4j5L9Kob2+941vX23f/D/7uK/XwdnUss3WHqW9WpFupbngdmrwnorGq/FPR+jPVjR0AcXDcy1o54qFiD5/ecgqU0m9/DAy67+rgnLXpfgKO0cwX)

### With no reputation items

The set of 29 October with no faction vendor items, PvP reputation items, Darkmoon Faire items or reputation rings. It was not searched again.

| Slot | Beta (BT5) | Proposed (PT3) |
| --- | --- | --- |
| Head | Enriched Thorium Helm | Stalwart Helm |
| Neck | Horn of Ve'han | Artifact Seeker's Pendant |
| Shoulders | Spaulders of Valor | Spaulders of Valor |
| Back | Shifting Cloak | Shifting Cloak |
| Chest | Enriched Thorium Breastplate | Enriched Thorium Breastplate |
| Wrist | Warder's Wristguards | Berserker Bracers |
| Hands | Heavy Thorium Gauntlets | Heavy Thorium Gauntlets |
| Waist | Warder's Waistguard | Warder's Waistguard |
| Legs | Azerothium Legplates | Legplates of Valor |
| Feet | Warder's Sabatons | Depleted Thorium Sabatons |
| Finger 1 | Ring of Awareness | Don Julio's Band |
| Finger 2 | Cutthroat's Signet | Cutthroat's Signet |
| Trinket 1 | Smotts' Compass | Weakness Analyzer |
| Trinket 2 | Defender's Grip Stabilizer | Defender's Grip Stabilizer |
| Main hand | Greenhammer | Greenhammer |
| Shield | Evergreen Shield | The Immovable Object |
| Libram | Libram of Fervor | Libram of Fervor |

wowsims links:

- [Beta, no reputation: BT5](https://wowsims.com/forever/paladin/protection/#eNrFVN9LFFEUnnNndvd6N5vZcdPp1sO2SI2CNOs6pL7MJEFBL0P1B7ih1oIPoj6UEahoSFSGhLg+aDkJIpUlBSYZYb90QfIhCgVNDSHqwUAIH7szo9sPpCehA3P5znfP+c65l7mH5GFQIAIqVMJ5qINmgNsAQwByDgaJbakQ4xx7eNmsBNrpx4KEaDOQAF4dFJXvOUTAPV8lti60OuS7m6A8DzPwme12HmPgIwOLuxlYag85jIBnBkXmLntuAL/0IgWcmnV0etjK44EIg2MMBvACC0yZDCwy8MnPePsJRMulqaS6Vqv9OFv66lHIuj4AvRDoPn0v0T8Iw6AMD8GN5LItrtjiqi22J68l12xxzhaXoC1Zgb2jmTAKAkGEG0dU1zQtXqTH45oei2sx5yvRY0W6VjyFhFmE5hG3gt7wJEwwdVp4PA1RTBgqimsNZA/JogHiwxOW6tuki/UGkkeCk4BZdNuGJWU2WHwuIZR5+H0fqP5NPqY1yAJF5ZysYqD5RJFziS+NEAYSHHVV1rtY04RzM0cmQOXlQqqS/TIlWdHAP2K/XbFY7C7q1XxhO5kMu+cY6YMM7mq15CNUJwXyIaIU5mJeDo6Dk/K2H9QA9U2yAjwJzvt/cRkkl7CmNZJPoyQUFUl2WiBM8WmLJSPJR7JH4TfXO0AaVCHT1DPWlE8OUu8aFywVZ5y0pfozcZO2k1XGam3T5mt2m/ivNj0ug2REOYX/gqo2ELTw7o/Nhc2r/OEsF2p3zFBvyrE5Q/EfiLu2bhRcCj84vtx0y/CeAjdr9PJ+qzZxsbo+2s17qc01ZmhLb6+nMW0cqHHtg1G8hiJG4Rji/os1mjurd3J7vYP3/+DvzuhHd6pimbt22OaWIhtGdcPr0BQ8lUhWRc4k6s9VN3YApMDbXjLKkQQV+6TN4aZBKXvuJ8BiY64OLjgD7ie6F8mL)
- [Proposed, no reputation: PT3](https://wowsims.com/forever/paladin/protection/#eNrFVN1LFFEUn3Nndvd6N5vZ0XS69aCL1ChIs7sNqS8zSVDQy1D9AW6oteCDqA9lBCoaEn0hsagPWk2CSGVJhUlGSB+6IElEoGR+RBT0YCCFBUF3ZnT7QHoSOg+H3/mdc3733MvMIbkYFMgDFSrgONRCE8AVgH4AOQuDxFIqRDjHbp82K4B2+rEgIdoMJIA/9InK5ywi4JdfJOZnWxzyxSVQHmUz8I5lL+5j4HsnKG83MzDfFnIYAU/2iSx80wJewdwa/yMJzHdOOWr3XT/MfADPsoIuk4FvSVDm/Iy370G4TBpPqEs12tejJU/uhKzz16AbAsnDN+K9fTAAykA/XEgs2OKiLb63xbbEucSSLU7b4jy0JsqxdzcThkAgiHAjKKwxixVrekyLMRCNxLSIrkeKdS0a0aNOMjKOhCmEZhC3iJ7xJJtg6oxydwLCmDBUHNPqyRaSQQPEh0ct1bdKR/V6kkuCY4BZdeuKJaUTrD6HEMoi/KoHVP8qH9HqZYGiMk5WMdACosg5xJdCCAMJDrkqyx1seMK5nYOjoPJyEVXJdpmSjHDgH7WfzlisdhP1znxsO50Mu/cY7IE07mix5D1UJ4XyTqIU5WBeDo6A0/K8F9QA9Y2xA3gSnPH/4tJI3s2G1kgBDZNQWCSZKYEwxQfNlowkH8kcgt9C7wIpUIX0UA/ZUD45SL1nnLVUnA5SlupP143ZTlcpO2udMZ+y18R/jelxaSQjyin8R1S5gqCZd79wLts8y+/KcKF21Qx1dzk2bSj+/Jhry0bhqexb+xcaLxveP8FNGd2836qJn6yqCyd5r7Wp2gyt6W31NCaM/GrXXhvRJZRnFA0j7r9Yg7mxegfX19tx8w/++qS+d6NOLHV9u22uKbKtVDuwDI3BQ/FEZd6ReN2xqoZ2gC7w0vNGGZKgfJu0uuU0KGG//QGw2L6rhRPOpvsJ9kvMXg==)

The proposed links load PT3 in the beta tree order. The live wowsims has no proposals, thus the site gives beta values for these talents.

### Results with each gear set

| Trees | Gear | Talents | TPS | DPS | DTPS | TMI | Crushing blows | No consumables: TPS, TMI, sec out of mana | No buffs: TPS, sec out of mana |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Proposed | Reference tank gear | PB1 | 1,077 | 600 | 250 | 30.9 | 0.6% | 872, 39.8, 0 | 519, 81 |
| Proposed | Reputation | PT3 | 1,190 | 673 | 214 | 21.8 | 0.5% | 977, 29.4, 0 | 447, 135 |
| Proposed | Reputation | PT3 option | 1,202 | 676 | 215 | 21.9 | 0.5% | 984, 29.4, 0 | 451, 139 |
| Proposed | Reputation | PB1 (search) | 1,171 | 661 | 211 | 21.7 | 0.5% | 962, 27.3, 0 | 440, 139 |
| Proposed | No reputation | PT3 | 1,155 | 669 | 220 | 25.1 | 0.5% | 957, 32.2, 0 | 426, 139 |
| Beta | Reference tank gear | Reference beta build | 946 | 525 | 276 | 38.4 | 10.9% | 754, 49.5, 2 | 401, 125 |
| Beta | Reputation | BT4b | 994 | 555 | 230 | 28.8 | 9.4% | 753, 36.2, 50 | 331, 148 |
| Beta | No reputation | BT5 | 860 | 491 | 223 | 27.4 | 7.6% | 634, 34.5, 63 | 264, 154 |

- **Gear gives more than talents.** For the proposed tank, the path gear gives −29% TMI and +10% TPS against the reference gear. PT3 adds +1.6% TPS against PB1.
- **The gear search drops Defense.** It takes Stamina, Strength and block value. With Redoubt (C-P1) and Holy Shield (C-P9), crushing blows stay at 0.5%.
- **Beta.** The path gear gives −25% TMI and +5% TPS against the reference gear. Crushing blows stay at 8–11%.
- The reference tank gear is the gear of `models/wowsims/data/julien_prot.json`.

## 4. Stat weights

Method: each stat + and − a small amount, 20,000 iterations, the same random seed, gear with reputation items. Steps: 10 Defense, 10 block value, 5 block rating, 12 dodge rating, 15 parry rating, 10 hit rating, 14 critical hit rating, 10 haste rating, 10 expertise rating, 20 for primary stats and spell damage, 40 attack power, 100 armor. Ratings for 1%: hit 10, crit 14, haste 10, expertise 10, block 5, dodge 12, parry 15. Armor is bonus armor.

### Balanced score (40% TPS, 20% DPS, 20% DTPS, 20% TMI), raid

Each weight is the change of the balanced score at the values of the build: 0.4 × TPS change / TPS + 0.2 × DPS change / DPS − 0.2 × DTPS change / DTPS − 0.2 × TMI change / TMI.

| Stat | Proposed (PT3), Strength = 1 | Beta (BT4b), Strength = 1 | Proposed (PT3), Spell damage = 1 | Beta (BT4b), Spell damage = 1 |
| --- | --- | --- | --- | --- |
| Defense | 7.58 | 7.95 | 4.43 | 4.24 |
| Block rating | 6.36 | 6.31 | 3.72 | 3.37 |
| Expertise rating | 4.59 | 4.60 | 2.68 | 2.45 |
| Block value | 4.27 | 1.42 | 2.50 | 0.75 |
| Dodge rating | 4.09 | 3.72 | 2.39 | 1.98 |
| Agility | 4.03 | 3.79 | 2.35 | 2.02 |
| Hit rating | 3.40 | 1.67 | 1.99 | 0.89 |
| Parry rating | 3.39 | 3.13 | 1.98 | 1.67 |
| Spell damage | 1.71 | 1.88 | 1.00 | 1.00 |
| Stamina | 1.62 | 2.01 | 0.95 | 1.07 |
| Crit rating | 1.20 | 1.34 | 0.70 | 0.71 |
| Strength | 1.00 | 1.00 | 0.58 | 0.53 |
| Haste rating | 0.87 | 1.13 | 0.51 | 0.60 |
| Attack power | 0.37 | 0.38 | 0.22 | 0.20 |
| Armor | 0.18 | 0.17 | 0.10 | 0.09 |
| Intellect | 0.00 | 0.05 | 0.00 | 0.03 |

### Threat only (TPS), Spell damage = 1, by mana case

Seconds out of mana: proposed 0 / 0 / 135, beta 0 / 50 / 148 (raid / no consumables / no buffs).

| Stat | Proposed raid | Proposed no consumables | Proposed no buffs | Beta raid | Beta no consumables | Beta no buffs |
| --- | --- | --- | --- | --- | --- | --- |
| Hit rating | 1.98 | 1.68 | 1.34 | 0.98 | 0.84 | 0.75 |
| Expertise rating | 1.95 | 1.61 | 1.47 | 1.83 | 1.64 | 1.63 |
| Block value | 1.01 | 1.03 | 0.96 | 0.00 | 0.00 | 0.00 |
| Spell damage | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Crit rating | 0.66 | 0.55 | 0.55 | 0.69 | 0.58 | 0.58 |
| Haste rating | 0.55 | 0.48 | 0.25 | 0.61 | 0.53 | 0.24 |
| Strength | 0.48 | 0.48 | 0.45 | 0.44 | 0.45 | 0.45 |
| Agility | 0.23 | 0.31 | 0.28 | 0.39 | 0.30 | 0.08 |
| Attack power | 0.20 | 0.20 | 0.20 | 0.18 | 0.19 | 0.21 |
| Stamina | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | −0.02 |
| Intellect | −0.02 | −0.01 | 4.57 | 0.03 | 0.37 | 0.20 |

### Survival only (TMI), Stamina = 1, raid

| Stat | Proposed (PT3) | Beta (BT4b) |
| --- | --- | --- |
| Defense | 3.01 | 2.10 |
| Block rating | 2.54 | 1.34 |
| Dodge rating | 1.64 | 0.92 |
| Parry rating | 1.31 | 0.74 |
| Agility | 1.26 | 0.73 |
| Stamina | 1.00 | 1.00 |
| Block value | 0.91 | 0.34 |
| Expertise rating | 0.42 | 0.31 |
| Armor | 0.06 | 0.05 |

### What the weights show

- **Defense is the best stat for both trees.** It removes crushing blows (beta) and boss critical hits, and it adds dodge, parry, block and miss. It has the best survival value.
- **Proposed: block rating and block value have high value.** Each block gives Holy Shield damage (C-P9), Reckoning charges (C-P6) and mana (C-P8). With the Wowhead shield values, the gear does not fill the combat table. Thus, block rating has value for threat and survival.
- **Beta: block value gives no threat.** In the beta, Holy Shield damage does not use block value.
- **Hit and expertise are the best threat stats.** With raid buffs, 1 hit rating gives the threat of about 2 spell damage (proposed). For the beta, expertise is first.
- **1 spell damage gives the threat of about 2 Strength** (proposed 2.1, beta 2.3).
- **Intellect.** With raid mana support, Intellect has no threat value. With no buffs, the proposed tank is out of mana for 135 sec. Then Intellect is the best threat stat (4.6 spell damage for each point).
