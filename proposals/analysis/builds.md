# Builds

**Question.** What are the main builds of each spec and role, with the proposals?

The builds use the proposed trees of calculator version 6 (the live version, with the proposals). All codes open in the calculator with 51 points. A code that starts with "v6p" opens the proposed trees. A code that starts with "b2" opens the live trees. For the best builds and stat weights of each spec, see the builds folder of the repository.

## Short answer

- **Each spec has a clear main build.** Each role also has real choices: saves, mana and PvP control.
- **Holy (HB2)** takes Reverence 50% (C-H1) and Devoted Sacrifice (C-P11) with 12 Protection points. Toughness removal (C-P13) moves Devoted Sacrifice to row 3. Thus, the healer loses no healing talent.
- **Protection (PT1)** puts 34 points in Protection for Shieldsworn and all tank talents. The other 17 points go to Retribution rows 1–2.
- **Retribution (RB1)** needs 31 points for Unsealed Wrath. The other 20 points go to Holy (Improved Seals, Reverence) and Protection (Divine Intellect).
- **PvP.** Two builds take Swift Judgement and Hammer of Justice each 45 sec: the Reckoning bomb (0/25/26) and an Unsealed Wrath build (0/20/31).

## 1. Holy

| Build | Points and code | Healing each sec (raid / one tank, 5 min) | What it gives |
| --- | --- | --- | --- |
| HB1. Raid healer, live talents | 38/5/8: [`v6p50325115202121251-5-0503`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p50325115202121251-5-0503) | 692 / 622 | All healing talents. Divine Intellect 5, Benediction 5, Conviction 3. Improved Seals 5, Holy Conduit 2 and Consecrated Ground 2 fill the rows |
| **HB2. Raid healer, Devoted Sacrifice** | 31/12/8: [`v6p50320115202101251-50122000000000002-0503`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p50320115202101251-50122000000000002-0503) | 728 / 658 | All healing talents, with Reverence 50% (C-H1), Light's Vigil (C-H7) and Oath of Light 30% (C-H8). Devoted Sacrifice 2/2 (C-P11): Lay on Hands drains only 50% of the mana. Guardian's Favor 2/2 (Hand of Protection each 3 min), Sacred Duty 2/2 (Divine Shield −60 sec), Precision 1 |

- **HB2 is the main build with the proposals.** It loses only two damage talents: Improved Seals and Consecrated Ground. Reverence 50% gives +5–6% healing in fights of 5 min, and +5–9% in fights of 10 min.
- **Both builds take Light's Vigil (C-H7).** In the proposed trees, it gives the raid healing: HB1 heals 692 in raids, against 479 with the live talent.
- **Holy needs 31 points for Light's Vigil.** Holy Conduit 2/2 fills the rows. It makes only Consecration, Holy Wrath, Exorcism and Hammer of Wrath cheaper.
- **The 3 Retribution points after Benediction** go to Conviction 3/3: +6% critical chance, thus more Illumination mana.
- **Healing values** use 175% critical heals (Holy Power 5/5, main hypothesis since 3 November). HB2 at 200%: 785 raid and 696 one tank. At 225%: 843 and 733. HB1 at 200%: 748 and 658. At 225%: 804 and 693. The one-tank values use Oath of Light 30% (C-H8). With the live Oath of Light, HB2 gives 602 and HB1 568 on one tank.
- **Hybrid builds with Light's Vigil (C-H7).** A build with 31 Holy points casts Holy Shock on an enemy each 6 sec (live: each 10 sec). The model gives +36 to +48 damage each sec, for about 49 mana each sec (live: 29). Illumination returns no mana on damage. In wowsims, Light's Vigil gives this build +9.3% in a raid (674 → 737 DPS, builds/shockadin.md). Without Vengeance and Unsealed Wrath, it stays below the Shockadin SB1 (23/0/28, 824 DPS) and RB1 (843). The risk is the PvP burst: three or four Holy Shocks in one stun (PvP burst check, part 6, and W30).

## 2. Protection

| Build | Points and code | Threat each sec | Damage taken each sec | TMI | What it gives |
| --- | --- | --- | --- | --- | --- |
| **PT1. Raid tank** | 0/34/17: [`v6p-3530110213501531-54233`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p-3530110213501531-54233) | 1,195 | 295 | 41.1 | Protection: Divine Intellect 3, Redoubt 5, Precision 3, Sacred Duty 1, Templar's Bulwark, Shield Specialization 2, Swift Judgement, Improved Righteous Fury 3, Anticipation 5, Holy Shield, Reckoning 5, Iron Creed 3, Shieldsworn. Retribution: Deflection 5, Benediction 4, Improved Judgement 2, Conviction 3, Sanctified Judgement 3 |
| Live tank, best found (BS2) | 0/35/16 in the live trees: [`b2-05302102313501531-52233000001`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2-05302102313501531-52233000001) | 1,147 | 328 | 49.9 | Sacred Arbiter and Sanctified Judgement 3, no Holy points. See builds/protection.md |
| Live tank (reference) | 12/32/7 in the live trees: [`b2050050002-05302102213301531-502`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2050050002-05302102213301531-502) | 1,133 | 336 | 51.0 | The wowsims default tank build, no proposals. Toughness 2 |

- **Values** come from wowsims with Redoubt (C-P1) and Toughness removal (C-P13). They use master commit 129fcd89e (Holy Shield rank 4, hotfixes of 12 November and push 114027). The runs use the item pool tank set and tank consumables (Analysis, Threat, part 6). The withdrawn Holy Strike Seal trigger (C1) gave PT1 1,012 threat each sec on 1 November (Holy Shield rank 3).
- **Righteous Fury (C25)** multiplies all threat by 1.42. PT1 then has about 1,702 threat each sec, 106% of the Warrior and 75% of the Druid (Analysis, Threat, part 6). The build does not change.
- **Survival set.** The table uses the item pool threat set. With the item pool survival set, PT1 has 1,142 threat each sec, 283 damage taken each sec and a TMI of 36.5. BS2 has 1,095, 316 and 44.6, and the live reference 1,082, 323 and 45.7. The build order does not change (builds/protection.md).
- **Divine Intellect 3 is necessary.** Row 4 needs 15 points in rows 1–3. With Divine Intellect 2, Swift Judgement is not available.
- **Toughness removal (C-P13)** frees 5 points. With the 0/38/13 tank of the Analysis model as the start, they go to Deflection 5 and Divine Intellect 1, and Benediction loses 1 point. Live talents, 1 November: Deflection 4 in place of Toughness 5 gave the same damage taken (340), but a worse TMI (58.1 against 55.9).
- **Devoted Sacrifice (C-P11)** is available to a tank for 2 points in place of Deflection. The sim does not model Lay on Hands.
- **Dungeons.** Dungeon enemies are level 62 or lower and cannot hit with crushing blows. A dungeon tank takes Reach of Law (C-P7) 2/2 for 2 Benediction points, for a 20 yard pull: [`v6p-353011021350153102-52233`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p-353011021350153102-52233) (0/36/15). It can also move Anticipation points to Stoicism or Guardian's Favor.

## 3. Retribution

| Build | Points and code | Raid DPS (with the withdrawn C1) | PvP burst (one stun) | What it gives |
| --- | --- | --- | --- | --- |
| **RB1. Raid** | 14/6/31: [`v6p050250002-501-05233011201301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p050250002-501-05233011201301351) | 843 (883) | — | The wowsims default build. Holy: Divine Strength 5, Reverence 2, Improved Seals 5, Holy Conduit 2. Protection: Divine Intellect 5, Precision 1. Retribution: Unsealed Wrath, Champion of the Light 5, Vengeance 3, Two-Handed Weapon Specialization 3, Sacred Arbiter, Seal of Command, Repentance, Unyielding Faith 1, Pursuit of Justice 2 |
| RB2. PvP, Unsealed Wrath | 0/20/31: [`v6p-50322130101000002-05233001211301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p-50322130101000002-05233001211301351) | 773 (809) | About 2,400 | Swift Judgement and Improved Hammer of Justice 3/3 (Hammer of Justice each 45 sec). Guardian's Favor, Sacred Duty, Devoted Sacrifice. Eye for an Eye 1. No Holy points |
| SB1. Shockadin (Holy Shock) | 23/0/28: [`v6p05025210221021--0523330110130033`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p05025210221021--0523330110130033) | 824 (—) | — | The wowsims Holy Shock build. Holy: Holy Shock, Divine Favor, Improved Seals 5, Consecrated Ground 2. Retribution: Vengeance 3, Champion of the Light 3, Two-Handed Weapon Specialization 3, Sacred Arbiter, Seal of Command. No Unsealed Wrath. See builds/shockadin.md |
| RB3. PvP, Reckoning bomb | 0/25/26: [`v6p-50322130101005002-052330012213013`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p-50322130101005002-052330012213013) | 636 (—) | About 2,070; with 4 stored attacks about 3,630 | Reckoning 5/5, Swift Judgement, Improved Hammer of Justice 3/3, Devoted Sacrifice. Eye for an Eye 2, Repentance, Vengeance 3. No Unsealed Wrath and no Champion of the Light |

- **Raid DPS** comes from wowsims, 3 min, full buffs. The wowsims rotation is made for RB1. Thus, the values of RB2 and RB3 are approximate.
- **The Holy points give RB1 the most.** Improved Seals gives +15% on Seals and Judgements, and Reverence gives mana. Without Holy points (RB2), raid DPS is 8% lower.
- **SB1 uses the [Shockadin set](https://ralgathor.github.io/forever-paladin-feedback/sets/build-shockadin.html)** (the wowsims Holy Shock set with item pool items, spell damage gear) and its rotation. Thus, its DPS against RB1 is approximate. Holy Shock gives SB1 +12%.
- **C1 (withdrawn) gave +5%** in RB1 and RB2. The C1 flag does not run with RB3.
- **The earlier wowsims build** (14/5/32, [`v6p050250002-5-05233301101301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v6p050250002-5-05233301101301351)) gives 832 (871 with C1). Precision 1 in place of Vindication gives RB1 +1.4%.
- **PvP burst** values come from PvP burst check. The kept proposals do not change them.

## 4. Points that the rows force

Some builds must put points into talents with little value, to open a deeper row.

| Build | Filler points | Cause |
| --- | --- | --- |
| Holy healer (HB2) | 2 (Holy Conduit) | Row 6 needs 25 points in rows 1–5. Holy rows 4–5 have only 10 points |
| Raid tank (PT1) | None | Divine Intellect gives mana. Deflection gives parry |
| Retribution raid (RB1) | Unyielding Faith 1, Pursuit of Justice 2 | Unsealed Wrath needs 30 points in rows 1–6. These 3 points give no damage |

## 5. Method and limits

- **Protection, Retribution and Shockadin:** wowsims Forever (master commit 129fcd89e of 12 November, evening, hotfixes of 12 November and push 114027, client 1.60.1.70888). Tank consumables for Protection, 3,000 iterations, 3 min, full buffs, and the Light's Vigil flag CH7 for SB1 (builds/shockadin.md). Gear: the item pool sets, the same item pool as Analysis, Damage and Threat: [Protection Paladin](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-pool-protection-paladin.html) (threat set; [survival set](https://ralgathor.github.io/forever-paladin-feedback/sets/tank-surv-protection-paladin.html)), [Retribution](https://ralgathor.github.io/forever-paladin-feedback/sets/build-retribution.html) (RB1) and [Shockadin](https://ralgathor.github.io/forever-paladin-feedback/sets/build-shockadin.html) (SB1).
- **Holy:** the healing model (`models/beta-30-oct/healing_b2.py`, 715 healing power, 5 min). The live test of Holy Power can change the Holy values (see Open items).
- **PvP:** the PvP burst model (`models/beta-30-oct/pvp_burst_b2.py`), one Hammer of Justice stun.
- wowsims does not model Lay on Hands, Shoulder the Burden (C-P5) or Hand of Sacrifice (C4).
- The values come from sims and models, not from combat logs.
- The earlier builds (calculator version 5, beta of 18 October) are in the history of the repository.
