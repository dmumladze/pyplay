from ps4a import *

def getWordScore(word, n):
    if not word:
        return 0

    score = 0
    for l in word:
        score += SCRABBLE_LETTER_VALUES.get(l, 0)
    if score > 0:
        score *= len(word)        
    if len(word) == n:
        score += 50
    
    return score

print(getWordScore("waybill", 7))