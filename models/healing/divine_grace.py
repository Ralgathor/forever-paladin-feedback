"""Divine Grace (C-H6): a heal from Divine Favor increases the armor from items of the target by 15/30% for 15 sec.
Value on a tank, as physical damage that the tank does not take (Analysis, Healing, part 5).
- Armor from items: the tank gear of models/wowsims (game data of wowsims Forever): 5,494 to 6,366.
- Other armor (Devotion Aura, Agility, Mark of the Wild, elixir): about 1,500. Divine Grace does not change it.
- Armor reduction against a level 63 boss: armor / (armor + 467.5*63 - 22167.5), as in Classic.
- Divine Favor each 2 min, used on the tank. Thus, the buff is up 15 of each 120 sec.
Run: python3 divine_grace.py"""

K63 = 467.5*63 - 22167.5     # 7,285
OTHER = 1500
UP = 15/120

def taken(armor): return 1 - armor/(armor + K63)

def value(items, bonus):
    """Physical damage taken: change while the buff is up, and change for the full fight."""
    base = taken(items + OTHER); buff = taken(items*(1 + bonus) + OTHER)
    d = buff/base - 1
    return d, d*UP

if __name__ == "__main__":
    print("armor from items | rank | while up | full fight (Divine Favor each 2 min)")
    for items in (5500, 6000, 6400):
        for rank, bonus in ((1, 0.15), (2, 0.30)):
            d, f = value(items, bonus)
            print(f"  {items:5d} | {rank}/2 | {d:+.1%} | {f:+.1%}")
    print("buff for 2 min (Classic Improved Lay on Hands): full fight = while up")
