package protection

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"testing"

	"github.com/wowsims/forever/sim/core"
	"github.com/wowsims/forever/sim/core/proto"
	"github.com/wowsims/forever/sim/core/stats"
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
		Name: "Prot", Race: proto.Race_RaceHuman, Class: proto.Class_ClassPaladin,
		Equipment:     feedbackItems(core.GetGearSet("../../../ui/specs/paladin/protection/gear_sets", "default").GearSet),
		Consumables:   feedbackConsumables(),
		TalentsString: talents,
		Spec:          DefaultOptions,
		Rotation:      core.GetAplRotation("../../../ui/specs/paladin/protection/apls", feedbackApl()).Rotation,
		BonusStats:    feedbackBonus(),
		Buffs:         core.FullTankIndividualBuffs,
		Profession1:   proto.Profession_Engineering, Profession2: proto.Profession_Enchanting,
		DistanceFromTarget: 5,
		HealingModel:       &proto.HealingModel{BurstWindow: 6},
		InFrontOfTarget:    true,
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
	rsr := &proto.RaidSimRequest{Raid: raid, Encounter: enc, SimOptions: &proto.SimOptions{Iterations: feedbackIter(), RandomSeed: 101}}
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
				per[tm.UnitIndex] += tm.Threat / float64(feedbackIter()) / dur
			}
		}
	}
	fmt.Printf("PERTARGET %v\n", per)
	if os.Getenv("FEEDBACK_MANA") != "" {
		for _, r := range u.Resources {
			if r.Type == proto.ResourceType_ResourceTypeMana {
				fmt.Printf("MANA %v events=%.1f gain=%.2f\n", r.Id, float64(r.Events)/3000, r.ActualGain/dur)
			}
		}
	}
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

// FEEDBACK_ITER: iterations (default 3000). FEEDBACK_BONUS: bonus stats "index:value,..." (proto Stat order).
func feedbackIter() int32 {
	if v := os.Getenv("FEEDBACK_ITER"); v != "" {
		n, _ := strconv.Atoi(v)
		return int32(n)
	}
	return 3000
}

func feedbackBonus() *proto.UnitStats {
	v := os.Getenv("FEEDBACK_BONUS")
	if v == "" {
		return nil
	}
	st := make([]float64, stats.SimStatsLen)
	for _, kv := range strings.Split(v, ",") {
		p := strings.SplitN(kv, ":", 2)
		i, _ := strconv.Atoi(p[0])
		x, _ := strconv.ParseFloat(p[1], 64)
		st[i] += x
	}
	return &proto.UnitStats{Stats: st}
}

func feedbackApl() string {
	if v := os.Getenv("FEEDBACK_APL"); v != "" {
		return v
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

// feedbackConsumables: wowsims has no Protection Paladin consumable preset (DefaultConsumables is only a
// Demonic Rune). The tank comparison gives the Paladin the same number of tank consumables as the Protection
// Warrior test (ui/specs/warrior/protection/presets.ts), with Paladin choices: Greater Arcane Elixir in place of
// Winterfall Firewater, and Brilliant Wizard Oil in place of the Dense Sharpening Stone. Checked on the survival
// set with C-P1 (3,000 iterations): these give the most threat of the mixes tested.
// FEEDBACK_CONSUMES=default keeps the Demonic Rune only (the runs before 4 November evening).
func feedbackConsumables() *proto.ConsumesSpec {
	if os.Getenv("FEEDBACK_CONSUMES") == "default" {
		return DefaultConsumables
	}
	return &proto.ConsumesSpec{
		OffensivePotId: 250943, // Major Frenzy Potion
		FoodId:         20452,  // Smoked Desert Dumplings
		ExplosiveId:    260817, // EZ-Thro Dark Bomb
		MhImbueId:      20749,  // Brilliant Wizard Oil
		ConjuredId:     9421,   // Major Healthstone
		// Elixir of Ferocity, Greater Arcane Elixir, Elixir of the Mongoose, Elixir of Greater Defense, Elixir of the Phalanx
		ElixirIds: []int32{250350, 13454, 13452, 13445, 250329},
		ExtraIds:  []int32{10646, 17048}, // Goblin Sapper Charge, Rumsey Rum
	}
}
