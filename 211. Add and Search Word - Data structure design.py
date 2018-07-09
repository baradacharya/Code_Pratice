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
        cur = self.root
        self.res = False
        self.DFS(cur, word)
        return self.res

    def DFS(self, node, word):
        if not word:
            if node.isEnd:
                self.res = True
            return
        if word[0] == ".":
            for c in node.children:
                self.DFS(node.children[c],word[1:])
        else:
            if word[0] in node.children:
                self.DFS(node.children[word[0]],word[1:])
            return

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)