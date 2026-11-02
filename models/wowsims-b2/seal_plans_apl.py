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
