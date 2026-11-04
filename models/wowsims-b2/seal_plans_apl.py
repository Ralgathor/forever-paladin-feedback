"""Seal plan rotations for the Unsealed Wrath check (W29). Run from the wowsims clone after run.sh.
Writes ui/specs/paladin/retribution/apls/fb_*.apl.siml from the default APL (default.apl.siml):
- fb_r<R>c<C>: Seal of Command after R copies of Seal of Righteousness, Seal of Righteousness after C copies of
  Seal of Command. The default APL is fb_r1c3.
- fb_<A><R><B><C>: the same with Seal A in place of Seal of Righteousness and Seal B in place of Seal of Command
  (R Righteousness, C Command, F Fury, W Wisdom, L Light, J Justice), for example fb_W1C3 or fb_F1R3.
- fb_only<X>: Seal X only, cast again when it ends.
Run a plan: FEEDBACK_APL=fb_r1c1 FEEDBACK_DUR=120 /tmp/rettest -test.run TestFeedbackRun -test.v
"""
import sys
W = sys.argv[1] if len(sys.argv) > 1 else "/tmp/wowsims-forever"
P = W + "/ui/specs/paladin/retribution/apls/"
base = open(P + "default.apl.siml").read()
# cast name, aura name (highest rank), copy aura name
SEAL = {"R": ("seal_of_righteousness", "seal_of_righteousness_20293", "echo_of_righteousness"),
        "C": ("seal_of_command", "seal_of_command_20920", "echo_of_command"),
        "F": ("seal_of_fury", "seal_of_fury_20423_tag0", "echo_of_fury"),
        "W": ("seal_of_wisdom", "seal_of_wisdom_20357", "echo_of_wisdom"),
        "L": ("seal_of_light", "seal_of_light_20349", "echo_of_light"),
        "J": ("seal_of_justice", "seal_of_justice", "echo_of_justice")}
SOC_STACKS = "aura(echo_of_righteousness).num_stacks(include_reaction_time=true) >= 1"
SOR_STACKS = "aura(echo_of_command).num_stacks(include_reaction_time=true) == 3"
assert SOC_STACKS in base and SOR_STACKS in base

def plan(a, r, b, c):
    """Seal b (role of Seal of Command) after r copies of Seal a; Seal a (role of Righteousness) after c copies of b."""
    t = base.replace(SOC_STACKS, "@A_ECHO@ >= %d" % r).replace(SOR_STACKS, "@B_ECHO@ >= %d" % c)
    t = (t.replace("aura(seal_of_command_20920)", "@B_AURA@").replace("aura(seal_of_righteousness_20293)", "@A_AURA@")
          .replace("cast seal_of_command", "@B_CAST@").replace("cast seal_of_righteousness", "@A_CAST@"))
    for k, s in (("A", SEAL[a]), ("B", SEAL[b])):
        t = (t.replace("@%s_ECHO@" % k, "aura(%s).num_stacks(include_reaction_time=true)" % s[2])
              .replace("@%s_AURA@" % k, "aura(%s)" % s[1]).replace("@%s_CAST@" % k, "cast " + s[0]))
    return t

def only(x):
    t = plan(x, 1, x, 1)
    i = t.index("var ${Should refresh SoC} ="); j = t.index("var ${Judge realism protection}")
    cast, aura, _ = SEAL[x]
    return (t[:i] + "var ${Should refresh SoC} =\n    (aura(%s).is_inactive or aura(%s).is_active and aura(%s).remaining_time <= auto_time_to_next(main_hand_auto))\n    and $judge_realism_protection\nvar ${Should refresh SoR} = false\n" % (aura, aura, aura) + t[j:])

out = {}
for r in (1, 2, 3):
    for c in (1, 2, 3):
        out["fb_r%dc%d" % (r, c)] = plan("R", r, "C", c)
for x in "FLWJ":
    out["fb_%s1C3" % x] = plan(x, 1, "C", 3)
for name, p in (("F1R3", ("F", 1, "R", 3)), ("R1F1", ("R", 1, "F", 1)), ("R1F3", ("R", 1, "F", 3)), ("W1R3", ("W", 1, "R", 3))):
    out["fb_" + name] = plan(*p)
for x in "CRF":
    out["fb_only" + x] = only(x)
for n, t in out.items():
    open(P + n + ".apl.siml", "w").write(t)
print(len(out), "APLs")
