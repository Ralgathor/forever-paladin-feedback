"""Model against wowsims: the same quantity from the Python models and from the sim, and the difference.
A difference above 5% is marked "check": the Analysis tabs explain each one. Run: python3 check.py"""
import importlib.util, os, re, sys
from concurrent.futures import ThreadPoolExecutor
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for d in ("damage", "threat", "healing"):
    sys.path.insert(0, os.path.join(ROOT, d))
import damage_model as DM, threat_model as TM, healing_model as HM
_spec = importlib.util.spec_from_file_location("heal_tables", os.path.join(ROOT, "healing", "run_tables.py"))
_ht = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_ht)
HEAL_PROP, mk = _ht.PROP, _ht.mk
_spec = importlib.util.spec_from_file_location("dmg_tables", os.path.join(ROOT, "damage", "run_tables.py"))
_dt = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_dt)
import run_damage as RD, run_threat as RT, run_healing as RH
from wowsims import *
from builds import *

LIMIT = 0.05

def model_values():
    g = DM.gear(0); swap = DM.retribution(g, "beta_swap"); P = DM.retribution(g)
    t = TM.PART1.but(boss_hit=4500, bv=60)    # first check (27 October): block value 60, Holy Shield (C-P9) at 200%
    tb = TM.paladin(t, TM.TANK_REF, proposed=False, c14=0); tp = TM.paladin(t, c14=2.0); w = TM.warrior(t)
    heal = {}
    for who, f, kw in (("beta, Blessing of Light", HM.paladin, {}), ("beta, no Blessing of Light", HM.paladin, {"bol": False}),
                       ("proposed", HM.paladin, HEAL_PROP), ("Priest", HM.priest, {})):
        for s in mk(f, 382, 180, False, **kw)["spells"]:
            if s.cost > 0: heal[(who, s.name)] = s.raw / s.cost
            if who == "Priest": heal[(who, s.name, "cast")], heal[(who, s.name, "cost")] = s.raw, s.cost
    return dict(ret_gain=P / swap, ret_arms=swap / DM.arms(g), ret_fury=_dt.RET_BETA_SIM * P / swap / _dt.PURE["Warrior"],
                tps_gain=tp - tb, beta_war=tb / w, prop_war=tp / w, heal=heal)

def sim_values():
    pr, _ = RD.proposals()
    r, _ = RD.classes()
    arms = RD.P(RET, "warrior/dps/gear_sets/prebis_arms")
    same = metrics(sim(request(arms, "raid")))["dps"] / r[("Arms Warrior (prebis gear)", "raid")]["dps"]
    t = RT.run()
    beta, prop, war = (t[k]["tps"] for k in (("Paladin beta (Julien)", "Julien gear", "raid"),
                                              ("All proposals", "Julien gear", "raid"), ("Warrior", "", "raid")))
    h = dict(ThreadPoolExecutor(4).map(lambda c: ((c[0], c[1]), RH.spell_stats(RH.heal_sim(c[2], c[3]))), RH.CASES))
    for sid, name in ((RH.GH, "Greater Heal"), (RH.FH, "Flash Heal")):
        m = player_metrics(RH.heal_sim(RH.priest(name, RH.PALADIN_GEAR)))
        casts = sum(t.get("casts", 0) for a in m["actions"] if a["id"].get("spellId") == sid for t in a["targets"])
        heal_ = sum(t.get("healing", 0) for a in m["actions"] if a["id"].get("spellId") == sid for t in a["targets"])
        mana = -sum(r["gain"] for r in m["resources"] if r["id"].get("spellId") == sid and r["gain"] < 0)
        h[("Priest", name, "cast")], h[("Priest", name, "cost")] = heal_ / casts, mana / casts
    return dict(ret_gain=pr[("All", "raid")]["dps"] / pr[("RB1, no proposals", "raid")]["dps"], ret_arms=same,
                ret_fury=r[("Retribution, proposed (RB1)", "raid")]["dps"] / r[("Fury Warrior (prebis gear)", "raid")]["dps"],
                tps_gain=prop - beta, beta_war=beta / war, prop_war=prop / war, heal=h)

# Threat with the same inputs: the model gets the stats of Julien's sim (beta talents, Consecration, Retribution
# Aura). Spell power and Attack Power come from the first Judgement of Fury in the sim debug log, the critical hit chance from the auto attacks
# of the sim (after the boss decrease). Weapon (35.3 DPS, 1.5 sec), block value (36 x 1.3) and hit (6%): the
# wowsims stat sheet of the same request (ComputeStats, read one time). Curse of the Elements (+10% Holy damage taken, in the raid debuffs of
# the sim) is not in the model: the table shows it apart.
JULIEN_TAL = {"is": 3, "prec": 3, "red": 5, "sj": 1, "ohws": 3, "reck": 5, "ic": 5, "hsh": 1, "ij": 2}
SIM_SOURCES = {"Seal of Fury": [20418], "Judgement of Fury": [20414], "Consecration": [20924], "Holy Shield": [20928],
               "Holy Strike": [10333], "Auto attacks and Reckoning": ["attack1"], "Retribution Aura": [10301]}

def threat_same_inputs():
    rq = request(julien(), "raid", tank=True, iters=1, dur=60); rq["simOptions"]["debug"] = True
    log = sim(rq)["logs"]
    ap, sp = (float(x) for x in re.search(r"\{SpellID: 20414\} \[DEBUG\] MAP: ([\d.]+), RAP: [\d.]+, SP: ([\d.]+)", log).groups())
    iters, dur = 3000, 180
    m = player_metrics(sim(request(julien(), "raid", tank=True, iters=iters, dur=dur)))
    def S(key, k):
        a = [x for x in m["actions"] if (x["id"].get("spellId") == key or
             (key == "attack1" and x["id"].get("otherId") == "OtherActionAttack"))]
        return sum(t.get(k, 0) for x in a for t in x["targets"])
    crit = S("attack1", "crits") / (S("attack1", "hits") + S("attack1", "crits")) + TM.CRIT_SUPP
    g = TM.PART1.but(sp=sp, ap=ap, wdps=35.3, wspeed=1.5, bv=36 * 1.3, hit=0.06, crit=crit)
    _, src = TM.paladin(g, JULIEN_TAL, proposed=False, c14=0, consecration=True, ret_aura=True, detail=True)
    model = {"Seal of Fury": src["Seal of Fury"], "Judgement of Fury": src["Judgement of Fury"],
             "Consecration": src["Consecration"], "Holy Shield": src["Holy Shield, base"] + src["Holy Shield, block value"],
             "Holy Strike": src["Holy Strike"], "Auto attacks and Reckoning": src["Auto attacks"] + src["Reckoning attacks"],
             "Retribution Aura": src["Retribution Aura"]}
    simv = {k: sum(S(i, "threat") for i in ids) / iters / dur for k, ids in SIM_SOURCES.items()}
    coe = {k: 1.0 if k == "Auto attacks and Reckoning" else 1.1 for k in model}
    return [(k, model[k], model[k] * coe[k], simv[k]) for k in model], dict(sp=sp, ap=ap, crit=crit)

HEAL_ROWS = [  # (label, model key, wowsims key)
    ("Beta, Holy Light, Blessing of Light", ("beta, Blessing of Light", "Holy Light"), ("Paladin beta, Blessing of Light", "Holy Light")),
    ("Beta, Flash of Light, Blessing of Light", ("beta, Blessing of Light", "Flash of Light"), ("Paladin beta, Blessing of Light", "Flash of Light")),
    ("Beta, Holy Light, no Blessing of Light", ("beta, no Blessing of Light", "Holy Light"), ("Paladin beta, no Blessing of Light", "Holy Light")),
    ("Beta, Flash of Light, no Blessing of Light", ("beta, no Blessing of Light", "Flash of Light"), ("Paladin beta, no Blessing of Light", "Flash of Light")),
    ("Beta, Flash of Light and Holy Light on Infusion, no Blessing of Light", ("beta, no Blessing of Light", "Flash of Light, Holy Light on Infusion"),
     ("Paladin beta, no Blessing of Light", "FoL, HL on Infusion")),
    ("Proposed, Holy Light", ("proposed", "Holy Light"), ("Paladin proposed", "Holy Light")),
    ("Proposed, Flash of Light", ("proposed", "Flash of Light"), ("Paladin proposed", "Flash of Light")),
    ("Proposed, Flash of Light then Holy Light", ("proposed", "Flash of Light, Holy Light on Infusion"), ("Paladin proposed", "FoL then HL")),
    ("Priest, Greater Heal (Paladin gear)", ("Priest", "Greater Heal"), ("Priest (Paladin gear)", "Greater Heal")),
    ("Priest, Flash Heal (Paladin gear)", ("Priest", "Flash Heal"), ("Priest (Paladin gear)", "Flash Heal")),
]

def rows(m, s):
    out = [("Damage", "Retribution, all proposals against the beta (same talents)", m["ret_gain"], s["ret_gain"], "ratio"),
           ("Damage", "Beta Retribution against Arms, same gear", m["ret_arms"], s["ret_arms"], "ratio"),
           ("Damage", "Retribution, all proposals, as a % of Fury (model: MythicSim ratio, part 5)", m["ret_fury"], s["ret_fury"], "ratio"),
           ("Threat", "Proposals, TPS added to the beta Paladin", m["tps_gain"], s["tps_gain"], "tps"),
           ("Threat", "Beta Paladin as a % of the Warrior", m["beta_war"], s["beta_war"], "ratio"),
           ("Threat", "Proposed Paladin as a % of the Warrior", m["prop_war"], s["prop_war"], "ratio")]
    out += [("Healing", "Healing per mana: " + l, m["heal"][mk_], s["heal"][sk]["net_hpm"], "hpm") for l, mk_, sk in HEAL_ROWS]
    for name in ("Greater Heal", "Flash Heal"):
        out += [("Healing", f"Priest, {name}: healing per cast", m["heal"][("Priest", name, "cast")], s["heal"][("Priest", name, "cast")], "int"),
                ("Healing", f"Priest, {name}: mana per cast", m["heal"][("Priest", name, "cost")], s["heal"][("Priest", name, "cost")], "int")]
    return out

def fmt(v, kind):
    return {"ratio": f"{v:.0%}", "tps": f"{v:+.0f}", "hpm": f"{v:.2f}", "int": f"{v:,.0f}"}[kind]

if __name__ == "__main__":
    m, s = model_values(), sim_values()
    print("| Tab | Value | Model | wowsims | Difference | |\n| --- | --- | --- | --- | --- | --- |")
    for tab, label, a, b, kind in rows(m, s):
        d = b / a - 1
        print(f"| {tab} | {label} | {fmt(a, kind)} | {fmt(b, kind)} | {d:+.1%} | {'check' if abs(d) > LIMIT else 'OK'} |")
    rows_t, inp = threat_same_inputs()
    print(f"\nThreat with the same inputs (spell power {inp['sp']:.0f}, Attack Power {inp['ap']:.0f}, "
          f"critical hit {inp['crit']:.1%} before the boss decrease)")
    print("| Source | Model | Model, Curse of the Elements | wowsims | Difference |\n| --- | --- | --- | --- | --- |")
    for k, a, a2, b in rows_t + [("Total", *(sum(r[i] for r in rows_t) for i in (1, 2, 3)))]:
        print(f"| {k} | {a:.0f} | {a2:.0f} | {b:.0f} | {b / a2 - 1:+.1%} |")
