import base64
import binascii

encodedSecret = "3d3d516343746d4d6d6c315669563362"

a = binascii.unhexlify(encodedSecret)
print(f'unhexlify: {a}')
a = a[::-1].decode()
print(f'reverse: {a}')
a = base64.b64decode(a)
print(f'b64decode: {a}')