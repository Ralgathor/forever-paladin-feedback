package paladin

import (
	"os"
	"strings"

	"github.com/wowsims/forever/sim/core"
	"github.com/wowsims/forever/sim/core/stats"
)

// Proposal flags for the feedback checks (PROPOSE=C1,BZ,UW20). Off by default.
func proposeFlag(f string) bool {
	for _, p := range strings.Split(os.Getenv("PROPOSE"), ",") {
		if p == f {
			return true
		}
	}
	return false
}

func (paladin *Paladin) applySimProposals() {
	// C1: Holy Strike triggers your active Seal the same as a melee attack (Command, Righteousness, Fury).
	// It stores and consumes no Unsealed Wrath copy.
	if proposeFlag("C1") {
		paladin.MakeProcTriggerAura(core.ProcTrigger{
			Name:           "C1 Holy Strike Seal trigger" + paladin.Label,
			Callback:       core.CallbackOnSpellHitDealt,
			ClassSpellMask: SpellMaskHolyStrike,
			Outcome:        core.OutcomeLanded,
			Handler: func(sim *core.Simulation, _ *core.Spell, result *core.SpellResult) {
				seal := paladin.activeSeal()
				if seal == nil || seal.echo == nil {
					return
				}
				switch seal.echoID {
				case echoOfCommandID, echoOfRighteousnessID, echoOfFuryID:
					seal.echo(sim, result.Target)
				}
			},
		})
	}
	// C-R4 Burning Zeal 2/2: +20% critical damage bonus of Seals, Judgements and Holy Strike (as Impale).
	if proposeFlag("BZ") {
		paladin.AddStaticMod(core.SpellModConfig{
			ClassMask:  SpellMaskSealProcs | SpellMaskAllJudgements | SpellMaskHolyStrike,
			Kind:       core.SpellMod_CritMultiplier_Flat,
			FloatValue: 0.20,
		})
	}
	// W29 option: Unsealed Wrath decreases the Seal cost by 20%.
	if proposeFlag("UW20") && paladin.Talents.UnsealedWrath {
		paladin.AddStaticMod(core.SpellModConfig{
			ClassMask:  SpellMaskAllSeals,
			Kind:       core.SpellMod_PowerCost_Pct,
			FloatValue: -0.20,
		})
	}
	// C-P1: each Holy Shield cast also starts Redoubt (full charges). RD20: Redoubt 4-20% (5/5 = 20%).
	if redoubt := paladin.GetAura("Redoubt" + paladin.Label); redoubt != nil {
		if proposeFlag("RD20") {
			redoubt.AttachStatBuff(stats.BlockPercent, -10)
		}
		if proposeFlag("CP1") {
			paladin.MakeProcTriggerAura(core.ProcTrigger{
				Name:           "C-P1 Holy Shield starts Redoubt" + paladin.Label,
				Callback:       core.CallbackOnCastComplete,
				ClassSpellMask: SpellMaskHolyShield,
				Handler: func(sim *core.Simulation, _ *core.Spell, _ *core.SpellResult) {
					redoubt.Activate(sim)
					redoubt.SetStacks(sim, redoubt.MaxStacks)
				},
			})
		}
	}
}
