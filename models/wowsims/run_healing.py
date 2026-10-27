"""Holy Paladin and Holy Priest, one spell rotation each (Analysis, Healing, part 9). Run: python3 run_healing.py

The heal targets the caster. The sim has no overheal model, so the result is raw healing per mana."""
from concurrent.futures import ThreadPoolExecutor
from wowsims import *
from builds import *

N = 1000
HL, FOL, GH, FH = 25292, 19943, 25314, 10917
INFUSION, ILLUMINATION, LINGERING = 437063, 20210, 1999001

def cast(s, cond=None):
    a = {"action": {"castSpell": {"spellId": {"spellId": s}, "target": {"type": "Self"}}}}
    if cond: a["action"]["condition"] = cond
    return a
aura = lambda i: {"auraIsActive": {"auraId": {"spellId": i}}}
casting = lambda i: {"spellIsCasting": {"spellId": {"spellId": i}}}
NOT = lambda v: {"not": {"val": v}}
ROT = {
    "Holy Light": [cast(HL)],
    "Flash of Light": [cast(FOL)],
    # Flash of Light only without Infusion: at low mana the plan waits for the Holy Light mana.
    "FoL, HL on Infusion": [cast(HL, {"and": {"vals": [aura(INFUSION), NOT(casting(HL))]}}), cast(FOL, NOT(aura(INFUSION)))],
    # The APL picks the next spell before the cast ends, so "HL after each FoL" looks at the FoL cast.
    "FoL then HL": [cast(HL, {"or": {"vals": [casting(FOL), {"and": {"vals": [aura(INFUSION), NOT(casting(HL))]}}]}}),
                    cast(FOL, {"and": {"vals": [NOT(aura(INFUSION)), NOT(casting(FOL))]}})],
    "Greater Heal": [cast(GH)],
    "Flash Heal": [cast(FH)],
}
PALADIN_GEAR = "paladin/holy/gear_sets/default"
PRIEST_GEAR = "priest/healer/gear_sets/preraid"

def buffs(bol=True):
    b = copy.deepcopy(load(REF)["buffs"])
    if not bol: b.pop("greaterBlessingOfLight", None)
    return b

def paladin(t, rot, bol=True):
    return {"name": "Player", "race": "RaceHuman", "class": "ClassPaladin", "equipment": gear(PALADIN_GEAR),
            "talentsString": t, "holyPaladin": {"options": {"classOptions": {}}},
            "rotation": {"type": "TypeAPL", "priorityList": ROT[rot]}, "consumables": {}, "buffs": buffs(bol)}

def priest(rot, gearpath):
    return {"name": "Player", "race": "RaceHuman", "class": "ClassPriest", "equipment": gear(gearpath),
            "talentsString": PRIEST, "healerPriest": {"options": {"classOptions": {}}},
            "rotation": {"type": "TypeAPL", "priorityList": ROT[rot]}, "consumables": {}, "buffs": buffs()}

def heal_sim(p, flags="", dur=180, iters=N):
    rq = request(p, "raid", iters=iters, dur=dur)
    rq["raid"]["parties"][0]["players"][0]["buffs"] = p["buffs"]   # request() puts the raid buffs back
    return sim(rq, flags)

def spell_stats(o, iters=N):
    """Healing per mana, with and without the mana that Illumination returns, and the Lingering Light share."""
    m = player_metrics(o); mana, heal = {}, {}
    for r in m["resources"]:
        if r["type"] == "ResourceTypeMana" and r["id"].get("spellId"):
            mana[r["id"]["spellId"]] = r["gain"]
    for a in m["actions"]:
        h = sum(t.get("healing", 0) for t in a["targets"])
        if h > 0: heal[a["id"].get("spellId")] = h
    spent = -sum(v for v in mana.values() if v < 0); total = sum(heal.values())
    return dict(hpm=total / spent, net_hpm=total / (spent - mana.get(ILLUMINATION, 0)),
                ll=heal.get(LINGERING, 0) / total, hps=m["hps"]["avg"], oom=m.get("secondsOomAvg", 0),
                mana=spent / iters)

CASES = []
for r in ("Holy Light", "Flash of Light", "FoL, HL on Infusion"):
    CASES += [("Paladin beta, Blessing of Light", r, paladin(HOLY_BETA, r, True), "BOL"),
              ("Paladin beta, no Blessing of Light", r, paladin(HOLY_BETA, r, False), ""),
              ("Paladin proposed", r, paladin(HOLY_PROP_TALENTS, r, False), HOLY_PROP)]
CASES.append(("Paladin proposed", "FoL then HL", paladin(HOLY_PROP_TALENTS, "FoL then HL", False), HOLY_PROP))
for r in ("Greater Heal", "Flash Heal"):
    CASES += [("Priest (Paladin gear)", r, priest(r, PALADIN_GEAR), ""),
              ("Priest (own pre-raid gear)", r, priest(r, PRIEST_GEAR), "")]

def run():
    return {(l, r): spell_stats(heal_sim(p, f)) for l, r, p, f in CASES}

if __name__ == "__main__":
    res = dict(ThreadPoolExecutor(4).map(lambda c: ((c[0], c[1]), spell_stats(heal_sim(c[2], c[3]))), CASES))
    print("| Healer | Rotation | HPS | Healing per mana | Net of Illumination | Lingering Light share | Time out of mana |")
    print("| --- | --- | --- | --- | --- | --- | --- |")
    for (l, r), s in res.items():
        print(f"| {l} | {r} | {s['hps']:.0f} | {s['hpm']:.2f} | {s['net_hpm']:.2f} | {s['ll']:.1%} | {s['oom']:.0f} sec |")
