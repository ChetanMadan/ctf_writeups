b = bytearray(open('server.py', 'rb').read())
for i in range(len(b)):
    b[i] ^= 0xea
open('b2.out', 'wb').write(b)