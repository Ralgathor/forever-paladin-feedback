# Builds

This section examines the builds that are possible with the proposed trees. It gives the best builds for each spec and role. It also gives the builds that use a different tree for a role.

## Summary

- The proposed trees (calculator version 4) have about 6.5 × 10^14 legal builds of 51 points. A search examined the trees of version 3 for each role with the models of this document. The builds of versions 4 and 5 keep the same talents where the rows permit it.
- Each talent is in at least one good build. No talent is without a use.
- The tank builds dip 13 points into Retribution for Sanctified Judgement and Improved Judgement (3/35/13). This dip gives more threat and mana than the Holy dip with Reverence (8/35/8): +12 threat per sec and +4.4 mana per sec.
- Each spec has a clear main build. Each role also has real choices: mana, threat, saves and PvP control.
- Only one build outside the main tree is good: Shock-Retribution (26/0/25) for short fights and PvP. Tanks and healers outside their tree are weaker.
- Toughness and Divine Strength removal (C-P3) deletes both talents. Each point in rows 1 and 2 now has a use for its spec. A tank build can have area and single-target talents together (part 3).
- Benediction (M-P1) moves to Protection row 1. The tank, Retribution and Holy builds keep their damage, threat and healing values. Retribution raid builds lose Guardian's Favor. Holy builds receive Benediction 5/5 and 4 free points.
- Two hybrids need 52 points: Holy Shock with Twist of Light, and Holy Shock with Holy Shield. This 1-point gap stops the two strongest hybrids.

## 1. Method

- **Search.** A program examined all legal builds for each role. It moved points between talents and kept the best result. It used the row rules and the requirements of the calculator.
- **Damage.** The model of Analysis, Damage: raid buffs, a level 63 boss, a 2 min fight.
- **Threat and mana.** The models of Analysis, Threat and Mana: pre-raid gear, 200 spell power, 60 block value, 3,400 mana. The mana column uses fresh level 60 gear (2,897 mana).
- **Healing.** The first version of the model of Analysis, Healing, with the Classic big heals of the other classes: 900 healing power. The "full fight" values use a 10 min fight.
- **PvP burst.** The model of Analysis, PvP burst check: one 6 sec Hammer of Justice stun.
- **Codes.** All codes open in version 5 of the calculator with 51 points and no error. A code that starts with "v5p" opens the proposed trees. The codes of versions 1 to 4 open on their own pages.

## 2. Holy

| Build | Points and code | Healing | What it gives |
| --- | --- | --- | --- |
| HB1. Raid and PvP healer | 34/12/5: v5p53201132251010512-30200000000000502-0005 | Reference. 22% critical heal chance | All useful Holy talents (34 points). Conviction 5. Benediction 5, Guardian's Favor (Hand of Protection each 3 min) and Devoted Sacrifice (Lay on Hands drains 50%, C-P11). Redoubt 3 opens row 3 |
| HB2. Healer with more saves | 32/14/5: v5p53200032251010512-30200020000000502-0005 | The same as HB1 | Sacred Duty 2/2 (Divine Shield −60 sec, +4% Stamina), Guardian's Favor, Devoted Sacrifice and Benediction 5. Redoubt 3. No Unyielding Faith or Voice of Truth. Possible only with Spiritual Focus in row 2 |
| HB3. PvP, Hammer of Justice each 45 sec | 28/18/5: v5p53201132251010002-50200010030000502-0005 | About −4% maximum, −8% for the full fight (estimate: as the 30/16/5 build of version 4, without Holy Power 1/5) | Improved Hammer of Justice 3/3 (row 4, 18 Protection points as in the beta), Redoubt 5, Sacred Duty 1/2, Devoted Sacrifice 2/2. Unyielding Faith 1/2. No Light's Vigil and no Holy Power |

- **Holy healing is complete at 32 points** (Lingering Light in row 3, C-H2; Holy Power in row 5, M-H3). HB1 adds Unyielding Faith 1/2 and Voice of Truth (2 points) for fear bosses and PvP. These are choices, not filler (part 7).
- **Conviction is the best next talent.** It gives +8% healing for the full fight: more critical heals and more mana from Illumination.
- **The other points give only utility:** Hand of Protection, Divine Shield or run speed (Pursuit of Justice). The 51st point has no healing value.
- **Value of each Holy talent for the full fight:** Reverence 38%, Illumination 28%, Healing Light 23%, Divine Favor 13%, Conviction 8%, Holy Power 8%, Lingering Light 6%. For the maximum healing per second: Infusion of Light 25%, Healing Light 23%.
- **Without the Retribution dip** (45/6/0): −4% maximum, −8% for the full fight. The extra Holy points have no healing value.

## 3. Protection

| Build | Points and code | Threat per sec (one target / with Consecration) | Mana per sec, fresh level 60 (no Consecration / Consecration on cooldown) | What it gives |
| --- | --- | --- | --- | --- |
| PB1. Raid tank | 3/35/13: v5p0003-53051321301551-522103 | 566 / 657 | +8.3 / −34.1 | Improved Seals 3. Sacred Duty 2/2 and Iron Creed 5/5. Deflection 5, Improved Judgement 2, Holy Conduit 2, Conviction 1 and Sanctified Judgement 3. Anticipation 5 and Deflection 5 for the stat targets against a boss (see Crushing blows) |
| PB2. Raid tank, more critical hit | 3/35/13: v5p0003-53051321301551-520303 | 573 / 665 | +8.3 / −62.3 | As PB1, with Conviction 3 in place of Holy Conduit. For one boss with no Consecration |
| PB3. Dungeon tank | 3/35/13: v5p0003-5323132130153102-522103 | 563 / 653 | +8.3 / −34.1 | As PB4, with Anticipation 3 and Reach of Law 2 |
| PB4. Raid tank, utility | 3/35/13: v5p0003-53251321301531-522103 | 563 / 653 | +8.3 / −34.1 | As PB1, with Guardian's Favor 2 and Iron Creed 3/5. Iron Creed then gives −6% damage taken, not −10% |

- **Holy Shield needs 31 Protection points.** A tank build with only useful points uses 33–35.
- **Bosses and dungeons.** Only enemies that are 3 or more levels above you can hit with crushing blows. Dungeon enemies are level 62 or lower. Thus, a dungeon tank does not need the full Anticipation. PB3 uses 2 of these points for Reach of Law. PB3 and PB4 have only these 2 points of difference.
- **Threat values** come from the threat model script (models/threat/run_tables.py) with the gear of Threat, part 1. The mana values come from the mana model script (models/mana/mana_model.py), as in Analysis, Mana. They do not include Blessing of Wisdom. Consecrated Ground is in Holy row 6 (27 Holy points, M-H4). A tank with Holy Shield cannot take it.
- **Raid tank: PB1 is better.** PB2 gives only +1% threat. With Consecration on cooldown, its mana lasts 46 sec at fresh level 60. The mana of PB1 lasts 1 min 25 sec.
- **Retribution dip (13 points).** Deflection 5, Improved Judgement 2 and 3 more points open Retribution row 3 for Sanctified Judgement. Improved Judgement gives +19 threat per sec and +0.7 mana per sec. Sanctified Judgement gives 14–17 mana per sec, more than Reverence (10.3). Holy Conduit saves 28 mana per sec with Consecration (see Mana).
- **Holy dip (8/35/8).** The first raid tank took Improved Seals, Unyielding Faith, Reverence and Conviction 3: v5p0003203-53051321301551-5003. It has 554 / 645 threat per sec and +3.9 mana per sec. Analysis, Threat uses this tank. PB1 has 2% more threat.
- **Why the first search missed the Retribution dip.** The threat model had no Improved Judgement, and the mana model had no Sanctified Judgement for the tank. Both models now have them.
- **Threat per sec for each point (8/35/8 tank):** Holy Shield 253 (1 point), Redoubt 17, Swift Judgement 13 (1 point), Reckoning 12, Improved Judgement 9.5 (in PB1), One-Handed Weapon Specialization 9, Improved Seals 7, Precision 4, Conviction 3, Iron Creed 2 (and −10% damage taken), Vindication about 0.5 (and about −1.5% boss melee damage, if no Demoralizing Shout or Roar is on the boss).
- **Benediction (Protection row 1, M-P1).** It saves about 4 mana per sec without Consecration and 11 with Consecration. It gives no threat. Thus, the tank builds take the Retribution dip first: Sanctified Judgement and Improved Judgement give more mana and threat for their points.
- **Divine Strength (removed by C-P3).** +10% Strength gave a tank about +15 Strength with pre-raid gear: about +30 Attack Power and +1 block value. Thus, all tank builds skipped it. Retribution received about +7 DPS for 5 points.

## 4. Retribution

| Build | Points and code | Raid DPS (with Consecration) | PvP burst (one stun) | What it gives |
| --- | --- | --- | --- | --- |
| RB1. Raid | 10/8/33: v5p000320302-030000000000005-0225531201330321 | 374 (423) | About 1,830 | Vindication 5 (C-P3). Benediction 5 and Precision 3. The best build on one target |
| RB2. Raid with Consecration | 12/8/31: v5p200320302-030000000000005-0225531001330321 | 374 (423) | About 1,830 | Divine Intellect 2/5: +4% Intellect, more mana for Consecration (see W16). Vindication 5 opens row 6. The build of Analysis, Damage |
| RB3. PvP, Hammer of Justice each 45 sec | 0/19/32: v5p-23200011030000502-0205531021331321 | 358 (406) | About 2,240 | Swift Judgement and Improved Hammer of Justice 3/3 (row 4), Repentance, Eye for an Eye, Guardian's Favor, Devoted Sacrifice, Sacred Duty 1/2 and Redoubt 2. No Holy Conduit and no Pursuit of Justice. Benediction 5 opens Protection row 2 |
| RB4. PvP, fear and heals | 7/8/36: v5p000320002-030000000000005-0225531221331321 | 374 (423) | About 1,830 | Unyielding Faith (Holy row 1, M-H2), Infusion of Light and Repentance. No Guardian's Favor |
| RB5. Reckoning (Protection and Retribution) | 0/26/25: v5p-532300210215002-5005031211331 | 278 (323) | About 3,020 | The build of PvP burst check (see W6) |

- **Raid DPS values** come from the damage model script (models/damage/run_tables.py) with the gear of Analysis, Damage, part 1. The value in brackets uses Consecration on cooldown.
- **DPS for each point:** Seal of Command 82 (1 point), Twist of Light 47 (1 point), Sacred Arbiter 9 (1 point), Two-Handed Weapon Specialization 6.6, Vengeance 5.3, Improved Judgement 5.2, Conviction 5.0, Precision 4.9, Improved Seals 4.7, Champion of the Light 4.4, Instrument of Law 1.9, Vindication 1.3 (5 ranks, C-P3).
- **About 6 points are free.** Each choice gives 1.5% DPS or less: Vindication, Divine Intellect, Infusion of Light or Pursuit of Justice.
- **The dips into Holy and Protection are strong:** Improved Seals +6%, Precision +4%. The Protection dip also gives Benediction 5/5 (M-P1). Holy Conduit is in the Retribution tree. Thus, rule 1 of Tree balance works for Retribution.
- **Benediction (M-P1) and the Protection dip.** Benediction 5 opens Protection row 2. Thus, the dip is 8 points (Benediction 5, Precision 3), and Guardian's Favor costs 2 more points. RB1, RB2 and RB4 skip Guardian's Favor. RB3 and RB5 take it.
- **Toughness and Divine Strength removal (C-P3) and Retribution.** Divine Strength gave about +7 DPS. Vindication 5 gives about +6 DPS with full uptime. RB2 loses about 1 DPS. RB1 had Vindication 3: it loses about 4 DPS (−1%).
- **Holy Power is not good for Retribution.** It is in Holy row 5 (M-H3). A 25/0/26 build with Holy Power loses Twist of Light and Champion of the Light: −19%.

## 5. Builds outside the main tree

| Role | Build | Points and code | Result | Status |
| --- | --- | --- | --- | --- |
| Damage | Shock-Retribution | 26/0/25: v5p502320322010105--022533120133 | 357 DPS (95% of RB2) for 2 min, 405 with Consecration (96% of RB2). Holy Shock and Holy Power (M-H3) replace Twist of Light and Champion of the Light. After about 2 min, the mana is too low for Holy Shock: 300 DPS (80%) | Good for short fights and PvP. In PvP, one Holy Shock adds about 560 damage to the burst (about 2,340). Holy Power gives Holy Shock and Holy Strike +15% critical hit |
| Damage | Shockadin | 38/0/13: v5p5023213225131251--02252002 | 311 DPS. The mana is zero after 30–50 sec. 63–70% for 2 min | Not good in raids |
| Tank | Retribution with Righteous Fury and a two-handed weapon | 12/8/31 (RB2) | 89% of the PB2 threat (511 against 573 threat per sec). With Consecration, 91% of PB2 with Consecration (607 against 665). About 1.65 times the damage taken | Possible in easy dungeons. The healer must do more work |
| Tank | Holy Shock tank | 30/21/0: v5p502320322012125-53201321301 | 56% of the PB2 threat (78% with Consecration). The mana lasts about 2 min (35 sec with Consecration) | For solo play while you level |
| PvP | Holy Shock with Iron Creed | 21/30/0: v5p5023203220101-5320132130145 | Righteous Fury stays active in PvP. Iron Creed then gives −10% damage taken. The build also has Templar's Bulwark, Reckoning and Holy Shock | Strong survival. See W17 |
| Tank | Healing tank | 29/22/0: v5p53202132251010002-53201311301100001 | See part 6 | Not good |

- **Holy Shock (rank 4).** 334–362 damage or 307–333 healing, 325 mana, 10 sec cooldown, 42.9% spell damage coefficient. On cooldown, it costs 32.5 mana per sec. Shock-Retribution has 18% spell hit: Holy Shock does not miss.
- **Threat for each mana point:** Holy Shield 10.5, Judgement 8.5, Holy Shock 2.8, Consecration 1.4 (one target).
- **Healing Light needs 28 Holy points.** A healer with fewer Holy points loses 23% healing. Thus, no healer build uses a different main tree.
- **Retribution tank.** The values use attacks from the front (14% parry) and dungeon buffs (Blessing of Might only). From behind with raid buffs, the model gives 116%. That value is not correct for a tank.
- **Consecrated Ground (Holy row 6, M-H4).** It needs 27 Holy points. Only deep Holy Shock builds (Shockadin) take it. Shock-Retribution takes Holy Power (row 5) in its place: with Consecrated Ground in row 5, it had 429 DPS with Consecration (101% of RB2). Shock-Retribution and Shockadin have Holy Conduit, but no Benediction. Retribution with Twist of Light (31 points) and tanks with Holy Shield (31 points) cannot take it.
- **The 52-point gaps.** Holy Shock needs 21 Holy points. Twist of Light and Holy Shield each need 31 points in their tree. Do not move Holy Shock up, or Twist of Light or Holy Shield down, without a new check of these two hybrids.

## 6. Healing threat

A tank can heal itself for threat.

- **Rules (Classic).** Each point of effective healing gives 0.5 threat. Overhealing gives no threat. The threat is divided between all enemies in the fight.
- **Righteous Fury.** Its Forever text says "Holy attacks". No test on heals exists (see Open questions). The table gives the two cases.
- **Base build.** The table uses the dungeon tank of version 1 (8/33/10: Conviction, Holy Conduit and Benediction). It has the threat talents of the 8/35/8 tank with Conviction 5: 560 threat per sec. The healing threat does not change with Toughness and Divine Strength removal (C-P3).

| Plan, one target | Healing on yourself per sec | Threat per sec (Righteous Fury ×1 / ×1.9 on heals) | Mana per sec | The mana lasts |
| --- | --- | --- | --- | --- |
| Dungeon tank (version 1), no heals | 0 | 560 / 560 | +14 | All the fight |
| Dungeon tank (version 1) and 1 Flash of Light each 10 sec | 42 | 565 / 584 | 0 | All the fight |
| Dungeon tank (version 1) and 1 Holy Light each 10 sec | 183 | 625 / 708 | −52 | 66 sec |
| Healing tank (29/22/0), 1 Holy Light and 1 Flash of Light each 10 sec | 293 | 335 / 467 | −68 | 50 sec |
| Healing tank (29/22/0), 2 Holy Light and 2 Flash of Light each 10 sec | 586 | 445 / 709 | −143 | 24 sec |

- **A healing tank is not a good build.** The mana lasts 24–50 sec. It has no Holy Shield and no Iron Creed.
- **A heal on yourself is a good tool.** If Righteous Fury multiplies healing threat, one Flash of Light each 10 sec gives +4% threat at no mana cost. One Holy Light each 10 sec gives +26% threat for about 1 min. With Infusion of Light (PB3, PB4), Holy Light has a 1.5 sec cast after Holy Strike.
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
