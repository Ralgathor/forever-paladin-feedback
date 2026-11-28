# Holy

The live version changes most of the Holy tree. Oath of Light, Boundless Light and the new Holy Power give the Paladin its single-target healing. The design goal of Holy is the best healer on one tank. At a 175% critical heal, the Druid has this place (W14). In raids, the Paladin stays below the other healers (see Beta test results). Holy is not a raid healer first, but the live Light's Vigil does not work as a group heal. Three Holy proposals stay: Reverence 25/50% (C-H1), a new Light's Vigil (C-H7) and Oath of Light 30% (C-H8). The spell changes (C2, C4, C5) also apply to Holy.

- More mana in long fights: Reverence keeps 50% of the mana regeneration during casts, as the healer talents of the other classes (Reverence, C-H1).
- A capstone that Holy uses: Light's Vigil becomes a buff on Holy Shock. Each 6 sec, one Holy Shock also heals the party of the target (Light's Vigil, C-H7).
- The best healer on one tank: Oath of Light gives 30% more healing on its target, in place of flat values (Oath of Light, C-H8).

## Holy layout

| Row (points necessary) | Talents | Points in the row |
| --- | --- | --- |
| 1 (0) | Spiritual Focus, Divine Strength | 10 |
| 2 (5) | Healing Light, Reverence (C-H1), Improved Seals, Purifying Power | 12 |
| 3 (10) | Divine Favor, Illumination, Holy Conduit | 8 |
| 4 (15) | Divine Precision, Infusion of Light, Oath of Light (C-H8) | 5 |
| 5 (20) | Consecrated Ground, Holy Shock, Boundless Light | 5 |
| 6 (25) | Holy Power | 5 |
| 7 (30) | Light's Vigil (C-H7) | 1 |

- Holy has 46 points, as in the live trees.
- All other talents keep their places and values of the live trees.

## C-H1. Reverence: 25/50% (live: 15/30%)

- **Live text.** "Allows 15/30% of your Mana regeneration to continue while casting." 2 ranks, row 2.
- **Proposed text.** "Allows 25/50% of your Mana regeneration to continue while casting."
- **Problem.** The Paladin has the least mana of the healers. Meditation (Priest), Reflection (Druid) and Mindfulness (Shaman) keep 50%. Reverence keeps 30%.
- **Model.** Meditation, Reflection and Mindfulness: 50% at the last rank.
- **Why this talent.** Holy Power already increases the critical heals, and its real size needs a live test. Reverence has no link to critical heals. It helps most in long fights, and it changes a live talent with no new talent.

**Healing model, against the Druid, 715 healing power, 3 / 5 / 10 min**

| Critical heal | One tank, live | One tank, Reverence 50% | Raid, live | Raid, Reverence 50% |
| --- | --- | --- | --- | --- |
| **175% (main hypothesis)** | **−12% / −10% / −16%** | **−7% / −5% / −8%** | **−43% / −40% / −42%** | **−39% / −35% / −36%** |
| 200% | −7% / −5% / −12% | −2% / +1% / −3% | −40% / −36% / −39% | −36% / −32% / −33% |
| 225% | −2% / −0% / −7% | +3% / +6% / +2% | −36% / −33% / −35% | −32% / −28% / −29% |

The Druid values use the development notes of 2 November 2026 (Bloom, Genesis 10%, no Gift of the Earthmother). All healers use the Forever Spirit regeneration (review of 24 November 2026). See Analysis, Healing.

- **HB2 heals 6–10% more than HB1.** The gain increases with the fight length: +6.5% / +7.6% / +9.9% in raids.
- **At 175% (main hypothesis),** the Druid stays first on one tank, but the gap decreases by 5–8 points. The Druid is then the best healer on one target. This is not the design goal of Holy (W14). Oath of Light (C-H8) gives the first place to the Paladin.
- **At 225%,** Reverence gives the Paladin the first place on one tank in all fight lengths. At 900 healing power, it is +4% / +8% / +4%. The lead stays far below the 20% limit (W14).
- **Raids.** About +4 to +6 points: the Paladin stays 35–39% below the Druid. Light's Vigil (C-H7) gives the raid healing.
- **Only one Holy healing talent.** Before the notes of 2 November 2026, a second healing talent gave a tank lead past the 20% limit. Now it gives 9–14% (see Analysis, Healing, part 7). Reverence 50% is a proposal again since 2 November 2026.

## Effect on Retribution

- **Retribution builds take Reverence 2/2.** RB1 has 7 Holy points in rows 1–2. With 50%, RB1 receives 10.3 mana each sec from Reverence (live: 6.2).
- **The mana lasts 1.6–2.2 min longer** with Blessing of Wisdom. At fresh level 60, plan 1 + 3 lasts 5 min 20 sec (live: 3 min 43 sec).
- **Damage in fights of 5 min (model, Blessing of Wisdom).** Fresh level 60 +2.8%, pre-raid +3.0%, Molten Core +2.1%. Blackwing Lair +0.8%, Naxxramas 0%. Fights of 3 min do not change.
- **wowsims, RB1, item pool set:** no buffs at fresh level 60, +5.3% in 3 min (323 → 340) and +4.8% in 5 min (316 → 331). Full raid buffs: 0% (939 in 2 min, 946 in 5 min). These values use commit dc09e002f0 with the item pool set and the enchants of 28 November. On commit ad6b13af8 with the set of 18 November, it gave +3.9% in 3 min and +4.8% in 5 min. With the preset enchants, it gave +4.0% in 3 min and +4.9% in 5 min. On commit 6084403a9 with the set of 15 November, it gave −0.1% in 3 min and −0.8% in 5 min. On commit 8c7b5a5f5, it gave −0.5% in 3 min and −1.0% in 5 min. With all three judgements ranged, it gave −0.2% in 3 min and −0.8% in 5 min.

  On commit 129fcd89e, it gave +0.1% in 3 min and −0.6% in 5 min. With the set of 12 November (commit 52471a100), it gave +1.0% in 3 min and −0.3% in 5 min. With the set of 11 November, it gave −0.9% in 3 min and −1.6% in 5 min. With the set of 4 November, the gain was +0.4% in 3 min. With the wowsims default set, the gain was +4.2% in 3 min and +5.3% in 5 min.
- **This is accepted.** The gain is only at fresh level 60 without buffs, and it decreases with gear. In a raid, it is 0%. Sacred Arbiter +10% stays the balance lever (W15).

## C-H7. Light's Vigil: a buff on Holy Shock (live: a cast on an ally)

- **Live text.** "Applies Light's Vigil to a friendly target for 30 sec. The caster's next Holy Shock on the target incurs no cooldown and heals the target and their party for 326 to 344. Only one Vigil per Paladin may be active in each party." Rank 1: 730 mana, 40 yd range, 1.5 sec cast, 6 sec cooldown. Rank 3 (level 60): 704 to 744 for each party member, 14.3% of healing power, 1,340 mana.
- **Proposed text.** "Your Holy Shock, Judgement and Holy Strike grant Light's Vigil for 30 sec, stacking up to 3 times. May only occur once every 6 sec. Casting Holy Shock consumes one stack, causing that Holy Shock to incur no cooldown and, when cast on an ally, to heal each member of the target's party for 60% of the amount healed."
- **Problem.** Rank 3 costs 1,340 mana, 89% of the base mana. It needs two casts (3 sec) for one party heal. It heals 4.7 for each mana point (Flash of Light: 6.2). In the model, the Paladin casts it only in fights of 3 min. In raids, the Paladin is 40–43% below the Druid and 18–19% below the Shaman.
- **Model.** Riptide (Shaman capstone) adds a bonus to Chain Heal. Prayer of Mending (Priest capstone) is an efficient group heal with a cooldown. Light's Vigil (C-H7) adds a party heal to Holy Shock, with a cooldown of 6 sec.
- **Why this design.** One spell (Holy Shock) does the work. The talent keeps the name, the 30 sec, the 6 sec and the "next Holy Shock triggers no cooldown" rule of the live talent. Each stack is one Holy Shock with no cooldown. No spell uses more than one stack, thus the stacks are not a resource for a finisher. The party heal is a % of the Holy Shock heal, thus it increases with the rank, the level, healing power and critical heals. The text uses the pattern of Unsealed Wrath (Retribution capstone): first the spells that give a stack and the stack limit, then the spell that consumes a stack and its effect.

**How it works**

- Start a fight with Holy Shock, Judgement or Holy Strike. You then have one stack of Light's Vigil.
- Each 6 sec, Holy Shock, Judgement or Holy Strike gives one more stack, up to 3. Each new stack sets the duration to 30 sec again.
- A Holy Shock with Light's Vigil uses one stack. It also gives a stack when the 6 sec cooldown is over. Thus each 6 sec, one Holy Shock heals the party. Holy Shock is enough: ranged and melee Paladins receive the same value.
- Planned burst: keep 3 stacks before a raid damage phase. Then four Holy Shocks one after the other heal the party in 4.5 sec. The first one gives the fourth stack.
- Light's Vigil does not end an active Holy Shock cooldown. After a plain Holy Shock, the next Holy Shock waits for its cooldown. Judgement has no global cooldown, thus it can give a stack at once.

**Healing model, 715 healing power, 3 / 5 / 10 min**

| Critical heal | Case | Live | Light's Vigil (C-H7) | C-H7 and Reverence 50% (C-H1) |
| --- | --- | --- | --- | --- |
| **175% (main hypothesis)** | **Raid, against the Druid** | **−43% / −40% / −42%** | **−21% / −13% / −12%** | **−18% / −8% / −7%** |
| 175% | Raid, against the Shaman | −19% / −18% / −19% | +13% / +19% / +23% | +18% / +26% / +30% |
| 175% | One tank, against the Druid | −12% / −10% / −16% | −12% / −10% / −16% | −7% / −5% / −8% |
| 200% | Raid, against the Druid | −40% / −36% / −39% | −15% / −6% / −5% | −11% / −1% / +1% |
| 225% | Raid, against the Druid | −36% / −33% / −35% | −9% / +1% / +2% | −5% / +7% / +8% |
| 225% | Raid, against the Shaman | −9% / −8% / −10% | +31% / +38% / +43% | +36% / +45% / +51% |

- **Raids.** With both Holy proposals (175%), the Paladin is 7–8% below the Druid in fights of 5 and 10 min. In fights of 3 min, it is 18% below. It stays 11–12% below the Priest. In sets from the level 60 item pool, the Druid has much more Spirit. The Paladin is then 36–42% below the Druid (Analysis, Healing, part 10).
- **Party heal 60%.** The value comes from the 175% hypothesis (decision of 3 November). At 35%, the Paladin is 21–28% below the Druid. At 70%, it is equal to the Druid in fights of 5 and 10 min (−3% / −1%). If the Holy Power test gives 225%, decrease the party heal to 35%: the Paladin is then 9% below the Druid in fights of 5 and 10 min.
- **One tank.** No change. The party heal goes to 5 players, thus the tank receives only a small part. The one-tank values come from Reverence 50% (C-H1) only. At 175%, the Druid stays first on one tank (W14). Oath of Light (C-H8) gives the first place to the Paladin.
- **Cast plan.** About 51 Holy Shocks with Light's Vigil in 5 min (one each 6 sec). Flash of Light stays the main heal.
- **Healing for each mana point.** A Holy Shock with Light's Vigil heals about 3,940 (raid, before overhealing): 985 on the target and 5 × 590 on the party. This is 11.3 healing for each mana point after overhealing. The party heal has 50% overhealing, as Wild Growth: it heals all 5 players, also the players at full health. Prayer of Mending gives 15.7.
- **Group burst.** With 3 stacks, four Holy Shocks with Light's Vigil heal about 15,800 in 6 sec, for about 820 mana. In 10 sec, with Flash of Light or a plain Holy Shock after them, they heal about 20,700 at all ranges. With 1 stack, about 9,700 in 6 sec. Priest: about 15,000 in 10 sec (Prayer of Mending and two Prayer of Healing). Druid: about 11,100 (two Wild Growth). Shaman: about 10,000 (four Chain Heal). The live talent with a Vigil on 4 parties: about 22,900 in 6 sec, for 4,190 mana.
- **Divine Favor.** With Divine Favor, the first Holy Shock is a sure critical heal, and its party heal also. The burst in 6 sec is then about 16,700 (+6%). In a fight, Divine Favor on Holy Light gives more healing: about 1,070 after overhealing, against 570 on a Holy Shock with Light's Vigil. Thus the model keeps Divine Favor on Holy Light.
- **Stacks before a fight.** Holy Shock out of combat gives stacks. A stack lasts 30 sec, thus the Paladin can start a fight with at most 3 stacks.
- **Damage.** The talent has no enemy effect of its own. On an enemy, Light's Vigil only removes the Holy Shock cooldown. In a 6 sec window, three or four Holy Shocks do 1,640 to 2,880 damage (400 to 715 spell damage). Without the talent, one Holy Shock does 550 to 720. Holy Power does not change damage. See Analysis, PvP burst check, part 6, and W30.
- **Hybrid builds.** With 31 Holy points, Holy Shock on an enemy each 6 sec gives +36 to +48 damage each sec (live: each 10 sec). In wowsims, this is +9.4% for the build in a raid (731 DPS). The build has no Unsealed Wrath and no Champion of the Light. Thus it stays below the Shockadin build with 23 Holy points (816) and Retribution (RB1: 830) in raids. See Analysis, Builds.
- **Other talents.** Spiritual Focus and Illumination name Light's Vigil. With C-H7, Light's Vigil has no cast and no heal of its own, thus the two texts no longer name it. This is not a change to the two talents. Illumination applies to the Holy Shock heal, not to the party heal.
- **The value depends on the critical heal size.** The Holy Power test (Open items) gives the real value. With both proposals, the raid values at 225% are 13–15 points higher than at 175%.

Model: `models/beta-30-oct/light_vigil_ch7.py`.

## C-H8. Oath of Light: 30% (live: +400 / +115 / +229)

- **Live text.** "Swear an Oath to protect target ally for 5 min, increasing the healing of your Holy Light on them by up to 400, your Flash of Light by up to 115, and your Holy Shock by up to 229. Only one Oath of Light may be sworn by the Paladin at any one time." 1 point, row 4.
- **Proposed text.** "Swear an Oath to protect target ally for 5 min, increasing the healing of your Holy Light, Flash of Light and Holy Shock on them by 30%. Only one Oath of Light may be sworn by the Paladin at any one time."
- **Problem.** At a 175% critical heal, the Druid is the best healer on one tank. With Reverence 50% (C-H1), the Paladin is 5–8% below the Druid (W14). Also, the flat values give a smaller % with better gear. At 715 healing power, they give Holy Light +19%, Flash of Light +19% and Holy Shock +37%. At 900, they give +18%, +17% and +32%. Forever talents give a % (W27).
- **Model.** Spiritual Healing (Priest) and Purification (Shaman) increase the heals by a %. Oath of Light gives a larger %, on one ally only.
- **Why this talent.** Oath of Light is the single-target talent of Holy. It helps only one ally, thus the raid healing does not change. Light's Vigil (C-H7) stays the raid talent, and Oath of Light becomes the tank talent. A % also gives the same bonus to all ranks of Holy Light (the live text says "up to 400").

**Healing model, one tank, 715 healing power, with Reverence 50% (C-H1) and Light's Vigil (C-H7), 3 / 5 / 10 min**

| Critical heal | Oath of Light | Against the Druid | Against the Shaman | Against the Priest |
| --- | --- | --- | --- | --- |
| 175% (main hypothesis) | Live | −7% / −5% / −8% | +16% / +21% / +24% | +16% / +21% / +23% |
| **175% (main hypothesis)** | **30% (C-H8)** | **+2% / +4% / +0%** | **+27% / +33% / +36%** | **+27% / +32% / +35%** |
| 225% | Live | +3% / +6% / +2% | +30% / +35% / +38% | +29% / +34% / +37% |
| 225% | 30% | +13% / +16% / +12% | +42% / +48% / +51% | +42% / +47% / +50% |
| 225% | 20% (the 225% value) | +4% / +7% / +3% | +31% / +36% / +40% | +31% / +36% / +38% |

- **At 175% (main hypothesis),** the Paladin is first or equal on one tank in all fight lengths: 0–4% above the Druid. At 900 healing power, it is +4% / +8% / +5%. This is the design goal of Holy, below the 20% limit (W14).
- **Why 30%.** It is the smallest value of the model that puts the Paladin at or above the Druid in all fight lengths at 175%. 25% gives the Druid level (−2% / +0% / −3%). 35% gives +4% to +8%, and +12% at 900 healing power.
- **The value for 225%.** At 225%, 30% gives 12–16% above the Druid at 715 healing power, and 16–20% at 900. This is at the 20% limit. If the Holy Power test gives 225%, decrease the value to 20%. The tank healing is then near the live value: 3–7% above the Druid (900: 7–11%).
- **Without Reverence 50% (C-H1),** the Paladin is 2–9% below the Druid at 175%.
- **Raids.** No change. The model gives no raid heal to the Oath target.
- **Recovery after a large hit (175%).** With all cooldowns, the Druid is 1–2% above the Paladin (live: 8%). With short cooldowns only, the Paladin is 18% above the Druid after 3 sec (live: 11%). At 225%, 30% gives 18–24% above the Druid with all cooldowns, and 20% gives 9–14%.
- **Maximum.** The raw healing each sec for 30 sec on one tank is 1,493 (live: 1,368, Druid: 1,312).
- **Shaman and Priest.** On one tank, the Paladin is 27–36% above them (live: 16–24%). The Druid is the healer to compare, because it is the best single-target healer of the other classes.
- **PvP.** The Paladin can put the Oath on itself. At 300 to 900 healing power, Holy Shock receives +151 to +237 (live: +256). Thus the instant self-heal decreases. Holy Light receives +603 to +747 (live: +448), and Flash of Light +147 to +233 (live: +129). An enemy can interrupt the 2.5 sec cast of Holy Light.
- **Gear.** The bonus increases with healing power, as the healing talents of the other classes.
- **Healing Light and Oath of Light.** The model multiplies the two % (×1.12 × 1.30). If the game adds them (+42%), the Paladin is −1% / +2% / −2% against the Druid at 175%, and +9% to +13% at 225%. A live test gives the rule (Open items).
- **Builds.** On one tank, HB2 heals 771 / 674 / 594 (live Oath of Light: 704 / 616 / 542). Oath of Light gives 23% of the HB2 healing on one tank (live: 16% of HB1).

Model: `models/beta-30-oct/oath_light_ch8.py`.
