"""Seal plan rotations for the Unsealed Wrath check (W29). Run from the wowsims clone after run.sh.
Writes ui/specs/paladin/retribution/apls/fb_r<R>c<C>.apl.json: the default APL, but Seal of Command after R
copies of Seal of Righteousness and Seal of Righteousness after C copies of Seal of Command. The default APL is
fb_r1c3. Run a plan: FEEDBACK_APL=fb_r1c1 FEEDBACK_DUR=120 PROPOSE=C1 /tmp/rettest -test.run TestFeedbackRun -test.v
"""
import copy, json, sys
W = sys.argv[1] if len(sys.argv) > 1 else "/tmp/wowsims-forever"
P = W + "/ui/specs/paladin/retribution/apls/"
ECHO_COMMAND, ECHO_RIGHTEOUSNESS = 1311703, 1311704
base = json.load(open(P + "default.apl.json"))

def set_stacks(apl, name, echo, n):
    def walk(o):
        if isinstance(o, dict):
            cmp = o.get("cmp")
            if cmp and "auraNumStacks" in cmp.get("lhs", {}):
                cmp["op"] = "OpGe"
                cmp["lhs"]["auraNumStacks"]["auraId"]["spellId"] = echo
                cmp["rhs"] = {"const": {"val": str(n)}}
            for x in o.values():
                walk(x)
        elif isinstance(o, list):
            for x in o:
                walk(x)
    for v in apl["valueVariables"]:
        if v["name"] == name:
            walk(v["value"])

for r in (1, 2, 3):
    for c in (1, 2, 3):
        apl = copy.deepcopy(base)
        set_stacks(apl, "Should refresh SoC", ECHO_RIGHTEOUSNESS, r)
        set_stacks(apl, "Should refresh SoR", ECHO_COMMAND, c)
        json.dump(apl, open(P + f"fb_r{r}c{c}.apl.json", "w"), indent=1)

# Other Seal pairs: fb_r1c3_<X>C puts Seal X in place of Seal of Righteousness (W Wisdom, F Fury, L Light, J Justice).
SEALS = {"W": (20357, 3, 1328206), "F": (20423, 7, 1311701), "L": (20349, 4, 1328198), "J": (20164, 1, 1311705)}
src = json.load(open(P + "fb_r1c3.apl.json"))
for x, (sid, rank, echo) in SEALS.items():
    apl = copy.deepcopy(src)
    def swap(o):
        if isinstance(o, dict):
            if o.get("spellId") == 20293 and o.get("rank") == 8:
                o["spellId"], o["rank"] = sid, rank
            elif o.get("spellId") == ECHO_RIGHTEOUSNESS and "rank" not in o:
                o["spellId"] = echo
            for v in o.values():
                swap(v)
        elif isinstance(o, list):
            for v in o:
                swap(v)
    swap(apl)
    json.dump(apl, open(P + f"fb_r1c3_{x}C.apl.json", "w"), indent=1)
