# encoding=utf8
import operator
import sys
import time
#reload(sys)
#sys.setdefaultencoding('utf8')
from keymap import *
from trie_dict import *


trie = TrieNode()

print("Loading dictionary...")
ti = time.time()
load_dict(trie)
print("Loaded dict in {} sec.".format(time.time() - ti))

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
            #print("{} matched {}".format(key, "".join(first_chars)))
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

# Computes the cartesian product of arbitrary number of sets.
def _cartesian(elements_set):
    result = []
    if len(elements_set) == 0:
        return result
    if len(elements_set) == 1:
        return [[e] for e in elements_set[0]]
    for i in range(0, 1):
        products = _cartesian(elements_set[i+1: ])
        for j in range(0, len(elements_set[i])):
            for prdct in products:
                result.append([elements_set[i][j]] + prdct)

    return result

def generate_sentence(en_sent):
    words = tokenize(en_sent)
    sentence_words = []
    for word in words:
        am_words = generate_am_words(word)
        sentence_words.append(am_words)

    # sort words by their edit distance.
    # for now if word is not found, lets assume it is unknown.
    scored_sentence_words = []
    for words in sentence_words:
        scored_words = []
        found = False
        for word in words:
            print("Calculating the edit distance for {}".format(word))
            max_cost = 1 if len(word) <= 4 else 2
            results = search(trie, word, max_cost)
            if len(results) >= 1:
                results.sort(key=operator.itemgetter(1))
                # Choose the word with the least cost.
                print(" Found a possible match {} with score {}".format(str(results[0][0]), results[0][1]))
                scored_words.append(results[0])
                found = True
            else:
                print("{} is unkown to our dictionary".format(word))
        if not found:
            print("no single word was a match to {}. Exiting.".format(words))
            return []
        scored_words.sort(key=operator.itemgetter(1))
        scored_sentence_words.append(scored_words)

    sentences = []
    sent = ""
    for i in range(0, len(scored_sentence_words)):
        print("Chose word {} with cost {}".format(str(scored_sentence_words[i][0][0]), scored_sentence_words[i][0][1]))
        sent += (str(scored_sentence_words[i][0][0]) + " ")
    sentences.append(sent)
    # This is is a very costly and perhaps not that useful strategy.
    '''
    combs = _cartesian(sentence_words)
    sentences = []
    for i in range(0, len(combs)):
        sent = ""
        for j in range(0, len(combs[i])):
           sent += combs[i][j]+ " "
        sentences.append(sent)
    '''
    return sentences
'''
en_word = "lili"
for am_word in generate_am_words(en_word):
    print(am_word)
'''
'''
# test cartesian
for result in _cartesian([['x', 'y', 'z'], ['a', 'b', 'c'], ['f', 'j', 'k']]):
    print(result)
'''

for sent in generate_sentence("lili konjo lij nat"):
    print(sent)

