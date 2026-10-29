# Judgements and Blessings in raids

## The problem

- **The rule.** Each Paladin can have only one Judgement active on a target.
- **The conflict.** Since the patch of 15 October, Salvation does not use a Blessing slot. Thus, two Paladins can give all Blessings to a raid. But raids prefer Judgement of Light and Judgement of Wisdom, because they help all players. Judgement of the Crusader helps mostly the Holy damage of the Paladins. Raids remove it. Thus, Retribution loses damage and Protection loses threat.
- **Judgement of Fury does not remove Judgement of the Crusader.** The problem is the one-Judgement limit, not the taunt.
- **Sacred Arbiter does not fix it.** Holy Strike refreshes all Judgements on the target, also those of other Paladins. But each Paladin still has only one Judgement.

## C2. Personal Judgement of the Crusader (recommended)

- **Change.** Judgement of the Crusader does not count against the one-Judgement limit. But it increases only the Holy damage of the Paladin who applies it.
- **Precedent.** Salvation does not use a Blessing slot now. Improved Seal of the Crusader is now baseline.
- **Tradeoff.** Other players who do Holy damage do not receive the bonus.
- **For Protection.** A raid can need the one Judgement of the tank for Light or Wisdom. In the beta, the tank then loses Judgement of the Crusader. With Personal Judgement of the Crusader (C2), the tank keeps it and can also apply Light or Wisdom. Judgement of the Crusader gives a Protection Paladin about +55 TPS (see Analysis, Threat).

## Alternatives to Personal Judgement of the Crusader (C2)

| ID | Option | How it works | Precedent | Tradeoff |
| --- | --- | --- | --- | --- |
| C2a | Merge Light and Wisdom (use this if Personal Judgement of the Crusader, C2, is rejected) | A Judgement of Seal of Light or Seal of Wisdom applies one Judgement of Grace. Attacks can heal the attacker for 61 and restore 59 mana | Weaponmaster merged four weapon talents | One Paladin must still choose |
| C2b | Judgement Echo (optional, with Personal Judgement of the Crusader, C2) | When your next Judgement replaces your Judgement of Light, Wisdom or Justice, the replaced Judgement stays on the target as an Echo for 40 sec | The Seal Echo of Twist of Light | It needs a Retribution Paladin with 30 points |

| Raid with two Paladins | Beta | C2 | C2a | C2b alone |
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

- **Effect on Holy.** In raids with 1 or 2 Paladins, most targets do not receive Blessing of Light. At 900 healing power, Flash of Light + Holy Light (Infusion of Light, C-H3) then gives 1,194 healing per sec and 4.96 healing per mana. This uses 19% critical heals. With Blessing of Light, it gives 1,405 and 5.83.
- **The same problem as Personal Judgement of the Crusader (C2).** The healing of the class changes with the number of Paladins in the raid.

## C3. Blessing of Light: removed, Healing Light gives 10/20/30% (recommended)

- **Change.** Remove Blessing of Light and Greater Blessing of Light. Healing Light (C-H4) has 3 ranks: 10/20/30% (beta: 4/8/12%).
- **Proposed text (Healing Light).** "Increases the amount healed by your Holy Light, Flash of Light, and Holy Shock spells by 10/20/30%."
- **Precedent.** Forever removed Blessing of Sanctuary.
- **Why a %.** Forever talents give a % bonus, not a flat value. A % bonus also increases with gear, as Forever wants. Blessing of Light gives a flat +400 to Holy Light and +115 to Flash of Light. Its value decreases with gear. At 700–900 healing power, it gives about +17–19% to these two heals. Thus, 12% + 18% = 30%.
- **Why Holy only.** Retribution and Protection lose almost nothing. In raids with 1 or 2 Paladins, they did not receive Blessing of Light. In PvP, a Paladin alone puts Kings on itself, not Light. Thus, the hybrid burst heal in PvP stays at 2,231 (see W12).
- **One or the other.** If Blessing of Light stays, raids with 3 or more Paladins receive the two bonuses. Thus, Blessing of Light removal (C3) removes the spell.
- **Holy Shock** also receives +30% (beta: +12%). It heals about 920 at 900 healing power. It stays an emergency heal.
- **While you level.** Healing Light 3/3 comes at level 37. Blessing of Light rank 1 came at level 40.

Flash of Light + Holy Light (Infusion of Light, C-H3), healing per sec with no critical heals:

| Healing power | Beta, Light on the target | Beta, no Light (1 or 2 Paladins) | C3 |
| --- | --- | --- | --- |
| 0 | 897 | 705 | 818 (−9%) |
| 300 | 1,025 | 833 | 967 (−6%) |
| 900 | 1,281 | 1,089 | 1,264 (−1%) |
| 1,100 | 1,366 | 1,174 | 1,363 (0%) |

- The % compares Blessing of Light removal (C3) with the beta when the target has Light.
- Raids with 3 or more Paladins lose 1–9%, mostly with little gear. Blessing of Light removal (C3) is equal at about 1,150 healing power.
- Raids with 1 or 2 Paladins receive 16–17% more healing.
- The healing of the Paladin does not change with the number of Paladins.
- For the comparison with the other healers, see Analysis, Healing, parts 4 and 5.

## Alternatives to Blessing of Light removal (C3)

| ID | Option | How it works | Precedent | Tradeoff |
| --- | --- | --- | --- | --- |
| C3a | Blessing of Light uses no Blessing slot (use this if Blizzard keeps the spell) | Blessing of Light is a fourth Blessing outside the limit, as Salvation is | Salvation, patch of 15 October | Raids must still cast it. The bonus stays flat. A Retribution Paladin in PvP has Kings and Light |
| C3b | The Blessing of Light bonus goes into the base values | Remove the Blessing. Holy Light rank 9 heals 1,980 (beta: 1,580). Flash of Light rank 6 heals 423 (beta: 308). Each rank from level 40 receives the bonus of the Blessing rank of its level | Forever removed Blessing of Sanctuary | Base values increase. This is against the Forever direction. All specs receive the bonus |

|  | Beta | C3 | C3a | C3b |
| --- | --- | --- | --- | --- |
| Raid with 1 or 2 Paladins, 900 healing power, no critical heals | 1,089 | 1,264 | 1,281 | 1,281 |
| Increases with gear | No | Yes | No | No |
| Blessing to cast | Yes | No | Yes | No |
| Hybrid burst heal in PvP (3 sec) | 2,231 | 2,231 | 2,746 | 2,746 |
| Spell removed | No | Yes | No | Yes |

## C4. Hand of Sacrifice: a damage pool

- **Change.** Hand of Sacrifice moves up to 825 damage to the Paladin, with a 15 sec cooldown. With Hands (C5), Blessing of Sacrifice is Hand of Sacrifice and uses no Blessing slot.
- **Proposed text (rank 2).** "Places a Hand on the party member, transferring up to 825 damage taken to the caster. Lasts 30 sec." 100 mana, 30 yards, instant, 15 sec cooldown.
- **Rank 1 (level 46).** Up to 675 damage, 80 mana. 15 hits of the beta value: 15 × 45.
- **Beta text (rank 2).** "Places a Blessing on the party member, transferring 55 damage taken per hit to the caster. Lasts 30 sec. Players may only have one Blessing on them per Paladin at any one time." No cooldown.
- **The Hand ends** after 30 sec or when 825 damage moves to the caster.

### The problem

- **55 for each hit is too small.** A Naxxramas boss hits a tank for about 8,000 before armor (see Analysis, Threat). After armor, 55 is about 2% of one hit.
- **It uses the Blessing slot.** In the beta, it replaces Kings or Might from the same Paladin. Thus, Paladins do not cast it. Hands (C5) removes this cost.

### The change

- **The same budget.** 825 is 15 hits of 55. The value does not change. It moves into one pool. Thus, all hits use the pool, also large hits.
- **Classic text.** The tooltip keeps the form of the beta spell. Only the numbers change. Hands (C5) changes the word "Blessing" to "Hand".
- **A flat value.** Hand of Sacrifice is a spell, not a talent. Spells use flat values, as Power Word: Shield does.
- **Why 15 sec.** With no Blessing slot, a Paladin can put a pool on each ally. The cooldown is half of the duration. Thus, each Paladin has two pools active at most: 1,650 damage.
- **One pool on a target.** On one ally, a new Hand replaces the old one (Hands, C5). Thus, a tank has one pool from each Paladin at a time: 825 damage each 15 sec.
- **The same for all specs.** No talent changes the cooldown. Holy, Protection and Retribution have the same Hand of Sacrifice.
- **Devoted Sacrifice (C-P11).** This Protection talent reduces the damage that the Paladin takes from the pool by 20/40%. The target is still protected from up to 825 damage.
- **The cost.** The damage does not disappear. It moves to the Paladin, and the Paladin must survive it and heal it. Thus, the health of the Paladin limits the number of pools.

### Divine Shield and the Classic trick

- **The rule stays.** If the Paladin is immune, the damage that moves to the Paladin has no effect. This is the Classic rule.
- **The trick stays.** A Paladin in Divine Shield can save an ally from 825 damage. The ally takes no damage, and the Paladin takes no damage.
- **The cooldown limits it.** Divine Shield lasts 12 sec. Thus, two pools are active in one Divine Shield at most: 1,650 damage on two allies. The Paladin cannot protect the full raid. See W20.
- **Damage on the Paladin.** The damage that moves to the Paladin can stop a Polymorph or a Sap on the Paladin. This is also a Classic rule.

### Use

| Use | Effect |
| --- | --- |
| Raid, other tank | 825 is about one third of a Naxxramas boss hit after armor (estimate). A short save for a tank swap or a crushing blow |
| Raid, area damage | The pool takes the area damage on one ally until it is empty. The Paladin takes this damage as well as its own |
| PvP | A shield against a Rogue or a Warrior burst on a healer. The Paladin takes the damage and heals it |

### Against the other classes

| Spell | Class | Value | Cooldown | Where the damage goes |
| --- | --- | --- | --- | --- |
| Hand of Sacrifice (C4) | Paladin | 825 | 15 sec | To the Paladin |
| Power Word: Shield | Priest | About 1,100 with healing power (see Analysis, Healing) | 4 sec, 15 sec on the same target | Removed |
| Blessing of Sacrifice (beta) | Paladin | 55 for each hit | None | To the Paladin |

- Power Word: Shield removes the damage. Hand of Sacrifice moves it to the Paladin. Thus, the Paladin must still heal it.
- The value does not increase with gear. The Paladin health increases with gear, and this limits the value.

## C5. Hands: Sacrifice, Protection and Freedom

- **Change.** Blessing of Sacrifice, Blessing of Protection and Blessing of Freedom become Hand of Sacrifice, Hand of Protection and Hand of Freedom. Hands do not use a Blessing slot. Each Paladin can have one Hand on a target. A new Hand replaces the old one.
- **Precedent.** Forever moved Curse of Agony and Curse of Doom into a new group: Bane of Agony and Bane of Doom. Each Warlock can have one Curse and one Bane on a target. Since the patch of 15 October, Salvation also does not use a Blessing slot.
- **A modern name.** "Hand" comes from a later version of the game. Banes also come from a later version, and Forever uses them. Thus, this name is an accepted exception to the rule against ideas from later versions.
- **Other text.** The proposals use the new names. For example, Guardian's Favor names Hand of Protection and Hand of Freedom.
- **Salvation does not change.** It already uses no Blessing slot. It is a long threat buff, not a save.

### The problem

- **A save removes a buff.** In the beta, Blessing of Protection, Blessing of Freedom and Blessing of Sacrifice use the Blessing slot. On the target, they replace Kings or Might from the same Paladin. After the save, the Paladin must cast the buff again. In combat, this costs a global cooldown and mana.

### One Hand for each Paladin

- **A choice.** One Paladin cannot put Hand of Protection and Hand of Sacrifice on the same target. Two Paladins can.
- **Why a limit.** Without it, one Paladin can put the three saves on one ally. The limit keeps one save from each Paladin, as the Bane limit keeps one Bane from each Warlock.
- **No change to the saves.** Hand of Protection and Hand of Freedom keep their effects, durations and cooldowns. Forbearance does not change.

### Use

| Use | Effect |
| --- | --- |
| Raid, Hand of Protection | The target keeps Kings or Might. The Paladin does not cast the buff again after the save |
| PvP, Hand of Freedom | A Warrior keeps Might. The Paladin does not cast Might again |
