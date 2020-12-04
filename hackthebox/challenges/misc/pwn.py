from pwn import *
import re
import time
import socket
from PIL import Image, ImageGrab
from pyzbar.pyzbar import decode

conn = remote('178.128.40.63', 32308)
conn.recvuntil("you got only 3 seconds!")
conn.recvlines(3)
data = conn.recvlines(51)

print(data)
time.sleep(0.2)
img = ImageGrab.grab()
a = decode(img)
print(a)

math_string = a[0].data.decode('utf-8')
math_string = math_string.replace('x', '*')
print(math_string)

total = eval(math_string[:len(math_string) - 3])

conn.send(total)
answer = conn.recvall().decode()
print(answer)

conn.close()