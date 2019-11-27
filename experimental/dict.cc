// C++ implementation of search and insert 
// operations on Trie
#include <algorithm>
#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <bits/stdc++.h>
#include "bktree.hpp"
#include "trie.hpp"
using namespace std;

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

void build_trie_from_file(std::ifstream& infile, trie * root) {
    std::string line;
    while (std::getline(infile, line))
    {
        std::istringstream iss(line);
        string word;
        int freq;
        if (!(iss >> word >> freq)) { break; } // error
        word = trim(word);
        std::cout << " Inserting: " << word << " Freq: " << freq << "\n";
        root->insert(word);
        //if(word == "ባለዐደራ"){
        //    std::cout << "YES! target is inserted.\n";
        //    return;
        //}
        // process pair (a,b)
    }
}

// Driver

int main()
{
    string keys[] = {"the", "a", "there",
        "answer", "any", "by",
        "bye", "their" };
    wstring ukeys [] = {L"ትቅምት", L"በዋጃት", L"ሙዳይን", L"እየወደዱ",
        L"ሙዳዩን", L"ይፋረደዋል", L"ገዝቶም", L"ባለዐደራ"};


    int n = sizeof(keys)/sizeof(keys[0]);
    n = 8;

    //struct TrieNode *root = getNode();
    trie * root = new trie();

    std::ifstream infile("data/dictionary.txt");
    //infile.imbue(loc);
    //Building the Trie
    build_trie_from_file(infile, root);

    // Construct trie
    //for (int i = 0; i < n; i++)
    //    insert(root, ukeys[i]);

    // Search for different keys
    std::vector<string> result = root->search("ባደራ", 1);
    std::wcout << "MATCHING: \n" << result.size() << " found.\n";
    for(auto& p : result){
        std::cout << p <<  '\n';
    }
    return 0;
}
