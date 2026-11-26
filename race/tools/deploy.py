import hashlib, json, os, subprocess, sys, time
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'sites')
SITES = {
 'second-draft-careers': '0fb64d39-27de-425b-90e4-d6e19137ba84',
 'hearth-and-host-race': '9b58d301-2ca1-4c77-a06a-dcaaedce3835',
 'solo-ops-studio': '64495fdf-a467-4218-bea7-3866018e33b6',
 'classroom-and-family-desk': '1011ffdc-cde6-46f1-8daa-9cf45fc259ac',
 'game-night-co-race': 'fc1e34bf-0373-4da7-b7f4-9a9547685a37',
}
AUTH = 'Authorization: Bearer proxy-injected'
CT = {'.html': 'text/html; charset=utf-8', '.xml': 'application/xml; charset=utf-8', '.txt': 'text/plain; charset=utf-8'}
def curl(args, data=None):
    r = subprocess.run(['curl','-s','-m','120','-H',AUTH]+args, input=data, capture_output=True)
    return r.stdout
def deploy(slug, sid):
    d = os.path.join(BASE, slug)
    files = {}
    for f in sorted(os.listdir(d)):
        files['/'+f] = hashlib.sha1(open(os.path.join(d,f),'rb').read()).hexdigest()
    out = json.loads(curl(['-X','POST','-H','Content-Type: application/json','-d',json.dumps({'files':files}),f'https://api.netlify.com/api/v1/sites/{sid}/deploys']))
    did = out['id']; req = set(out.get('required', []))
    for path, sha in files.items():
        if sha in req:
            ext = os.path.splitext(path)[1]
            body = open(os.path.join(d, path[1:]),'rb').read()
            curl(['-X','PUT','-H','Content-Type: '+CT.get(ext,'application/octet-stream'),'--data-binary','@-',f'https://api.netlify.com/api/v1/deploys/{did}/files{path}'], data=body)
    for _ in range(30):
        st = json.loads(curl([f'https://api.netlify.com/api/v1/deploys/{did}']))
        if st.get('state') in ('ready','error'): break
        time.sleep(3)
    return did, st.get('state'), st.get('error_message'), st.get('ssl_url') or st.get('url'), len(req)
for slug, sid in SITES.items():
    print(slug, deploy(slug, sid), flush=True)
