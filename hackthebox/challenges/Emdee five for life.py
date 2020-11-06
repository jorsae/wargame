# Just a programming challenge, have to md5 encrypt string within x time.

import requests
import re
import hashlib

host = 'http://206.189.19.217:32427/'

r = requests.get('http://206.189.19.217:32427/')

string = re.search("ing</h1><h3 align='center'>\w+", r.text)
string_to_hash = string.group()[27:]

hashed = hashlib.md5(string_to_hash.encode()).hexdigest()
data = { 'hash': hashed }

cookies = {'PHPSESSID': r.cookies.get('PHPSESSID')}
req = requests.post(host, cookies=cookies, data=data)
print(req.text)