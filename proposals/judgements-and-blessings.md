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
- **For Protection.** A raid can need the one Judgement of the tank for Light or Wisdom. In the beta, the tank then loses Judgement of the Crusader. With C18, the tank keeps it and can also apply Light or Wisdom. Judgement of the Crusader gives a Protection Paladin about +55 TPS (see Analysis, Threat).

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

- **Effect on Holy.** In raids with 1 or 2 Paladins, most targets do not receive Blessing of Light. At 900 healing power, Flash of Light + Holy Light (C3) then gives 1,194 healing per sec and 4.96 healing per mana (19% critical heals). With Blessing of Light, it gives 1,405 and 5.83.
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

Flash of Light + Holy Light (C3), healing per sec with no critical heals:

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
| Raid with 1 or 2 Paladins, 900 healing power, no critical heals | 1,089 | 1,264 | 1,281 | 1,281 |
| Increases with gear | No | Yes | No | No |
| Blessing to cast | Yes | No | Yes | No |
| Hybrid burst heal in PvP (3 sec) | 2,231 | 2,231 | 2,746 | 2,746 |
| Spell removed | No | Yes | No | Yes |

## C23. Hands: Sacrifice, Protection and Freedom

- **Change.** Blessing of Sacrifice, Blessing of Protection and Blessing of Freedom become Hands: Hand of Sacrifice, Hand of Protection and Hand of Freedom. They do not use a Blessing slot. Each Paladin can have one Hand on a target. A new Hand replaces the old one.
- **Hand of Sacrifice** also changes: it moves up to 825 damage to the Paladin, with a 15 sec cooldown (see below).
- **Precedent.** Forever moved Curse of Agony and Curse of Doom into a new group: Bane of Agony and Bane of Doom. Each Warlock can have one Curse and one Bane on a target. Since the patch of 15 October, Salvation also does not use a Blessing slot.
- **A modern name.** "Hand" comes from a later version of the game. Banes also come from a later version, and Forever uses them. Thus, this is an accepted exception to design rule 2.
- **Other text.** With C23, Guardian's Favor and the other spell texts name Hand of Protection and Hand of Freedom.
- **Salvation does not change.** It already uses no Blessing slot. It is a long threat buff, not a save.

### The problem

- **A save removes a buff.** In the beta, Blessing of Protection and Blessing of Freedom use the Blessing slot. On the target, they replace Kings or Might from the same Paladin. After the save, the Paladin must cast the buff again. In combat, this costs a global cooldown and mana.
- **Blessing of Sacrifice: 55 for each hit is too small.** A Naxxramas boss hits a tank for about 8,000 before armor (see Analysis, Threat). After armor, 55 is about 2% of one hit. It also replaces Kings or Might. Thus, Paladins do not cast it.

### One Hand for each Paladin

- **A choice.** One Paladin cannot put Hand of Protection and Hand of Sacrifice on the same target. Two Paladins can.
- **Why a limit.** Without it, one Paladin can put the three saves on one ally. The limit keeps one save from each Paladin, as the Bane limit keeps one Bane from each Warlock.
- **No change to the saves.** Hand of Protection and Hand of Freedom keep their effects, durations and cooldowns. Forbearance does not change.

### Hand of Sacrifice

- **Proposed text (rank 2).** "Places a Hand on the party member, transferring up to 825 damage taken to the caster. Lasts 30 sec." 100 mana, 30 yards, instant, 15 sec cooldown.
- **Rank 1 (level 46).** Up to 450 damage. 15 hits of the beta value: 15 × 30.
- **Beta text (rank 2).** "Places a Blessing on the party member, transfering 55 damage taken per hit to the caster. Lasts 30 sec. Players may only have one Blessing on them per Paladin at any one time." No cooldown.
- **The Hand ends** after 30 sec or when 825 damage moves to the caster.
- **The same budget.** 825 is 15 hits of 55. The value does not change. It moves into one pool. Thus, all hits use the pool, also large hits.
- **Classic text.** The tooltip keeps the form of the beta spell. Only the numbers and the word "Hand" change.
- **A flat value.** Hand of Sacrifice is a spell, not a talent. Spells use flat values, as Power Word: Shield does.
- **Why 15 sec.** With no Blessing slot, a Paladin can put a pool on each ally. The cooldown is half of the duration. Thus, each Paladin has two pools active at most: 1,650 damage.
- **The cost.** The damage does not disappear. It moves to the Paladin, and the Paladin must survive it and heal it. Thus, the health of the Paladin limits the number of pools.

### Divine Shield and the classic trick

- **The rule stays.** If the Paladin is immune, the damage that moves to the Paladin has no effect. This is the Classic rule.
- **The trick stays.** A Paladin in Divine Shield can save an ally from 825 damage. The ally takes no damage, and the Paladin takes no damage.
- **The cooldown limits it.** Divine Shield lasts 12 sec. Thus, two pools at most are active in one Divine Shield: 1,650 damage on two allies. The Paladin cannot protect the full raid. See W20.
- **Damage on the Paladin.** The damage that moves to the Paladin can stop a Polymorph or a Sap on the Paladin. This is also a Classic rule.

### Use

| Use | Effect |
| --- | --- |
| Raid, other tank | 825 is about one third of a Naxxramas boss hit after armor (estimate). A short save for a tank swap or a crushing blow |
| Raid, area damage | The pool takes the area damage on one ally until it is empty. The Paladin takes this damage as well as its own |
| Raid, Hand of Protection | The target keeps Kings or Might. The Paladin does not cast the buff again after the save |
| PvP | Hand of Freedom on a Warrior keeps Might. Hand of Sacrifice is a shield against a Rogue or a Warrior burst on a healer. The Paladin takes the damage and heals it |

### Against the other classes

| Spell | Class | Value | Cooldown | Where the damage goes |
| --- | --- | --- | --- | --- |
| Hand of Sacrifice (C23) | Paladin | 825 | 15 sec | To the Paladin |
| Power Word: Shield | Priest | About 1,100 with healing power (see Analysis, Healing) | 4 sec, 15 sec on the same target | Removed |
| Blessing of Sacrifice (beta) | Paladin | 55 for each hit | None | To the Paladin |

- Power Word: Shield removes the damage. Hand of Sacrifice moves it to the Paladin. Thus, the Paladin must still heal it.
- The value does not increase with gear. The Paladin health increases with gear, and this limits the value.
