# Retribution: best damage build, gear and stat weights

This file gives the best damage builds on one target for the beta trees and for the proposed trees (calculator version 6). It also gives the pre-raid gear and the stat weights. All values come from wowsims Forever (see [README](README.md)).

## Summary

| Trees | Case | Best build | Points | Code | DPS |
| --- | --- | --- | --- | --- | --- |
| Proposed | Raid | RB6 | 5/8/38 | `v6p2003-030000000000005-021533120133032153` | 881 |
| Proposed | Raid | Shock-Retribution | 28/0/23 | `v6p50032032201212302--02251010013300005` | 867 |
| Proposed | Fresh 60 | Ret build | 9/8/34 | `v6p3003003-030000000000005-02253310013303215` | 353 |
| Beta | Raid | Holy Shock build | 23/0/28 | `551030032001012--052152310012303` | 873 |
| Beta | Raid | Ret build | 15/0/36 | `55003002--05225331201330321` | 810 |
| Beta | Fresh 60 | Holy and Retribution build | 22/0/29 | `550031031101002--052251310013303` | 311 |

- **Raid.** "Raid" is full raid buffs and debuffs, with consumables. In the proposed trees, RB6 is the best build. Shock-Retribution is 1.6% below it. In the beta, the Holy Shock build is 8% above the best Ret build.
- **Fresh 60.** "Fresh 60" is no buffs, no debuffs and no consumables. The proposed Ret build is the best: 14% above the best beta build. The Holy Shock builds go out of mana.
- **Proposed against beta.** In a raid, the best proposed build is 0.9% above the best beta build. The beta Holy Shock build has Divine Strength 5 and Consecrated Ground 2. In the proposed trees, Divine Strength is removed (Toughness and Divine Strength removal, C-P3), and Consecrated Ground (M-H4) is in row 6.
- DPS values: gear with no Fist of Cenarius (part 3).

## 1. Method

- **Sim.** wowsims Forever commit a10f483 (30 October 2026) with `models/wowsims/proposals.patch`. Proposals in the sim: Holy Strike Seal trigger (C1), Reverence (C-H1), Conviction (C-R1), Twist of Light (C-R2), Sanctified Judgement (C-R3), Burning Zeal (C-R4) and Measure for Measure (C-R5). Vindication has 3 ranks with +2/4/6% Attack Power (C-P3), and Burning Zeal has 5 ranks.
- **Fight.** 3 min, one level 63 boss. The search uses 1,500 iterations. The final values use 10,000 iterations. The standard deviation of the mean is less than 1 DPS.
- **Rotations.** The default Twist of Light APL, and a Holy Shock APL (Holy Shock above 40% mana). Each result uses the better of the two.
- **Talent search.** The search starts from the best builds of Analysis, Builds (version 6). It moves 1 to 3 points at a time, with the rules of the calculator, and keeps a change when the DPS increases.
- **Path.** Gear search and talent search in turns, until neither changes. The gear search changes one slot at a time. It tests the 15 best pre-raid items for each slot, and all trinkets with an effect. Then each build is tested with the gear of all the other cases, and the best gear stays.
- **Gear rules.** Item level 66 or lower, no raid drops, no raid materials, Alliance. Reputation and PvP reputation rewards stay in. The enchants are the enchants of the wowsims Twist of Light preset. All sets use Libram of Law.
- **Beta.** The beta builds keep their talents. The gear search runs again on the new sim.
- **Codes.** All proposed codes load in calculator version 6 with 51 points.

## 2. Best builds

### Proposed

| Build | Code | Raid | Fresh 60 | Talents |
| --- | --- | --- | --- | --- |
| RB6, 5/8/38 | `v6p2003-030000000000005-021533120133032153` | **881** | 300 | Holy: Divine Intellect 2, Improved Seals 3. Protection: Precision 3, Benediction 5. Retribution: Improved Judgement 2, Holy Conduit 1, Conviction 5, Vindication 3, Burning Zeal 5, Sanctified Judgement 3, Seal of Command, Pursuit of Justice 2, Sacred Arbiter, Two-Handed Weapon Specialization 3, Vengeance 3, Measure for Measure 3, Champion of the Light 3, Instrument of Law 2, Twist of Light |
| Shock-Retribution, 28/0/23 | `v6p50032032201212302--02251010013300005` | 867 | 245 | Holy: Divine Intellect 5, Improved Seals 3, Unyielding Faith 2, Reverence 3, Purifying Power 2, Infusion of Light 2, Lingering Light 2, Divine Favor, Divine Precision 2, Holy Shock, Holy Power 3, Consecrated Ground 2. Retribution: Improved Judgement 2, Holy Conduit 2, Conviction 5, Vindication 1, Burning Zeal 5, Seal of Command, Sacred Arbiter, Two-Handed Weapon Specialization 3, Vengeance 3 |
| Holy Shock, 21/0/30 | `v6p50032032201010002--02253010013303205` | 862 | 249 | Holy: Divine Intellect 5, Improved Seals 3, Unyielding Faith 2, Reverence 3, Purifying Power 2, Infusion of Light 2, Lingering Light 2, Divine Favor, Holy Shock. Retribution: Improved Judgement 2, Holy Conduit 2, Conviction 5, Vindication 3, Burning Zeal 5, Seal of Command, Sacred Arbiter, Two-Handed Weapon Specialization 3, Vengeance 3, Champion of the Light 3, Instrument of Law 2 |
| Ret, fresh 60, 9/8/34 | `v6p3003003-030000000000005-02253310013303215` | 839 | **353** | Holy: Divine Intellect 3, Improved Seals 3, Reverence 3. Protection: Precision 3, Benediction 5. Retribution: Improved Judgement 2, Holy Conduit 2, Conviction 5, Vindication 3, Burning Zeal 5, Sanctified Judgement 3, Seal of Command, Sacred Arbiter, Two-Handed Weapon Specialization 3, Vengeance 3, Champion of the Light 3, Instrument of Law 2, Twist of Light |

- Each build uses its own gear set (part 3).
- **A 7/8/36 build has the same raid DPS.** `v6p4003-030000000000005-021531120133032153` (Divine Intellect 4, Sanctified Judgement 1) has 882 DPS in a raid. Alone, it is out of mana after about 35 sec and has 238 DPS. RB6 keeps Sanctified Judgement 3/3. Thus, RB6 stays the reference.
- **Sanctified Judgement and fresh 60.** Alone, Sanctified Judgement 3/3 and Reverence give the mana for the fight. Thus, the fresh 60 build keeps them and takes no Measure for Measure.
- **Shock-Retribution.** The search moved 1 point from Divine Precision to Holy Power (`v6p50032032201112402--02251010013300005`, +0.2%, within the noise). The code of Analysis, Builds stays.
- The Holy Shock builds need mana support. At fresh 60, they are 30% below the Ret build.

### Beta

| Build | Code | Raid | Fresh 60 | Talents |
| --- | --- | --- | --- | --- |
| Holy Shock, 23/0/28 | `551030032001012--052152310012303` | **873** | 272 | Holy: Divine Strength 5, Divine Intellect 5, Healing Light 1, Improved Seals 3, Reverence 3, Purifying Power 2, Divine Favor, Holy Shock, Consecrated Ground 2. Retribution: Benediction 5, Improved Judgement 2, Holy Conduit 1, Conviction 5, Vindication 2, Sanctified Judgement 3, Seal of Command, Sacred Arbiter, Two-Handed Weapon Specialization 2, Vengeance 3, Champion of the Light 3 |
| Ret, 15/0/36 | `55003002--05225331201330321` | 810 | 262 | Holy: Divine Strength 5, Divine Intellect 5, Improved Seals 3, Reverence 2. Retribution: Benediction 5, Improved Judgement 2, Holy Conduit 2, Conviction 5, Vindication 3, Sanctified Judgement 3, Seal of Command, Pursuit of Justice 2, Sacred Arbiter, Two-Handed Weapon Specialization 3, Vengeance 3, Champion of the Light 3, Instrument of Law 2, Twist of Light |
| Fresh 60, 22/0/29 | `550031031101002--052251310013303` | 777 | **311** | Holy: Divine Strength 5, Divine Intellect 5, Improved Seals 3, Unyielding Faith 1, Reverence 3, Purifying Power 1, Infusion of Light 1, Divine Favor, Consecrated Ground 2. Retribution: Benediction 5, Improved Judgement 2, Holy Conduit 2, Conviction 5, Vindication 1, Sanctified Judgement 3, Seal of Command, Sacred Arbiter, Two-Handed Weapon Specialization 3, Vengeance 3, Champion of the Light 3 |

## 3. Gear

### Main sets (no Fist of Cenarius)

The item list gives no source for Fist of Cenarius (item level 66, +40 spell damage, +2% critical hit). Thus, the main sets do not use it. Dragonslayer's Signet is not in the search, because it comes from an Onyxia quest.

| Slot | Proposed RB6, raid | Proposed Shock-Retribution, raid | Proposed Ret, fresh 60 | Beta Holy Shock, raid | Beta Ret, raid | Beta, fresh 60 |
| --- | --- | --- | --- | --- | --- | --- |
| Head | Lionheart Helm | Lionheart Helm | Black Dragonscale Helm | Lionheart Helm | Lionheart Helm | Black Dragonscale Helm |
| Neck | Medallion of the Dawn | Medallion of the Dawn | Amulet of the Dawn | Medallion of the Dawn | Beads of Ogre Might | Medallion of the Dawn |
| Shoulders | Theramore Pauldrons | Lightforge Spaulders | Mantle of the Timbermaw | Lightforge Spaulders | Highlander's Lamellar Spaulders | Highlander's Lamellar Spaulders |
| Back | Cloak of the Honor Guard | Cloak of the Honor Guard | Sergeant Major's Cape | Sergeant Major's Cape | Earthweave Cloak | Earthweave Cloak |
| Chest | Timbermaw Tunic | Timbermaw Tunic | Soulforge Breastplate | Timbermaw Tunic | Timbermaw Tunic | Soulforge Breastplate |
| Wrist | Deeprock Bracers | Rockfury Bracers | Soulforge Bracers | Rockfury Bracers | Deeprock Bracers | Rockfury Bracers |
| Hands | Soulforge Gauntlets | Soulforge Gauntlets | Soulforge Gauntlets | Soulforge Gauntlets | Soulforge Gauntlets | Storm Gauntlets |
| Waist | Belt of the Archmage | Belt of the Archmage | Belt of the Archmage | Belt of the Archmage | Belt of the Archmage | Belt of the Archmage |
| Legs | Sentinel's Lamellar Legguards | Sentinel's Lamellar Legguards | Titanic Leggings | Sentinel's Lamellar Legguards | Titanic Leggings | Titanic Leggings |
| Feet | Feralheart Boots | Feralheart Boots | Soulforge Boots | Feralheart Boots | Feralheart Boots | Feralheart Boots |
| Finger 1 | Band of Earthen Might | Band of Earthen Might | Channeler's Ring | Band of Earthen Might | Band of Earthen Might | Channeler's Ring |
| Finger 2 | Don Julio's Band | Don Julio's Band | Don Julio's Band | Don Julio's Band | Don Julio's Band | Don Julio's Band |
| Trinket 1 | Jewel of the Guard Captain | Jewel of the Guard Captain | Jewel of the Guard Captain | Jewel of the Guard Captain | Jewel of the Guard Captain | Jewel of the Guard Captain |
| Trinket 2 | Adaptive Combat Assistant | Adaptive Combat Assistant | Adaptive Combat Assistant | Adaptive Combat Assistant | Adaptive Combat Assistant | Adaptive Combat Assistant |
| Main hand | Arcanite Champion | Doomulus Prime | Doomulus Prime | Doomulus Prime | Arcanite Champion | Doomulus Prime |

All sets use Libram of Law.

wowsims links (gear, talents, rotation, buffs and encounter of each case):

- [Proposed RB6, raid](https://wowsims.com/forever/paladin/retribution/#eNrFV31sE2UY73PdrtdnbC3vOnZ9mXCeTLrqSHtlBghhhaFCcKbZoiAhkWO7bSVdi72WYEzMiEaIEZDEQFgMmk0SskBQ0AQWQWM0IvGPGRQRQxwlJJpoQGL4o4nG964t/VjXheDHJb289+vT5/39nvf56GGTAE4QQQIPbIYB2AZDALsB3gU4CkBc5rec8e0SCMIaCMEGoBONgt3J0ZeQFya3iDfr0Sa88gGIu21YJVz82skef3kbxG94tvj8Q4d4vY4tPj0C4msutrhwDMS9QWZ5Yx+wx2vsh6aHHxn+Ux3Dzx0Bdv/zgHHf/4mT3T+acLKt7vSIv9ahhT2fmnDKS53nw57fIr47W0J7RmAY7FdWHug+8/zVvTAG4thRSI063ghfG3XcHHX8MOrYG74x6jim3oIzRx2rZuUlB2EcqpBDyzg316f4fIFW89Om+NsCAb/i8wcCvoDiP89VTXBcijvXgAtxbgpEnLOyJxHeriY0SdX1cH9U65XUZFyVBeSxqlXx6SihawxmoyPNz0IMJSMRKa5G+7UCiwXoTsEcdIXi2japW1MjUqxP6ogNDqrRXtmG1WhtDej4KM5PQRPSIquucP9AQosl9aim67IdmXWrf1Gbji3YlAI3NnaoeiJPbWuyt18b1KKJAlOygMpYJzNytwWGCVdDHiEFDqztjG3XpERMGtQimkbctBFr0zyisP4JqT+pxnsp4y+cOAymg3neJoEn3DILdaV5pna1FlFflDrVrbG41LFaX2Yhq2gQF1MF3d5GAUjNMMcCIJw4Cx6r4Qg5FogGb71gJdW3bZxgpWZ8fIsUnd41JBvpBuwk60qIYK1cg/YRyPLBR7wtQhWxj+UASk9yjQJH7CO2HJJ17tdpTjJppg9hY5p3IekeiCUjvVJc64tr+oDUHeswKZweBU91JbMu0+yLw8C81dPZKajDWR2xqK71xNVEOBYlDlqbAkb88R2xeE9YHxSt3ubpMojUULtJ7mzIU+1dPe1JkhbKUjHNs1Rco+plDExS3zJSvDdRPsfIJroRnyZP4Xz5gYqu0NhLTPMNWP+MrpW6wZqUYOy1byjkgXzEvKegUtKSt4DuB3wVyE6YmcC8ND8X3YWbFznDFXQ5Nsm0AkmHXJsjevAdVvlTWZsH6D3Ll1bAZaDfAa4lT1amWOiveCezyFIcO9RB5thPdkFuVdghjEiZHYLUxlla3xZyZSbcLTibzHrCeJWFYEFi2uIMfB1yYCYNG8aAoDPNM82dhois57p4UbmTP4D+DvgmkD1QWVxB9MoIDNIVFSIvy9KM51ccIoVsyi2mEXJvISqVfQnoRUCdvFBZtNG5pgifkkeV065YWCAnLHC/wjLHXCpsCOjLGCD+mQuqmNdiltzZxb3yKqHg7c23ObKBPovryFqzv1eT6s+4u/3dnFWzvQ5jdmyxUHPY+X3NpR3dZDkCOedmX7wQYh0tXNJhn6Pr/9mdjBh/bCSPIk8XQ2L6T8STmjK/7OEXGDRXSP4CM/eUAUqyM1JxFf6JyKBKm1Jf1DiYNITHmGnR0Zlom7I8PziJjywyQ8WXDF2/noMLImjAypdQbj6S94EcB+yk6+6z/otKTKLzyjScK7zAzur7XSERcBldkgGyFY4tZCHWnIQ8IHrnsP8CNeN5iGY0KelySrrIdSCTmU42E9eKk+R+J1FF8ZdLxZtdoFB8BigSb0JZ8T9zvbc4ZafVYl5Lg8NWPsTSTYvLf3F2ExvqC7qHDxnXV+0P9pnXpXZlkhNtUrv3NGf5X65E8D/Z5uHj/9o+S81713vBlVkguNl4yzoEmafJ9lUF72G+gnct441sB+zg/gbVrfOw)
- [Proposed Shock-Retribution, raid](https://wowsims.com/forever/paladin/retribution/#eNrFV39sE1Uc7/e2Xa/fsrW8/bo+5nYcTLrqyPXKDBDCOoYKwZFmi4KERAq7bSXdir2WYGLMUCPECKgxGBZFs0lCFn4oaAKLaEI0IvEPjIqAIY4SEk00IDHGNNH47tpubdd1EvxxaS6vn/ve930+3/d93+89rBPACSJI4IZN0AfbYBBgN8DbAIcBSJX5lDOeLgY/rIIArAf6iyjYnBx9GnlhfLN4sxKtwnPvgbjbiqXC5WeB/f3xDRC/5Nngk/cd4vUKNjh7CMQXqtjg/BEQ9/qZ5Y19huU19qLp4TuGf1/B8I8OAbv/sd+4v/Kxk90/uOBkBl8cA/GnCrQw4OQFp7zEeS7k/jms/LY5sGcYhsB2pW1/1+knru6FURBHD0NixPFS6NqI4+aI4/KIY2/oxojjSPAWnD7sWDFrUrMfxqAUObSMcQ1Ki6L4VPZTFa/qVX3NzYqiqi1exasoXp/vHFd6geMS3JUaXIBzEiBiTduWWGh7MKZJQV0P9Q5o3VIwHg3KAvJY2qwqOkpYNQqz0ZHkZyEG4uGwFA0O9GpZFvPRlYAarApEtW1SlxYMS5EeqT3S3x8c6JatWIYlzT4d78eGBNQhzbHqDPX2xbRIXB/QdF22IbNu9i5s0bEJ6xLgwtr2oB6bpLY13t2r9WsDsSxTMp/KWCEzcrcFhglXA24hAQ4s74hs16RYROrXwppGXLQWy5M8orDuIak3Hox2U8ZfOH4QTAf1njqBJ9xSC61K8kztSi0cfErqCG6NRKX2lfpSC1lB/biIqujy1ApA7EMcC4Bw/Ay4SwxHyLFAVHsqhRJSdtvKCSXUjI+yUNXphCHZQNdjB1mTRwTLZTvahiHNB+/zNAmlxDaaASg9wdUKHLENWzNI2rlXpxnJZB6di9WkEmd7HIaSzRZqhn6R0mgS+HAE3GWkjbZiC/FhPalD+zAYD46dB3cplp8AZL6vvbqWcM6yQk6MqX9/E4hKFZxP5L/xxoR30kjnYW2Sr0LS1ReJh7ulqNYT1fQ+qSvSbpqdMtkVMes0zT49CExpJZ2dgAqc1R4Z0LUt0WAsFBkgDlqeYISEB3dEoltCer9Y4mmcLruJndrMwJ0JuMs8K6fNMtJE2TZJ8mybrArqBQxMUl8zUrwnVjj/yUa6AdeSR7BBvqeoKzTmEpN8NVY+qmv5btCeEIy59g0G3DAZMc9JKLahyGtAXwF8HshOmJlAfZKfg67syXOc4XK6DOtkWoSkQy7PEH39LVaZprI2F9Bzhs/fnZeAfgO4mjxcnGK2v9yZzAKQ4Nii9jPHXrILMqPs6mVEyqxepDzKttxtIVMChIliYJVZ9o6VWghmJaY1ysAXIQOm0rB6FAg6kzzT3GGISHuuiOaUIvIrazaALwPZA8XFZUWvgEA/XV4k8rIszbh+uSFSycbMYBohdxaifNkXgX4FqJMni4s2quoU4VPyqHja5QrzZYT57lZYapnzhQ0CfQZ9xDvzhsrltYgld3pwp7zyKHi6J8scWU8fwzVktdl7ykjZWW6i95h9NK8se5XG/G5jshyGjHOzLp4PsIoWyquwj9N1/+xME21JlaeLITH9x6JxTW0ouPhZBo1Fkj/LzDWluZN0/1arsj9wUqjaolbmFA4mDeEBZpqzdCbaoi6bbOpEIQvNUPF5HwRePQNnRdCA1c+gUH8k7wI5CthB19zl/s/ZYhKtL1BwrvACW6tvdwVEwKV0cQpI73BsIgvQfgImAdFTw75T7GOTEE1pUpOFlHSS60DGU5VsJq5FO8nddqKi4i/lizerQLb4FJAj3oTS4n/gum9x6s4Si3kt8Q+V8AGWblpU/pOzmdhgj981dMC4Pm+d22NeF1vVcU60Sq2eU5zlf7li/v9kmnuP/mvzLDHvne/429KAf5NxDDwAqX/jrSuyDopK1mHQODLugB3cXyS+CjE=)
- [Proposed Ret, fresh 60](https://wowsims.com/forever/paladin/retribution/#eNrFV31oE2cYz3NpL5entqlvU5u+du3tZmearZJc7FARG63bFNcRWjadCPM01zaSJu4uEQdjqzCmjKkTxGH/cKPdH1J0boqgZd1gMPxgfyhzzgkyFxHG2PCDsT8CG3vvkphLmqaI+ziS483vHp7393ve5yOHLQLUgwdE8MJmGILtMAKwB+AjgKMAxG0+5YynSyAEayAMG4BeaRKc9Rx9Ax3C1GmX504DW+z6DDx7HFgl/HIQkBcuv+W5zDP4wjHw3Kpji/Ns8Y6bLS6yxb4QM7y9H9jPe59A1sE5hv9Yx/BDl+rZ/c9DwO4HvjTWpxniEL5hlr/WoY0Bpy7VS0vrz0e9v8X8f2wJ7x2DUXBeX3mo/+yrN/bBBHgmjkJ63PVe9Kdx151x1w/jrn3R2+OuY8pdOHvUtWpOQXMIJqEKObRNcq3+oN/8dJrfLlnuCgYDfn8gGPQH5cB5ruoSx6W5LxpxIc5PgwfnrdyajO5Qkqqo6Hp0MK5GRCWlKZKAPFZ1yn4dRXRPwFx0Zfg5iOFULCZqSnxQtVgswOY0zEN3WFO3i/2qEhMTA2JPYnhYiUckB1ajvTOo49PYloYWpEVWfdHBoaSaSOlxVdclJzLrzsCiLh07sCUNzdjUo+jJArVtqcigOqzGkxZTsoBKWCcxcvcFhgk3wl4hDS6s7U3sUMVkQhxWY6pKmmkT1mZ4RGH9c+JgStEilPEXThwB00Grr0XgCbfMRt0ZnqldrcaU18VeZVtCE3tW68tsZBUN4WIqY7OvSQBSM8qxAAgnpsBrNxwhxwLR6GsQ7KT6voMT7NSMj3+RrNMHhmQj3YC9ZF0JEayVatA5Bjk++JSvQ6gizok8QOlJrkngiHPMkUdyzgM6zUsm7fQJbMrwbiT9Q4lULCJq6oCm6kNif6LHpHBmHLzVlcz6TLOvjwDz1kDnpqEO5/Qk4rq6VVOS0UScuGhtGhjxZ3cmtK1Rfdhj97XPlEGkhjpNclNhb7Vv9YwnSTooS8UMz1JxjaKXMTBJXWGkeF+yfI6RTXQjvkhewDbpsYqu0NjLk+EbseElXS11gzVpwdhr/0jYC4WI+U5BpaQlB4EeAHwbyC6YnUBrhp+PzdbNi5zhCrocWyRagaRLqs0T/eBDVvzTWZsH6JviSyvgGtDvANeS5ytTtPor3skssjTHDnWYOQ6Q3ZBfWTuEESmzQ5BajaX1fSFfZsKDgnNIrCdMVtkIWhLToTHwXciD2TRsnACC9Rmeae41ROQ812lF5U5+B3oP8H0ge6GyOEv0yggM0RUVIi9J4qznVxwimWzKL2YQ8nAhKpV9Fei3gDp5rbJoo3NNEz4tjyqnXbGwYF5Y8FGFZY+5VNgI0DcxSAKzF1Qxr8UsuXOLh+VVQsEXKbQ5soG+jOvIWrO/V5Pqr7gH/d2cVXN9LmN2bLFRc9gF/O2lHd1kOQZ552ZfvBhmHS1a0mFfoev/2Z2MGH9uJI8szRRDYvpPailVbit7+BaD9grJbzFrnjZASW5Gym7rn4gsKnfJDUWNg0lDeIaZFh2diXbJywuDk/jJIjNUfMnQDeh52BJBA5bPQbn5SD4Fchywl657xPovKjGRtpZpONd5gZ3V97vDHsBldEkWyFU4dpCFWHMSCoDHN4/9F6iZLEA0q0nOlFPSR24BuZntZLNxrThJHnUSVRR/rVS82QWs4rNAkXgTyon/mYvc5eRddpt5LQ2N2vkwSzdVk/7inCY2MhBqHj1sXBe6Hx8wr6vd8k3O4xC7fWc42/9yJUP/yTZPHv/X9llq3vs+Dq3MAaHNxpvWYcj+utm9yvIu5re8bxlvZTthJ/c3kd70Tg==)
- [Beta Holy Shock, raid](https://wowsims.com/forever/paladin/retribution/#eNrFV31sE2UY73PbrtenbC3vvm4vcxwHk646cr1SA4SwjqFCcKTZoiAhkUJvW0m3Yq8jGBMdaoQYASEGwxLRbJKQhQ8FTWARTYhGJP4BUREwxFFC4h8akBhjmmh879pubdd1Evx4/7i897vnnvf3e97nfZ47rBfACSJI4IKN0ANbYQBgF8C7AEcASJX5lDOeLgI/rIQArAP6iyjYnBx9HnlhbJN4uxKtwssfgLjLiqXC1ZeAwZdeFC/xDP7sQ4d4s4JNzh0G8dUqNrlwFMQ9fmZ4ay+w2xvsPdPB9wz/oYLhnxwGdv3jgHHd96mTXT+66GQGXx0H8acKtDDg1EWnvNh5Puz6OaL8timwewgGwXat9UDnmWeu74EREEeOQGLY8Xr4xrDj9rDj6rBjT/jWsONo8A6cOeJYPmNCsh9GoRQ5tIxyks/nUbyK4lUVxaN41OZmxad6fKrXw+5Vr+I9z5Ve5LgEd60G5+OsBIhY07o5Ht4WjGtSUNfD3X1aSAr2x4KygDyWNquKjhJWjcBMdCT5GYiB/khEigX7urUsi3lYl4AarArEtK1SpxaMSNEuqS3a2xvsC8lWLMOSZq+OD+PsBNQjzbHqCHf3xLVov96n6bpsQ2bd7Fng07EJ6xNQh7VtQT0+QW1Lf6hb69X64lmmZB6VsUJm5O4KDBOuB1xCAhxY3h7dpknxqNSrRTSN1NFaLE/yiMLax6Tu/mAsRBl/4cQhMB00uOsFnnBLLLQqyTO1K7RI8DmpPbglGpPaVuhLLGQ59eNCqmKdu1YAYh/kWACEE2fBVWI4Qo4FotpdKZSQsrtWTiihZnyUBapOxw3JeroO28nqPCJYLtvRNgRpPviQu0koJbaRDEDpSa5W4IhtyJpB0s49Os1IJnPpHKwmlTjT7TCUbLJQM/QLlUaTwMfD4CojrbQFfcSLDaQe7UNgPDh+AVylWH4SkPm+sX8N4ZxlhZwYS//+NhCVKjiPyH/jjXHvpJHOxdokX4WksyfaHwlJMa0rpuk9Ume0zTQ7bbIrYtZhmn1+CJjSSjozARU4oy3ap2ubY8F4ONpHHLQ8wQgJj26PxjaH9V6xxN04VXYTO7WZgTsbcJW5V0yZZaSJsmOS5NkxWRnUCxiYpL5hpHh3vHD+kw10Pa4hT+Bs+YGirtBYS0zy1Vj5pK7lu0F7QjDW2jsQcMFExNynoNiBIm8C3Qf4CpAdMD2BhiQ/C+uyF89xhsvoUqyXaRGSDrk8Q/Std1hpmsza3ED3WT7/dF4B+i3gKvJ4cYrZ/nJXMgtAgmOb2ssce8hOyMyyq5cRKbN6kfIYO3J3hUwJEMaLgVVm2TtaaiGYlZjWGANfgwyYSsPqESDoTPJMc7shIu25IpZTisivrNkAvgFkNxQXlxW9AgL9dFmRyMuyNO3+5YZIJRsykymE3FuI8mVfBvo1oE6eLS7aqKqThE/Ko+JplyvMmxHmvV9hqW3OFzYA9AX0Es/0ByqX10KW3OnJvfLKo+AOTZQ5so4+havJKrP3lJGyc9x47zH7aF5Z9iiN+d3GZDkEGedmXbwQYBUtnFdhn6Zr/9mVxtuSKk8VQ2L6j8f6NXV2wc3PMmgskvxZZnWTmjtJ92+1KvsDJ4WqPrUyp3AwaQiPMNOcrTNRn7p0oqkThSwwQ8XnfRB49AycFUEDVr+AQv2RvA/kGGA7XX2f5z/niEm0oUDBucYLbK++2xkQAZfQRSkgfcKxicxH+0mYAER3DftOsY9OQDSlSU0WUtJBbgIZS1Wy6bgW7ST324mKir+SL96sAtniU0COeBNKi/+RC93h1B0lFnMs9g+W8AGWblpM/pOzmdhAl79u8KAxvmyZ02WOyy3qGCdapRb3ac7yv4y4/z9Z5sFj/9o6i81rx3v+1jTg32j8Bh6E1N1Yy/KsH0Ul62fQ+GXcDtu5vwA0TQox)
- [Beta Ret, raid](https://wowsims.com/forever/paladin/retribution/#eNrFV31sE2UY73PdrtdnbC3vOta9TDhPJl11pL1SA4SwwlAhONNsUZCQyLHetpKuxV5LMCZmJAaIEZDEaFgMmk0SsoAY0AQWQeNHRP6aURExxFlC4h8aPmL4o4nG964tvXZdF4If98flvd89ed7f73mfjztsFcAJbhDBA1thEHbAMMA+gHcBjgEQl/GW098ugxCsgzBsAjrZLNidHH0JeWFqm/tGI9qEPSfAvc+GNcKVt4E9fn4U3N/wbPHFhw73tQa2+JQhe1xscfE4uA+EmOX1g7rlrfch5+Enhv/cwPDzR4Hd/3xTvx/6xMnuH0062VZ3+ty/NaCFPZ+edErLnReint9jvjvbwvtHYQTsV1a/2Xv2+asHYBzc48cgM+Z4LfrLmOPGmOPHMceB6PUxx3HlJpw95lgzpyg5BBNQgxxaJrj5waDPF/D55I4OX1CWg4GAX/b5AwFfQPZf4GomOS7DnW/CxTg/A26ct7ovFd2ppFRR0bToQFyNiEo6qUgC8ljTIfs0FNE1DnPRkeXnIIbTsZiYVOIDqsliEbZkYB66wkl1h9irKjEx0S92JYaGlHhEsmEtWjsCGj6KCzPQirTEqic6MJhSE2ktrmqaZEdm3eFfEtSwHVsz0ILNXYqWKlLbno4MqENqPGUyJYuohA0SI3dbYJhwNewRMuDA+u7ETlVMJcQhNaaqpIU2Y32WRxQ2PiEOpJVkhDL+wskjYDhY4G0VeMKtsFBXlmdq16ox5UWxW9meSIpda7UVFrKGhnAplbHF2ywAqRvhWACEk+fAY9UdIccC0eRtFKyk9raNE6zUiI9viazRu4ZkM92E3WRDGRGsl+rQPgp5PviIt12oIfbxAkDpKa5Z4Ih91FZA8s79Gi1IJm30IWzO8i4kvYOJdCwiJtX+pKoNir2JLoPCmTHw1FYz6zHMvjwCzFsjnZuBBpzTlYhral9SSUUTceKg9RlgxB/flUj2RbUht9XbNlMGkTpqN8idC3tqvWtnPEnSTlkqZnmWiusUrYKBQeo7Ror3pirnGNlCN+PT5ClcKD1Q1RXqe7mzfBM2PqOp5W6wLiPoex0cDnugGDHvaaiWtOQNoIcAXwGyG2YnsCDLz8cW8+YlznAVXYmtEq1C0iHVF4i+9Q6r/OmsjQP0nuPLK+Ay0O8B15Mnq1M0+yvdySiyDMcOdYg59pO9UFiZO4QeKaNDkPokS+vbQqHMhLsFZ5NYT5iosRA0JaYtycBXoQDm0rBpHAg6szzT3K2LyHtuSJaUO/kD6C3A14Hsh+riTNGrIDBEV1WJvCSJs55faYhksqWwmEHIvYWoXPYloN8CauSF6qL1zjVN+LQ8qp52pcICBWGB+xWWO+ZyYcNAX8YA8c9eUKW8lrLkzi/ulVcZBW+k2ObIJvosbiDrjf5eS2o/4+72d2NWzfU69NmxzUKNYef3tZV3dIPlKBScG33xYph1tGhZh32Obvxnd9Jj/LGePLI0UwyJ4T+VTKvywoqHbzJoq5L8JrOWaQOU5Gek7DJ/RORQOSg3ljQOJg3hMWZacnQGGpRXFgcn8ZElRqj4sqHr1wqwKYI6LH8FleYj+QDICcBuuuE+67+kxES6oELDucIL7Kx+2Bt2A66gy3JAvsKxnSzGulNQBNzeeexboG6iCNGcJjlbSUkPuQZkKtfJZuNadZLc7ySqKv5yuXijC5jF54AS8QaUF/8rF7nJybutFuNaHhqx8mGWbmpS+ouzG9hwf6hl5LB+fd35YL9xXeqUpzi3Tez0nuEs/8uVCv0n2zx84l/bZ7lx73kvtDoPhLbqf1mHIfc01bnG9B/mM/1r6X9ku2AX9zdrHfNv)
- [Beta, fresh 60](https://wowsims.com/forever/paladin/retribution/#eNrFV31sE2UY73PdrtdnbB3vOta+TDhPJl11pL1SA4SwwlAhONNsUZCQyEFvW0nX4l1LMDFmRCPECEhiICwGzaYJWUAUQgKL0wRjBOMfGBURQ8QSEv/Q8BHjH000vndt6bXbuhD8uDSX93598ry/3/M+H3fYKkAjeEAEH2yGAdgOQwB7AN4FOApA3Oa/nPHvEojAGojCBqCXWgRnI0dfQocwcdrludnEFq98BJ49DqwRrrwN7PGz98HzNc8WF46B53oDW5xjyGtu5IXLWzz7Iszwxn7D8PYHkHfwIzP8qYHhBy82svufB4HdD3xqrE8zxCF8xSx/bUAbA05dbJSWNp6P+35LBP7YEt07AsPgvLLyYO/Z56/ugzHwjB2F7KjrjfjPo66bo64fRl374jdGXceUW3D2qGvVrJLmCIxDDXJoG+fEcDgQCAXZLxgIBgJyR0cgLMvhIIMCwVAoEDrP1VzkuCz3STMuxLlZ8OCclVvT8R1KWhUVXY/3J9WYqGQ0RRKQx5oOOaCjiO4xmI2uHD8LMZpJJERNSfarFosF6M3CHHRHNXW72KsqCTHVJ3alBgeVZExyYC3aO0I6Porzs9CKtMyqJ94/kFZTGT2p6rrkRGbdEVwU1rEdW7PgxZYuRU+XqG3LxPrVQTWZtpiSBVTCBomRuyMwTLga9QlZcGF9d2qHKqZT4qCaUFXipS1Yn+MRhfVPiP0ZRYtRxl84cQRMB/P8rQJPuGU26s7xTO1qNaG8KHYr21Ka2LVaX2Yjq2gEF1MZvf4WAUjdMMcCIJyYAJ/dcIQcC0Szv0mwk9o7Dk6wUzM+gUWyTu8ako10A3aTdRVEsF6qQ+cIFPjgI/52oYY4x4oApSe5FoEjzhFHESk4D+q0KJm00YewJce7kfQOpDKJmKipfZqqD4i9qS6TwplR8NVWM+sxzT4/AsxbE52dhQac1ZVK6upWTUnHU0niovVZYMQf35nStsb1QY/d3zZdBpE66jTJTUR9tf7V054kaacsFXM8S8U1ij6FgUnqW0aK96enzjGyiW7Ep8lTOF96oKorNPby5PhmbHpGVyvdYF1WMPbaPxT1QSli/lNQLWnJW0APAL4KZBfMTGBejp+LXuvmZc5wBV2OrRKtQtIl1ReJHnqHlf9k1uYB+if4ygq4DPQ7wLXkyeoUrf7KdzKLLMuxQx1kjoNkNxRX1g5hRMrsEKReY2l9RyiWmXC34BwS6wnjNTaClsR0aAx8HYpgPg2bx4BgY45nmrsNEQXPDVpZuZPfgd4GfBPIXqguzhK9KQRG6IoqkZckccbzKw+RTDYVF9MIubcQVcq+BPQbQJ28UF200bkmCZ+UR9XTrlxYqCgsdL/C8sdcKWwI6MsYIsGZC6qc12KW3IXFvfKqoOCPldoc2UCfxXVkrdnfa0ntOe5ufzdn1Wy/y5gdW2zUHHbBQFtlRzdZjkDRudkXv4yyjhav6LDP0fX/7E5GjD82kkeWposhMf2ntYwqz5/y8C0GbVWS32LmnTRASWFGym7rS0QelcNyU1njYNIQHmOmZUdnomF5eWlwkgBZZIaKrxi6Qb0IWyJowPIXMNV8JB8COQ7YTdfdZ/2XlZhI503RcK7wAjur73dHPYDL6JI8UKhwbCcLse4klACPfw57F6gbL0E0r0nOTaWkh1wHci3fyWbiWnWS3O8kqir+cqV4swtYxeeBMvEmVBD/Cxe7xcm77DbzWhoZtvNRlm6qJv3FOU1sqC/iHT5sXBc6H+wzr0ud8jXO4xA7/Wc42/9ypSP/yTYPH//X9llq3nvei6wsAJHNxrfWYcg/XetcZfkaC1i+uIzvsp2wk/sbecL0lA==)

The live wowsims has no proposals. Thus, a proposed build loads with the beta values of its talents. The values of this file come from the sim with the proposals.

### With Fist of Cenarius

Fist of Cenarius in place of the two-handed weapon of each set. It adds 8 to 20 DPS in a raid. The order of the builds stays the same.

| Trees | Build | Raid | Fresh 60 |
| --- | --- | --- | --- |
| Proposed | RB6 | **900** | 311 |
| Proposed | Shock-Retribution | 887 | 254 |
| Proposed | Ret, fresh 60 | 851 | **365** |
| Beta | Holy Shock | **887** | 280 |
| Beta | Ret | 818 | 271 |
| Beta | Fresh 60 | 789 | **319** |

## 4. Stat weights

Method: one stat at a time is added to the main gear (no Fist of Cenarius). Steps: +100 for primary stats and spell damage, +200 for attack power and armor penetration, ±20 rating, +10 weapon DPS. 10,000 iterations, the same random seed for all runs. EP = DPS for each point of the stat / DPS for each point of Strength. A value below zero (noise) shows as 0.00.

| Stat | Proposed RB6, raid | Proposed Shock-Retribution, raid | Beta Holy Shock, raid | Beta Ret, raid | Proposed Ret, fresh 60 |
| --- | --- | --- | --- | --- | --- |
| DPS for each point of Strength | 0.421 | 0.429 | 0.448 | 0.428 | 0.203 |
| Strength | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Agility | 0.90 | 0.74 | 0.67 | 0.77 | 0.85 |
| Intellect | 0.61 | 0.20 | 0.63 | 0.55 | 1.69 |
| Spirit | 0.00 | 0.16 | 0.01 | 0.00 | 0.78 |
| Spell damage | 0.86 | 0.90 | 0.79 | 0.73 | 1.07 |
| Attack power | 0.45 | 0.45 | 0.41 | 0.41 | 0.50 |
| Hit rating, below the cap | 2.91 | 2.00 | 2.77 | 2.58 | 2.30 |
| Hit rating, above the cap | 0.17 | 0.18 | 0.69 | 0.27 | 0.21 |
| Critical hit rating | 1.21 | 1.09 | 1.00 | 1.05 | 1.29 |
| Haste rating | 0.77 | 1.09 | 1.15 | 0.45 | 1.56 |
| Expertise rating | 1.58 | 1.87 | 1.74 | 1.94 | 1.57 |
| Armor penetration | 0.11 | 0.09 | 0.09 | 0.11 | 0.04 |
| Weapon DPS | 6.04 | 6.37 | 5.79 | 5.64 | 6.80 |

- **Hit.** All sets are at the hit cap. 10 hit rating gives 1% hit. Below the cap, hit is the best stat. Above the cap, it has little value. Shock-Retribution has Divine Precision: its spells keep the cap with less melee hit.
- **Raid.** Hit rating below the cap, expertise rating and critical hit rating give more DPS than Strength. Strength is the best primary stat. Haste has more value for the Holy Shock builds than for the Ret builds.
- **Fresh 60.** Mana limits the DPS. Intellect (1.69), haste (1.56) and spell damage (1.07) are above Strength, and Spirit has value (0.78).
- **Spell damage against Strength.** Strength gives attack power, and attack power adds to melee swings and Seal of Command at the full rate. Spell damage adds nothing to melee swings, and each spell takes only a part of it.
- **Proposed against beta.** The weights are almost the same. Conviction (C-R1) adds critical hit chance to spells, and Burning Zeal (C-R4) adds critical damage. Thus, critical hit rating and spell damage have a little more value for the proposed builds.

## 5. Limits

- The two APLs are the same for all builds. A rotation made for each build can change the result by a few DPS.
- The gear search changes one slot at a time. Thus, it can miss a set bonus that needs several slots at the same time.
- The sources in the item list are not complete. The item list can include some items that are not pre-raid in the game.
- Some proposals are not in the sim (moves only, Lingering Light, Reckoning). They do not change the DPS of one Paladin on one target.
- The fights are 3 min on one boss. Longer fights cost the Holy Shock builds more mana.
