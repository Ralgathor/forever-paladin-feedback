package paladin

import (
	"os"
	"strings"
	"time"

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

// C-P6: Reckoning charges from blocks, dodges and parries (20-100%, once each 4 sec) and from critical hits
// taken (no limit). Stores up to 4. Holy Strike releases up to 2 stored extra attacks; auto attacks spend none.
func (paladin *Paladin) applyReckoningCP6(stored *core.Aura, gain func(*core.Simulation, *core.Spell, *core.SpellResult), tag int32, newTriggers bool) {
	chance := 0.20 * float64(paladin.Talents.Reckoning)
	if newTriggers {
		paladin.MakeProcTriggerAura(core.ProcTrigger{
			Name:       "C-P6 Reckoning - Avoid" + paladin.Label,
			Callback:   core.CallbackOnSpellHitTaken,
			Outcome:    core.OutcomeBlock | core.OutcomeDodge | core.OutcomeParry,
			ProcChance: chance,
			ICD:        4 * time.Second,
			Handler:    gain,
		})
		paladin.MakeProcTriggerAura(core.ProcTrigger{
			Name:       "C-P6 Reckoning - Crit" + paladin.Label,
			Callback:   core.CallbackOnSpellHitTaken,
			Outcome:    core.OutcomeCrit,
			ProcChance: chance,
			Handler:    gain,
		})
	}
	var extraAttack *core.Spell
	paladin.MakeProcTriggerAura(core.ProcTrigger{
		Name:               "C-P6 Reckoning - Holy Strike" + paladin.Label,
		Callback:           core.CallbackOnSpellHitDealt,
		ClassSpellMask:     SpellMaskHolyStrike,
		TriggerImmediately: true,
		ExtraCondition: func(_ *core.Simulation, _ *core.Spell, _ *core.SpellResult) bool {
			return extraAttack != nil && stored.IsActive()
		},
		Handler: func(sim *core.Simulation, _ *core.Spell, result *core.SpellResult) {
			count := min(stored.GetStacks(), 2)
			if stored.GetStacks() > count {
				stored.SetStacks(sim, stored.GetStacks()-count)
			} else {
				stored.Deactivate(sim)
			}
			target := result.Target
			sim.RunAfterCurrentEvent(func(sim *core.Simulation) {
				mainHand := paladin.AutoAttacks.MHAuto()
				extraAttack.SetSpellSchool(mainHand.SpellSchool)
				extraAttack.BonusCoefficient = mainHand.BonusCoefficient
				for range count {
					extraAttack.Cast(sim, target)
				}
			})
		},
	}).ApplyOnInit(func(_ *core.Aura, _ *core.Simulation) {
		if paladin.AutoAttacks.MHAuto() == nil {
			return
		}
		swing := *paladin.AutoAttacks.MHConfig()
		swing.ActionID = swing.ActionID.WithTag(tag)
		extraAttack = paladin.GetOrRegisterSpell(swing)
	})
}
