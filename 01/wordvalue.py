from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    words = []
    with open(DICTIONARY, 'r') as file:
         words = [line.rstrip() for line in file]
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    #pass
    result = 0
    for letter in word:
        score = LETTER_SCORES.get(letter.upper())
        result = result + score

    return result



def max_word_value(word_list=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    #pass
    score = 0
    word = ""
    if word_list == None:
        word_list = load_words()

    for word_to_check in word_list:
        if not word_to_check.isalpha():
            found_score = 0
        else:
            found_score = calc_word_value(word_to_check)

        if found_score > score:
            score = found_score
            word = word_to_check

    return word


if __name__ == "__main__":
    pass # run unittests to validate

