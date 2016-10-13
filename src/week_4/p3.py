from ps4a import *

def isValidWord(word, hand, wordList):
    if word not in wordList:
        return False
    hcopy = hand.copy()
    for l in word:
        v = hcopy.get(l)
        if v is None or v == 0:
            return False
        else:
            hcopy[l] -= 1
    return True     

words = loadWords()
print(isValidWord('rapture', {'a': 3, 't': 1, 'u': 1, 'p': 2, 'r': 1, 'e': 1}, words))
