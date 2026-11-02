package main

import (
	"bytes"
	"compress/zlib"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"os"
	"io"

	"github.com/wowsims/forever/sim"
	"github.com/wowsims/forever/sim/core"

	"github.com/wowsims/forever/sim/core/proto"
	googleProto "google.golang.org/protobuf/proto"
	"google.golang.org/protobuf/encoding/protojson"
)

type job struct {
	Spec  string            `json:"spec"`
	Items []*proto.ItemSpec `json:"items"`
	Dir   string            `json:"dir"`
	Label string            `json:"label"`
}

func load(f string) *proto.RaidSimRequest {
	b, err := os.ReadFile(f)
	if err != nil { panic(err) }
	r := &proto.RaidSimRequest{}
	if err := protojson.Unmarshal(b, r); err != nil { panic(err) }
	return r
}

func main() {
	ret := load("/tmp/zzdump/TestRetribution-Average-Default.json")
	var jobs []*job
	b, _ := os.ReadFile(os.Args[1])
	if err := json.Unmarshal(b, &jobs); err != nil { panic(err) }
	out := map[string]string{}
	for _, j := range jobs {
		r := load(j.Dir + "/Test" + j.Spec + "-Average-Default.json")
		p := r.Raid.Parties[0].Players[0]
		p.Equipment = &proto.EquipmentSpec{Items: j.Items}
		p.Buffs = ret.Raid.Parties[0].Players[0].Buffs
		r.Encounter.Duration = 120
		r.Encounter.DurationVariation = 5
		s := &proto.IndividualSimSettings{
			ApiVersion: 2,
			Settings:   &proto.SimSettings{Iterations: 10000},
			RaidBuffs:  ret.Raid.Buffs,
			PartyBuffs: ret.Raid.Parties[0].Buffs,
			Debuffs:    ret.Raid.Debuffs,
			Player:     p,
			Encounter:  r.Encounter,
		}
		bin, err := googleProto.Marshal(s)
		if err != nil { panic(err) }
		var buf bytes.Buffer
		w := zlib.NewWriter(&buf)
		w.Write(bin)
		w.Close()
		out[j.Spec] = base64.StdEncoding.EncodeToString(buf.Bytes())
	}
	o, _ := json.MarshalIndent(out, "", " ")
	fmt.Println(string(o))
	sim.RegisterAll()
	for k, v := range out {
		raw, _ := base64.StdEncoding.DecodeString(v)
		zr, _ := zlib.NewReader(bytes.NewReader(raw))
		bin, _ := io.ReadAll(zr)
		s := &proto.IndividualSimSettings{}
		if err := googleProto.Unmarshal(bin, s); err != nil { panic(err) }
		req := &proto.RaidSimRequest{
			Raid: &proto.Raid{Buffs: s.RaidBuffs, Debuffs: s.Debuffs, Parties: []*proto.Party{{Players: []*proto.Player{s.Player}, Buffs: s.PartyBuffs}}},
			Encounter: s.Encounter,
			SimOptions: &proto.SimOptions{Iterations: 10000, RandomSeed: 101},
		}
		res := core.RunRaidSim(req)
		if res.Error != nil { fmt.Fprintln(os.Stderr, k, res.Error.Message); continue }
		fmt.Fprintf(os.Stderr, "%s %.1f\n", k, res.RaidMetrics.Parties[0].Players[0].Dps.Avg)
	}
}
