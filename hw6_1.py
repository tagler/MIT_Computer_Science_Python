# 6.00x Problem Set 6
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """

    lowers = string.ascii_lowercase
    lowers_cipher = ''
    uppers = string.ascii_uppercase
    uppers_cipher = ''

    # lowercase shift
    for x in range(0, 26) :
        if (x+shift > 25):
            index = x + shift - 26
        else:
            index = x + shift
        lowers_cipher += ( lowers[index] )

    # uppercase shift
    for y in range(0, 26) :
        if (y+shift > 25):
            index = y + shift - 26
        else:
            index = y + shift
        uppers_cipher += ( uppers[index] )

    # combine letters into single string to create dictionary
    plain_text = lowers + uppers
    cipher_text = lowers_cipher + uppers_cipher

    # map dictionary
    dic = {}
    for z in range(0, 52):
        dic[ plain_text[z] ] = cipher_text[z]

    return dic

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    output = ''

    for x in range(0, len(text)):
        if text[x] not in coder:
            output += text[x]
        else:
            output += coder[ text[x] ]
    return output

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text, buildCoder(shift) )

#
# Problem 2: Decryption
#

"""
1. Set the maximum number of real words found to 0.
2. Set the best shift to 0.
3. For each possible shift from 0 to 26:
	4. Shift the entire text by this shift.
	5. Split the text up into a list of the individual words.
	6. Count the number of valid words in this list.
	7. If this number of valid words is more than the largest number of
	   real words found, then:
		8. Record the number of valid words.
		9. Set the best shift to the current shift.
	10. Increment the current possible shift by 1. Repeat the loop
	   starting at line 3.
11. Return the best shift.
"""

def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    most_words = 0
    best_shift = 0

    for shift in range(0,26):

        test_shift = applyShift(text, shift)
        words = test_shift.split()
        word_count = 0

        for each in words:
            if ( isWord(wordList, each) ):
                word_count += 1

        if (word_count > best_shift):
            most_words = word_count
            best_shift = shift

    return best_shift

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    wordList = loadWords()
    story_string = getStoryString()
    find_shift = findBestShift(wordList, story_string)
    decode = applyShift(story_string, find_shift)
    return decode

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
    assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    #    decryptStory()
