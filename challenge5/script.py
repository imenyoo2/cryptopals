


plain = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

key = b"ICE"

encrypt = b""

for i in range(len(plain)):
    encrypt += chr(plain[i] ^ key[i % 3]).encode()

print(encrypt.hex())

