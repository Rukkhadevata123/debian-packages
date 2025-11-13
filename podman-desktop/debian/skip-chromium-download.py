import json
p=json.load(open('package.json'))
p.setdefault('scripts',{})['postinstall']='echo skipped-playwright'
open('package.json','w').write(json.dumps(p,indent=2)+ '\n')