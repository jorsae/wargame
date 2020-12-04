import re
import time
import socket
from PIL import Image, ImageGrab
from pyzbar.pyzbar import decode

server = ('178.128.40.63', 32308)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(30)
s.connect(server)
data = ''
try:
    while True:
        msg = s.recv(1024)
        data += msg.decode('utf-8')
        if 'string' in data:
            break
except Exception as e:
    print(e)


print(data)
time.sleep(0.2)
img = ImageGrab.grab()
a = decode(img)
print(a)

math_string = a[0].data.decode('utf-8')
math_string = math_string.replace('x', '*')
print(math_string)

total = eval(math_string[:len(math_string) - 3])
total = str(total).encode()

try:
    s.sendall(total)
    print(f'sent result: {total}')
except Exception as e:
    print(e)

try:
    while True:
        ans = s.recv(1024)
        print(f'{answers}: {ans}')
except Exception as e:
    print(e)

print('DONE')
