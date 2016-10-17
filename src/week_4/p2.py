from ps4a import *

def updateHand(hand, word):
    result  = hand.copy()
    for l in word:
        score = result.get(l, None)
        if score:
            result[l] -= 1
    return result

hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
print(hand)
displayHand(hand)
hand = updateHand(hand, 'quail')
print(hand)
displayHand(hand)

