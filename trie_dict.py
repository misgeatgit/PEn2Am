# encoding=utf8
#!/usr/bin/python
#By Steve Hanov, 2011. Released to the public domain
import time
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

DICTIONARY = "/usr/share/dict/words";
DICTIONARY = "data/dictionary.txt";

# Keep some interesting statistics
NodeCount = 0
WordCount = 0

# The Trie data structure keeps a set of words, organized with one node for
# each letter. Each node has a branch for each letter that may follow it in the
# set of words.
class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}

        global NodeCount
        NodeCount += 1

    def insert( self, word ):
        node = self
        for letter in word:
            #print("Inserting {}".format(letter))
            if letter not in node.children: 
                node.children[letter] = TrieNode()

            node = node.children[letter]

        node.word = word

# The search function returns a list of all words that are less than the given
# maximum distance from the target word
def search( trie, word, maxCost ):

    # build first row
    currentRow = range( len(word) + 1 )

    results = []

    # recursively search each branch of the trie
    for letter in trie.children:
        searchRecursive( trie.children[letter], letter, word, currentRow, 
            results, maxCost )

    return results

# This recursive helper is used by the search function above. It assumes that
# the previousRow has been filled in already.
def searchRecursive( node, letter, word, previousRow, results, maxCost ):

    columns = len( word ) + 1
    currentRow = [ previousRow[0] + 1 ]

    # Build one row for the letter, with a column for each letter in the target
    # word, plus one for the empty string at column 0
    for column in range( 1, columns ):

        insertCost = currentRow[column - 1] + 1
        deleteCost = previousRow[column] + 1

        if word[column - 1] != letter:
            replaceCost = previousRow[ column - 1 ] + 1
        else:
            replaceCost = previousRow[ column - 1 ]

        currentRow.append( min( insertCost, deleteCost, replaceCost ) )

    # if the last entry in the row indicates the optimal cost is less than the
    # maximum cost, and there is a word in this trie node, then add it.
    if currentRow[-1] <= maxCost and node.word != None:
        results.append( (node.word, currentRow[-1] ) )

    # if any entries in the row are less than the maximum cost, then 
    # recursively search each branch of the trie
    if min( currentRow ) <= maxCost:
        for letter in node.children:
            searchRecursive( node.children[letter], letter, word, currentRow, 
                results, maxCost )

def load_dict(trie):
    global WordCount
    with open(DICTIONARY, "rt") as word_freq:
        for wf in word_freq:
            word = wf.split()[0].strip()
            WordCount += 1
            trie.insert(word)

if __name__ == '__main__':
    # read dictionary file into a trie
    trie = TrieNode()
    load_dict(trie)
    print("Read {} words into {} nodes".format(WordCount, NodeCount))
    TARGET = sys.argv[1]
    MAX_COST = int(sys.argv[2])
    start = time.time()
    results = search(trie, TARGET, MAX_COST )
    end = time.time()

    for result in results: print("({},{})".format(result[0], result[1]))

    print("Search took {} s".format(end - start))
