import base64
from pwn import xor


t =    "I'm back anuiI'm ringin' the b"
key = b'Terminator X: Bring the noise'

with open("6.txt", "r") as f:
    cipher = base64.b64decode(f.read())
    print(cipher[0:30])
    print(chr(cipher[11] ^ ord('d')))
    print(chr(cipher[12] ^ ord(' ')))
    print(xor(cipher, key))
