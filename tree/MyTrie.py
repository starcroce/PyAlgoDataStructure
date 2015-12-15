from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.chars = defaultdict(TrieNode)
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for w in word:
            curr = curr.chars[w]
        curr.isWord = True

    def search_word(self, word):
        curr = self.root
        for w in word:
            if w not in curr.chars:
                return False
            curr = curr.chars[w]
        return curr.isWord

    def search_prefix(self, prefix):
        curr = self.root
        for w in prefix:
            if w not in curr.chars:
                return False
            curr = curr.chars[w]
        return True

    def auto_complete(self, prefix):
        curr = self.root
        for w in prefix:
            if w not in curr.chars:
                return []
            curr = curr.chars[w]
        res, sol = [], ''
        self.auto_complete_helper(curr, sol, res)
        return [prefix + sol for sol in res]

    def auto_complete_helper(self, node, sol, res):
        if len(node.chars) == 0 and node.isWord:
            res.append(sol)
            return
        for c in node.chars:
            sol += c
            self.auto_complete_helper(node.chars[c], sol, res)
