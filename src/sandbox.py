def isWordGuessed(secretWord, lettersGuessed):
    lettersGuessed = {l:0 for l in lettersGuessed}
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True  

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))