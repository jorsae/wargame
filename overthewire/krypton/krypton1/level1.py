import codecs

data = open('krypton1', 'r').read()
print(data)

uncoded = codecs.decode(data, 'rot-13')
print(uncoded)