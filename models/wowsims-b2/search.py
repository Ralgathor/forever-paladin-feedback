"""Talent search in wowsims Forever for builds/ (trees of 30 October 2026).

Run: python3 search.py <case> [start code ...]. Needs the test binaries of run.sh in /tmp (rettest, prottest).
Cases: ret-raid, ret-fresh, shock-raid, shock-fresh, prot (beta trees), and the same with -prop (proposed trees of
calculator version 6). The shock cases use the wowsims Holy Shock set, rotation and consumables (FEEDBACK_SHOCK=1).
The trees (ranks, rows, requirements) come from trees.json: the talent data of calculator/index.html.

A hill climb: each step tests all 1-point moves to a talent with value for the spec, at 1,000 iterations (SEARCH_ITER), and keeps
the best move. It stops when no move gains more than the noise limit. The best builds then run at 3,000 iterations.
"""
import json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
TREES = json.load(open(os.path.join(HERE, "trees.json")))
BIN = {"ret": os.environ.get("RETTEST", "/tmp/rettest"), "prot": os.environ.get("PROTTEST", "/tmp/prottest")}
BIN["shock"] = BIN["ret"]
DIRS = {"ret": "sim/paladin/retribution", "prot": "sim/paladin/protection", "shock": "sim/paladin/retribution"}
WOWSIMS = os.environ.get("WOWSIMS", "/tmp/wowsims-forever")
VALUE = {
    "ret": "ds rev is pp hc dp cg hs di pre ben ij con sanj soc sa ths rep ven cotl uw".split(),
    "shock": "ds rev is pp df ill hc dp iol cg hs hp lv di pre ben ij con sanj vin soc poj sa ths rep ven cotl uw".split(),
    "prot": ("ds is rev hc di red pre sd tb ss sj irf ant hsh rec ic shs dsac def ben ij con sanj vin soc sa ths "
             "ven").split(),
}
PROP_FLAGS = {"ret": "REV50", "prot": "CP1,NOTOUGH", "shock": "REV50,CH7"}  # withdrawn on 2 November 2026: Reckoning (C-P12: RK100,RKICD4) and the Holy Strike Seal trigger (C1)
NOISE = {"ret": 2.0, "prot": 0.004, "shock": 2.0}
STEP_ITER = int(os.environ.get("SEARCH_ITER", "1000"))  # iterations of each climb step

def tree(mode):
    return TREES["prop" if mode == "prop" else "beta"]

def decode(code, mode):
    """A calculator code (no prefix) to {key: points}."""
    T = tree(mode)
    parts = code.split("-") + ["", "", ""]
    out = {}
    for i, tr in enumerate(("holy", "prot", "ret")):
        keys = [t["key"] for t in T if t["tree"] == tr]
        digits = parts[i]
        for j, k in enumerate(keys):
            out[k] = int(digits[j]) if j < len(digits) else 0
    return out

def encode(b, mode):
    T = tree(mode)
    return "-".join("".join(str(b[t["key"]]) for t in T if t["tree"] == tr).rstrip("0")
                    for tr in ("holy", "prot", "ret")).rstrip("-")

def sim_string(b, mode):
    """The sim uses the beta order. In the proposed trees, Toughness is 0 and Devoted Sacrifice has no effect."""
    bb = {t["key"]: b.get(t["key"], 0) for t in TREES["beta"]}
    return encode(bb, "beta")

def valid(b, mode):
    T = tree(mode)
    if sum(b.values()) > 51:
        return False
    for t in T:
        p = b[t["key"]]
        if p < 0 or p > t["ranks"]:
            return False
        if p == 0:
            continue
        below = sum(b[u["key"]] for u in T if u["tree"] == t["tree"] and u["tier"] < t["tier"])
        if below < (t["tier"] - 1) * 5:
            return False
        if t["req"] and b[t["req"]] < next(u["ranks"] for u in T if u["key"] == t["req"]):
            return False
    return True

HERE = os.path.dirname(os.path.abspath(__file__))
def pool_ids(spec):  # the item pool set of each spec (FEEDBACK_ITEMS); FEEDBACK_GEAR=default keeps the wowsims default set
    # TANK_SET=surv: the survival tank set (tank_gear/set_prot_surv.json) in place of the threat tank set
    f = {"ret": "matched_gear/set_Retribution.json", "prot": "tank_gear/set_prot.json", "shock": "tank_gear/set_shock.json"}[spec]
    if spec == "prot" and os.environ.get("TANK_SET") == "surv":
        f = "tank_gear/set_prot_surv.json"
    d = json.load(open(os.path.join(HERE, f)))
    ids = [x.get("id", 0) for x in d["items"]] if isinstance(d, dict) else d
    return ",".join(str(i) for i in (ids + [0] * 17)[:17])

def run(spec, case, b, mode, it=1000, extra=None):
    env = dict(os.environ, FEEDBACK_DUR="180", FEEDBACK_ITER=str(it), FEEDBACK_TALENTS=sim_string(b, mode),
               PROPOSE=PROP_FLAGS[spec] if mode == "prop" else "")
    if case == "fresh":
        env["FEEDBACK_BUFFS"] = "none"
    if spec == "shock":
        env["FEEDBACK_SHOCK"] = "1"
    if os.environ.get("FEEDBACK_GEAR") != "default":
        env["FEEDBACK_ITEMS"] = pool_ids(spec)
    env.update(extra or {})
    out = subprocess.run([BIN[spec], "-test.run", "TestFeedbackRun", "-test.v"], cwd=os.path.join(WOWSIMS, DIRS[spec]),
                         env=env, capture_output=True, text=True).stdout
    r = {}
    for line in out.splitlines():
        if line.startswith(("RESULT", "TMI")):
            for kv in line.split()[1:]:
                if "=" in kv:
                    k, v = kv.split("=", 1)
                    try:
                        r[k] = float(v.rstrip("%"))
                    except ValueError:
                        pass
    if "avg" in r:
        r["tmi"] = r.pop("avg")
    return r

def score(spec, r, ref):
    if spec in ("ret", "shock"):
        return r["dps"]
    return (0.4 * r["tps"] / ref["tps"] + 0.2 * r["dps"] / ref["dps"] + 0.2 * ref["dtps"] / r["dtps"]
            + 0.2 * ref["tmi"] / r["tmi"])

def moves(b, spec, mode):
    keys = [t["key"] for t in tree(mode)]
    for a in keys:
        if b[a] == 0:
            continue
        for c in VALUE[spec]:
            if c == a or c not in b:
                continue
            n = dict(b); n[a] -= 1; n[c] += 1
            if valid(n, mode):
                yield n

def moves2(b, spec, mode):
    """2-point moves: two points out, two points in (at least one into a talent with value)."""
    keys = [t["key"] for t in tree(mode)]
    seen = set()
    for i, a in enumerate(keys):
        for c in keys[i:]:
            if b[a] == 0 or b[c] == 0 or (c == a and b[a] < 2):
                continue
            for x in VALUE[spec]:
                if x not in b:
                    continue
                for d in keys:
                    n = dict(b); n[a] -= 1; n[c] -= 1; n[x] += 1; n[d] += 1
                    k = encode(n, mode)
                    if n != b and k not in seen and valid(n, mode):
                        seen.add(k)
                        yield n

def batch(spec, case, mode, cands, it):
    with ThreadPoolExecutor(4) as ex:
        return list(ex.map(lambda n: run(spec, case, n, mode, it=it), cands))

def climb(spec, case, mode, start, log):
    b = decode(start, mode)
    assert valid(b, mode) and sum(b.values()) == 51, start
    ref = run(spec, case, b, mode, it=STEP_ITER)
    cur = score(spec, ref, ref)
    seen = {encode(b, mode)}
    two_done = os.environ.get("SEARCH_2PT", "1") == "0"   # one 2-point round for each climb at most
    print(f"start {encode(b, mode)} {cur:.4f} {ref}", file=log, flush=True)
    while True:
        cands = [n for n in moves(b, spec, mode) if encode(n, mode) not in seen]
        seen.update(encode(n, mode) for n in cands)
        res = batch(spec, case, mode, cands, STEP_ITER)
        best = max(zip(cands, res), key=lambda x: score(spec, x[1], ref), default=None)
        if (best is None or score(spec, best[1], ref) <= cur + NOISE[spec]) and two_done:
            break
        if best is None or score(spec, best[1], ref) <= cur + NOISE[spec]:
            two_done = True
            # 2-point round: 250 iterations, then the 6 best and the current build again at 2,000
            c2 = [n for n in moves2(b, spec, mode) if encode(n, mode) not in seen]
            seen.update(encode(n, mode) for n in c2)
            print(f"  2-point round: {len(c2)} moves", file=log, flush=True)
            r2 = batch(spec, case, mode, c2, 250)
            top = [n for n, _ in sorted(zip(c2, r2), key=lambda x: -score(spec, x[1], ref))[:6]]
            rr = batch(spec, case, mode, [b] + top, 2000)
            base = score(spec, rr[0], ref)
            best = max(zip(top, rr[1:]), key=lambda x: score(spec, x[1], ref), default=None)
            if best is None or score(spec, best[1], ref) <= base + NOISE[spec]:
                break
            cur = base + 0.0
        b, cur = best[0], score(spec, best[1], ref)
        print(f"step {encode(b, mode)} {cur:.4f} {best[1]} ({len(cands)} moves)", file=log, flush=True)
    return b, ref

if __name__ == "__main__":
    case_arg = sys.argv[1]
    spec, case = ("prot", "raid") if case_arg.startswith("prot") else tuple(case_arg.split("-")[:2])
    mode = "prop" if case_arg.endswith("-prop") else "beta"
    starts = sys.argv[2:]
    with open(os.path.join(HERE, "logs", f"search_{case_arg}.log"), "a") as log:
        finals = []
        for s in starts:
            b, ref = climb(spec, case, mode, s, log)
            finals.append(b)
        for b in finals:
            r = run(spec, case, b, mode, it=3000)
            print(f"final {encode(b, mode)} {r}", file=log, flush=True)
