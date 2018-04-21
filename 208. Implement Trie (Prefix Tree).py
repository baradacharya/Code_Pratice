"""
https://leetcode.com/problems/implement-trie-prefix-tree/solution/
"""
class TriNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TriNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur  = self.root
        for c in word:
            if c not in cur.children: #if char not in trienode insert new node
                cur.children[c] = TriNode()
            #then traverse along its children
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur  = self.root
        for c in word:
            if c  not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isEnd


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur  = self.root
        for c in prefix:
            if c  not in cur.children:
                return False
            cur = cur.children[c]
        return True

# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("leet")
print trie.search("leet")
print trie.startsWith("le")

