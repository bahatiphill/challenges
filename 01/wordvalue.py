from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    result = []
    #Open DICTIONARY file in reading mode
    with open(DICTIONARY, mode="r") as f:
        for word in f.readlines():
            result.append(word.strip())
    return result

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    result = 0
    #Get every letter in "word"
    letters = list(word.upper())

    #Loop through it, Get its scrabble value
    for letter in letters:
        if letter not in LETTER_SCORES.keys():
            continue
        result =result + LETTER_SCORES.get(letter)

    return result

def max_word_value(words_list=[]):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    
    words_values = {}
    winner = ["", 0]

    #check if there are words passed in
    if len(words_list) == 0:
        words_list = load_words()

    for word in words_list:
        value = calc_word_value(word)
        #words_values[word] = value
        if value < winner[1]:
            continue
        winner = [word, value]
    return winner[0]

if __name__ == "__main__":
    pass # run unittests to validate
