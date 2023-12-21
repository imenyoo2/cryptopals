


def xor(a, b):
    A = bytes.fromhex(a)
    B = bytes.fromhex(b)
    C = b''
    for i, j in zip(A, B):
        C += chr(i ^ j).encode()
    return (C)

print(xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965").hex())
