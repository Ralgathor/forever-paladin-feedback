package protection

import (
	"fmt"
	"os"
	"strconv"
	"testing"

	"github.com/wowsims/forever/sim/core"
	"github.com/wowsims/forever/sim/core/proto"
)

// FEEDBACK_DUR (sec), PROPOSE flags. Prints DTPS, TPS and the boss attack table on the tank.
func TestFeedbackRun(t *testing.T) {
	if os.Getenv("FEEDBACK_DUR") == "" {
		t.Skip()
	}
	dur, _ := strconv.ParseFloat(os.Getenv("FEEDBACK_DUR"), 64)
	talents := DefaultProtectionTalents
	if v := os.Getenv("FEEDBACK_TALENTS"); v != "" {
		talents = v
	}
	player := &proto.Player{
		Name: "Prot", Race: proto.Race_RaceHuman, Class: proto.Class_ClassPaladin,
		Equipment:     core.GetGearSet("../../../ui/specs/paladin/protection/gear_sets", "default").GearSet,
		Consumables:   DefaultConsumables,
		TalentsString: talents,
		Spec:          DefaultOptions,
		Rotation:      core.GetAplRotation("../../../ui/specs/paladin/protection/apls", "default").Rotation,
		Buffs:         core.FullTankIndividualBuffs,
		Profession1:   proto.Profession_Engineering, Profession2: proto.Profession_Enchanting,
		DistanceFromTarget: 5,
		HealingModel:       &proto.HealingModel{BurstWindow: 6},
		InFrontOfTarget:    true,
	}
	enc := core.MakeSingleTargetEncounter(5)
	enc.Duration = dur
	raid := core.SinglePlayerRaidProto(player, core.FullPartyBuffs, core.FullRaidBuffs, core.FullDebuffs)
	raid.Tanks = append(raid.Tanks, &proto.UnitReference{Type: proto.UnitReference_Player, Index: 0})
	rsr := &proto.RaidSimRequest{Raid: raid, Encounter: enc, SimOptions: &proto.SimOptions{Iterations: 3000, RandomSeed: 101}}
	res := core.RunRaidSim(rsr)
	if res.Error != nil {
		t.Fatal(res.Error.Message)
	}
	u := res.RaidMetrics.Parties[0].Players[0]
	var casts, hits, crits, miss, dodge, parry, block, crush float64
	for _, a := range res.EncounterMetrics.Targets[0].Actions {
		for _, tm := range a.Targets {
			if os.Getenv("FEEDBACK_RAW") != "" {
				fmt.Printf("RAW %v casts=%d hits=%d crits=%d miss=%d dodge=%d parry=%d block=%d crush=%d glance=%d\n", a.Id, tm.Casts, tm.Hits, tm.Crits, tm.Misses, tm.Dodges, tm.Parries, tm.Blocks, tm.Crushes, tm.Glances)
			}
			hits += float64(tm.Hits)
			crits += float64(tm.Crits)
			miss += float64(tm.Misses)
			dodge += float64(tm.Dodges)
			parry += float64(tm.Parries)
			block += float64(tm.Blocks)
			crush += float64(tm.Crushes)
			casts += float64(tm.Casts)
		}
	}
	var extra float64
	for _, a := range u.Actions {
		if os.Getenv("FEEDBACK_RAW") != "" && a.Id.GetOtherId() == proto.OtherAction_OtherActionAttack {
			fmt.Printf("PACT %v %d\n", a.Id, a.Targets[0].Casts)
		}
		if a.Id.GetOtherId() == proto.OtherAction_OtherActionAttack && a.Id.Tag == 1326084 {
			for _, tm := range a.Targets {
				extra += float64(tm.Casts)
			}
		}
	}
	if u.Tmi != nil {
		fmt.Printf("TMI avg=%.2f std=%.2f\n", u.Tmi.Avg, u.Tmi.Stdev)
	}
	fmt.Printf("EXTRA per min=%.2f\n", extra/3000/(dur/60))
	all := casts
	_ = hits
	fmt.Printf("RESULT dur=%.0f propose=%q tps=%.1f dps=%.1f dtps=%.1f swings=%.1f hit=%.1f%% miss=%.1f%% dodge=%.1f%% parry=%.1f%% block=%.1f%% crit=%.1f%% crush=%.1f%%\n",
		dur, os.Getenv("PROPOSE"), u.Threat.Avg, u.Dps.Avg, u.Dtps.Avg, all/3000, 100*hits/all, 100*miss/all, 100*dodge/all, 100*parry/all,
		100*block/all, 100*crits/all, 100*crush/all)
}
