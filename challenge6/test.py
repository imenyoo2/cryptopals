import itertools
from englishFreqMatchScore import englishFreqMatchScore
from tqdm import tqdm
import enchant

a = [
['B', 'C', 'D', 'H', 'I', 'N', 'n'],
['O', 'o'],
['A', 'D', 'H', 'I', 'i'],
['A', 'B', 'R', 'S', 's'],
['C', 'D', 'E', 'e']
]

words = []
scors = []
d = enchant.Dict("en_US")

for word in tqdm(list(itertools.product(*a))):
    txt = "".join(word)
    score = englishFreqMatchScore(txt)
    words.append(txt)
    scors.append(score)

for word in tqdm(words):
    if d.check(word):
        print(word)
