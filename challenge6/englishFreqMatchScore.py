#Frequency Finder
# http://inventwithpython.com/hacking (BSD Licensed)
# frequency taken from http://en.wikipedia.org/wiki/Letter_frequency

englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getLetterCount(message):
    # Returns a dictionary with keys of single letters and values of the
    # count of how many times they appear in the message parameter.
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1

    return letterCount


def getItemAtIndexZero(x):
    return x[0]


def getFrequencyOrder(message):
    # Returns a string of the alphabet letters arranged in order of most
    # frequently occurring in the message parameter.

    # first, get a dictionary of each letter and its frequency count
    letterToFreq = getLetterCount(message)

    # second, make a dictionary of each frequency count to each letter(s)
    # with that frequency
    freqToLetter = {}
    for letter in LETTERS:
        if letterToFreq[letter] not in freqToLetter:
            freqToLetter[letterToFreq[letter]] = [letter]
        else:
            freqToLetter[letterToFreq[letter]].append(letter)

    # third, put each list of letters in reverse "ETAOIN" order, and then
    # convert it to a string
    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])

    # fourth, convert the freqToLetter dictionary to a list of tuple
    # pairs (key, value), then sort them
    freqPairs = list(freqToLetter.items())
    freqPairs.sort(key=getItemAtIndexZero, reverse=True)

    # fifth, now that the letters are ordered by frequency, extract all
    # the letters for the final string
    freqOrder = []
    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])

    return ''.join(freqOrder)

from letter_freq import reference_letter_freq_dict
import string

def fixed_xor(bytes1, bytes2):
    """Challenge 2
    XORs two equal-length bytes objects or byte arrays
    """
    assert len(bytes1) == len(bytes2), "You must pass equal-length objects"
    """
    Here we create tuple a, b for each pair of bytes in the inputs. Each byte is represented as an integer.
    We perform a bitwise xor on each pair, then create a list of the XOR'd bytes in sequence.
    Finally, we join all of these bytes together to a new bytes object and return it.
    """
    return bytes().join([bytes([a ^ b]) for a, b in zip(bytes1, bytes2)])

def single_byte_xor_cryptanalysis(ciphertext):
    """Challenge 3
    Performs cryptanalysis on a bytes object (ciphertext) that has been XOR'd against a single byte.
    Returns tuple of most likely plaintext, most likely key byte, and likelihood score.
    """
    plaintexts_dict = {}  # Holds each candidate plaintext and its score
    keys_dict = {}  # Holds each candidate key and its score
    for key_byte in range(256):  # Try decrypting using each byte
        xor_bytes = bytes([key_byte]) * len(ciphertext)  # Expand candidate byte to length of ciphertext
        candidate_plaintext = fixed_xor(ciphertext, xor_bytes)
        # Calculate score of candidate_plaintext using weights from a frequency distribution of letter usage
        score = float(0)
        for pt_byte in candidate_plaintext:
            c = chr(pt_byte)
            if c in string.ascii_lowercase:
                score += reference_letter_freq_dict[c]
            # Upper-case letters count slightly less than lower-case
            if c in string.ascii_uppercase:
                score += reference_letter_freq_dict[c.lower()] * 0.75
        score /= len(ciphertext)  # Normalize score over length of plaintext
        # Decrement score by 5% for every character that is not a letter, number, or common punctuation
        for pt_byte in candidate_plaintext:
            if chr(pt_byte) not in (string.ascii_letters + " ,.'?!\"\n"):
                score *= 0.95
        plaintexts_dict[candidate_plaintext] = score
        keys_dict[key_byte] = score
    return max(plaintexts_dict, key=plaintexts_dict.get), \
           max(keys_dict, key=keys_dict.get), \
           max(plaintexts_dict.values())

def englishFreqMatchScore(message):
    # Return the number of matches that the string in the message
    # parameter has when its letter frequency is compared to English
    # letter frequency. A "match" is how many of its six most frequent
    # and six least frequent letters is among the six most frequent and
    # six least frequent letters for English.
    freqOrder = getFrequencyOrder(message)

    matchScore = 0
    # Find how many matches for the six most common letters there are.
    for commonLetter in ETAOIN[:6]:
        if commonLetter in freqOrder[:6]:
            matchScore += 1
    # Find how many matches for the six least common letters there are.
    for uncommonLetter in ETAOIN[-6:]:
        if uncommonLetter in freqOrder[-6:]:
            matchScore += 1

    return matchScore

if __name__ == "__main__":
    print(englishFreqMatchScore("hello wordl"));
    print(single_byte_xor_cryptanalysis(b"hello wordl"));
    print(englishFreqMatchScore("sdfsddfsdfsdf"));
    print(single_byte_xor_cryptanalysis(b"sdfsddfsdfsdf"));
    print(englishFreqMatchScore("this is stupid"));
    print(single_byte_xor_cryptanalysis(b"this is stupid"));
