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

def julien():
    return copy.deepcopy(PROT["raid"]["parties"][0]["players"][0])

def request(player, scen="raid", tank=False, iters=3000, dur=180, keep_buffs=False):
    """scen: "raid" (same raid buffs for all, preset consumables), "raid_nocons" (weapon oils and
    poisons only) or "solo" (no buffs, no debuffs, no consumables)."""
    ref_raid = json.load(open(os.path.join(DUMP, REF + ".raid.json")))
    ref_ind = load(REF)["buffs"]
    p = copy.deepcopy(player); p["name"] = "Player"
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

def sim(req, flags=""):
    """Runs the CLI. flags: the PROPOSE list (see README.md). Results are cached by request and flags."""
    key = hashlib.md5((json.dumps(req, sort_keys=True) + "|" + flags).encode()).hexdigest()[:16]
    os.makedirs(CACHE, exist_ok=True)
    fi, fo = os.path.join(CACHE, key + ".in.json"), os.path.join(CACHE, key + ".out.json")
    if not os.path.exists(fo):
        json.dump(req, open(fi, "w"))
        subprocess.run([CLI, "sim", "--infile", fi, "--outfile", fo],
                       env=dict(os.environ, PROPOSE=flags), capture_output=True)
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
