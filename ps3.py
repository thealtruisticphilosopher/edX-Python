import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
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
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for ch in secretWord:
        if ch not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word = ''
    for ch in secretWord:
        if ch not in lettersGuessed:
            word += '_ '
        else:    
            word += ch
    return word


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letters = string.ascii_lowercase
    avblLetters = ''
    for ch in letters:
        if ch not in lettersGuessed:
            avblLetters += ch
    
    return avblLetters

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print ("Welcome to the game, Hangman!")
    secretWord = chooseWord(wordlist)
    print ("I am thinking of a word that is", len(secretWord), "letters long")
    print ("- - - - - - - - - - - - - - -")
    guesses = 8
    lettersGuessed = []
    while guesses>0:
        print ("You have", guesses, "guesses left.")
        print ("Available letters: " + getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        guessL = guess.lower()
        
        if guessL in secretWord:
            if guessL in lettersGuessed:
                print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                print ("- - - - - - - - - - - - - - -")
            else:
                lettersGuessed.append(guessL)
                word = getGuessedWord(secretWord, lettersGuessed)
                print ("Good guess: " + word)
                print ("- - - - - - - - - - - - - - -")
                if word==secretWord:
                    print ("Congratulations, you won!")
                    break
        
        else:
            if guessL in lettersGuessed:
                print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                print ("- - - - - - - - - - - - - - -")
            else:
                lettersGuessed.append(guessL)
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                print ("- - - - - - - - - - - - - - -")
                guesses -= 1
                if guesses==0:
                    print ("Sorry, you ran out of guesses. The word was " + secretWord + ".")
        

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)