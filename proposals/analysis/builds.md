# Builds

This section examines the builds that are possible with the proposed trees. It gives the best builds for each spec and role. It also gives the builds that use a different tree for a role.

## Summary

- The proposed trees have about 3.5 × 10^15 legal builds of 51 points. A search examined them for each role with the models of this document.
- Each talent is in at least one good build. No talent is without a use.
- Each spec has a clear main build. Each role also has real choices: mana, threat, saves and PvP control.
- Only one build outside the main tree is good: Shock-Retribution (21/0/30) for short fights and PvP. Tanks and healers outside their tree are weaker.
- C8 removes Divine Strength. Each point in rows 1 and 2 now has a use for its spec. A tank build can have area and single-target talents together (part 3).
- Two hybrids need 52 points: Holy Shock with Twist of Light, and Holy Shock with Holy Shield. This 1-point gap stops the two strongest hybrids.

## 1. Method

- **Search.** A program examined all legal builds for each role. It moved points between talents and kept the best result. It used the row rules and the requirements of the calculator.
- **Damage.** The model of Analysis, Damage: raid buffs, a level 63 boss, a 2 min fight.
- **Threat and mana.** The models of Analysis, Threat and Mana: pre-raid gear, 200 spell power, 60 block value, 3,400 mana. The mana column uses fresh level 60 gear (2,897 mana).
- **Healing.** The first version of the model of Analysis, Healing, with the Classic big heals of the other classes: 900 healing power. The "full fight" values use a 10 min fight.
- **PvP burst.** The model of Analysis, PvP burst check: one 6 sec Hammer of Justice stun.
- **Codes.** All codes open in version 2 of the calculator with 51 points and no error. A code that starts with "v2p" opens the proposed trees. The codes of version 1 (before C8) open on the version 1 page.

## 2. Holy

| Build | Points and code | Healing | What it gives |
| --- | --- | --- | --- |
| HB1. Raid and PvP healer | 35/8/8: v2p53202132251010512-502000000000001-0305 | Reference. 22% critical heal chance | All useful Holy talents (35 points). Conviction and Benediction. Redoubt and Guardian's Favor (Blessing of Protection each 3 min). Holy Conduit 1 |
| HB2. Healer with more saves | 34/12/5: v2p53201132251010512-5320002-0005 | The same as HB1 | Sacred Duty 2/2 (Divine Shield −60 sec, +4% Stamina) and Guardian's Favor. No Benediction. Possible only with Spiritual Focus in row 2 (M2) |
| HB3. PvP, Hammer of Justice each 45 sec | 30/13/8: v2p53202132251010102-5320000003-0305 | −3% maximum, −6% for the full fight | Improved Hammer of Justice 3/3. No Light's Vigil. Holy Power 1/5 |

- **Holy is complete at 34–35 points.** These points give all healing talents and the useful utility talents.
- **Conviction is the best next talent.** It gives +8% healing for the full fight: more critical heals and more mana from Illumination.
- **The other points give only utility:** Blessing of Protection, Divine Shield or run speed (Pursuit of Justice). The 51st point has no healing value.
- **Value of each Holy talent for the full fight:** Reverence 38%, Illumination 28%, Healing Light 23%, Divine Favor 13%, Conviction 8%, Holy Power 8%, Lingering Light 6%. For the maximum healing per second: Infusion of Light 25%, Healing Light 23%.
- **Without the Retribution dip** (45/6/0): −4% maximum, −8% for the full fight. The extra Holy points have no healing value.

## 3. Protection

| Build | Points and code | Threat per sec (one target / with Consecration) | Mana per sec, fresh level 60 | What it gives |
| --- | --- | --- | --- | --- |
| PB1. Raid tank | 8/35/8: v2p0003203-53051321301551-5003 | 562 / 650 | +4.5 | Improved Seals, Unyielding Faith and Reverence. Sacred Duty 2/2. Deflection 5 and Anticipation 5 for the stat targets against a boss (see Crushing blows) |
| PB2. Raid tank, more critical hit | 5/35/11: v2p00032-53051321301551-5105 | 569 / 657 | −4.5 | Conviction 5 and Benediction 1. No Reverence |
| PB3. Dungeon tank | 12/34/5: v2p00032030200002-5323130100155122-5 | About 527 / 666 | +4.5. Consecration lasts about 76 sec (108 sec with pre-raid mana) | Consecrated Ground and Holy Conduit (C8). Guardian's Favor, Fury's Reach and Shoulder the Burden. Anticipation 3, Deflection 5. No One-Handed Weapon Specialization, no Sacred Duty |
| PB4. Raid tank, area threat | 12/34/5: v2p00032030200002-532513010015512-5 | About 527 / 666 | The same as PB3 | As PB3, with Anticipation 5 and Deflection 5 for the stat targets against a boss. No Fury's Reach |

- **Holy Shield needs 31 Protection points.** A tank build with only useful points uses 33–35.
- **Bosses and dungeons.** Only enemies that are 3 or more levels above you can hit with crushing blows. Dungeon enemies are level 62 or lower. Thus, a dungeon tank does not need the full Anticipation. PB3 uses 2 of these points for Fury's Reach. PB3 and PB4 have only these 2 points of difference.
- **PB3 and PB4 values** come from the threat model script (models/threat). The script gives about 5% less threat than this table for PB1 (533 / 639). Thus, the PB3 and PB4 values use the script result relative to PB1. Consecrated Ground adds 10% to all Holy damage on targets in Consecration. The mana values come from Analysis, Mana.
- **Raid tank: PB1 is better.** PB2 gives only +1% threat and loses 9 mana per sec.
- **Area threat and mana together.** With C8, Holy Conduit is in Protection row 2. PB3 and PB4 have Consecrated Ground and Holy Conduit together. They skip One-Handed Weapon Specialization (about −27 threat per sec on one target) and Sacred Duty. Reckoning (C11) has more value against groups: each block, dodge and parry can give a charge.
- **One build can have both.** v2p00032030200002-530503013015512-5 (12/34/5) has Consecrated Ground, Holy Conduit and One-Handed Weapon Specialization, with Anticipation 5 and Deflection 5: about 552 / 692 threat per sec. It skips Shoulder the Burden, Guardian's Favor and Sacred Duty. Thus, the tank choice is threat or utility, not one target or a group.
- **Threat per sec for each point:** Holy Shield 270 (1 point), Redoubt 18, Reckoning 11, Swift Judgement 10 (1 point), One-Handed Weapon Specialization 9, Improved Seals 4, Precision 4, Conviction 4, Iron Creed 2 (and −10% damage taken), Vindication about 1 (and about −1.5% boss melee damage, if no Demoralizing Shout or Roar is on the boss).
- **Divine Strength (removed by C8).** +10% Strength gave a tank about +15 Strength with pre-raid gear: about +30 Attack Power and +1 block value. Thus, all tank builds skipped it. Retribution received about +7 DPS for 5 points.

## 4. Retribution

| Build | Points and code | Raid DPS (with Consecration) | PvP burst (one stun) | What it gives |
| --- | --- | --- | --- | --- |
| RB1. Raid | 10/7/34: v2p000320302-032000000000002-0325531201330321 | About 370 (420) | About 1,830 | Vindication 5 (C8). The best build on one target |
| RB2. Raid with Consecration | 12/7/32: v2p00032030200002-032000000000002-0325531001330321 | 370 (450) | About 1,830 | Consecrated Ground (see W16). Vindication 5 opens row 6. The build of Analysis, Damage |
| RB3. PvP, Hammer of Justice each 45 sec | 0/14/37: v2p-332000010300002-0325531221331321 | About 345 | About 2,240 | Swift Judgement, Repentance, Eye for an Eye and Guardian's Favor. Redoubt 3 opens Protection row 3 |
| RB4. PvP, fear and heals | 7/7/37: v2p000320002-032000000000002-0325531221331321 | 370 | About 1,830 | Unyielding Faith (Holy row 1, C8), Infusion of Light and Repentance |
| RB5. Reckoning (Protection and Retribution) | 0/26/25: v2p-532300210215002-5005031211331 | About 280 | About 3,020 | The build of PvP burst check (see W6) |

- **DPS for each point:** Seal of Command 82 (1 point), Twist of Light 47 (1 point), Sacred Arbiter 9 (1 point), Two-Handed Weapon Specialization 6.6, Vengeance 5.3, Improved Judgement 5.2, Conviction 5.0, Precision 4.9, Improved Seals 4.7, Champion of the Light 4.4, Instrument of Law 1.9, Vindication 1.4 (5 ranks, C8).
- **About 6 points are free.** Each choice gives 1.5% DPS or less: Vindication, Consecrated Ground, Infusion of Light or Pursuit of Justice.
- **The dips into Holy and Protection are strong:** Improved Seals +6%, Precision +4%. The Protection dip also gives Guardian's Favor and Holy Conduit (C8). Thus, rule 1 of Tree balance works for Retribution.
- **C8 and Retribution.** Divine Strength gave about +7 DPS. Vindication 5 gives about +7 DPS with full uptime. RB2 does not change. RB1 had Vindication 3: it loses about 4 DPS (−1%).
- **Holy Power is not good for Retribution.** A 30/0/21 build loses Twist of Light and Vengeance: −23%.

## 5. Builds outside the main tree

| Role | Build | Points and code | Result | Status |
| --- | --- | --- | --- | --- |
| Damage | Shock-Retribution | 21/0/30: v2p50232030201012--032533110133032 | 351 DPS (95% of RB2) for 2 min. Holy Shock replaces Twist of Light. After about 2 min, the mana is too low for Holy Shock: 305 DPS (82%) | Good for short fights and PvP. In PvP, one Holy Shock adds about 560 damage to the burst (about 2,340) |
| Damage | Shockadin | 38/0/13: v2p5023213225131251--03251002 | 311 DPS. The mana is zero after 30–50 sec. 63–70% for 2 min | Not good in raids |
| Tank | Retribution with Righteous Fury and a two-handed weapon | 12/7/32 (RB2) | 75–95% of 569 threat per sec (the dungeon tank of version 1). About 1.65 times the damage taken | Possible in easy dungeons. The healer must do more work |
| Tank | Holy Shock tank | 30/21/0: v2p502320312013125-53201321301 | 60% of 569 threat per sec (74% with Consecration). The mana lasts about 2 min (35 sec with Consecration) | For leveling and solo play |
| PvP | Holy Shock with Iron Creed | 21/30/0: v2p50232030201012-5320132130145 | Righteous Fury stays active in PvP. Iron Creed then gives −10% damage taken. The build also has Templar's Bulwark, Reckoning and Holy Shock | Strong survival. See W17 |
| Tank | Healing tank | 29/22/0: v2p53202132251010002-5320131130110001 | See part 6 | Not good |

- **Holy Shock (rank 4).** 334–362 damage or 307–333 healing, 325 mana, 10 sec cooldown, 42.9% spell damage coefficient. On cooldown, it costs 32.5 mana per sec.
- **Threat for each mana point:** Holy Shield 10.8, Judgement 8.2, Holy Shock 2.9, Consecration 1.2 (one target).
- **Healing Light needs 28 Holy points.** A healer with fewer Holy points loses 23% healing. Thus, no healer build uses a different main tree.
- **Retribution tank.** The values use attacks from the front (14% parry) and dungeon buffs (Blessing of Might only). From behind with raid buffs, the model gives 106%. That value is not correct for a tank.
- **The 52-point gaps.** Holy Shock needs 21 Holy points. Twist of Light and Holy Shield each need 31 points in their tree. Do not move Holy Shock up, or Twist of Light or Holy Shield down, without a new check of these two hybrids.

## 6. Healing threat

A tank can heal itself to get threat.

- **Rules (Classic).** Each point of effective healing gives 0.5 threat. Overhealing gives no threat. The threat is divided between all enemies in the fight.
- **Righteous Fury.** Its Forever text says "Holy attacks". No test on heals exists (see Open questions). The table gives the two cases.
- **Base build.** The table uses the dungeon tank of version 1 (8/33/10: Conviction, Holy Conduit and Benediction, 567 threat per sec). The healing threat does not change with C8.

| Plan, one target | Healing on yourself per sec | Threat per sec (Righteous Fury ×1 / ×1.9 on heals) | Mana per sec | The mana lasts |
| --- | --- | --- | --- | --- |
| Dungeon tank (version 1), no heals | 0 | 567 / 567 | +14 | All the fight |
| Dungeon tank (version 1) and 1 Flash of Light each 10 sec | 42 | 578 / 597 | 0 | All the fight |
| Dungeon tank (version 1) and 1 Holy Light each 10 sec | 183 | 642 / 725 | −52 | 66 sec |
| Healing tank (29/22/0), 1 Holy Light and 1 Flash of Light each 10 sec | 293 | 348 / 480 | −68 | 50 sec |
| Healing tank (29/22/0), 2 Holy Light and 2 Flash of Light each 10 sec | 586 | 477 / 740 | −143 | 24 sec |

- **A healing tank is not a good build.** The mana lasts 24–50 sec. It has no Holy Shield and no Iron Creed.
- **Self-healing is a good tool.** If Righteous Fury multiplies healing threat, one Flash of Light each 10 sec gives +5% threat at no mana cost. One Holy Light each 10 sec gives +28% threat for about 1 min. With Infusion of Light (PB3, PB4), Holy Light has a 1.5 sec cast after Holy Strike.
- **With 4 enemies,** each enemy gets 25% of the healing threat in this table.
- The values include the melee swings that stop during a cast. Healing threat is only possible when you have lost that much health.

## 7. Points that the rows force

The row rules make some builds take talents that do not help their role (filler).

| Build | Filler | Cause |
| --- | --- | --- |
| Holy healer | 2 points (Unyielding Faith or Voice of Truth) | Row 4 needs 15 points in rows 1–3. Row 6 needs 25 points in rows 1–5 |
| Holy PvP with Improved Hammer of Justice | Precision 3 | Row 3 needs 10 points in rows 1–2 |
| Main builds of Protection and Retribution | None | Useful talents fill all rows |

- **Spiritual Focus in row 2 decreases the filler for Holy.** With Spiritual Focus in row 4 (a withdrawn idea), a Holy healer needed 3 points of filler. HB2 was not possible.
- Purifying Power counts as a useful talent here (Cleanse costs 20% less).

## 8. Limits

- The values come from models, not from combat logs.
- The damage-taken values are approximate: one enemy hit of 1,000, 60 block value and the same gear for all tanks. Use them to compare builds, not as exact values.
- The Shockadin model uses a two-handed weapon and Retribution gear. A Shockadin with caster gear is not in the model.
- The mana values include Blessing of Wisdom when the text does not give a different condition.
- Spell miss against level 62 enemies: 6% (assumed).
- Holy Shock range: 20 yards in the client data. One website gives 40 yards.
