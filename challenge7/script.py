"""
AES in ECB mode
"""

from Crypto.Cipher import AES
import base64

key = b'YELLOW SUBMARINE'
cipher = AES.new(key, AES.MODE_ECB)

ciphertxt = open("7.txt", 'r').read()
ciphertxt = base64.b64decode(ciphertxt)

plaintxt = b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

print(cipher.encrypt(plaintxt))

print(cipher.decrypt(ciphertxt))