# Builds

This section gives the main builds for each spec and role on the proposed trees of calculator version 6 (beta of 30 October 2026, with the proposals). All codes open in the calculator with 51 points and no error. A code that starts with "v6p" opens the proposed trees.

## Summary

- Each spec has a clear main build. Each role also has real choices: saves, mana and PvP control.
- **Holy** takes Devoted Sacrifice (C-P11) with 12 Protection points. Toughness removal (C-P13) moves Devoted Sacrifice to row 3. Thus, the healer loses no healing talent.
- **Protection** uses 34 points for Shieldsworn and all tank talents. The tank then has 17 points for Retribution rows 1–2: Deflection, Benediction, Improved Judgement, Conviction and Sanctified Judgement.
- **Retribution** needs 31 points for Unsealed Wrath. The dips into Holy (Divine Strength, Reverence, Improved Seals, Holy Conduit) and Protection (Divine Intellect) are strong.
- **PvP.** The Reckoning bomb (0/25/26) and the Unsealed Wrath build (0/20/31) both take Swift Judgement and Hammer of Justice each 45 sec.
- **Method.** wowsims Forever (branch paladin/hotfix-113554-port, 3,000 iterations, 3 min, full buffs) for Protection and Retribution. The Holy healing model (models/beta-30-oct/healing_b2.py, 715 healing power, 5 min) for Holy. The PvP burst model (models/beta-30-oct/pvp_burst_b2.py) for one Hammer of Justice stun.

## 1. Holy

| Build | Points and code | Healing (raid / one tank, healing each sec) | What it gives |
| --- | --- | --- | --- |
| HB1. Raid healer, beta talents | 38/5/8: v6p50325115202121251-5-0503 | 533 / 633 | The build of the healing model. Divine Intellect 5, Benediction 5, Conviction 3. Improved Seals 5, Holy Conduit 2 and Consecrated Ground 2 fill the rows |
| HB2. Raid healer, Devoted Sacrifice | 31/12/8: v6p50320115202101251-50122000000000002-0503 | 533 / 633 | Devoted Sacrifice 2/2 (C-P11): Lay on Hands drains only 50%. Guardian's Favor 2/2 (Hand of Protection each 3 min), Sacred Duty 2/2 (Divine Shield −60 sec). Precision 1. No Improved Seals and no Consecrated Ground |

- **HB2 is the main build with the proposals.** It gives up only damage talents: Improved Seals and Consecrated Ground. The healing does not change.
- **Holy needs 31 points for Light's Vigil.** Holy Conduit 2/2 fills rows 1–5. Thus, a Holy healer has 2 points of filler (Holy Conduit gives only cheaper Consecration, Holy Wrath, Exorcism and Hammer of Wrath).
- **The 3 Retribution points after Benediction** go to Conviction 3/3: +6% critical chance, also more Illumination mana.
- **Healing values.** The model uses a 225% critical heal (Holy Power 5/5). At 175%, raid healing is 479 and one tank is 568 (see Open items).

## 2. Protection

| Build | Points and code | Threat each sec | Damage taken each sec | TMI | What it gives |
| --- | --- | --- | --- | --- | --- |
| PT1. Raid tank | 0/34/17: v6p-3530110213501531-45233 | 1,010 | 296 | 45.2 | Divine Intellect 3, Redoubt 5, Precision 3, Sacred Duty 1, Templar's Bulwark, Shield Specialization 2, Swift Judgement, Improved Righteous Fury 3, Anticipation 5, Holy Shield, Reckoning 5, Iron Creed 3, Shieldsworn. Deflection 4, Benediction 5, Improved Judgement 2, Conviction 3, Sanctified Judgement 3 |
| Beta tank (reference) | 0/38/13 in the beta trees, with Toughness 5 | 927 | 340 | 55.9 | The tank of Beta test results, no proposals |

- **Values.** wowsims with the proposals Redoubt (C-P1) and Reckoning (C-P12). The beta tank uses the beta talents and no proposal.
- **Row 4 needs 15 points in rows 1–3.** Divine Intellect 3 gives the last point. With Divine Intellect 2, Swift Judgement is not available.
- **Toughness removal (C-P13).** The 5 free points go to Deflection 4 and Divine Intellect 1. With the beta talents, Deflection 4 in place of Toughness 5 gives the same damage taken (340 against 340) and a worse TMI (58.1 against 55.9).
- **Devoted Sacrifice (C-P11)** is available to a tank for 2 points in place of Deflection. The sim does not model Lay on Hands.
- **Dungeons.** Dungeon enemies are level 62 or lower and cannot hit with crushing blows. A dungeon tank can move Anticipation points to Stoicism or Guardian's Favor.

## 3. Retribution

| Build | Points and code | Raid DPS, beta / with Holy Strike Seal trigger (C1) | PvP burst (one stun) | What it gives |
| --- | --- | --- | --- | --- |
| RB1. Raid | 14/5/32: v6p050250002-5-05233301101301351 | 838 / 871 (+3.9%) | — | The wowsims Unsealed Wrath build. Divine Strength 5, Reverence 2, Improved Seals 5, Holy Conduit 2. Divine Intellect 5. Unsealed Wrath, Champion of the Light 5, Vengeance 3, Two-Handed Weapon Specialization 3, Sacred Arbiter, Seal of Command. Pursuit of Justice 1 |
| RB2. PvP, Unsealed Wrath | 0/20/31: v6p-50322130101000002-05233001211301351 | 755 / 787 | About 2,400 (2,510 with C1) | Swift Judgement and Improved Hammer of Justice 3/3 (Hammer of Justice each 45 sec). Guardian's Favor, Sacred Duty, Devoted Sacrifice. Eye for an Eye 1. No Holy points: the mana is empty after about 22 sec in a raid |
| RB3. PvP, Reckoning bomb | 0/25/26: v6p-50322130101005002-052330012213013 | 648 / 677 | About 2,070, with 4 stored attacks about 3,630 (2,180 and 3,740 with C1) | Reckoning 5/5 (critical hit trigger), Swift Judgement, Improved Hammer of Justice 3/3, Devoted Sacrifice. Eye for an Eye 2, Repentance, Vengeance 3. No Unsealed Wrath and no Champion of the Light |

- **Raid DPS** from wowsims, 3 min, full buffs. The wowsims rotation is the rotation of RB1. Thus, the values of RB2 and RB3 are only approximate.
- **The Holy dip is the strongest part of RB1:** Improved Seals +15% on Seals and Judgements, and Reverence for mana. Without Holy points (RB2), raid DPS is 10% lower.
- **Holy Strike Seal trigger (C1)** gives +4% in each build.
- **PvP burst** from Analysis, PvP burst check. The proposals add 3–5%.

## 4. Points that the rows force

| Build | Filler | Cause |
| --- | --- | --- |
| Holy healer (HB2) | Holy Conduit 2 | Row 6 needs 25 points in rows 1–5. Without Improved Seals and Consecrated Ground, only 23 of these points help a healer |
| Raid tank (PT1) | None | Divine Intellect gives mana. Deflection gives parry |
| Retribution raid (RB1) | Pursuit of Justice 1 | The last of the 51 points has no damage value |

## 5. Limits

- The values come from wowsims and models, not from combat logs.
- wowsims does not model Lay on Hands, Shoulder the Burden (C-P5) or Hand of Sacrifice (C4).
- The Holy model uses 225% critical heals. The beta test of Holy Power can change the Holy values (see Open items).
- The earlier builds (calculator version 5, beta of 18 October) are in the history of the repository.
