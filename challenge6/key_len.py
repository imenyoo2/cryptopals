
# msg is in str
def index_of_coindicence(msg):
    for step in range(1, 50):
        match = total = 0
        for i in range(len(msg)):
            for j in range(i + step, len(msg), step):
                total += 1
                if msg[i] == msg[j]: match += 1

        ioc = float(match) / float(total)

        # output the IoC as a percentage, and plot it as an ASCII bar chart
        print("%3d%7.2f%% %s" % (step, 100*ioc, "#" * int(0.5 + 500*ioc)))

def hamming(a, b):
    dif = abs(len(a) - len(b))
    for i in range(min(len(a), len(b))):
        for j in range(8):
            if (1 & (a[i] >> j)) != (1 & (b[i] >> j)):
                dif += 1
    return (dif)

# cipher is in bytes
def get_key_len_hamming(cipher):
    key_size = []
    distance = []
    for key in range(2, 41):
        key_size.append(key)
        #distance.append(hamming(cipher[0:key], cipher[key:2 * key]))
        average = 0
        count = 0
        for i in range(int(len(cipher) / key)):
            for j in range(int(len(cipher) / key) - i - 1):
                average += hamming(cipher[(i)*key:(1+i)*key], cipher[(1+j)*key:(2+j) * key])
                count += 1
        average = average / (count * key)
        #average = hamming(cipher[0:key], cipher[key:2 * key]) / key
        print("%d:%d %s" % (key, average, "#" * (int(average))))