// Batch runner for the matched-gear damage comparison. Reads jobs from argv[1], writes results to argv[2].
package main

import (
	"encoding/json"
	"fmt"
	"os"
	"runtime"
	"sync"

	"github.com/wowsims/forever/sim"
	"github.com/wowsims/forever/sim/core"
	"github.com/wowsims/forever/sim/core/proto"
	"google.golang.org/protobuf/encoding/protojson"
)

type job struct {
	Spec  string            `json:"spec"`
	Items []*proto.ItemSpec `json:"items"`
	Iters int32             `json:"iters"`
	Dur   float64           `json:"dur"`
	Cons  bool              `json:"cons"`
	Bonus map[int]float64   `json:"bonus"`
	Pseudo map[int]float64  `json:"pseudo"`
	Dps   float64           `json:"dps"`
	Sd    float64           `json:"sd"`
	Err   string            `json:"err"`
}

func load(f string) *proto.RaidSimRequest {
	b, err := os.ReadFile(f)
	if err != nil { panic(err) }
	r := &proto.RaidSimRequest{}
	if err := protojson.Unmarshal(b, r); err != nil { panic(err) }
	return r
}

func one(j *job, ret *proto.RaidSimRequest) {
	r := load("/tmp/zzdump/Test" + j.Spec + "-Average-Default.json")
	p := r.Raid.Parties[0].Players[0]
	if j.Items != nil { p.Equipment = &proto.EquipmentSpec{Items: j.Items} }
	if !j.Cons {
		c := p.Consumables
		n := &proto.ConsumesSpec{}
		if c != nil { n.MhWeaponImbueId = c.MhWeaponImbueId; n.OhWeaponImbueId = c.OhWeaponImbueId }
		p.Consumables = n
	}
	if len(j.Bonus) > 0 || len(j.Pseudo) > 0 {
		us := &proto.UnitStats{Stats: make([]float64, len(proto.Stat_name)), PseudoStats: make([]float64, len(proto.PseudoStat_name))}
		for k, v := range j.Bonus { us.Stats[k] = v }
		for k, v := range j.Pseudo { us.PseudoStats[k] = v }
		p.BonusStats = us
	}
	r.Raid.Buffs = ret.Raid.Buffs
	r.Raid.Debuffs = ret.Raid.Debuffs
	r.Raid.Parties[0].Buffs = ret.Raid.Parties[0].Buffs
	p.Buffs = ret.Raid.Parties[0].Players[0].Buffs
	if j.Dur == 0 { j.Dur = 120 }
	r.Encounter.Duration = j.Dur
	r.Encounter.DurationVariation = 5
	if j.Iters == 0 { j.Iters = 1000 }
	r.SimOptions.Iterations = j.Iters
	r.SimOptions.RandomSeed = 101
	res := core.RunRaidSim(r)
	if res.Error != nil { j.Err = res.Error.Message; return }
	m := res.RaidMetrics.Parties[0].Players[0]
	j.Dps, j.Sd = m.Dps.Avg, m.Dps.Stdev
}

func main() {
	sim.RegisterAll()
	ret := load("/tmp/zzdump/TestRetribution-Average-Default.json")
	var jobs []*job
	b, _ := os.ReadFile(os.Args[1])
	if err := json.Unmarshal(b, &jobs); err != nil { panic(err) }
	ch := make(chan *job)
	var wg sync.WaitGroup
	for w := 0; w < runtime.NumCPU(); w++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for j := range ch {
				func() {
					defer func() { if e := recover(); e != nil { j.Err = fmt.Sprint("panic: ", e) } }()
					one(j, ret)
				}()
			}
		}()
	}
	for _, j := range jobs { ch <- j }
	close(ch)
	wg.Wait()
	out, _ := json.Marshal(jobs)
	os.WriteFile(os.Args[2], out, 0644)
}
