"""Tables of Analysis, Healing (proposals/analysis/healing.md). Run: python3 run_tables.py
Healing per sec after overhealing (raid and one tank) for fights of 3, 5 and 10 min."""
import healing_model as H
from healing_model import paladin, priest, druid, shaman, solve, budget, max_hps

PROP = dict(rev=0.5, light=1.30, bol=False, ling=0.2, conv=0.05, bened=0.09, inf_all=True)
TS = (180, 300, 600)
OTHERS = (("Priest", priest), ("Druid", druid), ("Shaman", shaman))

def mk(f, hp, T, tank, **kw):
    if f is shaman: return shaman(hp, tank=tank, T=T)
    return f(hp, tank=tank, **kw)

def others(hp, T, tank):
    return {n: solve(mk(f, hp, T, tank), T, tank)["eff"] for n, f in OTHERS}

def pal(hp, T, tank, **kw):
    return solve(paladin(hp, tank=tank, **kw), T, tank)["eff"]

def pct(a, b): return f"{a/b-1:+.0%}"

if __name__ == "__main__":
    print("## Mana (715)")
    for n, f, kw in (("Priest", priest, {}), ("Druid", druid, {}), ("Shaman", shaman, {}),
                     ("Paladin, beta", paladin, {}), ("Paladin, proposed", paladin, PROP)):
        k = mk(f, 715, 180, False, **kw)
        print(f"  {n:18s} pool {k['pool']:,.0f}  regen while casting {k['castfrac']*k['regen']:.1f}/s  "
              + " / ".join(f"{budget(mk(f, 715, T, False, **kw), T):,.0f}" for T in TS))
    print("## Spells (715): raw and effective healing per mana")
    for n, f, kw in (("Priest", priest, {}), ("Druid", druid, {}), ("Shaman", shaman, {}),
                     ("Paladin, beta", paladin, {}), ("Paladin, proposed", paladin, PROP)):
        for s in mk(f, 715, 180, False, **kw)["spells"]:
            if s.cost > 0: print(f"  {n:18s} {s.name:48s} {s.raw/s.cost:6.2f} {s.eff/s.cost:6.2f}")
    for hp in (715, 900):
        for tank in (False, True):
            print(f"## {'One tank' if tank else 'Raid'}, {hp}")
            O = {T: others(hp, T, tank) for T in TS}
            for n in ("Priest", "Druid", "Shaman"):
                print(f"  {n:18s} " + " | ".join(f"{O[T][n]:5.0f}" for T in TS))
            for n, kw in (("Paladin, beta", {}), ("Paladin, proposed", PROP)):
                v = {T: pal(hp, T, tank, **kw) for T in TS}
                print(f"  {n:18s} " + " | ".join(
                    f"{v[T]:5.0f} (Sha {pct(v[T], O[T]['Shaman'])}, Dru {pct(v[T], O[T]['Druid'])}, "
                    f"Pri {pct(v[T], O[T]['Priest'])}, best {pct(v[T], max(O[T].values()))}, low {pct(v[T], min(O[T].values()))})"
                    for T in TS))
        print(f"## Maximum (raw, one tank, 30 sec), {hp}")
        print("  " + "  ".join(f"{n} {max_hps(mk(f, hp, 30, True)):.0f}" for n, f in OTHERS)
              + f"  Paladin beta {max_hps(paladin(hp)):.0f}  proposed {max_hps(paladin(hp, **PROP)):.0f}")
    print("## Cast plans, proposed Paladin (715)")
    for tank in (False, True):
        for T in TS:
            r = solve(paladin(715, tank=tank, **PROP), T, tank)
            print(f"  {'tank' if tank else 'raid'} {T}: " + ", ".join(f"{a} {b:.1f}" for a, b in r["casts"].items())
                  + f"; idle {r['idle']:.0f}")
