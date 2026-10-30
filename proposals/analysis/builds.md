# Builds

This section examines the builds that are possible with the proposed trees. It gives the best builds for each spec and role. It also gives the builds that use a different tree for a role.

## Summary

- The proposed trees (calculator version 4) have about 6.5 × 10^14 legal builds of 51 points. A search examined the trees of version 3 for each role with the models of this document. The builds of versions 4 to 6 keep the same talents where the rows permit it.
- Each talent is in at least one good build. No talent is without a use.
- The tank builds dip 13 points into Retribution for Sanctified Judgement and Improved Judgement (3/35/13). This dip gives more threat and mana than the Holy dip with Reverence (8/35/8): +12 threat per sec and +4.4 mana per sec.
- Each spec has a clear main build. Each role also has real choices: mana, threat, saves and PvP control.
- Only one build outside the main tree is good: Shock-Retribution. In version 6, Divine Precision is in its beta place (Holy row 5), with no requirement (M-H5). Shock-Retribution is then equal to RB6 in a raid in wowsims (part 5). Tanks and healers outside their tree are weaker.
- Toughness and Divine Strength removal (C-P3) deletes both talents. Each point in rows 1 and 2 now has a use for its spec. A tank build can have area and single-target talents together (part 3).
- Benediction (M-P1) moves to Protection row 1. The tank, Retribution and Holy builds keep their damage, threat and healing values. Retribution raid builds lose Guardian's Favor. Holy builds receive Benediction 5/5 and 4 free points.
- Three hybrids need 52 points. They are Holy Shock with Twist of Light, Holy Shock with Holy Shield, and Holy Shield with Retribution row 5. This 1-point gap stops the strongest hybrids.

## 1. Method

- **Search.** A program examined all legal builds for each role. It moved points between talents and kept the best result. It used the row rules and the requirements of the calculator.
- **Damage.** The model of Analysis, Damage: raid buffs, a level 63 boss, a 2 min fight.
- **wowsims search (30 October 2026).** A second search used wowsims Forever for the new talents. It started from RB6 and from Shock-Retribution. Each step moved 1–3 points and kept the best of 64 builds. Raid buffs, a 3 min fight, the Retribution preset gear and the Holy Shock rotation (models/wowsims/run_damage.py).
- **wowsims search, version 6 (30 October 2026).** 14 searches on the version 6 trees: 7 for raid damage and 7 for tanks. They started from RB2, RB6, Shock-Retribution, PT3, PB1, PT2 and 7 random builds. Each step moved 1–3 points and kept the best of 48 builds. A check at 6,000 iterations then compared the best builds. The new builds are in parts 3, 4 and 5.
- **Threat and mana.** The models of Analysis, Threat and Mana: pre-raid gear, 200 spell power, 108 block value, 3,400 mana. The mana column uses fresh level 60 gear (2,897 mana).
- **Healing.** The first version of the model of Analysis, Healing, with the Classic big heals of the other classes: 900 healing power. The "full fight" values use a 10 min fight.
- **PvP burst.** The model of Analysis, PvP burst check: one 6 sec Hammer of Justice stun.
- **Codes.** All codes open in version 6 of the calculator with 51 points and no error. A code that starts with "v6p" opens the proposed trees. The codes of versions 1 to 5 open on their own pages.
- **Version 6 (Retribution layout, M-R4, M-R5, Burning Zeal with 5 ranks, and Vindication with 3 ranks).** Vengeance requires Burning Zeal 5/5, and Sanctified Judgement requires Improved Judgement 2/2. Vindication has 3 ranks with +2/4/6% Attack Power (C-P3). Thus, the Retribution builds of version 5 changed. Each build takes Burning Zeal 5/5 and Vindication 3/3. A wowsims search (raid and fresh 60, 6,000 iterations) chose the other points.

## 2. Holy

| Build | Points and code | Healing | What it gives |
| --- | --- | --- | --- |
| HB1. Raid and PvP healer | 34/12/5: v6p53201132251010512-30200000000000502-0005 | Reference. 22% critical heal chance | All useful Holy talents (34 points). Conviction 5. Benediction 5, Guardian's Favor (Hand of Protection each 3 min) and Devoted Sacrifice (Lay on Hands drains 50%, C-P11). Redoubt 3 opens row 3 |
| HB2. Healer with more saves | 32/14/5: v6p53200032251010512-30200020000000502-0005 | The same as HB1 | Sacred Duty 2/2 (Divine Shield −60 sec, +4% Stamina), Guardian's Favor, Devoted Sacrifice and Benediction 5. Redoubt 3. No Unyielding Faith or Voice of Truth. Possible only with Spiritual Focus in row 2 |
| HB3. PvP, Hammer of Justice each 45 sec | 28/18/5: v6p53201132251010002-50200010030000502-0005 | About −4% maximum, −8% for the full fight (estimate: as the 30/16/5 build of version 4, without Holy Power 1/5) | Improved Hammer of Justice 3/3 (row 4, 18 Protection points as in the beta), Redoubt 5, Sacred Duty 1/2, Devoted Sacrifice 2/2. Unyielding Faith 1/2. No Light's Vigil and no Holy Power |
| HB4. Tank healer with the new talents | 35/12/4: v6p5320013025101051222-30200000000000502-0004 | −1% against HB1 (Conviction 4/5). After a large hit, Merciful Light (C-H5) on a tank at or below 35% health. Divine Grace (C-H6): the tank takes 1.4% less physical damage (2.3% with one Lay on Hands in a 3 min fight) | Divine Grace 2/2 and Merciful Light 2/2. Voice of Truth. No Unyielding Faith or Purifying Power. Conviction 4/5 |
| HB5. Tank healer with Divine Grace | 34/12/5: v6p5320003225101051202-30200000000000502-0005 | The same healing as HB1 (Conviction 5/5). Divine Grace (C-H6): the tank takes 1.4% less physical damage (10–11% for 15 sec after each Divine Favor or Lay on Hands; 2.3% with one Lay on Hands in a 3 min fight) | HB1 with Divine Grace 2/2 in place of Unyielding Faith and Voice of Truth. Purifying Power or Merciful Light: a 2-point choice |

- **With Merciful Light (C-H5) and Divine Grace (C-H6), the Holy tank healer is complete at 36 points.** HB4 (35/12/4) keeps the Protection dip. It gives up Unyielding Faith, Purifying Power and 1 point of Conviction. HB1 and HB2 keep their codes: the new talents are at the end of the Holy code.
- **Conviction 5/5 is better than Merciful Light for long fights.** HB5 keeps Conviction 5/5 and Devoted Sacrifice: +1% healing against HB4. Divine Grace does not change the healing. It gives armor to the tank. Thus, HB5 is for a healer on the main tank, and HB1 for a raid healer. Take Merciful Light in place of Purifying Power for the burst on a tank after a large hit. The healing model script gives the values (models/healing/run_tables.py, Holy builds).
- **PvP with Merciful Light.** HB3 can use Merciful Light 2/2 in place of Lingering Light 2/2: v6p532011322510100002-50200010030000502-0005. At 715 healing power, Holy Shock then heals about 1,630 on an ally at or below 35% health.
- **Without Merciful Light and Divine Grace, Holy healing is complete at 32 points** (Lingering Light in row 3, C-H2; Holy Power in row 5, M-H3). HB1 adds Unyielding Faith 1/2 and Voice of Truth (2 points) for fear bosses and PvP. These are choices, not filler (part 7).
- **Conviction is the best next talent.** It gives +8% healing for the full fight: more critical heals and more mana from Illumination.
- **The other points give only utility:** Hand of Protection, Divine Shield or run speed (Pursuit of Justice). The 51st point has no healing value.
- **Value of each Holy talent for the full fight:** Reverence 38%, Illumination 28%, Healing Light 23%, Divine Favor 13%, Conviction 8%, Holy Power 8%, Lingering Light 6%. For the maximum healing per second: Infusion of Light 25%, Healing Light 23%.
- **Without the Retribution dip** (45/6/0): −4% maximum, −8% for the full fight. The extra Holy points have no healing value.

## 3. Protection

| Build | Points and code | Threat per sec (one target / with Consecration) | Mana per sec, fresh level 60 (no Consecration / Consecration on cooldown) | What it gives |
| --- | --- | --- | --- | --- |
| PB1. Raid tank | 3/35/13: v6p0003-53051321301551-522103 | 558 / 649 | +25.7 / −16.7 | Improved Seals 3. Sacred Duty 2/2 and Iron Creed 5/5. Deflection 5, Improved Judgement 2, Holy Conduit 2, Conviction 1 and Sanctified Judgement 3. Anticipation 5 and Deflection 5 for the stat targets against a boss (see Crushing blows) |
| PB2. Raid tank, more critical hit | 3/35/13: v6p0003-53051321301551-520303 | 565 / 656 | +25.7 / −44.9 | As PB1, with Conviction 3 in place of Holy Conduit. For one boss with no Consecration |
| PB3. Dungeon tank | 3/35/13: v6p0003-5323132130153102-522103 | 554 / 645 | +25.7 / −16.7 | As PB4, with Anticipation 3 and Reach of Law 2 |
| PB4. Raid tank, utility | 3/35/13: v6p0003-53251321301531-522103 | 554 / 645 | +25.7 / −16.7 | As PB1, with Guardian's Favor 2 and Iron Creed 3/5. Iron Creed then gives −6% damage taken, not −10% |

- **Holy Shield needs 31 Protection points.** A tank build with only useful points uses 33–35.
- **Bosses and dungeons.** Only enemies that are 3 or more levels above you can hit with crushing blows. Dungeon enemies are level 62 or lower. Thus, a dungeon tank does not need the full Anticipation. PB3 uses 2 of these points for Reach of Law. PB3 and PB4 have only these 2 points of difference.
- **Threat values** come from the threat model script (models/threat/run_tables.py) with the gear of Threat, part 1. The mana values come from the mana model script (models/mana/mana_model.py), as in Analysis, Mana. They do not include Blessing of Wisdom. Consecrated Ground is in Holy row 6 (27 Holy points, M-H4). A tank with Holy Shield cannot take it.
- **Raid tank: PB1 is better.** PB2 gives only +1% threat. With Consecration on cooldown, its mana lasts 1 min 4 sec at fresh level 60. The mana of PB1 lasts 2 min 53 sec.
- **Retribution dip (13 points).** Deflection 5, Improved Judgement 2 and 3 more points open Retribution row 3 for Sanctified Judgement. Improved Judgement gives +19 threat per sec and +0.7 mana per sec. Sanctified Judgement gives 14–17 mana per sec, more than Reverence (10.3). Holy Conduit saves 28 mana per sec with Consecration (see Mana).
- **Holy dip (8/35/8).** The first raid tank took Improved Seals, Unyielding Faith, Reverence and Conviction 3: v6p0003203-53051321301551-5003. It has 546 / 637 threat per sec and +21.3 mana per sec. Analysis, Threat uses this tank. PB1 has 2% more threat.
- **Version 6: PT3 with Burning Zeal 3.** The wowsims search found v6p0003-53040221301551-52050000010000003 (3/32/16). It has +1.1% threat against PT3 (1,191 against 1,178 TPS) and +0.6% damage taken (257 against 256). TMI is 31.8 (PT3: 31.5). It takes Burning Zeal 3/5 and Anticipation 4. It drops Vindication 2, Holy Conduit 1 and 1 point of Shield Specialization. Two other searches ended at almost the same build. It has less mana than PT3 (no Holy Conduit). Thus, it is a raid build with mana support. Burning Zeal 3/5 gives Seals and Judgements +12% critical damage bonus.
- **Why the first search missed the Retribution dip.** The threat model had no Improved Judgement, and the mana model had no Sanctified Judgement for the tank. Both models now have them.
- **Threat per sec for each point (8/35/8 tank):** Holy Shield 245 (1 point), Redoubt 16, Swift Judgement 13 (1 point), Reckoning 12, Improved Judgement 9.5 (in PB1), One-Handed Weapon Specialization 9, Improved Seals 7, Precision 4, Conviction 3, Iron Creed 2 (and −10% damage taken), Vindication about 0.5 (and about −1.5% boss melee damage, if no Demoralizing Shout or Roar is on the boss).
- **Benediction (Protection row 1, M-P1).** It saves about 4 mana per sec without Consecration and 11 with Consecration. It gives no threat. Thus, the tank builds take the Retribution dip first: Sanctified Judgement and Improved Judgement give more mana and threat for their points.
- **Divine Strength (Toughness and Divine Strength removal, C-P3).** +10% Strength gave a tank about +15 Strength with pre-raid gear: about +30 Attack Power and +1 block value. Thus, all tank builds skipped it. Retribution received about +7 DPS for 5 points.

## 4. Retribution

| Build | Points and code | Raid DPS (with Consecration) | PvP burst (one stun) | What it gives |
| --- | --- | --- | --- | --- |
| RB1. Raid | 7/8/36: v6p000320101-030000000000005-020533120133032152 | 381 (430). wowsims: 845 | About 1,830 (critical hits ×2.2) | Vindication 3 (C-P3). Benediction 5 and Precision 3. Burning Zeal 5/5 and Measure for Measure 2/3. Reverence 1 and Infusion of Light 1. The best build on one target |
| RB2. Raid with Consecration | 9/8/34: v6p2003103-030000000000005-020533100133032152 | 382 (430). wowsims: 847 | About 1,830 (critical hits ×2.2) | Divine Intellect 2/5: +4% Intellect, more mana for Consecration (see W16). Burning Zeal 5/5 and Measure for Measure 2/3. Unyielding Faith 1/2, no Infusion of Light. Analysis, Damage, parts 1 to 10, use the version 5 talents (Holy Conduit 2/2, Vindication 5/5) |
| RB3. PvP, Hammer of Justice each 45 sec | 1/19/31: v6p0001-23200011030000502-02053110013313215 | 370 (418). wowsims: 811 | About 2,240 (critical hits ×2.2) | Swift Judgement and Improved Hammer of Justice 3/3 (row 4), Repentance, Guardian's Favor, Devoted Sacrifice, Sacred Duty 1/2 and Redoubt 2. Improved Seals 1/3, Sanctified Judgement 1/3 and Burning Zeal 5/5. No Holy Conduit, no Pursuit of Justice and no Eye for an Eye. Benediction 5 opens Protection row 2 |
| RB4. PvP, fear and heals | 5/8/38: v6p00032-030000000000005-022533120133132151 | 380 (428). wowsims: 846 | About 1,830 (critical hits ×2.2) | Unyielding Faith (Holy row 1, M-H2), Holy Conduit 2 and Repentance. Burning Zeal 5/5 and Measure for Measure 1/3. No Reverence, Infusion of Light, Guardian's Favor or Eye for an Eye |
| RB5. Reckoning (Protection and Retribution) | 0/26/25: v6p-532300210215002-32050210013300005 | 280 (325). wowsims: 670 | About 3,020 (critical hits ×2.2) | The build of PvP burst check (see W6). Improved Judgement 2/2 (for Sanctified Judgement 2/3) and Burning Zeal 5/5. No Vindication and no Pursuit of Justice |
| RB6. Raid with the new talents | 5/8/38: v6p2003-030000000000005-021533120133032153 | 383 (432). wowsims: 852, +0.6% against RB2 | About 1,830 (critical hits ×2.2) | Burning Zeal 5/5 (C-R4) and Measure for Measure 3/3 (C-R5). Improved Seals 3, Divine Intellect 2, Holy Conduit 1. No Reverence or Infusion of Light (see Analysis, Damage, part 11) |

- **Raid DPS values** come from the damage model script (models/damage/run_tables.py) with the gear of Analysis, Damage, part 1. The value in brackets uses Consecration on cooldown. The damage model has no Holy Conduit, Eye for an Eye or Sanctified Judgement. Thus, it shows only the gain of Burning Zeal, Measure for Measure and Vindication +6% (+1.6%). The wowsims values use the Retribution preset gear, a 3 min fight and raid buffs.
- **Sanctified Judgement and fresh 60.** Without raid buffs, Sanctified Judgement 3/3 is important for mana. RB4 without Sanctified Judgement 3/3 has 253 DPS alone. With Sanctified Judgement 3/3, it has 303. Thus, no raid build gives up Sanctified Judgement for Burning Zeal. RB3 is a PvP build: it keeps Sanctified Judgement 1/3.
- **RB6 in wowsims.** RB6 has 852 DPS in a raid. RB2 had 824 in version 5 and has 847 in version 6 (Burning Zeal 5/5, Measure for Measure 2/3, Vindication +6%). RB6 is then 108% of the pure average (see Analysis, Damage, part 11). Alone (no buffs), RB6 has 302 DPS: without Reverence, the mana is zero after about 40 sec. RB2 of version 6 has 317 alone (version 5: 326). Holy Conduit 2/2 decreases the Consecration cost, and the mana is the limit alone. A wowsims search from RB6 found no better Retribution build. The version 6 search also found none. It found one equal build with no Protection dip: 8/0/43, v6p5003--422533120133032153. It has 851.5 DPS in a raid (RB6: 852) and 286 alone (RB6: 302). It takes Divine Intellect 5 and Deflection 4 in place of Precision 3 and Benediction 5. With raid buffs and the preset gear, it has the hit cap without Precision.
- **DPS for each point:** Seal of Command 82 (1 point), Twist of Light 47 (1 point), Sacred Arbiter 9 (1 point), Two-Handed Weapon Specialization 6.6, Vengeance 5.3, Improved Judgement 5.2, Conviction 5.0, Precision 4.9, Improved Seals 4.7, Champion of the Light 4.4, Instrument of Law 1.9, Vindication 2.6 (3 ranks, +2% Attack Power for each rank, C-P3).
- **About 6 points are free.** Each choice gives 1.5% DPS or less: Vindication, Divine Intellect, Infusion of Light or Pursuit of Justice.
- **The dips into Holy and Protection are strong:** Improved Seals +6%, Precision +4%. The Protection dip also gives Benediction 5/5 (M-P1). Holy Conduit is in the Retribution tree. Thus, rule 1 of Tree balance works for Retribution.
- **Benediction (M-P1) and the Protection dip.** Benediction 5 opens Protection row 2. Thus, the dip is 8 points (Benediction 5, Precision 3), and Guardian's Favor costs 2 more points. RB1, RB2 and RB4 skip Guardian's Favor. RB3 and RB5 take it.
- **Toughness and Divine Strength removal (C-P3) and Retribution.** Divine Strength gave about +7 DPS. Vindication 3 (+6% Attack Power) gives about +7 DPS with full uptime. Thus, Retribution loses no damage.
- **Holy Power is not good for Retribution.** It is in Holy row 5 (M-H3). A 25/0/26 build with Holy Power loses Twist of Light and Champion of the Light: −19%.

## 5. Builds outside the main tree

| Role | Build | Points and code | Result | Status |
| --- | --- | --- | --- | --- |
| Damage | Shock-Retribution with Divine Precision | 28/0/23: v6p50032032201212302--02251010013300005 | wowsims: 852.5 DPS in a raid (equal to RB6, 108% of the pure average). 249 DPS alone (−22% against RB2) | Divine Precision 2/3 (Holy row 5, beta place), Consecrated Ground 2/2 and Holy Power 3/5. Burning Zeal 5/5, Two-Handed Weapon Specialization 3/3 and Vindication 1/3. Holy Shock and Consecration do not miss |
| Damage | Shock-Retribution with Divine Precision in Holy row 4 (version 5 place, withdrawn) | 21/0/30: v6p50032031201210001--02253010013303205 (it does not load in version 6) | wowsims: 869 DPS in a raid, 2.0% above RB6 | Divine Precision 2/3 and Vindication 3/3 replaced Sanctified Judgement, 1 point of Lingering Light and 1 point of Purifying Power. Divine Precision 2/3 gave +1.6%. Shock-Retribution was then stronger than pure Retribution. Thus, Divine Precision is in Holy row 5 again (see Withdrawn ideas) |
| Damage | Shock-Retribution, version 5, no Divine Precision | 26/0/25: v5p502320322010105--022533120133 (a version 5 code) | 357 DPS (95% of RB2) for 2 min, 405 with Consecration (96% of RB2). wowsims: 791 (96% of RB2). Holy Shock and Holy Power (M-H3) replace Twist of Light and Champion of the Light. After about 2 min, the mana is too low for Holy Shock: 300 DPS (80%) | 28/0/23 replaces it. In PvP, one Holy Shock adds about 560 damage to the burst (about 2,340). Holy Power gives Holy Shock and Holy Strike +15% critical hit |
| Damage | Shockadin | 38/0/13: v6p5023213225131251--02252002 | 311 DPS. The mana is zero after 30–50 sec. 63–70% for 2 min | Not good in raids |
| Tank | Retribution with Righteous Fury and a two-handed weapon | 12/8/31 (RB2) or 5/8/38 (RB6), version 5 talents | Model: RB2 90% of the PB2 threat (511 against 565 threat per sec), RB6 97% (542). wowsims, raid: RB2 868 and RB6 932 threat per sec, 75% and 81% of PT3 (1,151). About 2.8 times the damage taken, with 15% crushing blows | Possible in easy dungeons. The healer must do more work. Measure for Measure gives about +7% threat |
| Tank | Holy Shock tank | 30/21/0: v6p502320322012125-53201321301 | 56% of the PB2 threat (79% with Consecration). The mana lasts about 2 min (35 sec with Consecration) | For solo play while you level |
| PvP | Holy Shock with Iron Creed | 21/30/0: v6p5023203220101-5320132130145 | Righteous Fury stays active in PvP. Iron Creed then gives −10% damage taken. The build also has Templar's Bulwark, Reckoning and Holy Shock | Strong survival. See W17 |
| Tank | Healing tank | 29/22/0: v6p53202132251010002-53201311301100001 | See part 6 | Not good |

- **Holy Shock (rank 4).** 334–362 damage or 307–333 healing, 325 mana, 10 sec cooldown, 42.9% spell damage coefficient. On cooldown, it costs 32.5 mana per sec. Without spell hit, Holy spells miss a level 63 boss 17% of the time. Precision and most Forever hit gear also give spell hit. With Divine Precision 2/3 and the hit from gear, Shock-Retribution reaches the cap: Holy Shock and Consecration do not miss. The 26/0/25 build and the Holy Shock build 21/0/30 (builds/retribution.md) have no Divine Precision. In version 6, 21/0/30 has 854 DPS in a raid (equal to RB6) and 267 alone.
- **Threat for each mana point:** Holy Shield 10.2, Judgement 8.5, Holy Shock 2.8, Consecration 1.4 (one target).
- **Healing Light needs 28 Holy points.** A healer with fewer Holy points loses 23% healing. Thus, no healer build uses a different main tree.
- **Retribution tank.** The model values use attacks from the front (14% parry) and dungeon buffs (Blessing of Might only). From behind with raid buffs, the model gives 116%. That value is not correct for a tank. The wowsims values use raid buffs and the Retribution gear (models/wowsims/run_damage.py). The two results are different. Use the wowsims values to compare with Protection.
- **Consecrated Ground (Holy row 6, M-H4).** It needs 27 Holy points. Shock-Retribution 28/0/23 and Shockadin take it, with Holy Power. In wowsims, the rotation of Shock-Retribution casts Consecration. Shock-Retribution and Shockadin have Holy Conduit, but no Benediction. Retribution with Twist of Light (31 points) and tanks with Holy Shield (31 points) cannot take it.
- **The 52-point gaps.** Holy Shock needs 21 Holy points. Twist of Light and Holy Shield each need 31 points in their tree. Do not move Holy Shock up, or Twist of Light or Holy Shield down, without a new check of these two hybrids.
- **Tanks and Retribution row 5.** Measure for Measure (C-R5) needs 20 points in Retribution rows 1–4: 21 points at least. Holy Shield needs 31 Protection points. Thus, no tank with Holy Shield can take them. With 52 points, Measure for Measure 3/3 gives PB1 +7% threat. Burning Zeal gives a tank +0.2%. A tank with no Holy Shield (0/30/21) has 56% of the PB1 threat.
- **Shock-Retribution and the new Retribution talents.** Shock-Retribution has 3 or 4 points in row 5. Vengeance 3/3 is better there: Burning Zeal and Measure for Measure give 35–55 DPS less in wowsims.

## 6. Healing threat

A tank can heal itself for threat.

- **Rules (Classic).** Each point of effective healing gives 0.5 threat. Overhealing gives no threat. The threat is divided between all enemies in the fight.
- **Righteous Fury.** Its Forever text says "Holy attacks". No test on heals exists (see Open questions). The table gives the two cases.
- **Base build.** The table uses the dungeon tank of version 1 (8/33/10: Conviction, Holy Conduit and Benediction). It has the threat talents of the 8/35/8 tank with Conviction 5: 552 threat per sec. The healing threat does not change with Toughness and Divine Strength removal (C-P3).

| Plan, one target | Healing on yourself per sec | Threat per sec (Righteous Fury ×1 / ×1.9 on heals) | Mana per sec | The mana lasts |
| --- | --- | --- | --- | --- |
| Dungeon tank (version 1), no heals | 0 | 552 / 552 | +14 | All the fight |
| Dungeon tank (version 1) and 1 Flash of Light each 10 sec | 42 | 557 / 576 | 0 | All the fight |
| Dungeon tank (version 1) and 1 Holy Light each 10 sec | 183 | 617 / 700 | −52 | 66 sec |
| Healing tank (29/22/0), 1 Holy Light and 1 Flash of Light each 10 sec | 293 | 335 / 467 | −68 | 50 sec |
| Healing tank (29/22/0), 2 Holy Light and 2 Flash of Light each 10 sec | 586 | 445 / 709 | −143 | 24 sec |

- **A healing tank is not a good build.** The mana lasts 24–50 sec. It has no Holy Shield and no Iron Creed.
- **A heal on yourself is a good tool.** If Righteous Fury multiplies healing threat, one Flash of Light each 10 sec gives +4% threat at no mana cost. One Holy Light each 10 sec gives +27% threat for about 1 min. With Infusion of Light (PB3, PB4), Holy Light has a 1.5 sec cast after Holy Strike.
- **With 4 enemies,** each enemy receives 25% of the healing threat in this table.
- The values include the melee swings that stop during a cast. Healing threat is only possible when you have lost that much health.

## 7. Points that the rows force

The row rules make some builds take talents that do not help their role (filler).

| Build | Filler | Cause |
| --- | --- | --- |
| Holy healer | None (Lingering Light in row 3, C-H2; Holy Power in row 5, M-H3). Before: 2 points (Unyielding Faith or Voice of Truth) | Row 4 needs 15 points in rows 1–3: they hold 16 healer points. Row 6 needs 25 points in rows 1–5: they hold 28 |
| Holy PvP with Improved Hammer of Justice | Redoubt 5 and Sacred Duty 1 (a small PvP defense) | Row 4 needs 15 points in rows 1–3. Benediction, Guardian's Favor and Devoted Sacrifice give 9 |
| Main builds of Protection and Retribution | None | Useful talents fill all rows |

- **Spiritual Focus in row 2 decreases the filler for Holy.** With Spiritual Focus in row 4 (a withdrawn idea), a Holy healer needed 3 points of filler. HB2 was not possible.
- **Lingering Light in row 3 (C-H2) and Holy Power in row 5 (M-H3) remove the last filler.** See Analysis, Tree balance.
- Purifying Power counts as a useful talent here (Cleanse costs 20% less).

## 8. Limits

- The values come from models, not from combat logs.
- The damage-taken values are approximate: one enemy hit of 1,000, 60 block value and the same gear for all tanks. Use them to compare builds, not as exact values.
- The Shockadin model uses a two-handed weapon and Retribution gear. A Shockadin with caster gear is not in the model.
- The mana values include Blessing of Wisdom when the text does not give a different condition.
- Spell miss against level 62 enemies: 6% (assumed).
- Holy Shock range: 20 yards in the client data. One website gives 40 yards.
