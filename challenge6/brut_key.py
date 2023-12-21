import itertools
from tqdm import tqdm
from pwn import xor
import base64
from englishFreqMatchScore import englishFreqMatchScore


arr = [["TERMINATOR", "Terminator", "terminator"], ["Is", "IS"], ["BRING", "Bring", "bring"], ["THE", "The", "the"], ["BOARD", "BOISE", "Boise", "HOARD", "NOISE", "Noise", "noise"]]

scors = []
txt = []
keys = []

with open("6.txt", "r") as f:
    cipher = base64.b64decode(f.read())
    for key in tqdm(list(itertools.product(*arr))):
        KEY = " ".join(key).encode()
        keys.append(KEY)
        scors.append(englishFreqMatchScore(xor(cipher, KEY).decode()))
        txt.append(xor(cipher, KEY).decode())

max_ = max(scors)
while(max(scors) == max_):
    print("-------------------------------------------------------------")
    print(txt.pop(scors.index(max(scors)))[0:30])
    print(keys.pop(scors.index(max(scors))))
    print("-------------------------------------------------------------")
    del scors[max(scors)]
