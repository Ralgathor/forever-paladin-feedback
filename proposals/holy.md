# Holy

Most saved Holy builds stop at about 20 points. These proposals make the deep Holy talents better for healers. They also give Retribution and Protection a reason to put a few points in Holy.

## Holy layout

| Row (points necessary) | Talents | Points in the row |
| --- | --- | --- |
| 1 (0) | Improved Seals (M-H1), Unyielding Faith (M-H2), Divine Intellect | 10 |
| 2 (5) | Infusion of Light (C-H3), Reverence (C-H1), Spiritual Focus | 7 |
| 3 (10) | Voice of Truth, Purifying Power, Lingering Light (C-H2) | 5 |
| 4 (15) | Illumination, Divine Favor | 6 |
| 5 (20) | Divine Precision, Holy Shock, Holy Power (M-H3) | 9 |
| 6 (25) | Consecrated Ground (M-H4), Healing Light (C-H4) | 5 |
| 7 (30) | Light's Vigil | 1 |

- Holy has 43 points (beta: 46).
- You can use each talent when its row opens.
- Illumination still requires Reverence (straight arrow in column 2).
- Toughness and Divine Strength removal (C-P3) deletes Divine Strength. Unyielding Faith (M-H2) goes to row 1.
- A Holy healer needs no filler. Rows 1–3 hold 16 healer points (row 4 needs 15). Rows 1–5 hold 28 (row 6 needs 25). See Analysis, Tree balance.

## C-H1. Reverence: 10/20/30% → 17/33/50%, row 3 → row 2

- **Proposed text.** "Allows 17/33/50% of your Mana regeneration to continue while casting."
- **Model.** Meditation (Priest), Reflection (Druid) and Mindfulness (Shaman) give 50% with 3 ranks.
- **Illumination is not sufficient.** Other healers have a mana return in addition to their 50% (Litany of Light, Water Shield, Mana Tide Totem). Forever also decreased Illumination to 50% of the base cost.
- **Row 2.** Holy has its mana talent early, while it levels.
- **If it is too strong:** use 13/27/40%.

## C-H2. Lingering Light (new talent): row 3, column 4, 2 ranks

- **Proposed text.** "Your non-periodic critical heals cause the target to be healed for an additional 10/20% of the amount healed over 6 sec. Refreshing this effect carries over any remaining healing."
- **Identity.** It is the only Holy heal over time. It is not the same as Divine Aegis (Priest), because Divine Aegis is a shield.
- **Text model.** "Non-periodic critical heals" comes from Divine Aegis and Inspiration (Priest). "Refreshing this effect carries over any remaining healing" comes from Blessed Recovery (Priest). Blessed Recovery already works this way in Forever.
- **Why critical heals.** Healing Light already gives a bonus to each heal. The Holy tree has many critical hit talents (Illumination, Divine Favor, Holy Power). This talent gives them more value.
- **Value.** At 22% critical heal chance: 22% × 1.5 (critical heal) × 20% = about +6.6% of a normal heal. Critical ticks add about 11% to this: about +7.3%. Some of it is overhealing on targets with full health.
- **Why row 3.** Holy row 3 had only 3 points, the smallest row 3 of all classes. With Lingering Light, it has 5. A Holy healer then needs no filler for row 4. Retribution and Protection can take it with 10 Holy points. They have few critical heals, thus its value for them is small (see W12 for PvP).
- **Why 10/20%.** Healing Light (C-H4) gives the main healing bonus. Lingering Light gives a smaller bonus, and only on critical heals. At 20%, it gives about 3.6% for each point, as Spiritual Healing (Priest) does. After overhealing, it adds about 5% healing in raids and on one tank, in all fight lengths (see Analysis, Healing, part 6). At 30%, it adds about 8%, and the Paladin is first on one tank by 4–12%, not 1–9%.

**How the heal over time works.** It works as Ignite and Blessed Recovery do in Forever, not as Deep Wounds.

|  | Ignite (Mage) | Deep Wounds (Warrior) | Lingering Light |
| --- | --- | --- | --- |
| Amount | 8–40% of the critical hit damage | 20–60% of average weapon damage, the same for each critical hit | 10/20% of the critical heal |
| Duration | 4 sec, one tick each 2 sec | 12 sec | 6 sec, one tick each 2 sec |
| New critical hit while active | The old damage stays and the new damage is added | Only the duration starts again | The old healing stays. The new healing is added. The total spreads over a new 6 sec |
| Number | One for each Mage on each target | One for each target | One for each Paladin on each target |

- **Amount.** It uses the full critical heal, with the overhealing.
- **No double bonus.** Healing bonuses apply one time, to the critical heal. They do not apply again to the heal over time. Each tick can be a critical heal, as other heals over time in Forever. A critical tick does not start Lingering Light again. Only a direct critical heal starts it again.
- **Use.** Many critical heals on the tank make a large heal over time. Divine Favor on Holy Light gives one large heal over time when you want it. Holy Shock critical heals (+15% from Holy Power) give many small amounts.

## C-H3. Infusion of Light: no critical hit necessary, Holy Strike added, row 4 → row 2

- **Proposed text.** "Your Holy Shock and Flash of Light spells and your Holy Strike hits reduce the cast time of your next Holy Light cast within 15 sec by 0.5/1 sec."
- **Change.** A critical hit is not necessary now. Holy Strike is a new trigger. A miss, dodge or parry does not trigger it. The values and the duration are the same as in the beta.
- **Problem.** No talent decreases the cast time of Holy Light. Divine Fury (Priest), Naturalist (Druid) and Improved Healing Wave (Shaman) give −0.5 sec to the big heal of their class. Thus, healing power gives the smallest increase in healing per second to the Paladin. In the beta, Infusion of Light works only after a critical hit. Thus, it is not reliable.
- **Use (Holy).** Cast Flash of Light, then Holy Light, and do this again. At rank 2, Holy Light then has a 1.5 sec cast. With 900 healing power and 19% critical heals, this gives 1,405 healing per sec and 5.83 healing per mana. Holy Light alone gives 1,288 and 5.40. With Blessing of Light removal (C3: no Blessing of Light, Healing Light 30%), the mix gives 1,386 and 5.75.
- **Long fights.** The best cast plan also uses the least mana. Flash of Light is the most efficient heal, and it makes Holy Light faster.
- **Use (Retribution and Protection).** These specs have only two heals. Flash of Light is too small in PvP. After each Holy Strike, the next Holy Light has a 1.5 sec cast. This is a fast emergency heal one time each 10 sec.
- **Limits.** Holy Strike has a 10 sec cooldown. Holy Light costs 660 mana. Players can still interrupt the cast. Mortal Strike decreases the heal by 50% (see Analysis, Healing, part 7).
- **Row 2.** Retribution and Protection keep a healing reason to put points in Holy: faster heals, not larger heals.
- **Risk.** A 7-point Holy dip gives a 1.5 sec Holy Light after each Holy Strike in PvP. This is on the watch list (W12).

## C-H4. Healing Light: row 2 → row 6, 10/20/30%

- **Proposed text.** "Increases the amount healed by your Holy Light, Flash of Light, and Holy Shock spells by 10/20/30%."
- **Change.** 3 ranks: 10/20/30% (beta: 4/8/12%). The maximum increases from 12% to 30%, because Blessing of Light removal (C3) removes the spell. The 18% difference replaces the Blessing of Light bonus (see C3).
- **Why row 6.** The healing bonus is now at 25 points, as Spiritual Healing (Priest) and Purification (Shaman) are.
- **Deep Holy** keeps Healing Light, Holy Power and Light's Vigil. Thus, a deep Holy build stays clearly better for healing. Lingering Light is in row 3 (C-H2), but its value comes from critical heals.
- **Cost.** A Holy Paladin who levels has the full bonus at level 37, not at level 17. Blessing of Light rank 1 came at level 40.

## M-H1. Improved Seals: row 2 → row 1

- **Text.** "Increases the damage done by your Seals and Judgements by 5/10/15%." 3 ranks, the same as the beta.
- **Change.** Only the row changes. Row 1 has Divine Intellect 5, Improved Seals 3 and Unyielding Faith 2 (M-H2).
- **Dip.** With Improved Seals 3 and Unyielding Faith 2, Retribution and Protection open Holy row 2. They receive +15% Seal and Judgement damage and −30% Fear and Disorient duration. Retribution then takes Infusion of Light (7 points).

## M-H2. Unyielding Faith: row 2 → row 1

- **Text.** "Reduces the duration of Fear and Disorient effects on you by 15/30%." 2 ranks, the same as the beta.
- **Position.** Row 1, column 2. It fills the 2 points that Divine Strength leaves (C-P3).
- **Why.** With Improved Seals 3 (M-H1), it opens Holy row 2 for Retribution and Protection. Iron Will (Warrior) is also in row 1.

## M-H3. Holy Power: row 6 → row 5

- **Text.** "Increases the critical strike chance of your Holy Shock and Holy Strike spells by 3/6/9/12/15%, and all other spells by 1/2/3/4/5%." 5 ranks, the same as the beta.
- **Position.** Row 5, column 3.
- **Why.** In row 6, a Holy healer needed 2 points of filler: rows 1–5 held only 23 healer points. With Holy Power in row 5, they hold 28. Holy healing is then complete at 32 points.
- **Retribution and Protection cannot take it.** Twist of Light and Holy Shield need 31 points. Holy Power needs 25 Holy points. 25/0/26 with Holy Power loses Twist of Light and Champion of the Light: −19% (see Builds, part 4).

## M-H4. Consecrated Ground: row 5 → row 6

- **Text.** "Gives your Holy spells 5/10% increased damage against the first 4 enemies that enter your Consecration." 2 ranks, the same as the beta.
- **Position.** Row 6, column 1. Healing Light stays in column 3. The Light's Vigil arrow uses column 2.
- **Why.** Row 5 has Holy Power now (M-H3). Consecrated Ground moves one row lower. Thus, row 5 has 9 points and row 6 has 5.
- **Who takes it.** Only deep Holy builds with Holy Shock (Shockadin, 38/0/13).
