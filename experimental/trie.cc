// C++ implementation of search and insert 
// operations on Trie
#include <algorithm>
#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

const int ALPHABET_SIZE = 24 * 16;

// trie node
struct TrieNode
{
    struct TrieNode *children[ALPHABET_SIZE];
    wstring word = L"";
    // isEndOfWord is true if the node represents
    // end of a word
    bool isEndOfWord;
};

// Returns new trie node (initialized to NULLs)
struct TrieNode *getNode(void)
{
    struct TrieNode *pNode = new TrieNode;

    pNode->isEndOfWord = false;

    for (int i = 0; i < ALPHABET_SIZE; i++)
        pNode->children[i] = NULL;

    return pNode;
}

// If not present, inserts key into trie
// If the key is prefix of trie node, just
// marks leaf node
void insert(struct TrieNode *root, wstring ukey)
{
    //wstring ukey(key.begin(), key.end());
    struct TrieNode *pCrawl = root;

    for (int i = 0; i < ukey.length(); i++)
    {
        int index = ukey[i] - L'ሀ';

        if ( 0 <= index and index < ALPHABET_SIZE){
           if(!pCrawl->children[index])
                pCrawl->children[index] = getNode();
           pCrawl = pCrawl->children[index];
        }
    }
    pCrawl->word = ukey;
    // mark last node as leaf
    pCrawl->isEndOfWord = true;
}

void searchRecursive( TrieNode* node, wchar_t letter, wstring word,
                      vector<int>& previousRow,
                      vector<pair<wstring,int>>& results, int maxCost )
{
    int columns = word.length() + 1;
    vector<int> currentRow;
    currentRow.push_back(previousRow[0] + 1);

    // Build one row for the letter, with a column for each letter in the target
    // word, plus one for the empty string at column 0
    for (int i = 1; i < columns ; i++ ){

        int insertCost = currentRow[i - 1] + 1;
        int deleteCost = previousRow[i] + 1;
        int replaceCost = 0;

        if (word[i - 1] != letter)
            replaceCost = previousRow[ i - 1 ] + 1;
        else
            replaceCost = previousRow[ i - 1 ];
        std::vector<int> costs{insertCost, deleteCost, replaceCost};
        int minimum = *std::min_element(costs.begin(), costs.end());
        currentRow.push_back(minimum);
    }
    //if the last entry in the row indicates the optimal cost is less than the
    // maximum cost, and there is a word in this trie node, then add it.
    if (currentRow[currentRow.size() - 1] <= maxCost and (node->word).length() )
        results.push_back(std::make_pair(node->word,
                    currentRow[currentRow.size() - 1]));

    // if any entries in the row are less than the maximum cost, then 
    // recursively search each branch of the trie
    if (*std::min_element(currentRow.begin(), currentRow.end()) <= maxCost)
        for (int i = 0; i < ALPHABET_SIZE; i++)
        {
            if(node->children[i] != nullptr) {
                wchar_t letter = wchar_t((unsigned int)i  + (unsigned int)L'ሀ');
                searchRecursive(node->children[i], letter, word, currentRow,
                        results, maxCost );
            }
        }
}

// The search function returns a list of all words that are less than the given
// maximum distance from the target word
vector<pair<wstring, int>> search(wstring word, int maxCost , TrieNode* root)
{

    //build first row
    vector<int> currentRow(word.length() + 1);
    for(int i = 0; i < currentRow.size(); i++)
        currentRow[i] = i;

    vector<pair<wstring,int>> results;
    // recursively search each branch of the trie
    for (int i = 0; i < ALPHABET_SIZE; i++)
    {
        if(root->children[i] != nullptr) {
            wchar_t letter = wchar_t((unsigned int)i  + (unsigned int)L'ሀ');
            searchRecursive(root->children[i], letter, word, currentRow,
                    results, maxCost );
        }
    }

    return results;
}
string trim(const string& str)
{
    size_t first = str.find_first_not_of(' ');
    if (string::npos == first)
    {
        return str;
    }
    size_t last = str.find_last_not_of(' ');
    return str.substr(first, (last - first + 1));
}

void build_trie_from_file(std::ifstream& infile, TrieNode * root) {
    std::string line;
    while (std::getline(infile, line))
    {std::locale loc ("");
    std::locale::global (loc);
    std::wcout.imbue (loc);
    infile.imbue(loc);

        std::istringstream iss(line);
        iss.imbue(loc);
        string word; int freq;
        if (!(iss >> word >> freq)) { break; } // error
        word = trim(word);
        printf("WORD: %s", word.c_str());
        wstring wsword = wstring(word.begin(), word.end());
        std::wcout << L" Inserting: " << wsword << L" Freq: " << freq << L"\n";
        if(wsword == L":ባለዐደራ"){
            std::wcout << "YES! target is inserted.\n";
            return;
        }
        insert(root, wsword);
        // process pair (a,b)
    }
}
// Driver

int main()
{
    // Input keys (use only 'a' through 'z'
    // and lower case)
    string keys[] = {"the", "a", "there",
        "answer", "any", "by",
        "bye", "their" };
    wstring ukeys [] = {L"ትቅምት", L"በዋጃት", L"ሙዳይን", L"እየወደዱ",
        L"ሙዳዩን", L"ይፋረደዋል", L"ገዝቶም", L"ባለዐደራ"};


    int n = sizeof(keys)/sizeof(keys[0]);
    n = 8;

    struct TrieNode *root = getNode();
    //std::locale loc ("");
    //std::locale::global (loc);
    //std::wcout.imbue (loc);
    //wstring am = L"ሁሀ";
    //std::wcout << (unsigned int)am[0] - (unsigned int)L'ሀ' << std::endl;

    std::ifstream infile("data/dictionary.txt");
    //infile.imbue(loc);
    //Building the Trie
    build_trie_from_file(infile, root);

    // Construct trie
    //for (int i = 0; i < n; i++)
    //    insert(root, ukeys[i]);

    // Search for different keys
    std::vector<std::pair<wstring,int>> result = search( L"ባደራ", 2, root);
    std::wcout << L"MATCHING: \n" << result.size() << L" found.\n";
    for(auto& p : result){
        std::wcout << p.first << " " << p.second << '\n';
    }
    return 0;
}
