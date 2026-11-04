package protection

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"testing"

	"github.com/wowsims/forever/sim/core"
	"github.com/wowsims/forever/sim/core/proto"
	"google.golang.org/protobuf/encoding/protojson"
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
		Name: "Prot", Race: proto.Race_RaceHuman, Class: proto.Class_ClassWarrior,
		Equipment:     feedbackItems(core.GetGearSet("../../../ui/specs/warrior/protection/gear_sets", "prebis").GearSet),
		Consumables:   DefaultConsumables,
		TalentsString: talents,
		Spec:          DefaultOptions,
		Rotation:      core.GetAplRotation("../../../ui/specs/warrior/protection/apls", warApl()).Rotation,
		Buffs:         core.FullTankIndividualBuffs,
		Profession1:   proto.Profession_Engineering, Profession2: proto.Profession_Blacksmithing,
		DistanceFromTarget: 0,
		HealingModel:       &proto.HealingModel{BurstWindow: 6},
		InFrontOfTarget:    true,
	}
	if os.Getenv("FEEDBACK_NOENG") != "" {
		player.Profession1 = proto.Profession_Mining
	}
	if os.Getenv("FEEDBACK_CHARGE") != "" {
		player.DistanceFromTarget = 20
	}
	enc := core.MakeSingleTargetEncounter(5)
	enc.Duration = dur
	// FEEDBACK_BOSS: "fast" = a swing each 1.2 sec with 60% damage (same damage each sec), "dw" = a boss with two weapons.
	if v := os.Getenv("FEEDBACK_BOSS"); v != "" {
		for _, tg := range enc.Targets {
			if strings.Contains(v, "fast") {
				tg.SwingSpeed, tg.MinBaseDamage = 1.2, tg.MinBaseDamage*0.6
			}
			if strings.Contains(v, "dw") {
				tg.DualWield = true
			}
		}
	}
	ntg := 1
	if v := os.Getenv("FEEDBACK_TARGETS"); v != "" {
		ntg, _ = strconv.Atoi(v)
		t0 := core.FreshDefaultTargetConfig()
		t0.MinBaseDamage *= 1.0 / 3
		enc.Targets = nil
		for i := 0; i < ntg; i++ {
			enc.Targets = append(enc.Targets, t0)
		}
	}
	raid := core.SinglePlayerRaidProto(player, core.FullPartyBuffs, core.FullRaidBuffs, core.FullDebuffs)
	raid.Tanks = append(raid.Tanks, &proto.UnitReference{Type: proto.UnitReference_Player, Index: 0})
	rsr := &proto.RaidSimRequest{Raid: raid, Encounter: enc, SimOptions: &proto.SimOptions{Iterations: 3000, RandomSeed: 101}}
	if os.Getenv("FEEDBACK_BURST") != "" {
		enc.DurationVariation = 0 // the burst windows need the same fight length
		core.BurstStart()
	}
	if os.Getenv("FEEDBACK_LOG") != "" {
		rsr.SimOptions.Debug = true
		rsr.SimOptions.Iterations = 1
	}
	if d := os.Getenv("FEEDBACK_DUMP"); d != "" { // the request as JSON, for the wowsims links of sets/ (models/wowsims-b2/sets)
		b, _ := protojson.Marshal(rsr)
		os.WriteFile(d, b, 0644)
	}
	res := core.RunRaidSim(rsr)
	if os.Getenv("FEEDBACK_LOG") != "" {
		fmt.Println(res.Logs)
	}
	if os.Getenv("FEEDBACK_SRC") != "" {
		for _, a := range res.RaidMetrics.Parties[0].Players[0].Actions {
			thr, casts := 0.0, 0.0
			for _, tm := range a.Targets {
				thr += tm.Threat
				casts += float64(tm.Casts)
			}
			if thr != 0 {
				fmt.Printf("SRC %v threat=%.1f casts=%.2f\n", a.Id, thr/float64(rsr.SimOptions.Iterations), casts/float64(rsr.SimOptions.Iterations))
			}
		}
	}
	if os.Getenv("FEEDBACK_BURST") != "" {
		core.BurstReport(os.Getenv("FEEDBACK_BURST"), int(rsr.SimOptions.Iterations), []float64{1.5, 3, 4.5, 6, 8, 10, 15, 20, 30}, []float64{3, 6, 10})
	}
	if res.Error != nil {
		t.Fatal(res.Error.Message)
	}
	u := res.RaidMetrics.Parties[0].Players[0]
	per := make([]float64, ntg)
	for _, a := range u.Actions {
		for _, tm := range a.Targets {
			if int(tm.UnitIndex) < ntg {
				per[tm.UnitIndex] += tm.Threat / 3000 / dur
			}
		}
	}
	fmt.Printf("PERTARGET %v\n", per)
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
	all := casts
	_ = hits
	if u.Tmi != nil {
		fmt.Printf("TMI avg=%.0f\n", u.Tmi.Avg)
	}
	fmt.Printf("RESULT dur=%.0f propose=%q tps=%.1f dps=%.1f dtps=%.1f swings=%.1f hit=%.1f%% miss=%.1f%% dodge=%.1f%% parry=%.1f%% block=%.1f%% crit=%.1f%% crush=%.1f%%\n",
		dur, os.Getenv("PROPOSE"), u.Threat.Avg, u.Dps.Avg, u.Dtps.Avg, all/3000, 100*hits/all, 100*miss/all, 100*dodge/all, 100*parry/all,
		100*block/all, 100*crits/all, 100*crush/all)
}

func warApl() string {
	if os.Getenv("FEEDBACK_CHARGE") != "" {
		return "charge"
	}
	return "default"
}

// feedbackItems: FEEDBACK_ITEMS is a comma list of 17 item ids (0 = empty slot), for example the pool sets of
// tank_gear/. The enchants of the default set stay on their slots.
func feedbackItems(eq *proto.EquipmentSpec) *proto.EquipmentSpec {
	v := os.Getenv("FEEDBACK_ITEMS")
	if v == "" {
		return eq
	}
	out := &proto.EquipmentSpec{}
	for i, s := range strings.Split(v, ",") {
		id, _ := strconv.Atoi(strings.TrimSpace(s))
		it := &proto.ItemSpec{Id: int32(id)}
		if i < len(eq.Items) && eq.Items[i] != nil && id != 0 {
			it.Enchant = eq.Items[i].Enchant
			if eq.Items[i].Id == it.Id { // the same item: keep its random suffix
				it.RandomSuffix = eq.Items[i].RandomSuffix
			}
		}
		out.Items = append(out.Items, it)
	}
	return out
}
