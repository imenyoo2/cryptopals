# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    script.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayait-el <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/26 17:40:55 by ayait-el          #+#    #+#              #
#    Updated: 2023/11/26 17:45:57 by ayait-el         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#import enchant
from string import ascii_letters
#from collection import Counter
from englishFreqMatchScore import englishFreqMatchScore

cipher = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

#d = enchant.Dict("en_US")

plains = []
scors = []

for i in range(1, 255):
    decrypt = b""
    for j in cipher:
        letter = chr(j ^ i).encode()
        decrypt += letter
    try:
        plains.append(decrypt.decode())
        scors.append(englishFreqMatchScore(decrypt.decode()))
    except:
        pass

if __name__ == "__main__":
    print(plains[scors.index(max(scors))])
    #print(plains[scors.index(4)])
    #print(scors)
