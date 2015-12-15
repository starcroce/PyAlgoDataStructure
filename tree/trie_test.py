import MyTrie

if __name__ == '__main__':
    dictionary = ['san diego', 'san francisco', 'los angles']
    tree = MyTrie.Trie()
    for word in dictionary:
        tree.insert(word)

    print tree.search_word('san diego')
    print tree.search_word('santa cruz')

    print tree.search_prefix('san')
    print tree.search_prefix('santa')

    print tree.auto_complete('san')
    print tree.auto_complete('sab')
