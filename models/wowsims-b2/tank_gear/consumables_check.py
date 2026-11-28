"""Consumable checks of 28 November 2026 (logs/consumables_dc09e002f0.log): the full threat consumables of 18 November, then one
change at a time (remove an item, add an item, or replace an elixir of the same group). Threat sets with their enchants, 3 min.
Usage: python3 consumables_check.py <wowsims clone> P W D. Needs the test binaries of run_pool.sh in /tmp/bin. IT: iterations (1000)."""
import json, os, subprocess, sys
D=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
W=sys.argv.pop(1)
ITER=os.environ.get('IT','1000')
def ids(f): return ','.join(map(str,json.load(open(f'{D}/tank_gear/{f}'))))
T={'P':('prottest','sim/paladin/protection','TestFeedbackRun','prot'),'W':('wartest','sim/warrior/protection','TestFeedbackRun','war'),'D':('beartest','sim/druid/feralbear','TestFeedbackBear','bear')}
BASE={
 'P':dict(flaskId=13512,foodId=13933,offensivePotId=250937,mhImbueId=20749,explosiveId=260817,conjuredId=9421,elixirIds=[250350,13454,13452,13445,250329,21546,9088],extraIds=[10646,17048,12451,12460,8410,12217,10309,10310,10305]),
 'W':dict(flaskId=13510,foodId=20452,offensivePotId=250943,mhImbueId=18262,explosiveId=260814,conjuredId=9421,elixirIds=[250350,13452,13445,250329,9088],extraIds=[10646,17048,12451,12460,8410,12217,10309,10310,10305]),
 'D':dict(flaskId=13510,foodId=20452,offensivePotId=250943,conjuredId=9421,elixirIds=[250350,13452,13445,250329,9088],extraIds=[10646,17048,12451,12460,8410,12217,10309,10310,10305]),
}
def run(t,c,extra_env={}):
    b,dr,r,s=T[t]
    env=dict(os.environ,FEEDBACK_ITEMS=ids(f'set_{s}.json'),FEEDBACK_ENCHANTS=ids(f'enchants_{s}.json'),FEEDBACK_CONSUMES_JSON=json.dumps(c),FEEDBACK_DUR='180',FEEDBACK_ITER=ITER,FEEDBACK_STATS='1',**extra_env)
    if t=='P': env['RF_ALL']='1.90'
    o=subprocess.run(['/tmp/bin/'+b,'-test.run',r,'-test.v'],cwd=W+'/'+dr,env=env,capture_output=True,text=True).stdout
    res=[l for l in o.splitlines() if l.startswith('RESULT')][0]; stl=[l for l in o.splitlines() if l.startswith('STATS')]
    g=lambda k: float(res.split(k+'=')[1].split()[0].rstrip('%'))
    return g('tps'),g('dtps'),(stl[0][6:] if stl else '')
db={c['id']:c['name'] for c in json.load(open(W+'/assets/database/db.json'))['consumables']}
groups={'Strength':[250350,9206,13453],'Agility':[9187,250328],'Crit':[13452,250351,250337],'Armor':[13445],'Health':[250329,250335],'Spell':[13454],'Holy':[21546],'Shadow res':[9088]}
add=[9187,250328,10307,12820,250335,10308,13453,9206,250351,250337,13454,21546]
out=sys.stdout
for t in sys.argv[1:]:
    base=BASE[t]; b0=run(t,base); print(t,'full',*b0,file=out,flush=True)
    for k in ('elixirIds','extraIds'):
        for i in base[k]:
            c=json.loads(json.dumps(base)); c[k].remove(i); r=run(t,c)
            print(t,f'-{db.get(i,i)}',r[0],r[1],f'{(r[0]/b0[0]-1)*100:+.2f}%',r[2],file=out,flush=True)
    for i in add:
        if i in base['elixirIds'] or i in base['extraIds']: continue
        c=json.loads(json.dumps(base)); (c['extraIds'] if i in (10307,10308) else c['elixirIds']).append(i); r=run(t,c)
        print(t,f'+{db.get(i,i)}',r[0],r[1],f'{(r[0]/b0[0]-1)*100:+.2f}%',r[2],file=out,flush=True)
    for g,L in groups.items():
        cur=[i for i in base['elixirIds'] if i in L]
        for i in L:
            if not cur or i in cur: continue
            c=json.loads(json.dumps(base)); c['elixirIds']=[x for x in c['elixirIds'] if x not in cur]+[i]; r=run(t,c)
            print(t,f'{db.get(cur[0])} -> {db.get(i,i)}',r[0],r[1],f'{(r[0]/b0[0]-1)*100:+.2f}%',r[2],file=out,flush=True)
