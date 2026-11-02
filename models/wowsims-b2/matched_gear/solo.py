import json,sys,subprocess,os
from concurrent.futures import ThreadPoolExecutor
jobs=json.load(open(sys.argv[1]))
def run(i):
    f=f'/tmp/ms/solo/{os.path.basename(sys.argv[1])}.{i}'
    json.dump([jobs[i]],open(f+'.in','w'))
    subprocess.run(['/tmp/ms/zzbatch',f+'.in',f+'.out'],capture_output=True)
    return json.load(open(f+'.out'))[0]
with ThreadPoolExecutor(4) as ex: out=list(ex.map(run,range(len(jobs))))
json.dump(out,open(sys.argv[2],'w'))
