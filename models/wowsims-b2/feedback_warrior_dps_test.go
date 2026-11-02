package dps

import (
	"fmt"
	"os"
	"strconv"
	"testing"

	"github.com/wowsims/forever/sim/core"
	"github.com/wowsims/forever/sim/core/proto"
)

// FEEDBACK_DUR (sec), FEEDBACK_SPEC (fury|arms), FEEDBACK_GEAR (prebis|p1). Full buffs as the Retribution feedback test.
func TestFeedbackDps(t *testing.T) {
	if os.Getenv("FEEDBACK_DUR") == "" {
		t.Skip()
	}
	dur, _ := strconv.ParseFloat(os.Getenv("FEEDBACK_DUR"), 64)
	spec := os.Getenv("FEEDBACK_SPEC")
	gear := os.Getenv("FEEDBACK_GEAR")
	talents := DefaultFuryTalents
	if spec == "arms" {
		talents = DefaultArmsTalents
	}
	player := &proto.Player{
		Name: "War", Race: proto.Race_RaceHuman, Class: proto.Class_ClassWarrior,
		Equipment:     core.GetGearSet("../../../ui/specs/warrior/dps/gear_sets", gear+"_"+spec).GearSet,
		Consumables:   DefaultConsumables,
		TalentsString: talents,
		Spec:          DefaultOptions,
		Rotation:      core.GetAplRotation("../../../ui/specs/warrior/dps/apls", spec).Rotation,
		Buffs:         core.FullIndividualBuffs,
		Profession1:   proto.Profession_Engineering, Profession2: proto.Profession_Blacksmithing,
	}
	enc := core.MakeSingleTargetEncounter(5)
	enc.Duration = dur
	rsr := &proto.RaidSimRequest{
		Raid:       core.SinglePlayerRaidProto(player, core.FullPartyBuffs, core.FullRaidBuffs, core.FullDebuffs),
		Encounter:  enc,
		SimOptions: &proto.SimOptions{Iterations: 3000, RandomSeed: 101},
	}
	res := core.RunRaidSim(rsr)
	if res.Error != nil {
		t.Fatal(res.Error.Message)
	}
	u := res.RaidMetrics.Parties[0].Players[0]
	fmt.Printf("RESULT %s %s dur=%.0f dps=%.1f\n", spec, gear, dur, u.Dps.Avg)
}
