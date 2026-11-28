"""Item pool case: each healer in a level 60 set from the item pool (24 November 2026).
Run: python3 pool_gear_b2.py (tables from pool_gear_b2.json); python3 pool_gear_b2.py --build (new sets, about 5 min).
The item database: /tmp/wowsims-forever/assets/database/db.json (wowsims Forever clone, as for opt.py).

class_gear_b2.py uses the totals of the DoubleZug profiles. Those totals are typed in the sheets, and each sheet uses
other buffs and other multipliers. This script builds the four sets from the item database with the same rules for
all, and calculates the totals with the same buffs for all.

Item pool: the rules of the matched sets (../wowsims-b2/matched_gear/opt.py, pre_raid): launch items, item level 63
or less, no raid or world boss drop, no PvP item, no Revered or Exalted reputation reward. Items with a condition
(versus undead, in an area) are not used. Armor and weapons by class. Random suffix items are not used.
Static stats only: Intellect, healing power, Spirit, critical strike rating (14 = 1%) and MP5, and the Druid idol
Mystic Mushroom (Spirit +5%) and the weapon enchant Insight (Spirit +100% for 10 sec, mean x1.20). Use effects, procs and relic effects on spells are not counted. Set bonuses: the dungeon set 3-piece (+18 healing) and 6-piece (+8 MP5).
Enchants: the enchants of the database for the slot, with a source, phase 1, no raid source and no Revered or Exalted
reputation (the rules of search_enchants_dps.py).

Totals (game files, wowsims Forever; buffs and consumables of the DoubleZug profiles):
- Intellect = (class base + gear + Arcane Intellect 31 + Mark of the Wild 16 + food 20 for Paladin and Shaman)
  x1.10 Blessing of Kings x1.10 class talent (Divine Intellect, Mental Strength, Heart of the Wild, Ancestral
  Knowledge: each 10% at 5/5 in the game files).
- Spirit = (class base + gear + Divine Spirit 40 + Mark 16 + Kreeg's Stout 25 + food 20 for Druid and Priest)
  x1.10 Kings x1.15 Dark Inspiration (Shadow Priest) x1.15 Living Spirit (Druid only).
- Healing power = gear + enchants + set bonus + Brilliant Mana Oil 30 (game files: 30 healing, 15 MP5).
- MP5 = gear + enchants + set bonus + Mana Spring 25 + Blessing of Wisdom 40 + oil 15.
- Critical chance = class base (Paladin 3.5%, Priest 0.8%, Shaman 2.3%, Druid 1.8%) + Intellect / 59.9 (Priest 59.5,
  Shaman 59.2) + gear rating / 14 + 3% aura + talents as in the model (Priest 5%, Druid 4%, Shaman 10%; Paladin:
  Conviction 6% in the model).
No racial. 
Set choice: a search slot by slot (all candidates of a slot, then the next slot, until no change), and the pairs of
a one-hand weapon and an off hand (the 8 best of each), on the model value:
the mean of raid and one tank healing after overhealing in a 5 min fight. Paladin: live talents, critical heal 175%.
"""
import json, os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "healing")); sys.path.insert(0, D)
sys.path.insert(0, os.path.join(D, "..", "wowsims-b2", "matched_gear"))
import healing_model as H
from healing_model import solve
import healing_b2 as B
import light_vigil_ch7 as V

cwd = os.getcwd(); os.chdir(os.path.join(D, "..", "wowsims-b2", "matched_gear"))
import opt as P            # pool rules (loads the database from /tmp/wowsims-forever)
os.chdir(cwd)
db = P.d
INT, HEAL, SPI, CRIT, MP5S = 3, 4, 13, 18, 31
CID = {"Paladin": 2, "Priest": 5, "Shaman": 7, "Druid": 11}
ARMOR = {"Paladin": {1, 2, 3, 4}, "Priest": {1}, "Shaman": {1, 2, 3}, "Druid": {1, 2}}
# weapon types: 1 axe, 2 dagger, 3 fist, 4 mace, 5 held in off hand, 6 polearm, 7 shield, 8 staff, 9 sword
WEAP = {"Paladin": {1, 4, 5, 6, 7, 9}, "Priest": {2, 4, 5, 8}, "Shaman": {1, 2, 3, 4, 5, 7, 8}, "Druid": {2, 3, 4, 5, 8}}
RANGED = {"Paladin": {7}, "Priest": {5}, "Shaman": {8}, "Druid": {6}}   # libram, wand, totem, idol
NO_2H = {"Priest": {4}}                                                   # Priest: one-hand maces only
BASE = {"Paladin": (70, 75, 0.035, 59.9), "Priest": (120, 125, 0.008, 59.5),
        "Shaman": (87, 100, 0.023, 59.2), "Druid": (100, 110, 0.018, 59.9)}     # Int, Spirit, crit, Int for 1% crit
TAL_CRIT = {"Paladin": 0.0, "Priest": 0.05, "Shaman": 0.10, "Druid": 0.04}
FOOD_INT = {"Paladin", "Shaman"}
DUNGEON_SETS = {182, 185, 187, 188}     # Devout, Wildheart, The Elements, Lightforge
SLOTS = ["Head", "Neck", "Shoulder", "Back", "Chest", "Wrist", "Hands", "Waist", "Legs", "Feet",
         "Finger 1", "Finger 2", "Trinket 1", "Trinket 2", "Main hand", "Off hand", "Relic"]

def ok(it, c):
    ca = it.get("classAllowlist")
    if ca and CID[c] not in ca: return False
    if it.get("mobTypes") or it.get("areaTypes"): return False
    t = it.get("type")
    if t in (1, 3, 5, 6, 7, 8, 9, 10) and it.get("armorType") not in ARMOR[c]: return False
    if t == 13:
        if it.get("weaponType") not in WEAP[c]: return False
        if it.get("handType") == 4 and it.get("weaponType") in NO_2H.get(c, ()): return False
    if t == 14 and it.get("rangedWeaponType") not in RANGED[c]: return False
    return True

def stats(it): return {k: v for k, v in P.st(it).items() if k in (INT, HEAL, SPI, CRIT, MP5S)}

def fits(it, s):
    t = it.get("type")
    if t != P.SLOT_TYPE[s]: return False
    if s == 14: return it.get("handType") in (1, 2, 4) and it.get("weaponType") not in (5, 7)
    if s == 15: return it.get("handType") == 3 or it.get("weaponType") in (5, 7)
    return True

SPI_MULT = {249396: 1.05}     # Mystic Mushroom (Druid idol, crafted): Spirit +5% (game files)
# Enchant Weapon - Insight (vendor): a spell cast has a 35% chance to give Spirit +100% for 10 sec, 45 sec cooldown
# (game files). Mean uptime about 20%: 10 sec of each 45 + 5 sec. The model uses the mean: Spirit x1.20.
SPI_ENCH = {8216: 1.20}

def pool(c):
    its = [it for it in db["items"] if P.pre_raid(it) and ok(it, c) and (stats(it) or it["id"] in SPI_MULT)]
    return {s: [it for it in its if fits(it, s)] for s in range(17)}

def legal_ench(e):
    srcs = e.get("sources") or []
    if any("drop" in s and s["drop"].get("zoneId") in P.RAID_ZONES for s in srcs): return False
    if any("rep" in s and s["rep"].get("repLevel", 0) >= 6 for s in srcs): return False
    return bool(srcs) and e.get("phase", 1) < 2

def ench_for(s, it):
    if it is None: return [None]
    out = [None]
    for e in db["enchants"]:
        if not legal_ench(e): continue
        es = {i: v for i, v in enumerate(e.get("stats", [])) if v and i in (INT, HEAL, SPI, CRIT, MP5S)}
        if not es and e["effectId"] not in SPI_ENCH: continue
        types = [e.get("type")] + e.get("extraTypes", [])
        if P.SLOT_TYPE[s] not in types: continue
        if s in (14, 15):
            et, ht, wt = e.get("enchantType", 0), it.get("handType"), it.get("weaponType")
            if wt == 7: ok_e = et == 2
            elif wt == 5: ok_e = et == 5
            elif et == 1: ok_e = ht == 4
            else: ok_e = et == 0
            if not ok_e: continue
        if s == 16: continue
        out.append(dict(e, st=es))
    return out

def totals(c, gear, ench):
    g = {}
    for it in gear:
        if it is None: continue
        for k, v in stats(it).items(): g[k] = g.get(k, 0) + v
    for e in ench:
        if e is None: continue
        for k, v in e["st"].items(): g[k] = g.get(k, 0) + v
    sets = {}
    for it in gear:
        if it is not None and it.get("setId") in DUNGEON_SETS: sets[it["setId"]] = sets.get(it["setId"], 0) + 1
    n = max(sets.values(), default=0)
    hp = g.get(HEAL, 0) + (18 if n >= 3 else 0) + 30
    mp5 = g.get(MP5S, 0) + (8 if n >= 6 else 0) + 25 + 40 + 15
    bi, bs, bc, ipc = BASE[c]
    intel = (bi + g.get(INT, 0) + 31 + 16 + (20 if c in FOOD_INT else 0)) * 1.1 * 1.1
    spi = (bs + g.get(SPI, 0) + 40 + 16 + 25 + (0 if c in FOOD_INT else 20)) * 1.1 * 1.15 * (1.15 if c == "Druid" else 1)
    for it in gear:
        if it is not None: spi *= SPI_MULT.get(it["id"], 1.0)
    for e in ench:
        if e is not None: spi *= SPI_ENCH.get(e["effectId"], 1.0)
    crit = bc + intel/ipc/100 + g.get(CRIT, 0)/14/100 + 0.03 + TAL_CRIT[c]
    return dict(hp=hp, intel=intel, spi=spi, crit=crit, mp5=mp5, gear_hp=g.get(HEAL, 0), gear_int=g.get(INT, 0),
                gear_spi=g.get(SPI, 0), gear_crit=g.get(CRIT, 0), gear_mp5=g.get(MP5S, 0), set_n=n)

ORIG = B.paladin_b2

def oath30(hp, tank=False, oath=None, bonus=0.75, **kw):
    """Oath of Light 30% (C-H8): +30% on Holy Light, Flash of Light and Holy Shock on the Oath target, in place of
    the flat values (as oath_light_ch8.py, with the gear arguments)."""
    if oath is None: oath = tank
    if not oath: return ORIG(hp, tank, oath, bonus, **kw)
    kw["boundless"] = 0.0
    k = ORIG(hp, tank, False, bonus, **kw)
    sp = {s.name: s for s in k["spells"]}
    for n in ("Divine Favor + Holy Light", "Holy Shock", "Flash of Light", "Holy Light"):
        sp[n].raw *= 1.30; sp[n].eff *= 1.30
    f, h, c = sp["Flash of Light"], sp["Holy Light"], k["crit"]
    combo = sp["Flash of Light, Holy Light on Infusion"]
    combo.raw = f.raw + c*h.raw; combo.eff = f.eff + c*h.eff
    return k

def model(c, t, tank, case="Live", bonus=0.75):
    if c == "Paladin":
        g = dict(spi=t["spi"], intel=t["intel"], crit=t["crit"])
        if case == "Live": return B.paladin_b2(t["hp"], tank, bonus=bonus, **g)
        if case == "C-H7": return V.ch7(t["hp"], tank, bonus=bonus, **g)
        if case == "C-H8":
            B.paladin_b2 = oath30
            try: return V.ch7(t["hp"], tank, bonus=bonus, rev=0.50, **g)
            finally: B.paladin_b2 = ORIG
        return V.ch7(t["hp"], tank, bonus=bonus, rev=0.50, **g)
    g = dict(spi=t["spi"], intel=t["intel"], crit=t["crit"])
    if c == "Druid": return H.druid(t["hp"], tank=tank, **g)
    if c == "Priest": return H.priest(t["hp"], tank=tank, **g)
    return H.shaman(t["hp"], tank=tank, T=TT, **g)

TT = 300
def hps(c, t, T, tank, **kw):
    global TT
    old = H.MP5; H.MP5 = t["mp5"]; TT = T
    try: return solve(model(c, t, tank, **kw), T, tank)["eff"]
    finally: H.MP5 = old

def value(c, gear, ench):
    t = totals(c, gear, ench)
    return 0.5*(hps(c, t, 300, False) + hps(c, t, 300, True))

def build(c):
    pl = pool(c)
    gear = [None]*17; ench = [None]*17
    def val(): return value(c, gear, ench)
    best = val()
    for p in range(6):
        changed = False
        for s in range(17):
            if s == 15 and gear[14] is not None and gear[14].get("handType") == 4: continue
            used = {x["id"] for i, x in enumerate(gear) if x is not None and i != s}
            cands = [None] + [it for it in pl[s] if it["id"] not in used]
            cur_g, cur_e = gear[s], ench[s]
            bg, be, bv = cur_g, cur_e, best
            for it in cands:
                gear[s] = it
                if s == 14 and it is not None and it.get("handType") == 4: off, offe, gear[15], ench[15] = gear[15], ench[15], None, None
                for e in ench_for(s, it):
                    ench[s] = e
                    v = val()
                    if v > bv + 1e-6: bg, be, bv = it, e, v
                if s == 14 and it is not None and it.get("handType") == 4: gear[15], ench[15] = off, offe
            gear[s], ench[s] = bg, be
            if s == 14 and bg is not None and bg.get("handType") == 4: gear[15] = None; ench[15] = None
            if bv > best + 1e-6: best = bv; changed = True
        # Weapons: a slot search cannot leave a two-hand weapon for a one-hand weapon and an off hand (two slots).
        # Thus also try the pairs: the 8 best one-hand weapons (with their best enchant) and the 8 best off hands.
        def wv(mh, me, oh, oe):
            g0, e0 = gear[14:16], ench[14:16]
            gear[14:16], ench[14:16] = [mh, oh], [me, oe]
            v = val(); gear[14:16], ench[14:16] = g0, e0
            return v
        used = {x["id"] for i, x in enumerate(gear) if x is not None and i not in (14, 15)}
        mhs = [it for it in pl[14] if it.get("handType") in (1, 2) and it["id"] not in used]
        mh_r = sorted(((max(wv(x, e, None, None) for e in ench_for(14, x)), x) for x in mhs), key=lambda z: -z[0])[:8]
        oh_r = sorted(((max(wv(None, None, y, e) for e in ench_for(15, y)), y) for y in pl[15] if y["id"] not in used),
                      key=lambda z: -z[0])[:8]
        for _, x in mh_r:
            for e in ench_for(14, x):
                for _, y in oh_r:
                    for f in ench_for(15, y):
                        v = wv(x, e, y, f)
                        if v > best + 1e-6:
                            best = v; gear[14:16], ench[14:16] = [x, y], [e, f]; changed = True
        if not changed: break
    return gear, ench, best

TS = (180, 300, 600)
CASES = (("Live", "Live"), ("Light's Vigil (C-H7)", "C-H7"), ("C-H7 + Reverence 50% (C-H1)", "C-H1"),
         ("C-H7 + C-H1 + Oath of Light 30% (C-H8)", "C-H8"))

def tables(T_):
    O = {(T, t): {c: hps(c, T_[c], T, t) for c in ("Druid", "Priest", "Shaman")} for T in TS for t in (False, True)}
    for tank in (False, True):
        print(f"## {'One tank' if tank else 'Raid'}, item pool sets: HPS after overhealing, 3 | 5 | 10 min")
        for n in ("Druid", "Priest", "Shaman"):
            print(f"  {n:40s} " + " | ".join(f"{O[(T, tank)][n]:5.0f}" for T in TS))
        for b, bl in ((0.75, "175%"), (1.25, "225%")):
            for n, case in CASES:
                v = {T: hps("Paladin", T_["Paladin"], T, tank, case=case, bonus=b) for T in TS}
                print(f"  Paladin, {n}, {bl}".ljust(42) + " | ".join(
                    f"{v[T]:4.0f} (Dru {v[T]/O[(T, tank)]['Druid']-1:+.0%}, Pri {v[T]/O[(T, tank)]['Priest']-1:+.0%}, "
                    f"Sha {v[T]/O[(T, tank)]['Shaman']-1:+.0%})" for T in TS))

if __name__ == "__main__":
    J = os.path.join(D, "pool_gear_b2.json")
    if "--build" in sys.argv or not os.path.exists(J):
        out = {}
        for c in ("Paladin", "Druid", "Priest", "Shaman"):
            gear, ench, v = build(c)
            t = totals(c, gear, ench)
            out[c] = dict(items=[dict(slot=SLOTS[s], item=g["name"], id=g["id"], stats=stats(g),
                                      enchant=e["name"] if e else None) for s, (g, e) in enumerate(zip(gear, ench)) if g],
                          totals=t)
        json.dump(out, open(J, "w"), indent=1)
    out = json.load(open(J))
    for c, o in out.items():
        print(f"## {c} set")
        for x in o["items"]:
            print(f"  {x['slot']:10s} {x['item']} ({x['id']})" + (f" + {x['enchant']}" if x["enchant"] else ""))
        print("  totals: " + ", ".join(f"{k} {v:.4g}" for k, v in o["totals"].items()))
    tables({c: o["totals"] for c, o in out.items()})
