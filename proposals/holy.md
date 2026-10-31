# Holy

The beta of 30 October 2026 changes most of the Holy tree. Oath of Light, Boundless Light and the new Holy Power make the Paladin the best healer on one tank. In raids, the Paladin is still the weakest healer, and mana is the limit (see Beta test results). These proposals now aim at raid healing and mana.

## Holy layout

| Row (points necessary) | Talents | Points in the row |
| --- | --- | --- |
| 1 (0) | Spiritual Focus, Divine Strength | 10 |
| 2 (5) | Healing Light, Reverence (C-H1), Improved Seals, Purifying Power | 12 |
| 3 (10) | Divine Favor, Illumination, Holy Conduit, Lingering Light (C-H2) | 10 |
| 4 (15) | Divine Precision, Infusion of Light (C-H3), Oath of Light | 5 |
| 5 (20) | Consecrated Ground, Holy Shock, Boundless Light | 5 |
| 6 (25) | Holy Power | 5 |
| 7 (30) | Light's Vigil | 1 |

- Holy has 48 points (beta: 46).
- All talents keep their beta places. Lingering Light (C-H2) uses the free place in row 3, column 4.
- Healing Light and Oath of Light keep their beta values. The proposal for Healing Light 10/20/30% (C-H4) is withdrawn (see Withdrawn ideas).

## C-H1. Reverence: 15/30% → 25/50%

- **Proposed text.** "Allows 25/50% of your Mana regeneration to continue while casting."
- **Beta.** 2 ranks, 15/30%, in row 2. The beta of 30 October moved Reverence to row 2, as this proposal asked. Thus, only the values change now.
- **Model.** Meditation (Priest), Reflection (Druid) and Mindfulness (Shaman) give 50%.
- **Why.** In raids, the Paladin is still 18–26% below the Druid. The best cast plan is almost only Flash of Light, because mana is the limit (see Beta test results).
- **Illumination is not sufficient.** Other healers have a mana return in addition to their 50% (Litany of Light, Water Shield, Mana Tide Totem). Forever also decreased Illumination to 50% of the base cost.
- **If it is too strong:** use 20/40%.

## C-H2. Lingering Light (new talent): row 3, column 4, 2 ranks

- **Proposed text.** "Your non-periodic critical heals cause the target to be healed for an additional 10/20% of the amount healed over 6 sec. Refreshing this effect carries over any remaining healing."
- **Identity.** It is the only Holy heal over time. It is not the same as Divine Aegis (Priest), because Divine Aegis is a shield.
- **Text model.** "Non-periodic critical heals" comes from Divine Aegis and Inspiration (Priest). "Refreshing this effect carries over any remaining healing" comes from Blessed Recovery (Priest). Blessed Recovery already works this way in Forever.
- **Why critical heals.** The Holy tree has many critical heal talents: Illumination, Divine Favor, Boundless Light and Holy Power. This talent gives them more value.
- **Values to model again.** In the beta of 30 October, Holy Power makes each critical heal larger. Thus, Lingering Light also gives more. The values of Analysis, Healing use the beta of 18 October.
- **Position.** Row 3, column 4, a free place. Retribution and Protection can take it with 10 Holy points. They have few critical heals. Thus, its value for them is small (see W12 for PvP).

**How the heal over time works.** It works as Ignite and Blessed Recovery do in Forever, not as Deep Wounds.

|  | Ignite (Mage) | Deep Wounds (Warrior) | Lingering Light |
| --- | --- | --- | --- |
| Amount | 8–40% of the critical hit damage | 20–60% of average weapon damage, the same for each critical hit | 10/20% of the critical heal |
| Duration | 4 sec, one tick each 2 sec | 12 sec | 6 sec, one tick each 2 sec |
| New critical hit while active | The old damage stays and the new damage is added | Only the duration starts again | The old healing stays. The new healing is added. The total spreads over a new 6 sec |
| Number | One for each Mage on each target | One for each target | One for each Paladin on each target |

- **Amount.** It uses the full critical heal, with the overhealing.
- **No double bonus.** Healing bonuses apply one time, to the critical heal. They do not apply again to the heal over time. Each tick can be a critical heal, as other heals over time in Forever. A critical tick does not start Lingering Light again. Only a direct critical heal starts it again.

## C-H3. Infusion of Light: no critical hit necessary, Holy Strike added

- **Proposed text.** "Your Holy Shock and Flash of Light spells and your Holy Strike hits reduce the cast time of your next Holy Light cast within 15 sec by 0.5/1 sec."
- **Change.** A critical hit is not necessary now. Holy Strike is a new trigger. A miss, dodge or parry does not trigger it. The values, the duration and the place (row 4, column 2) are the same as in the beta.
- **Problem.** No talent decreases the cast time of Holy Light in all cases. Divine Fury (Priest), Naturalist (Druid) and Improved Healing Wave (Shaman) give −0.5 sec to the large heal of their class. In the beta, Infusion of Light works only after a critical hit. Thus, it is not reliable.
- **Use (Holy).** Cast Flash of Light, then Holy Light, and do this again. At rank 2, Holy Light then has a 1.5 sec cast.
- **Use (Retribution and Protection).** These specs have only two heals. After each Holy Strike, the next Holy Light has a 1.5 sec cast. This is a fast emergency heal.
- **Limits.** Holy Light costs 660 mana. Players can still interrupt the cast. Mortal Strike decreases the heal by 50% (see Analysis, Healing, part 7).
- **Risk.** The talent now needs 15 Holy points (the earlier proposal moved it to row 2). A Protection tank with Shieldsworn has a Holy Strike each 6 sec. See W12.
