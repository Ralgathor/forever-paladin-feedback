"""Shared code for the wowsims runs: request builder, CLI call with a cache, metrics.

Run setup.sh first. WOWSIMS_WORK sets the work folder (default: models/wowsims/.work)."""
import copy, hashlib, json, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.environ.get("WOWSIMS_WORK", os.path.join(HERE, ".work"))
CLI = os.path.join(WORK, "wowsimcli")
DUMP = os.path.join(WORK, "dump")
SPECS = os.path.join(WORK, "forever", "ui", "specs")
CACHE = os.path.join(WORK, "out")

PROT = json.load(open(os.path.join(HERE, "data", "julien_prot.json")))
REF = "ClassPaladin__default__default__default__Default"   # the Retribution preset gives the common raid buffs
IMBUES = ("mhImbueId", "ohImbueId", "mhWeaponImbueId", "ohWeaponImbueId")

def load(name):
    """A dumped preset player. name: file name without .player.json, with the sub folder if any."""
    return json.load(open(os.path.join(DUMP, name + ".player.json")))

def gear(path):
    """A wowsims gear set, for example "warrior/dps/gear_sets/prebis_fury"."""
    return json.load(open(os.path.join(SPECS, path + ".gear.json")))

# Epic shields: wowsims takes shield block from a game table by item level, and that table is about 32% too
# high for Forever. These are the Wowhead Forever values (block + block value). Other items already match.
WOWHEAD_BV = {21269: 70, 19321: 66, 21610: 57, 18825: 55, 18826: 55, 22198: 48, 18168: 44,
              272591: 44, 272838: 44, 278468: 44, 278469: 44, 279262: 44}
FAKE_ID = 9000000
_DB = None

def wowhead_shields(p):
    """Swaps each epic shield for a copy with the Wowhead block value. The sim does not replace an item
    it already has, so the copy takes a new id. These shields have no item effects to lose."""
    global _DB
    items = p.get("equipment", {}).get("items", [])
    new = []
    for e in items:
        if e.get("id") in WOWHEAD_BV:
            if _DB is None:
                _DB = {i["id"]: i for i in json.load(open(os.path.join(WORK, "forever", "assets", "database", "db.json")))["items"]}
            it = copy.deepcopy(_DB[e["id"]]); it["id"] = FAKE_ID + e["id"]
            for so in it["scalingOptions"].values():
                so["stats"]["24"] = WOWHEAD_BV[e["id"]]
            new.append(it); e["id"] = it["id"]
    if new:
        p["database"] = {"items": new}

LEGACY = {i["id"]: i for i in json.load(open(os.path.join(HERE, "data", "legacy_items.json")))["items"]}
_IDS = None

def legacy_items(p):
    """Items of the saved gear sets that left the wowsims item list (data/legacy_items.json).
    The request gives their old values to the sim."""
    global _IDS
    if _IDS is None:
        _IDS = {i["id"] for i in json.load(open(os.path.join(WORK, "forever", "assets", "database", "db.json")))["items"]}
    add = [copy.deepcopy(LEGACY[e["id"]]) for e in p.get("equipment", {}).get("items", [])
           if e.get("id") in LEGACY and e["id"] not in _IDS]
    if add:
        p.setdefault("database", {}).setdefault("items", []).extend(add)

def julien():
    return copy.deepcopy(PROT["raid"]["parties"][0]["players"][0])

def request(player, scen="raid", tank=False, iters=3000, dur=180, keep_buffs=False, wowhead=False):
    """scen: "raid" (same raid buffs for all, preset consumables), "raid_nocons" (weapon oils and
    poisons only) or "solo" (no buffs, no debuffs, no consumables). wowhead: Wowhead shield values."""
    ref_raid = json.load(open(os.path.join(DUMP, REF + ".raid.json")))
    ref_ind = load(REF)["buffs"]
    p = copy.deepcopy(player); p["name"] = "Player"
    if wowhead:
        wowhead_shields(p)
    legacy_items(p)
    raid = {"parties": [{"players": [p]}], "numActiveParties": 1}
    if scen in ("raid", "raid_nocons"):
        raid["buffs"] = ref_raid["buffs"]; raid["debuffs"] = ref_raid["debuffs"]
        raid["parties"][0]["buffs"] = ref_raid["parties"][0]["buffs"]
        if not tank and not keep_buffs:
            p["buffs"] = ref_ind
    else:
        raid["buffs"] = {}; raid["debuffs"] = {}; p["buffs"] = {}
    if scen in ("raid_nocons", "solo"):
        p["consumables"] = {k: v for k, v in p.get("consumables", {}).items() if k in IMBUES}
    enc = copy.deepcopy(PROT["encounter"]); enc["duration"] = dur
    if tank:
        raid["tanks"] = [{"type": "Player", "index": 0}]
        p["inFrontOfTarget"] = True
        p.setdefault("healingModel", PROT["raid"]["parties"][0]["players"][0]["healingModel"])
    else:
        t = enc["targets"][0]; t["minBaseDamage"] = 0; t.pop("canCrush", None)
    return {"raid": raid, "encounter": enc, "simOptions": {"iterations": iters, "randomSeed": "101"}}

# Ability threat of the other tanks (tank_threat.patch). wowsims gives these abilities threat for the damage only.
# Druid: player data (Analysis, Threat, part 6). Warrior: the Shield Slam value is not known, x2.25 is a test case.
DRUID_THREAT = {"DRU_MAUL": "1.75", "DRU_SWIPE": "1.75", "DRU_PB": "3", "DRU_FF": "120"}
SHIELD_SLAM_225 = {"WAR_SS": "2.25"}

def sim(req, flags="", env=None):
    """Runs the CLI. flags: the PROPOSE list (see README.md). env: threat values of tank_threat.patch.
    Results are cached by request, flags and env."""
    env = env or {}
    key = hashlib.md5((json.dumps(req, sort_keys=True) + "|" + flags + ("|" + json.dumps(env, sort_keys=True) if env else "")).encode()).hexdigest()[:16]
    os.makedirs(CACHE, exist_ok=True)
    fi, fo = os.path.join(CACHE, key + ".in.json"), os.path.join(CACHE, key + ".out.json")
    if not os.path.exists(fo) or os.path.getsize(fo) == 0:
        json.dump(req, open(fi, "w"))
        r = subprocess.run([CLI, "sim", "--infile", fi, "--outfile", fo],
                           env=dict(os.environ, PROPOSE=flags, **env), capture_output=True, text=True)
        if not os.path.exists(fo):
            raise RuntimeError(f"wowsimcli gave no result (run setup.sh first?): {r.stderr[-400:]}")
    o = json.load(open(fo))
    if o.get("error"):
        raise RuntimeError(o["error"].get("message", "")[:400])
    return o

def player_metrics(o):
    return o["raidMetrics"]["parties"][0]["players"][0]

def metrics(o):
    pl = player_metrics(o)
    return dict(dps=pl["dps"]["avg"], tps=pl["threat"]["avg"], hps=pl["hps"]["avg"],
                dtps=pl.get("dtps", {}).get("avg", 0), tmi=pl.get("tmi", {}).get("avg", 0),
                oom=pl.get("secondsOomAvg", 0))

def boss_swings(o):
    """Outcome of the boss swings on the tank, in %."""
    bt = o["encounterMetrics"]["targets"][0]["actions"]
    sw = max(bt, key=lambda a: sum(x.get("casts", 0) for x in a["targets"]))["targets"]
    S = lambda k: sum(x.get(k, 0) for x in sw); c = S("casts") or 1
    return {k: 100 * S(k) / c for k in ("crushes", "blocks", "dodges", "parries", "misses", "hits", "crits")}

def with_talents(p, t):
    p = copy.deepcopy(p); p["talentsString"] = t; return p
