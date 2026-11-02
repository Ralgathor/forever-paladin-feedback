import json, os, subprocess, sys, tempfile
W='/tmp/wowsims-forever'
d=json.load(open(f'{W}/assets/database/db.json'))
by={i['id']:i for i in d['items']}
atl={i['id']:i.get('sources',[]) for i in json.load(open(f'{W}/assets/db_inputs/atlasloot_db.json'))['items']}
RAID_ZONES={2717,2677,2159,1977,3429,3428,3456}
WORLD_BOSS={6109,12397,14889,14888,14887,14890}
PVP=("Marshal","General","Warlord","Knight-","Lieutenant","Champion","Legionnaire","Blood Guard","Centurion","Commander")
CLASS={'DpsWarrior':1,'Retribution':2,'Hunter':3,'Rogue':4,'Fire':8,'DemonologyFireBrand':9}
ARMOR={1:{1,2,3,4},2:{1,2,3,4},3:{1,2,3},4:{1,2},8:{1},9:{1}}
# melee weapon types allowed (1 axe,2 dagger,3 fist,4 mace,5 offhand,6 polearm,7 shield,8 staff,9 sword)
WEAP={1:{1,2,3,4,6,8,9},2:{1,4,6,9},3:{1,2,3,6,8,9},4:{2,3,4,9},8:{2,5,8,9},9:{2,5,8,9}}
RANGED={1:{1,2,3,4},2:{7},3:{1,2,3},4:{1,2,3,4},8:{5},9:{5}}
RAIDISH={18404,18821,12798,19491,19325,19618,19619,19620,19518,19147,20047,23057,21415,18543,18820,19379,23451,19366}
PVPREP={509,510,729,730,889,890}
def ilvl(it): return it['scalingOptions']['0'].get('ilvl',0)
def pre_raid(it):
    if ilvl(it)>63 or it['id'] in RAIDISH or it.get('quality',0)>4 or it.get('quality',0)<2: return False
    if it.get('reqLvl',0)>60: return False
    if any(p in it['name'] for p in PVP): return False
    if it.get('factionRestriction')==2: return False
    for s in (it.get('sources') or [])+atl.get(it['id'],[]):
        if 'pvp' in s or (s.get('rep') or {}).get('repFactionId') in PVPREP: return False
        dr=s.get('drop')
        if dr and (dr.get('zoneId') in RAID_ZONES or dr.get('npcId') in WORLD_BOSS): return False
    return True
def ok_class(it,c):
    ca=it.get('classAllowlist')
    if ca and c not in ca: return False
    t=it.get('type')
    if t in (1,3,5,6,7,8,9,10) and it.get('armorType') not in ARMOR[c]: return False
    if t==13 and it.get('weaponType') not in WEAP[c]: return False
    if t==14 and it.get('rangedWeaponType') not in RANGED[c]: return False
    return True
SLOT_TYPE=[1,2,3,4,5,6,7,8,9,10,11,11,12,12,13,13,14]
def st(it): return {int(k):v for k,v in it['scalingOptions']['0'].get('stats',{}).items()}
def run(jobs):
    fi=tempfile.mktemp(suffix='.json',dir='/tmp/ms'); fo=fi+'.out'
    json.dump(jobs,open(fi,'w'))
    subprocess.run(['/tmp/ms/zzbatch',fi,fo],check=True)
    r=json.load(open(fo)); os.remove(fi); os.remove(fo)
    for j in r:
        if j.get('err'): print('ERR',j['err'],file=sys.stderr)
    return r
def ep(spec,items):
    base={'spec':spec,'items':items,'iters':2000}
    S={0:60,1:60,3:60,5:60,7:60,11:60,14:120,15:120,17:15,18:15,19:15,20:60,13:60}
    jobs=[dict(base)]+[dict(base,bonus={str(k):v}) for k,v in S.items()]+[dict(base,pseudo={str(p):10}) for p in (0,1,2)]
    r=run(jobs); b=r[0]['dps']
    w={k:(r[1+i]['dps']-b)/v for i,(k,v) in enumerate(S.items())}
    pw={p:(r[1+len(S)+i]['dps']-b)/10 for i,p in enumerate((0,1,2))}
    return w,pw
def score(it,w,pw,slot):
    s=sum(w.get(k,0)*v for k,v in st(it).items())
    if it.get('type') in (13,14):
        dps=it['scalingOptions']['0'].get('unroundedDps',0)
        s+=dps*pw[{14:0,15:1,16:2}[slot]]
    return s
