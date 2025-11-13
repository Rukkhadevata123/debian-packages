import json
p = json.load(open('package.json'))
if 'packageManager' in p:
	del p['packageManager']
open('package.json','w').write(json.dumps(p, indent=2) + '\n')