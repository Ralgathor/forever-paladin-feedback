"""builds/level-up.md: a greedy talent order from level 10 to 60 on the beta trees of 30 October 2026.

Run: python3 levelup.py [full|half]. Needs the Retribution test binary with TestFeedbackLevelUp (RETTEST, default
/tmp/rettest). Each level adds the 1 point that gives the shortest time for each kill:
  kill = 5,000 health / DPS, rest = the longer of mana / 120 per sec and damage taken / 80 per sec,
  travel = 10 sec / (1 + 7.5% for each point of Pursuit of Justice).
full: the enemy hits for 400 (health limits the rest). half: 200 (mana limits the rest more often).
"""
import os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
import search as S

BIN = os.environ.get("RETTEST", "/tmp/rettest")
HIT = {"full": "400", "half": "200"}

def run(b, hit):
    env = dict(os.environ, FEEDBACK_LEVELUP="1", FEEDBACK_ITER="1000", FEEDBACK_HIT=hit,
               FEEDBACK_TALENTS=S.encode(b, "beta") or "-")
    out = subprocess.run([BIN, "-test.run", "TestFeedbackLevelUp", "-test.v"], env=env, capture_output=True, text=True,
                         cwd=os.path.join(S.WOWSIMS, S.DIRS["ret"])).stdout
    line = next(l for l in out.splitlines() if l.startswith("LEVELUP"))
    r = {k: float(v) for k, v in (kv.split("=") for kv in line.split()[1:])}
    kill = 5000 / r["dps"]
    rest = max(r["mps"] * kill / 120, r["dtps"] * kill / 80)
    travel = 10 / (1 + 0.075 * b["poj"])
    r.update(kill=kill, rest=rest, total=kill + rest + travel)
    return r

def valid_partial(b):
    return S.valid(b, "beta")

def ordered(target, log):
    """The order of the points of one level 60 build: each level adds the point of that build with the shortest
    average time for each kill of the two cases."""
    keys = [t["key"] for t in S.TREES["beta"]]
    tb = S.decode(target, "beta")
    b = {k: 0 for k in keys}
    for level in range(10, 61):
        cands = [(k, dict(b, **{k: b[k] + 1})) for k in keys if b[k] < tb[k]]
        cands = [c for c in cands if valid_partial(c[1])]
        def both(n):
            return run(n, "200"), run(n, "400")
        with ThreadPoolExecutor(2) as ex:
            res = list(ex.map(lambda c: both(c[1]), cands))
        (k, n), (h, f) = min(zip(cands, res), key=lambda x: x[1][0]["total"] + x[1][1]["total"])
        b = n
        print(f"level {level} {k} {b[k]} {S.encode(b, 'beta')} half={h['total']:.2f} full={f['total']:.2f} "
              f"dps={h['dps']:.1f}", file=log, flush=True)

def beam(target, log, width=8):
    """Beam search for the order of the points of one level 60 build. Score of a path: the sum over levels 10-60 of
    level x (time for each kill, half case + full case) / 2. The weight gives more value to the slow, high levels."""
    keys = [t["key"] for t in S.TREES["beta"]]
    tb = S.decode(target, "beta")
    cache = {}
    def both(n):
        c = S.encode(n, "beta")
        if c not in cache:
            cache[c] = (run(n, "200")["total"] + run(n, "400")["total"]) / 2
        return cache[c]
    paths = [(0.0, {k: 0 for k in keys}, [])]
    for level in range(10, 61):
        nxt = {}
        todo = []
        for sc, b, path in paths:
            for k in keys:
                if b[k] < tb[k]:
                    n = dict(b, **{k: b[k] + 1})
                    if valid_partial(n):
                        todo.append((sc, n, path + [k]))
        with ThreadPoolExecutor(4) as ex:
            vals = list(ex.map(lambda x: both(x[1]), todo))
        for (sc, n, path), v in zip(todo, vals):
            key = S.encode(n, "beta")
            s2 = sc + level * v
            if key not in nxt or s2 < nxt[key][0]:
                nxt[key] = (s2, n, path)
        paths = sorted(nxt.values(), key=lambda x: x[0])[:width]
        print(f"level {level} best {S.encode(paths[0][1], 'beta')} {paths[0][0]:.0f}", file=log, flush=True)
    sc, b, path = paths[0]
    print("ORDER " + " ".join(path), file=log, flush=True)
    cur = {k: 0 for k in keys}
    for level, k in zip(range(10, 61), path):
        cur[k] += 1
        print(f"level {level} {k} {cur[k]} {S.encode(cur, 'beta')} kill={cache[S.encode(cur, 'beta')]:.2f}", file=log,
              flush=True)

if __name__ == "__main__":
    if sys.argv[1] == "beam":
        beam(sys.argv[2], sys.stdout)
        sys.exit()
    if sys.argv[1] == "order":
        ordered(sys.argv[2], sys.stdout)
        sys.exit()
    case = sys.argv[1] if len(sys.argv) > 1 else "half"
    keys = [t["key"] for t in S.TREES["beta"]]
    b = {k: 0 for k in keys}
    print(f"level 9 - {run(b, HIT[case])}", flush=True)
    for level in range(10, 61):
        cands = []
        for k in keys:
            n = dict(b); n[k] += 1
            if valid_partial(n):
                cands.append((k, n))
        with ThreadPoolExecutor(2) as ex:
            res = list(ex.map(lambda c: run(c[1], HIT[case]), cands))
        (k, n), r = min(zip(cands, res), key=lambda x: x[1]["total"])
        b = n
        print(f"level {level} {k} {b[k]} {S.encode(b, 'beta')} total={r['total']:.2f} kill={r['kill']:.2f} "
              f"rest={r['rest']:.2f} dps={r['dps']:.1f} dtps={r['dtps']:.1f} mps={r['mps']:.1f}", flush=True)
