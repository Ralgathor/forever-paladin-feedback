package retribution

import (
	"fmt"
	"os"
	"strconv"
	"testing"

	"github.com/wowsims/forever/sim/core"
	"github.com/wowsims/forever/sim/core/proto"
)

// FEEDBACK_DUR (sec), FEEDBACK_BUFFS (full|lean), PROPOSE flags. Prints DPS, time to OOM and sec OOM.
func TestFeedbackRun(t *testing.T) {
	if os.Getenv("FEEDBACK_DUR") == "" {
		t.Skip()
	}
	dur, _ := strconv.ParseFloat(os.Getenv("FEEDBACK_DUR"), 64)
	raid, party, indiv := core.FullRaidBuffs, core.FullPartyBuffs, core.FullIndividualBuffs
	if os.Getenv("FEEDBACK_BUFFS") == "lean" {
		raid = &proto.RaidBuffs{GiftOfTheWild: true, BattleShout: 1}
		party = &proto.PartyBuffs{}
		indiv = &proto.IndividualBuffs{GreaterBlessingOfKings: true, GreaterBlessingOfWisdom: true, GreaterBlessingOfMight: true}
	}
	player := &proto.Player{
		Name: "Ret", Race: proto.Race_RaceHuman, Class: proto.Class_ClassPaladin,
		Equipment:     core.GetGearSet("../../../ui/specs/paladin/retribution/gear_sets", "default").GearSet,
		Consumables:   DefaultConsumables,
		TalentsString: UnsealedWrathTalents,
		Spec:          DefaultSpecOptions,
		Rotation:      core.GetAplRotation("../../../ui/specs/paladin/retribution/apls", "default").Rotation,
		Buffs:         indiv,
		Profession1:   proto.Profession_Engineering, Profession2: proto.Profession_Blacksmithing,
		DistanceFromTarget: 25,
	}
	enc := core.MakeSingleTargetEncounter(5)
	enc.Duration = dur
	rsr := &proto.RaidSimRequest{
		Raid:       core.SinglePlayerRaidProto(player, party, raid, core.FullDebuffs),
		Encounter:  enc,
		SimOptions: &proto.SimOptions{Iterations: 3000, RandomSeed: 101},
	}
	res := core.RunRaidSim(rsr)
	if res.Error != nil {
		t.Fatal(res.Error.Message)
	}
	u := res.RaidMetrics.Parties[0].Players[0]
	fmt.Printf("RESULT dur=%.0f buffs=%s propose=%q dps=%.1f tto=%.1f oom=%.1f\n", dur, os.Getenv("FEEDBACK_BUFFS"),
		os.Getenv("PROPOSE"), u.Dps.Avg, u.Tto.Avg, u.SecondsOomAvg)
}
