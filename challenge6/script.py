import base64
from englishFreqMatchScore import englishFreqMatchScore, single_byte_xor_cryptanalysis
import string
from key_len import get_key_len_hamming, index_of_coindicence


key_size = []
distance = []

with open("6.txt", "r") as f:
    cipher = base64.b64decode(f.read())
    index_of_coindicence(cipher)
    blocks = []
    print(get_key_len_hamming(cipher))

    probable_key = 29
    print(probable_key)
    # spliting to blocks of probable_key sized chunks
    for i in range(0, len(cipher), probable_key):
        blocks.append(cipher[i:i + probable_key])
    
    lenoflast = len(blocks[-1])
    # brute forcing the key
    KEY = b""
    
    # maybe trying for len of last !!!
    for i in range(0, probable_key):
        line = b""
        results = []
        for chunk in blocks[:-1]:
            line += chr(chunk[i]).encode()
        for key in range(1, 256):
            result = b""
            for byte in line:
                c = chr(key ^ byte)
                result += c.encode()
            results.append(result)
        maxscore = 0
        maxindex = []
        for i in range(0, 255):
            try:
                #print(results[i].decode())
                score = englishFreqMatchScore(results[i].decode())
                #score = single_byte_xor_cryptanalysis(results[i])[1]
                if score >= maxscore:
                    if (chr(i+1) in (string.ascii_letters + " ")):
                        maxscore = score
                        maxindex.append(i)
            except:
                pass
        print(maxscore, [chr(i+1) for i in maxindex])
#print(hamming(b"this is a test", b"wokka wokka!!!"))
