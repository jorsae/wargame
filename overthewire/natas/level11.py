from binascii import hexlify, unhexlify
import base64
import json
from urllib.parse import unquote # decodes the %xx part of the cookie. See https://en.wikipedia.org/wiki/Percent-encoding
from os import urandom

def xor(key, string):
    # i is the position within the key
    i = 0
    arr = []
    for ch in string:
    	# Convert the key char and the plaintext char to
        # integers using `ord`, XOR them and add them to
        # the array.
        arr.append(ord(ch) ^ ord(key[i]))
        
		# Manage the "repeating" part of the repeating key.
        # If the end of the key is reached start back at the
        # beginning.
        i += 1
        if (i == len(key)):
            i = 0

	# Finally convert our array to a byte array (which
    # hexlify likes), then convert to hex and return it.
    return hexlify(bytearray(arr))


"""
    original_data XOR KEY = kryptert_data
    original_data XOR kryptert_data = KEY
"""

# %3D needs to be converted
cookie = unquote('ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D')
decoded_cookie = base64.b64decode(cookie).decode()
default = '{"showpassword":"no","bgcolor":"#ffffff"}'

key = xor(default, decoded_cookie).decode()
key = unhexlify(key).decode()
print(f'Key: {key}')
# key = qw8J

key = 'qw8J'
encrypted = '{"showpassword":"yes","bgcolor":"#ffffff"}'
new_cookie = xor(key, encrypted)
new_cookie = unhexlify(new_cookie)
new_cookie = base64.b64encode(new_cookie).decode()
print(f'new cookie: {new_cookie}')