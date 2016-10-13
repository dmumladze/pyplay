from ps4a import *

def playHand(hand, wordList, n):
    total = 0
    hcopy = hand.copy()

    while sum(hcopy.values()) != 0:
        # Display the hand        
        print('Current Hand: ', displayHand(hcopy))
        # Ask user for input
        userInput = input('Enter word, or a "." to indicate that you are finished: ')
        # If the input is a single period:
        if userInput == '.':
            # End the game (break out of the loop)
            break            
        # Otherwise (the input is not a single period):
        elif userInput != '.': 
            # If the word is not valid:
            if isValidWord(userInput, hcopy, wordList) == False:
                # Reject invalid word (print a message followed by a blank line)
                print('Invalid word, please try again.')
                print()                
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                total += getWordScore(userInput, n)
                print(userInput , 'earned ', getWordScore(userInput, n), 'points. ', 'Total: ', total)
                print()                
                # Update the hand 
                hcopy = updateHand(hcopy, userInput)
                print()

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if userInput == '.' or sum(hcopy.values()) == 0:
        print('Run out of letters. Total score: ', total,' points.')

wordList = loadWords()
playHand({'h':1, 'i':1, 'c':1, 'z':1, 'm':2, 'a':1}, wordList, 7)