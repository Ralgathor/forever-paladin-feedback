# Judgements and Blessings in raids

## The problem

- **The rule.** Each Paladin can have only one Judgement active on a target.
- **The conflict.** The beta of 30 October removes Blessing of Light and Salvation. Thus, two Paladins can give all Blessings to a raid: Kings, Might and Wisdom. But raids prefer Judgement of Light and Judgement of Wisdom, because they help all players. Judgement of the Crusader helps mostly the Holy damage of the Paladins. Raids remove it. Thus, Retribution loses damage and Protection loses threat.
- **Judgement of Fury does not remove Judgement of the Crusader.** The problem is the one-Judgement limit, not the taunt.
- **Sacred Arbiter does not fix it.** Holy Strike refreshes all Judgements on the target, also those of other Paladins. But each Paladin still has only one Judgement.

## C2. Personal Judgement of the Crusader (recommended)

- **Change.** Judgement of the Crusader does not count against the one-Judgement limit. But it increases only the Holy damage of the Paladin who applies it.
- **Precedent.** Improved Seal of the Crusader is now baseline.
- **Tradeoff.** Other players who do Holy damage do not receive the bonus.
- **For Protection.** A raid can need the one Judgement of the tank for Light or Wisdom. In the beta, the tank then loses Judgement of the Crusader. With Personal Judgement of the Crusader (C2), the tank keeps it and can also apply Light or Wisdom. Judgement of the Crusader gives a Protection Paladin about +55 TPS (see Analysis, Threat).

## Alternatives to Personal Judgement of the Crusader (C2)

| ID | Option | How it works | Precedent | Tradeoff |
| --- | --- | --- | --- | --- |
| C2a | Merge Light and Wisdom (use this if Personal Judgement of the Crusader, C2, is rejected) | A Judgement of Seal of Light or Seal of Wisdom applies one Judgement of Grace. Attacks can heal the attacker for 61 and restore 59 mana | Weaponmaster merged four weapon talents | One Paladin must still choose |

| Raid with two Paladins | Beta | C2 | C2a |
| --- | --- | --- | --- |
| Holy + Holy | Light + Wisdom | Light + Wisdom | Grace |
| Holy + Retribution | Two of three | All three | Grace + Crusader |
| Holy + Protection | Two of three | All three | Grace + Crusader |
| Protection + Retribution | Two of three | All three | Grace + Crusader |

## Blessing of Light: removed in the beta of 30 October

- **Adopted.** The beta of 30 October removes Blessing of Light and Greater Blessing of Light, as Blessing of Light removal (C3) asked. C3 is no longer a proposal.
- **Oath of Light.** The beta adds Oath of Light, a Holy row 4 talent. It gives the Blessing of Light bonus (+400 Holy Light, +115 Flash of Light) and +229 Holy Shock, on one ally only.
- **Oath of Light stays.** Oath of Light keeps its beta version. Healing Light keeps 4/8/12%. The proposal for Healing Light 10/20/30% (C-H4) is withdrawn.

## C4. Hand of Sacrifice: a damage pool

- **Change.** Hand of Sacrifice moves up to 825 damage to the Paladin. It lasts 30 sec and has a 15 sec cooldown. With Hands (C5), Blessing of Sacrifice is Hand of Sacrifice and uses no Blessing slot.
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
- **Precedent.** Forever moved Curse of Agony and Curse of Doom into a new group: Bane of Agony and Bane of Doom. Each Warlock can have one Curse and one Bane on a target.
- **A modern name.** "Hand" comes from a later version of the game. Banes also come from a later version, and Forever uses them. Thus, this name is an accepted exception to the rule against ideas from later versions.
- **Other text.** The proposals use the new names. For example, Guardian's Favor names Hand of Protection and Hand of Freedom.

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
