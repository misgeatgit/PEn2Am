# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from keymap import *
#from trie_dict import *

# This may end up doing more complex tokenizations.
def tokenize(sentence):
    return sentence.split()

# Generate all possible combination of amharic characters
# which is represented by the given english word string.
def generate_am_words(en_word):
    am_words = []
    if en_word == '':
        return am_words

    # Assuming the maximum length of english char sequence which
    # reprensents a single amharic char is three.
    for i in range(0, 3):
        key = en_word[0: i+1]
        if key in KEY_MAP:
            first_chars = KEY_MAP[key]
            print("{} matched {}".format(key, unicode("".join(first_chars))))
            # If we don't have any more english substring to match for.
            if len(en_word)-1 < i+1:
                for char in first_chars:
                    am_words.append(char)
                break
            substr_list = generate_am_words(en_word[i+1: ])
            if len(substr_list) > 0:
                for char in first_chars:
                    for substr in substr_list:
                        am_words.append(char + substr)

    return am_words


def _combination(elements_set):
    result = []
    for i in range(0, len(elements_set)):
        for j in range(0, len(elements_set[i])):
            if i + 1 < len(elements_set):
                for cmb in _combination(elements_set[i+1: ]):
                    result.append([elements_set[i][j]] + cmb)
            else:
                result.append([elements_set[i][j]])

    return result

def generate_sentence(en_sent):
    words = (en_sent)
    sentence_words = []
    for word in words:
        am_words = generate_am_words(word)
        sentence_words.append(am_words)

    sentences = _combination(sentence_words)
    # TODO Use edit distance for scoring
    return sentnces
'''
en_word = "lili"
for am_word in generate_am_words(en_word):
    print(unicode(am_word))
'''
# test combination
for result in _combination([['x', 'y', 'z'], ['a', 'b', 'c'], ['f', 'j', 'k']]):
    print(result)
