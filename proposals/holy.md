# Holy

The live version changes most of the Holy tree. Oath of Light, Boundless Light and the new Holy Power make the Paladin the best healer on one tank. This is the design goal of Holy. In raids, the Paladin stays below the other healers (see Beta test results). Holy is not a raid healer first, but the live Light's Vigil does not work as a group heal. Two Holy proposals stay: Reverence 25/50% (C-H1) and a new Light's Vigil (C-H7). The spell changes (C2, C4, C5) also apply to Holy.

- More mana in long fights: Reverence keeps 50% of the mana regeneration during casts, as the healer talents of the other classes (Reverence, C-H1).
- A capstone that Holy uses: Light's Vigil becomes a buff on Holy Shock. Each 6 sec, one Holy Shock also heals the party of the target (Light's Vigil, C-H7).

## Holy layout

| Row (points necessary) | Talents | Points in the row |
| --- | --- | --- |
| 1 (0) | Spiritual Focus, Divine Strength | 10 |
| 2 (5) | Healing Light, Reverence (C-H1), Improved Seals, Purifying Power | 12 |
| 3 (10) | Divine Favor, Illumination, Holy Conduit | 8 |
| 4 (15) | Divine Precision, Infusion of Light, Oath of Light | 5 |
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
| **225% (main hypothesis)** | **+1% / +3% / −5%** | **+6% / +9% / +3%** | **−34% / −30% / −32%** | **−30% / −25% / −27%** |
| 200% | −4% / −3% / −10% | +1% / +3% / −2% | −37% / −33% / −36% | −33% / −29% / −30% |
| 175% | −9% / −8% / −15% | −5% / −3% / −7% | −40% / −37% / −39% | −37% / −33% / −34% |

The Druid values use the development notes of 2 November 2026 (Bloom, Genesis 10%, no Gift of the Earthmother). See Analysis, Healing.

- **HB2 heals 6–9% more than HB1.** The gain increases with the fight length: +5.6% / +6.6% / +8.6% in raids.
- **At 225%,** Reverence gives the Paladin the first place on one tank in all fight lengths. Without it, the Druid is first in fights of 10 min. At 900 healing power, it is +7% / +10% / +5%. The lead stays far below the 20% limit (W14).
- **At 175%,** the Druid stays first on one tank, but the gap decreases by 4–8 points.
- **Raids.** About +3 to +5 points: the Paladin stays 25–30% below the Druid.
- **Only one Holy healing talent.** Before the notes of 2 November 2026, a second healing talent gave a tank lead past the 20% limit. Now it gives 10–16% (see Analysis, Healing, part 7). Reverence 50% is a proposal again since 2 November 2026.

## Effect on Retribution

- **Retribution builds take Reverence 2/2.** RB1 has 7 Holy points in rows 1–2. With 50%, RB1 receives 10.3 mana each sec from Reverence (live: 6.2).
- **The mana lasts 1.6–2.2 min longer** with Blessing of Wisdom. At fresh level 60, plan 1 + 3 lasts 5 min 20 sec (live: 3 min 43 sec).
- **Damage in fights of 5 min (model, Blessing of Wisdom).** Fresh level 60 +2.8%, pre-raid +3.0%, Molten Core +2.1%. Blackwing Lair +0.8%, Naxxramas 0%. Fights of 3 min do not change.
- **wowsims, RB1:** no buffs at fresh level 60, +4.1% in 3 min (303 → 315) and +5.2% in 5 min (288 → 303). Full raid buffs: 0% (906 in 2 min, 914 in 5 min).
- **This is accepted.** The gain is small and it decreases with gear. Sacred Arbiter +10% stays the balance lever (W15).

## C-H7. Light's Vigil: a buff on Holy Shock (live: a cast on an ally)

- **Live text.** "Applies Light's Vigil to a friendly target for 30 sec. The caster's next Holy Shock on the target incurs no cooldown and heals the target and their party for 326 to 344. Only one Vigil per Paladin may be active in each party." Rank 1: 730 mana, 40 yd range, 1.5 sec cast, 6 sec cooldown. Rank 3 (level 60): 704 to 744 for each party member, 14.3% of healing power, 1,340 mana.
- **Proposed text.** "Your Holy Shock, Judgement and Holy Strike grant a stack of Light's Vigil for 30 sec. This effect cannot occur more than once every 6 sec. Stacks up to 3 times. While Light's Vigil is active, your next Holy Shock triggers no cooldown and consumes one stack. On an allied target, Holy Shock also heals the target's party for 35% of the amount healed."
- **Problem.** Rank 3 costs 1,340 mana, 89% of the base mana. It needs two casts (3 sec) for one party heal. It heals 4.7 for each mana point (Flash of Light: 6.2). In the model, the Paladin casts it only in fights of 3 min. In raids, the Paladin is 30–34% below the Druid and 7–9% below the Shaman.
- **Model.** Riptide (Shaman capstone) adds a bonus to Chain Heal. Prayer of Mending (Priest capstone) is an efficient group heal with a cooldown. Light's Vigil (C-H7) adds a party heal to Holy Shock, with a cooldown of 6 sec.
- **Why this design.** One spell (Holy Shock) does the work. The talent keeps the name, the 30 sec, the 6 sec and the "next Holy Shock triggers no cooldown" rule of the live talent. Each stack is one Holy Shock with no cooldown. No spell uses more than one stack, thus the stacks are not a resource for a finisher. The party heal is a % of the Holy Shock heal, thus it increases with the rank, the level, healing power and critical heals.

**How it works**

- Start a fight with Holy Shock, Judgement or Holy Strike. You then have one stack of Light's Vigil.
- Each 6 sec, Holy Shock, Judgement or Holy Strike gives one more stack, up to 3. Each new stack sets the duration to 30 sec again.
- A Holy Shock with Light's Vigil uses one stack. It also gives a stack when the 6 sec cooldown is over. Thus each 6 sec, one Holy Shock heals the party. Holy Shock is enough: ranged and melee Paladins receive the same value.
- Planned burst: keep 3 stacks before a raid damage phase. Then four Holy Shocks one after the other heal the party in 4.5 sec. The first one gives the fourth stack.
- Light's Vigil does not end an active Holy Shock cooldown. After a plain Holy Shock, the next Holy Shock waits for its cooldown. Judgement has no global cooldown, thus it can give a stack at once.

**Healing model, 715 healing power, 3 / 5 / 10 min**

| Critical heal | Case | Live | Light's Vigil (C-H7) | C-H7 and Reverence 50% (C-H1) |
| --- | --- | --- | --- | --- |
| **225% (main hypothesis)** | **Raid, against the Druid** | **−34% / −30% / −32%** | **−17% / −11% / −11%** | **−14% / −5% / −5%** |
| 225% | Raid, against the Shaman | −8% / −7% / −9% | +14% / +18% / +21% | +19% / +25% / +28% |
| 225% | One tank, against the Druid | +1% / +3% / −5% | +1% / +3% / −5% | +6% / +9% / +3% |
| 200% | Raid, against the Druid | −37% / −33% / −36% | −23% / −17% / −17% | −20% / −12% / −12% |
| 175% | Raid, against the Druid | −40% / −37% / −39% | −28% / −23% / −23% | −25% / −18% / −18% |
| 175% | Raid, against the Shaman | −18% / −17% / −18% | −1% / +2% / +4% | +3% / +8% / +10% |

- **Raids.** With both Holy proposals, the Paladin is 5% below the Druid in fights of 5 and 10 min, and 14% below in fights of 3 min (225%). It stays below the Priest. At 175%, it is 18–25% below the Druid.
- **One tank.** No change. The party heal goes to 5 players, thus the tank receives only a small part. The one-tank values come from Reverence 50% (C-H1) only.
- **Cast plan.** About 51 Holy Shocks with Light's Vigil in 5 min (one each 6 sec). Flash of Light stays the main heal.
- **Healing for each mana point.** A Holy Shock with Light's Vigil heals about 3,230 (raid, before overhealing): 1,170 on the target and 5 × 410 on the party. This is 9.9 healing for each mana point after overhealing. The party heal has 50% overhealing, as Wild Growth: it heals all 5 players, also the players at full health. Prayer of Mending gives 15.7.
- **Group burst.** With 3 stacks, four Holy Shocks with Light's Vigil heal about 12,900 in 6 sec, for about 820 mana. In 10 sec, with Flash of Light or a plain Holy Shock after them, they heal about 17,300 at all ranges. With 1 stack, about 8,500 in 6 sec. Priest: about 15,000 in 10 sec (Prayer of Mending and two Prayer of Healing). Druid: about 11,100 (two Wild Growth). Shaman: about 10,000 (four Chain Heal). The live talent with a Vigil on 4 parties: about 25,600 in 6 sec, for 4,190 mana.
- **Stacks before a fight.** Holy Shock out of combat gives stacks. A stack lasts 30 sec, thus the Paladin can start a fight with at most 3 stacks.
- **Damage.** The talent has no enemy effect of its own. On an enemy, Light's Vigil only removes the Holy Shock cooldown. With 3 stacks, four Holy Shocks one after the other do 2,130 to 2,670 damage in 4.5 sec (400 to 715 spell damage). Without the talent, one Holy Shock does 533 to 668 in the same time.
- **Other talents.** Spiritual Focus and Illumination name Light's Vigil. With C-H7, Light's Vigil has no cast and no heal of its own, thus the two texts no longer name it. Illumination applies to the Holy Shock heal, not to the party heal.
- **The value depends on the critical heal size.** The Holy Power test (Open items) gives the real value. With both proposals, the raid values at 175% are 11–13 points lower than at 225%.

Model: `models/beta-30-oct/light_vigil_ch7.py`.
