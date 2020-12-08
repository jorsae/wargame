import sys
import re
import time
import socket
from PIL import Image, ImageGrab
from pyzbar.pyzbar import decode

server = (sys.argv[1], int(sys.argv[2]))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server)
s.setblocking(True)
data = ''
try:
    while True:
        msg = s.recv(1024)
        data += msg.decode('utf-8')
        if 'Wrong!' in data or 'ecoded string' in data:
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
    s.send(total)
    s.send('\n'.encode())
    print(f'sent result: {total}')
except Exception as e:
    print(e)


try:
    ans = s.recv(1024).decode('utf-8')
    print(f'{ans}')
except Exception as e:
    print(e)
