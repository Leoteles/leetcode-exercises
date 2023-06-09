#%%
#https://leetcode.com/problems/implement-trie-prefix-tree/


#Solution 89% 84%

class Trie:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        node = self.tree
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['has_word'] = True

    def search(self, word: str) -> bool:
        node = self.tree
        for c in word:
            if c in node:
                node = node[c]
            else:
                return False
        if 'has_word' in node:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        node = self.tree
        for c in prefix:
            if c in node:
                node = node[c]
            else:
                return False
        return True

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # return True
print(trie.search("app"))     # return False
print(trie.startsWith("app")) # return True
trie.insert("app")
print(trie.search("app"))     # return True