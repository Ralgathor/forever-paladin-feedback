# Beta test results

## Holy talents

| Talent | Result in the beta | Effect on the proposals |
| --- | --- | --- |
| Divine Strength, Divine Intellect | % of base, gear and flat buff stats. Multiplies with Kings | C8 removes Divine Strength |
| Healing Light | Increases the full heal, not only the base | Supports C2: a second flat healing talent overlaps with it |
| Spiritual Focus | Adds to other pushback resistance (Concentration Aura 35% + 70% = immune) | None |
| Improved Seals | Increases the full damage, not only the base. No effect on Seal of the Crusader | None |
| Unyielding Faith | Diminishing returns not tested | C8 moves it to Holy row 1 |
| Reverence | Keeps a % of Spirit regeneration during casts. The 5-second rule starts again when a cast ends | Supports C1 |
| Purifying Power | Multiplies with Benediction (×0.80 × 0.90) | None |
| Illumination | Returns 50% of the base cost. Cost decreases do not decrease the return | None |
| Divine Favor | Not on the global cooldown | None |
| Divine Precision | The spell hit cap is 18%, with no fixed 1% miss. 3/3 gives the full cap | None |
| Holy Shock | Damage uses spell damage. Healing uses healing power. Both at 42.9% | None |
| Consecrated Ground | Increases all your Holy damage on those targets, also Retribution Aura and Consecration | None |
| Light's Vigil | 3 ranks: 730, 1,000 and 1,340 mana. Rank 3 heals each party member for 684–724 | None |

## Protection talents

| Talent | Result in the beta | Effect on the proposals |
| --- | --- | --- |
| Toughness | Only armor from items. Nothing from Devotion Aura, scrolls, elixirs, potions or Mark of the Wild | Supports C8 |
| Redoubt | A blocked hit can start it without the use of a charge | C6 keeps the proc |
| Precision | Melee, ranged and spell hit. Each ability uses the correct hit type | Confirms it as the shared hit talent |
| Anticipation | A raid boss stops critical hits at 440 Defense. Anticipation gives 20 | The stat targets use this cap |
| Improved Seal of Fury | The mana return does not change with the rank of the Seal. The mana gives no threat | Removed by C10 |
| Improved Righteous Fury | Applies after armor. Multiplies with Iron Creed (×0.94 × 0.90) | Removed by C9 |
| Shield Specialization | Multiplies Shield Block Value. Mana return is 4%. The mana gives no threat | Stays the main mana source. C13 changes the limit to 2 sec |
| Sacred Duty | % of total Stamina, multiplies with Kings. Decreases the cooldowns of Forbearance spells | None |
| Swift Judgement | Not on the global cooldown | None |
| One-Handed Weapon Specialization | Melee attacks, Seals, Judgements, Holy Strike and the Twist of Light Echo | None |
| Templar's Bulwark | An absorb, not a heal. Mortal Strike effects do not decrease it | None |
| Reckoning | Stored attacks hit with the next melee hit. Each can trigger Seals and Judgements | C11: Holy Strike releases the charges |
| Iron Creed | Holy Strike threat ×1.90 (Righteous Fury) × 1.25 | C7 keeps these multipliers |
| Holy Shield | Threat ×1.90 (Righteous Fury) × 1.20. More tests are necessary | None |

## Retribution talents

| Talent | Result in the beta | Effect on the proposals |
| --- | --- | --- |
| Benediction | Its cost decrease multiplies with Purifying Power, Holy Conduit and Twist of Light | C8 moves it to Protection row 1. It keeps 5 ranks |
| Holy Conduit | With Benediction, Consecration costs ×0.60 × 0.90 | None |
| Conviction | Also applies to damage Seals and Hammer of Wrath | C15 adds only Holy Shock, Exorcism, Consecration and heals |
| Vindication | About 5 procs each minute. Ranks: −67/136/204 Attack Power on the target and +1/2/3% on you | C8: row 2, 5 ranks, +1/2/3/4/5% |
| Sanctified Judgement | Returns 60% of the base cost of the Seal, before talent cost decreases: 126 mana for Seal of Command with Benediction and Twist of Light | The mana models use 126 |
| Pursuit of Justice | 15% at 2/2. Better than the 8% boot enchant | On the watch list (W1) |
| Eye for an Eye | Uses the damage taken after armor and resistance | None |
| Sacred Arbiter | +20% Holy Strike damage. Refreshes Light, Wisdom, Justice and Crusader | Holy Strike triggers all Seals (C16, spell change) |
| Two-Handed Weapon Specialization | Melee attacks, Seals, Judgements, Holy Strike and the Twist of Light Echo | Supports M6 |
| Vengeance | Multiplies with other % damage. Critical hits from procs add stacks | None |
| Repentance | Diminishing returns category not tested | None |
| Instrument of Law | Rank 2 makes Hammer of Wrath instant. The threat decrease multiplies with Salvation | None |
| Twist of Light | More tests are necessary. With Benediction, Seals cost ×0.72 | None |

## Spells

| Spell | Result in the beta | Source |
| --- | --- | --- |
| Holy Strike | Uses normalized weapon damage. The Holy part uses 0.429 × weapon %: 21.45% of spell power at rank 8. Does not trigger Seal of Fury, Righteousness or Command. Triggers Seal of Light, Justice and Wisdom | Player tests |
| Seal of Fury | 35 Holy damage + 10% of spell power for each hit (rank 7). Improved Seals multiplies the full hit: 40.25 + 11.5% of spell power. No Attack Power. Critical hit: ×2 damage, with a separate roll. Cannot miss | Player tests; game files (flat 35, spell 20418) |
| Seal of Righteousness | 10% of spell power with a one-handed weapon, 12% with a two-handed weapon. Weapon speed has no effect | Player tests; patch note, 16 October |
| Seal of Command | 29% × 70% weapon damage = 20.3% of spell power. 7 procs each minute. Uses the melee hit table | Player tests |
| Judgement of Fury, Righteousness and Command | 42.9% of spell power. Melee hit table. Critical hit: ×2 damage. Judgement of Command: ×2 damage against a stunned target | Player tests; patch note, 16 October |
| Judgement of Fury | The damage hits before the taunt. The taunt copies the top threat. The threat from the damage is not added. The taunt does not remove Judgement of the Crusader | Player tests |
| Judgement of the Crusader | The bonus uses the coefficient of each spell, as spell power does. Seal of Command receives the full 29% | Player tests |
| Consecration | 0.042 of spell power for each tick (33.6% for each target). First 4 enemies only. Ticks can be critical hits (×1.5) | Patch note, 16 October; player tests |
| Retribution Aura | 6% of spell power | Patch note, 8 October |
| Holy Shield | The spell power coefficient is not known. Classic: 5% for each block | Classic data |
| Mana return | Mana from Shield Specialization, Improved Seal of Fury and Sanctified Judgement gives no threat | Patch notes, 8 and 16 October |
| Rage | Rage from damage taken was repaired on 8 October. It uses 20–40% armor, related to level. Critical hits give ×2 rage. Bear Form: ×1.5 threat | Patch note, 8 October |
| Lay on Hands | Heals for your maximum health. Drains all your current mana. The drain does not stop mana regeneration. 20 min cooldown (Classic: 1 hour). Ranks 2 and 3 restore 250 and 550 mana to the target | Forever spellbook (client data); player tests |
