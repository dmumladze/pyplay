# Hangman game

import random
import string

WORDLIST_FILENAME = "./data/words.txt"

def loadWords():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    lettersGuessed = {l:0 for l in lettersGuessed}
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True 

def getGuessedWord(secretWord, lettersGuessed):
    lettersGuessed = {l:0 for l in lettersGuessed}
    wordGuessed = []
    for letter in secretWord:
        if letter in lettersGuessed:
            wordGuessed.append(letter)
        else:
            wordGuessed.append("_")
    return " ".join(wordGuessed)   

def getAvailableLetters(lettersGuessed):
    lettersGuessed = {l:0 for l in lettersGuessed}
    availableLetters = []
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            availableLetters.append(letter)
    return "".join(availableLetters)  
    

def hangman(secretWord):    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {0} letters long.".format(len(secretWord)))
    print("-------------")

    numberOfGuesses = 8
    mistakesMade = 0
    lettersGuessed = {}
    wordGuessed = getGuessedWord(secretWord, lettersGuessed)
    word = {l:0 for l in secretWord}

    while mistakesMade < numberOfGuesses:                        
        print("You have {0} guesses left.".format(numberOfGuesses - mistakesMade))  

        availableLetters = getAvailableLetters(lettersGuessed)
        print("Available Letters: {0}".format(availableLetters))
        guess = input("Please guess a letter: ")        
        guessInLowerCase = guess.lower()  

        if guessInLowerCase in lettersGuessed:
            print("Oops! You've already guessed that letter: {0}".format(wordGuessed))
        else:
            lettersGuessed[guessInLowerCase] = 0
            wordGuessed = getGuessedWord(secretWord, lettersGuessed)
            if guessInLowerCase in word:
                print("Good guess: {0}".format(wordGuessed))
            else:
                print("Oops! That letter is not in my word: {0}".format(wordGuessed))
                mistakesMade += 1
                
        print("-----------")  
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!") 
            return                

    print("Sorry, you ran out of guesses. The word was {0}.".format(secretWord))     

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
