# Judgements and Blessings in raids

## The problem

- **The rule.** Each Paladin can have only one Judgement active on a target.
- **The conflict.** Since the patch of 15 October, Salvation does not use a Blessing slot. Thus, two Paladins can give all Blessings to a raid. But raids prefer Judgement of Light and Judgement of Wisdom, because they help all players. Judgement of the Crusader helps mostly the Holy damage of the Paladins. Raids remove it. Thus, Retribution loses damage and Protection loses threat.
- **Judgement of Fury does not remove Judgement of the Crusader.** The problem is the one-Judgement limit, not the taunt.
- **Sacred Arbiter does not fix it.** Holy Strike refreshes all Judgements on the target, also those of other Paladins. But each Paladin still has only one Judgement.

## C18. Personal Judgement of the Crusader (recommended)

- **Change.** Judgement of the Crusader does not count against the one-Judgement limit. But it increases only the Holy damage of the Paladin who applies it.
- **Precedent.** Salvation does not use a Blessing slot now. Improved Seal of the Crusader is now baseline.
- **Tradeoff.** Other players who do Holy damage do not get the bonus.
- **For Protection.** A raid can need the one Judgement of the tank for Light or Wisdom. In the beta, the tank then loses Judgement of the Crusader. With C18, the tank keeps it and can also apply Light or Wisdom. Judgement of the Crusader gives a Protection Paladin about +50 TPS (see Analysis, Threat).

## Alternatives to C18

| ID | Option | How it works | Precedent | Tradeoff |
| --- | --- | --- | --- | --- |
| C18a | Merge Light and Wisdom (use this if C18 is rejected) | A Judgement of Seal of Light or Seal of Wisdom applies one Judgement of Grace. Attacks can heal the attacker for 61 and restore 59 mana | Weaponmaster merged four weapon talents | One Paladin must still choose |
| C18b | Judgement Echo (optional, with C18) | When your next Judgement replaces your Judgement of Light, Wisdom or Justice, the replaced Judgement stays on the target as an Echo for 40 sec | The Seal Echo of Twist of Light | It needs a Retribution Paladin with 30 points |

| Raid with two Paladins | Beta | C18 | C18a | C18b alone |
| --- | --- | --- | --- | --- |
| Holy + Holy | Light + Wisdom | Light + Wisdom | Grace | Light + Wisdom |
| Holy + Retribution | Two of three | All three | Grace + Crusader | All three |
| Holy + Protection | Two of three | All three | Grace + Crusader | Two of three |
| Protection + Retribution | Two of three | All three | Grace + Crusader | All three |

## The problem with Blessings

- **The rule.** A player can have one Blessing from each Paladin. Since the patch of 15 October, Salvation does not use a Blessing slot. Forever removed Blessing of Sanctuary.
- **The order.** Each player takes Kings first. Then melee players take Might, and the other players take Wisdom. Blessing of Light is always third, because it increases only the heals of Paladins.
- **Greater Blessings work on a class.** To put Light only on the tanks, a Paladin must cast the single Blessing on each tank. This replaces the Kings of the same Paladin on that tank.

| Paladins in the raid | Melee | Casters and healers | Tanks |
| --- | --- | --- | --- |
| 1 | Kings | Kings | Kings |
| 2 | Kings + Might | Kings + Wisdom | Kings + Might, or Kings + Light |
| 3 or more | Kings + Might + Light | Kings + Wisdom + Light | Kings + Might + Light |

- **Effect on Holy.** In raids with 1 or 2 Paladins, most targets do not receive Blessing of Light. At 900 healing power, Flash of Light + Holy Light (C3) then gives 1,089 healing per sec and 4.67 healing per mana. With Blessing of Light, it gives 1,281 and 5.49.
- **The same problem as C18.** The healing of the class changes with the number of Paladins in the raid.

## C19. Blessing of Light: removed, Healing Light gives 10/20/30% (recommended)

- **Change.** Remove Blessing of Light and Greater Blessing of Light. Healing Light (C4) gets 3 ranks: 10/20/30% (beta: 4/8/12%).
- **Proposed text (Healing Light).** "Increases the amount healed by your Holy Light, Flash of Light, and Holy Shock spells by 10/20/30%."
- **Precedent.** Forever removed Blessing of Sanctuary.
- **Why a %.** Forever talents give a % bonus, not a flat value. A % bonus also increases with gear, as Forever wants. Blessing of Light gives a flat +400 to Holy Light and +115 to Flash of Light. Its value decreases with gear. At 700–900 healing power, it gives about +17–19% to these two heals. Thus, 12% + 18% = 30%.
- **Why Holy only.** Retribution and Protection lose almost nothing. In raids with 1 or 2 Paladins, they did not get Blessing of Light. In PvP, a Paladin alone puts Kings on himself, not Light. Thus, the hybrid burst heal in PvP stays at 2,231 (see W12).
- **One or the other.** If Blessing of Light stays, raids with 3 or more Paladins get the two bonuses. Thus, C19 removes the spell.
- **Holy Shock** also gets +30% (beta: +12%). It heals about 920 at 900 healing power. It stays an emergency heal.
- **Leveling.** Healing Light 3/3 comes at level 37. Blessing of Light rank 1 came at level 40.

Flash of Light + Holy Light (C3), healing per sec:

| Healing power | Beta, Light on the target | Beta, no Light (1 or 2 Paladins) | C19 |
| --- | --- | --- | --- |
| 0 | 897 | 705 | 818 (−9%) |
| 300 | 1,025 | 833 | 967 (−6%) |
| 900 | 1,281 | 1,089 | 1,264 (−1%) |
| 1,100 | 1,366 | 1,174 | 1,363 (0%) |

- The % compares C19 with the beta when the target has Light.
- Raids with 3 or more Paladins lose 1–9%, mostly with little gear. C19 is equal at about 1,150 healing power.
- Raids with 1 or 2 Paladins get 16–17% more healing.
- The healing of the Paladin does not change with the number of Paladins.
- For the comparison with the other healers, see Analysis, Healing, parts 4 and 5.

## Alternatives to C19

| ID | Option | How it works | Precedent | Tradeoff |
| --- | --- | --- | --- | --- |
| C19a | Blessing of Light uses no Blessing slot (use this if Blizzard keeps the spell) | Blessing of Light is a fourth Blessing outside the limit, as Salvation is | Salvation, patch of 15 October | Raids must still cast it. The bonus stays flat. A Retribution Paladin in PvP gets Kings and Light |
| C19b | The Blessing of Light bonus goes into the base values | Remove the Blessing. Holy Light rank 9 heals 1,980 (beta: 1,580). Flash of Light rank 6 heals 423 (beta: 308). Each rank from level 40 gets the bonus of the Blessing rank of its level | Forever removed Blessing of Sanctuary | Base values go up. This is against the Forever direction. All specs get the bonus |

|  | Beta | C19 | C19a | C19b |
| --- | --- | --- | --- | --- |
| Raid with 1 or 2 Paladins, 900 healing power | 1,089 | 1,264 | 1,281 | 1,281 |
| Increases with gear | No | Yes | No | No |
| Blessing to cast | Yes | No | Yes | No |
| Hybrid burst heal in PvP (3 sec) | 2,231 | 2,231 | 2,746 | 2,746 |
| Spell removed | No | Yes | No | Yes |
