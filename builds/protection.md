# Protection: best tank build, gear and stat weights

This file gives the best tank build for the beta trees and for the proposed trees. It also gives the pre-raid gear and the stat weights of each build. All values come from wowsims Forever (see [README](README.md)).

## Summary

| Trees | Build | Code | TPS | DPS | DTPS | TMI | Crushing blows |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Proposed | PT3 | `v6p0003-53030321301551-5215200001` | 1,240 | 710 | 208 | 22.5 | 0.5% |
| Beta | BT4b | `50003-5230513021301351-50201` | 884 | 506 | 212 | 26.0 | about 6% |

- Values: raid with consumables, path gear with reputation items (part 3), 3 min fight, level 63 boss, 3,000 iterations.
- The search used Holy Shield (C-P9) at 200% of block value and the wowsims shield values. With 100% and the Wowhead Forever shield values, PT3 has 1,151 TPS and 23.0 TMI (Analysis, Threat, part 7).
- The proposed tank has 40% more threat than the beta tank, with lower TMI. Redoubt (C-P1) and Holy Shield (C-P9) push crushing blows off the combat table.
- The beta tank keeps 6–11% crushing blows with all gear sets of this file. No beta build in the search removes them.

## 1. Method

- **Score.** The search uses a balanced score: 40% TPS, 20% DPS, 20% damage taken (DTPS), 20% TMI.
- **Talent search.** A hill climb from 8 start builds (3 goals: balanced, threat, survival). It moves one point at a time and keeps the best move. The full run then tests 179 builds at 3,000 iterations.
- **Path.** Gear search and talent search in turns, until neither changes. The gear search changes one slot at a time. It tests the 12 best pre-raid items for each slot.
- **Gear rules.** Pre-raid items only, no raid drops, Alliance. All items are in the wowsims item list of 28 October 2026. The enchants and the libram are the enchants and the libram of the reference tank.
- **Last points.** A check of all 1-point moves from the best beta build, at 3,000 iterations. The last points change the score by less than 1%.
- **Limit.** The search is a local search, not a test of all builds. Builds with no Holy Shield are far below (73–83% of the reference score).
- **Codes.** All codes load in calculator version 6 with 51 points. In version 6, Vindication gives +2% Attack Power for each rank (C-P3). The TPS values of this file use +1% for each rank. PT1 (Vindication 3) and PT3 (Vindication 2) then have a little more threat.

## 2. Best builds

### Proposed: PT3

`v6p0003-53030321301551-5215200001` (3/32/16)

- Holy: Improved Seals 3.
- Protection: Redoubt 5, Precision 3, Anticipation 3, Shield Specialization 3, Sacred Duty 2, Swift Judgement, One-Handed Weapon Specialization 3, Templar's Bulwark, Reckoning 5, Iron Creed 5, Holy Shield.
- Retribution: Deflection 5, Improved Judgement 2, Holy Conduit 1, Conviction 5, Vindication 2, Sacred Arbiter.

Against PB1 (Analysis, Builds), PT3 has +5% TPS with the same gear and about the same TMI. PT3 takes Sacred Arbiter, 4 more points of Conviction and Vindication 2. It drops Sanctified Judgement 3, 1 point of Holy Conduit, 2 points of Anticipation and Shoulder the Burden. With Holy Strike Seal trigger (C1), Holy Strike also triggers Seal of Fury.

**Version 6 option.** `v6p0003-53040221301551-52050000010000003` (3/32/16) takes Burning Zeal 3/5 and Anticipation 4. It drops Vindication 2, Holy Conduit 1 and 1 point of Shield Specialization. In wowsims (raid, Wowhead shield values), it has +1.1% TPS against PT3 and +0.6% damage taken. It has less mana (no Holy Conduit).

**Mana.** PT3 needs raid mana support (Judgement of Wisdom, Blessing of Wisdom). With no buffs and no consumables, PT3 is out of mana for 140 sec. PB1 keeps its mana longer (Sanctified Judgement 3, Holy Conduit 2). Thus, PB1 is the better tank at fresh level 60 with no mana support.

### Beta: BT4b

`50003-5230513021301351-50201` (8/35/8)

- Holy: Divine Strength 5, Improved Seals 3.
- Protection: Toughness 5, Redoubt 2, Precision 3, Anticipation 5, Improved Seal of Fury, Improved Righteous Fury 3, Sacred Duty 2, Swift Judgement, One-Handed Weapon Specialization 3, Templar's Bulwark, Reckoning 3, Iron Creed 5, Holy Shield.
- Retribution: Deflection 5, Improved Judgement 2, Conviction 1.

In the beta, each point of threat costs survival. Toughness, Sacred Duty and Improved Righteous Fury come first with this gear. Without consumables, BT4b is out of mana for about 60 sec.

### Other builds

| Trees | Build | Code | Use |
| --- | --- | --- | --- |
| Proposed | PT1 | `v6p0003-52040321301551-5205300001` | Best with the older gear (Precision 2, Anticipation 4, Conviction 5, Vindication 3). 1,226 TPS and TMI 22.6 with the path gear |
| Proposed | PT2, maximum threat | `v6p0003-53040311301551-0225301201` | +2% TPS against PT1, but +9% damage taken. No Deflection. Version 6: Vindication 3 (+6% Attack Power) and Holy Conduit 2 in place of Vindication 5 (estimate, no new sim) |
| Proposed | PB1 | `v6p0003-53051321301551-522103` | Fresh level 60 with no mana support |
| Beta | BT5 | `50003-5330513011301451-502` | Best beta build with the gear with no reputation items (part 3) |
| Beta | Maximum threat | `50003-0530511101301541-50205` | +3% TPS against the reference beta tank, but TMI +9% |

## 3. Gear

### With reputation items (main sets)

| Slot | Beta (BT4b) | Proposed (PT3) |
| --- | --- | --- |
| Head | Enriched Thorium Helm | Stalwart Helm |
| Neck | Horn of Ve'han | Amulet of the Darkmoon |
| Shoulders | Highlander's Plate Spaulders | Highlander's Plate Spaulders |
| Back | Shifting Cloak | Shifting Cloak |
| Chest | Enriched Thorium Breastplate | Darksoul Breastplate |
| Wrist | Warder's Wristguards | Berserker Bracers |
| Hands | Heavy Thorium Gauntlets | Theramore Gauntlets |
| Waist | Warder's Waistguard | Redeemer's Waistcord |
| Legs | Sentinel's Chain Leggings | Legplates of Valor |
| Feet | Warder's Sabatons | Depleted Thorium Sabatons |
| Finger 1 | Signet Ring of the Bronze Dragonflight | Signet Ring of the Bronze Dragonflight |
| Finger 2 | Warden's Signet of Vigilance | Warden's Signet of Vigilance |
| Trinket 1 | Stormpike Insignia Rank 6 | Stormpike Insignia Rank 6 |
| Trinket 2 | Defender's Grip Stabilizer | Defender's Grip Stabilizer |
| Main hand | Greenhammer | Greenhammer |
| Shield | Evergreen Shield | The Immovable Object |
| Defense from gear and enchants | +98 | +37 |

wowsims links:
- [Beta: BT4b and beta gear](https://wowsims.com/forever/paladin/protection/#eJzFVN1LFFEUn3NndvZ6N5vZcdNp8kEXqVGQZncbUl9mkqCgl6H6A9xQa8EHUR/KCDQ0pE+RkJTQaloQqUwpMMkI+9IFSSIKJU0NISpQEMLH7szo9kH0JHRgLr/zu7/zcS9zD8nBIEMeqFABJ6AWmgBuAPQBSFkYRLqlQoRx7P4ZswKUDh5zIlKagfjxUlKQV7IIh699Eek6fd0hX7eD/CREwSe6e2U/Be8pmNtKwXxr0GE4PJkUqPthEDzBM0/J4TdJoGv7NyfbygUHD0+JVDBLA7tMCuYo+MhT3n4I4TJxPKEu12jfj5U8Hwxal25BN/g7j9yJ9yahH+T+PricWLCFRVtYsoXWxMXEsi1M28I8tCTKsXc2E4aAI4gwIyhX1zQtVqxHY5oeiWlR+kVieqRY16JaZBxxUwjNIGYRvWRJiGDFaeLBBIQxoag4ptWTbSRD8RMfHrVU3zod1etJDgmMAabqljVLTG9QfTYhCvXw2x5Q+XU+otVLnILKGEnFoBQQWcomvhRCGEhgyM2y2kHbJowbOTAKKisVKSrJlRSSEfb/Q/v1nEW1WxSv5lPbiaTYPcdAD6Rxx1lL2qvopFDaReSibMxKgRFwQl71gupXfGO0AEsCM/xPLo2kPbRpjRQoYRIMCyQzxRGa8VGzJSHRRzKH4BfXO0AKVC7d1GPalE8KKN41zloqTjspS+XTujHbiSqltf7S5gt6m/iPNj0ujSSkMDL7GVWuIWhm3X+bCZnn2d0ZLtRumsHuLsemDZnPj7m2ahSeDt07sNB41fBeAzNldLO8VRM/VVUX7mS90KZqM7iRb7uXY8LIr3btnRFdRnlG0TBi/os1mJub79Df8+28+xt/e1Lft1kVS921zTY3MtJ5VNu/Co2Bw/FEZd7ReN3xqoY2gC7wtueNMiRC+Q5xfb5pUEIf/EGw6KSrhZPOjPsBWazK7A==)
- [Proposed: PT3 and proposed gear](https://wowsims.com/forever/paladin/protection/#eJzFVN1LFFEUn3NndvZ6N9vZcdNp6kEXqVGQZncbUl9mkqCgl6H6A9xQa8EHUR/KCFQ0pE+REldCq0kQqSwpMMkIsdKlSCICJfMDoqBCQQjrqTsz6/aB9CR0Hi6/8zvn/M65l5lDcjBIkAsKlMNxqIFGgGsA/QBiFgaBhhQIM7bdPW2Ug9zFY05AchMQL/7Y55eWswiHrS6g5/RVm3zVDtLjIAVfEyBd2kfBjy6Q3m+mYPyFYDMcvjIlUPddcyphrjXg8q/7bJ32LwI9l8/ZeNjJnKUJCYOC750gzfF2xwcQKhUm4spStfrtaPH4vYB54QZ0g7fz8K1Ybx8MgDTQDxfjC5Z/0fJ/sPyt8fPxJcs/bfnnoSVeht27GTAEHEGEGUEhlVq0SNWiapSCSDiqhjUtXKSpkbAWsYPhCcRNITSDmEX0jCVBgmV7lPuTEMKEoqKoWke2kAzZSzx41FQ8KTqi1ZEc4hsDTLNbVk0hHaD52YTI1MNvekDhU3xYrRM5GZUyooJBzieSmE08SYQwEN+Qo7LSQYcnjFM5OAoKKxbKCtkuyiQj5P1H7uczJs3dJLs9n1h2JcXOPQZ7II07mk1xj6yRAnEnkQqzMSv6RsAued4Lilf2jNEGLPHN8L+4NBJ306FVki+HSCDkJ5lJjlDFh02miAQPyRyC31z3AklQuPRQj+hQHtEnu884ayo47SRNhU/njVl2VQnttc6YT+lr4r/GdLk0EpHMSOwnVLGKoIl1vnAmaJxld2U4UL1uBLoTtk3rEp8XdWxFLzgVvLN/oeGy7v4TzJTezfJmdexkZW2ok3VLG6uMwJreVldjUs+rcuytHllCuXrhMGL+i9UbG6t3cH29Hbf/4G++1PZuVMcS52yzjDVFupVqBlagwXcoFq/IPRKrPVZZ3waQADc8r5ciAcq2Caktp0Ix/e0PgEn3XQ2csDfdTydLy8U=)

### With no reputation items

The same path with no faction vendor items, PvP reputation items, Darkmoon Faire items or reputation rings.

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
| Defense from gear and enchants | +103 | +64 |

wowsims links:
- [Beta, no reputation: BT5](https://wowsims.com/forever/paladin/protection/#eJzFVN9LFFEUnnNndvd6N5vZcdPp1sO2SI2CNOs6pL7MJEFBL0P1B7ih1oIPoj6UEahoSFSGhLg+aDkJIpUlBSYZYb90QfIhCgVNDSHqwUAIH7szo9sPpCehA3P5znfP+c65l7mH5GFQIAIqVMJ5qINmgNsAQwByDgaJbakQ4xx7eNmsBNrpx4KEaDOQAF4dFJXvOUTAPV8lti60OuS7m6A8DzPwme12HmPgIwOLuxlYag85jIBnBkXmLntuAL/0IgWcmnV0etjK44EIg2MMBvACC0yZDCwy8MnPePsJRMulqaS6Vqv9OFv66lHIuj4AvRDoPn0v0T8Iw6AMD8GN5LItrtjiqi22J68l12xxzhaXoC1Zgb2jmTAKAkGEG0dU1zQtXqTH45oei2sx5yvRY0W6VjyFhFmE5hG3gt7wJEwwdVp4PA1RTBgqimsNZA/JogHiwxOW6tuki/UGkkeCk4BZdNuGJWU2WHwuIZR5+H0fqP5NPqY1yAJF5ZysYqD5RJFziS+NEAYSHHVV1rtY04RzM0cmQOXlQqqS/TIlWdHAP2K/XbFY7C7q1XxhO5kMu+cY6YMM7mq15CNUJwXyIaIU5mJeDo6Dk/K2H9QA9U2yAjwJzvt/cRkkl7CmNZJPoyQUFUl2WiBM8WmLJSPJR7JH4TfXO0AaVCHT1DPWlE8OUu8aFywVZ5y0pfozcZO2k1XGam3T5mt2m/ivNj0ug2REOYX/gqo2ELTw7o/Nhc2r/OEsF2p3zFBvyrE5Q/EfiLu2bhRcCj84vtx0y/CeAjdr9PJ+qzZxsbo+2s17qc01ZmhLb6+nMW0cqHHtg1G8hiJG4Rji/os1mjurd3J7vYP3/+DvzuhHd6pimbt22OaWIhtGdcPr0BQ8lUhWRc4k6s9VN3YApMDbXjLKkQQV+6TN4aZBKXvuJ8BiY64OLjgD7ie6F8mL)
- [Proposed, no reputation: PT3](https://wowsims.com/forever/paladin/protection/#eJzFVN1LFFEUn3Nndvd6N5vZ0XS69aCL1ChIs7sNqS8zSVDQy1D9AW6oteCDqA9lBCoaEn0hsagPWk2CSGVJhUlGSB+6IElEoGR+RBT0YCCFBUF3ZnT7QHoSOg+H3/mdc3733MvMIbkYFMgDFSrgONRCE8AVgH4AOQuDxFIqRDjHbp82K4B2+rEgIdoMJIA/9InK5ywi4JdfJOZnWxzyxSVQHmUz8I5lL+5j4HsnKG83MzDfFnIYAU/2iSx80wJewdwa/yMJzHdOOWr3XT/MfADPsoIuk4FvSVDm/Iy370G4TBpPqEs12tejJU/uhKzz16AbAsnDN+K9fTAAykA/XEgs2OKiLb63xbbEucSSLU7b4jy0JsqxdzcThkAgiHAjKKwxixVrekyLMRCNxLSIrkeKdS0a0aNOMjKOhCmEZhC3iJ7xJJtg6oxydwLCmDBUHNPqyRaSQQPEh0ct1bdKR/V6kkuCY4BZdeuKJaUTrD6HEMoi/KoHVP8qH9HqZYGiMk5WMdACosg5xJdCCAMJDrkqyx1seMK5nYOjoPJyEVXJdpmSjHDgH7WfzlisdhP1znxsO50Mu/cY7IE07mix5D1UJ4XyTqIU5WBeDo6A0/K8F9QA9Y2xA3gSnPH/4tJI3s2G1kgBDZNQWCSZKYEwxQfNlowkH8kcgt9C7wIpUIX0UA/ZUD45SL1nnLVUnA5SlupP143ZTlcpO2udMZ+y18R/jelxaSQjyin8R1S5gqCZd79wLts8y+/KcKF21Qx1dzk2bSj+/Jhry0bhqexb+xcaLxveP8FNGd2836qJn6yqCyd5r7Wp2gyt6W31NCaM/GrXXhvRJZRnFA0j7r9Yg7mxegfX19tx8w/++qS+d6NOLHV9u22uKbKtVDuwDI3BQ/FEZd6ReN2xqoZ2gC7w0vNGGZKgfJu0uuU0KGG//QGw2L6rhRPOpvsJ9kvMXg==)

The proposed links load PT3 in the beta tree order. The live wowsims has no proposals, thus the site gives beta values for these talents.

### Results with each gear set

| Trees | Gear | Talents | TPS | DPS | DTPS | TMI | Crushing blows | No consumables: TPS, TMI, sec out of mana | No buffs: TPS, sec out of mana |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Proposed | Reference tank gear | PB1 | 1,156 | 645 | 252 | 31.2 | 0.6% | 942, 40.1, 0 | 559, 81 |
| Proposed | Reputation | PT3 | 1,240 | 710 | 208 | 22.5 | 0.5% | 1,038, 29.1, 0 | 448, 140 |
| Proposed | No reputation | PT3 | 1,245 | 708 | 217 | 24.6 | 0.5% | 1,049, 31.5, 0 | 466, 139 |
| Beta | Reference tank gear | Reference beta build | 988 | 553 | 278 | 38.8 | 10.8% | 789, 50.0, 1 | 414, 125 |
| Beta | Reputation | BT4 (Benediction 1) | 874 | 499 | 212 | 25.9 | 6.0% | 646, 33.1, 62 | 271, 154 |
| Beta | No reputation | BT5 | 863 | 494 | 221 | 27.1 | 7.6% | 636, 34.2, 63 | 264, 154 |

- BT4b has about +10 TPS against BT4 with the same TMI. It moves the Benediction point to Reckoning.
- **Gear gives more than talents.** For the proposed tank, the path gear gives −29% TMI against the reference gear. PT3 adds +5% TPS.
- **The gear search drops Defense.** It takes Stamina, Strength and block value. With Redoubt (C-P1) and Holy Shield (C-P9), boss critical hits stay at 0.1% with only +37 Defense.
- **Beta.** The path gear gives −29% TMI and −9% TPS against the reference gear. A beta tank that needs more threat keeps a part of the reference gear.
- The reference tank gear is the gear of `models/wowsims/data/julien_prot.json`.

## 4. Stat weights

Method: each stat + and − a small amount, 20,000 iterations, the same random seed, raid with consumables. Gear with reputation items. Ratings for 1%: hit 10, crit 14, haste 10, expertise 10, block 5, dodge 12, parry 15. Armor is bonus armor. The noise is about ±0.02 TPS and ±0.002 TMI for each point.

### Balanced score (40% TPS, 20% DPS, 20% DTPS, 20% TMI)

| Stat | Proposed (PT3), Strength = 1 | Beta (BT4b), Strength = 1 | Proposed (PT3), Spell damage = 1 | Beta (BT4b), Spell damage = 1 |
| --- | --- | --- | --- | --- |
| Block value | 5.82 | 2.12 | 3.90 | 1.24 |
| Defense | 4.71 | 12.22 | 3.16 | 7.14 |
| Expertise rating | 3.90 | 4.37 | 2.61 | 2.55 |
| Agility | 3.44 | 5.31 | 2.31 | 3.10 |
| Hit rating | 2.06 | 2.93 | 1.38 | 1.71 |
| Stamina | 2.01 | 2.87 | 1.35 | 1.68 |
| Dodge rating | 1.53 | 6.23 | 1.03 | 3.64 |
| Spell damage | 1.49 | 1.71 | 1.00 | 1.00 |
| Parry rating | 1.23 | 5.06 | 0.83 | 2.96 |
| Crit rating | 1.09 | 1.22 | 0.73 | 0.71 |
| Strength | 1.00 | 1.00 | 0.67 | 0.58 |
| Haste rating | 0.80 | 0.99 | 0.54 | 0.58 |
| Attack power | 0.34 | 0.36 | 0.23 | 0.21 |
| Armor | 0.20 | 0.23 | 0.13 | 0.14 |
| Intellect | 0.09 | 0.20 | 0.06 | 0.12 |
| Block rating | 0.05 | 9.87 | 0.03 | 5.77 |

### Threat only (TPS), Spell damage = 1, by mana case

Seconds out of mana: proposed 0 / 0 / 140, beta 0 / 65 / 155 (raid / no consumables / no buffs).

| Stat | Proposed raid | Proposed no consumables | Proposed no buffs | Beta raid | Beta no consumables | Beta no buffs |
| --- | --- | --- | --- | --- | --- | --- |
| Block value | 2.16 | 2.25 | 1.86 | 0.00 | 0.00 | 0.00 |
| Expertise rating | 2.02 | 1.68 | 1.59 | 1.89 | 1.76 | 1.89 |
| Hit rating | 1.55 | 1.25 | 1.01 | 1.75 | 1.38 | 1.36 |
| Spell damage | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Crit rating | 0.69 | 0.57 | 0.55 | 0.71 | 0.59 | 0.58 |
| Strength | 0.56 | 0.56 | 0.53 | 0.47 | 0.50 | 0.50 |
| Attack power | 0.21 | 0.21 | 0.23 | 0.20 | 0.21 | 0.23 |
| Agility | 0.12 | 0.16 | 0.26 | 0.36 | 0.30 | 0.18 |
| Stamina | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| Intellect | −0.02 | 0.04 | 5.67 | 0.13 | 0.37 | 0.62 |

### Survival only (TMI), Stamina = 1

| Stat | Proposed (PT3) | Beta (BT4b) |
| --- | --- | --- |
| Defense | 1.67 | 2.50 |
| Stamina | 1.00 | 1.00 |
| Agility | 0.97 | 0.86 |
| Block value | 0.88 | 0.39 |
| Dodge rating | 0.56 | 1.21 |
| Parry rating | 0.41 | 0.97 |
| Expertise rating | 0.28 | 0.24 |
| Block rating | 0.01 | 1.86 |

### What the weights show

- **Proposed: block value is the best stat.** Holy Shield (C-P9) adds block value to each hit. The search used 200%. At 100%, each point of block value has half the threat value. Block rating has no value, because Holy Shield and Redoubt (C-P1) already fill the combat table.
- **Proposed: Defense, dodge and parry lower the threat.** They take the place of blocks. Each block gives Holy Shield damage, Reckoning charges and mana. Defense still has the best TMI value.
- **Beta: Defense is the best stat.** Each point removes crushing blows. Block rating is second. Block value gives no threat in the beta.
- **Both trees: expertise and hit are the best threat stats after block value.** 1 spell damage gives the threat of 1.8 Strength (proposed) or 2.1 Strength (beta).
- **Intellect.** With raid mana support, Intellect has no threat value. With no buffs, the proposed tank is out of mana for 140 sec. Then Intellect is the best threat stat (5.7 spell damage for each point).
