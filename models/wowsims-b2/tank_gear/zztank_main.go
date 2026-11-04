// zztank runs tank sims from a dumped feedback request (FEEDBACK_DUMP) with other items.
// Copy to cmd/zztank/main.go, then: go run -tags with_db ./cmd/zztank jobs.json out.json
// Each job: {"file": dumped request, "items": [item id for each of the 17 slots, 0 = empty], "iters": n}.
// The enchants of the dumped set stay on their slots. Output: threat, damage and damage taken per sec, and TMI.
package main

import (
	"encoding/json"
	"os"

	"github.com/wowsims/forever/sim"
	"github.com/wowsims/forever/sim/core"
	"github.com/wowsims/forever/sim/core/proto"
	"google.golang.org/protobuf/encoding/protojson"
)

type job struct {
	File  string  `json:"file"`
	Items []int32 `json:"items"`
	Iters int32   `json:"iters"`
}

type result struct {
	Tps  float64 `json:"tps"`
	Dps  float64 `json:"dps"`
	Dtps float64 `json:"dtps"`
	Tmi  float64 `json:"tmi"`
	Err  string  `json:"err,omitempty"`
}

func main() {
	sim.RegisterAll()
	var jobs []*job
	b, _ := os.ReadFile(os.Args[1])
	if err := json.Unmarshal(b, &jobs); err != nil {
		panic(err)
	}
	var out []result
	for _, j := range jobs {
		raw, err := os.ReadFile(j.File)
		if err != nil {
			panic(err)
		}
		r := &proto.RaidSimRequest{}
		if err := protojson.Unmarshal(raw, r); err != nil {
			panic(err)
		}
		p := r.Raid.Parties[0].Players[0]
		if j.Items != nil {
			old := p.Equipment.Items
			var items []*proto.ItemSpec
			for i, id := range j.Items {
				it := &proto.ItemSpec{Id: id}
				if i < len(old) && old[i] != nil && id != 0 {
					it.Enchant = old[i].Enchant
					if old[i].Id == id { // the same item: keep its random suffix
						it.RandomSuffix = old[i].RandomSuffix
					}
				}
				items = append(items, it)
			}
			p.Equipment = &proto.EquipmentSpec{Items: items}
		}
		r.SimOptions.Iterations = j.Iters
		r.SimOptions.RandomSeed = 101
		res := core.RunRaidSim(r)
		if res.Error != nil {
			out = append(out, result{Err: res.Error.Message})
			continue
		}
		u := res.RaidMetrics.Parties[0].Players[0]
		tmi := 0.0
		if u.Tmi != nil {
			tmi = u.Tmi.Avg
		}
		out = append(out, result{Tps: u.Threat.Avg, Dps: u.Dps.Avg, Dtps: u.Dtps.Avg, Tmi: tmi})
	}
	o, _ := json.Marshal(out)
	os.WriteFile(os.Args[2], o, 0644)
}
