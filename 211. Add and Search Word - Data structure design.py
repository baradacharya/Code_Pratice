#Trie + DFS
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        trie = self.root
        self.res = False
        self.DFS(trie, word)
        return self.res

    def DFS(self, trie, word):
        if not word:
            if trie.isEnd:
                self.res = True
            return
        ch = word[0]
        if ch == ".":
            for c in trie.children:
                self.DFS(trie.children[c], word[1:])
        else:
            if ch in trie.children:
                self.DFS(trie.children[ch], word[1:])
            return

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)