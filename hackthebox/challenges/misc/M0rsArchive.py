from PIL import Image
import zipfile
import os

def parse_image(img):
    im = Image.open(img)
    width, height = im.size
    rgb_image = im.convert('RGB')
    set_r, set_g, set_b = rgb_image.getpixel((0, 0))
    output = ''
    char_length = 0
    for h in range(1, height, 2):
        for w in range(0, width):
            r, g, b = rgb_image.getpixel((w, h))
            if b != set_b:
                char_length += 1
            else:
                if char_length == 3:
                    output += '-'
                elif char_length == 1:
                    output += '.'
                char_length = 0
        output += ' '
    return output

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

CODE_REVERSED = {value:key for key,value in CODE.items()}
def from_morse(s):
    return ''.join(CODE_REVERSED.get(i) for i in s.split()).lower()

def unzip(file, pwd):
    with zipfile.ZipFile(file) as z:
        z.extractall(pwd=pwd.encode())

start = 'flag_999.zip'
image_name = 'pwd.png'
flag_folder = 'flag'

unzip('M0rsarchive.zip', 'hackthebox')
m = parse_image(image_name)
p = from_morse(m)
unzip(start, p)

while True:
    morse = parse_image(image_name)
    pwd = from_morse(morse)
    print(f'{start} : {pwd}')
    unzip(start, pwd)
    os.replace(f'{flag_folder}/pwd.png', 'pwd.png')
    files = os.listdir(flag_folder)
    for file in files:
        if file.startswith('flag'):
            start = file
            os.replace(f'flag/{file}', file)

