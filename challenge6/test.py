import itertools
from englishFreqMatchScore import englishFreqMatchScore
from tqdm import tqdm

a = [
['H', 'P', 'R', 'S', 'T', 't'],
['E', 'e'],
['A', 'B', 'C', 'G', 'H', 'I', 'P', 'R', 'r'],
['A', 'B', 'D', 'F', 'I', 'J', 'L', 'M', 'm'],
['A', 'C', 'G', 'H', 'I', 'i'],
['A', 'B', 'D', 'N', 'n'],
['A', 'a'],
['A', 'E', 'I', 'O', 'P', 'Q', 'R', 'T', 't'],
['A', 'H', 'O', 'o'],
['A', 'B', 'C', 'G', 'H', 'I', 'O', 'R', 'r']
]

words = []
scors = []

for word in tqdm(list(itertools.product(*a))):
    txt = "".join(word)
    score = englishFreqMatchScore(txt)
    words.append(txt)
    scors.append(score)

max_int = max(scors)
while max(scors) == max_int:
    print(words.pop(scors.index(max_int)))
    del scors[scors.index(max_int)]
