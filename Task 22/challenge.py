# Task 1.

def add_prefix_un(word):

    """Add the prefix 'un' to a word.
    :param word: a string that represents a word
    :return: a new string that has the prefix 'un' added to the word
    """

    un_prefixed_word = "un" + word
    return un_prefixed_word


print(add_prefix_un("happy"))
print(add_prefix_un("manageable"))


# Task 2.

def make_word_groups(vocab_words):

    """Concatenate a prefix to a list of words with a separator.
       :param vocab_words: a list of strings in the form of [<prefix>, <word_1>, <word_2>, ..., <word_n>]
       :return: a string that concatenates the prefix and each word with a separator '::'
    """
    
    prefix = vocab_words[0]
    word_1 = prefix + vocab_words[1]
    word_2 = prefix + vocab_words[2]
    word_3 = prefix + vocab_words[3]

    return prefix + " :: " + word_1 + " :: " + word_2 + " :: " + word_3

print(make_word_groups(['en', 'close', 'joy', 'lighten']))
print(make_word_groups(['pre', 'serve', 'dispose', 'position']))
print(make_word_groups(['auto', 'didactic', 'graph', 'mate']))
print(make_word_groups(['inter', 'twine', 'connected', 'dependent']))


# Task 3.

def remove_suffix_ness(word):
    """Remove the suffix 'ness' from a word.
    If the fifth last letter of the word is 'i', replace it with 'y'.
    Otherwise, just remove the last four letters.
    """
    if word[-5] == "i":
        return word[:-5] + "y"
    else:
        return word[:-4]

print(remove_suffix_ness("heaviness"))
print(remove_suffix_ness("sadness"))


# Task 4

def adjective_to_verb(sentence, index):
    """Converts an adjective in a sentence to a verb.

    Parameters:
    sentence (str): a sentence using the vocabulary word
    index (int): the index of the word, once the sentence is split
    
    Returns:
    str: the extracted adjective as a verb, ending with "en"
    """

    sentence = sentence.strip(".").split()
    return sentence[index] + "en"
    
print(adjective_to_verb('I need to make that bright.', -1 ))
print(adjective_to_verb('It got dark as the sun set.', 2))
