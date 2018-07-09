"""
https://leetcode.com/problems/implement-trie-prefix-tree/solution/
"""


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.data = None
        self.rank = 0


class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.keyword = ""
        for i, sentence in enumerate(sentences):
            self.addRecord(sentence, times[i])

    def addRecord(self, sentence, time):
        cur = self.root
        for c in sentence:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True
        cur.data = sentence
        cur.rank -= time  # to sort in descending order

    def dfs(self, root):
        ret = []
        if root:
            if root.isEnd:
                ret.append((root.rank, root.data))
            for c in root.children:
                ret.extend(self.dfs(root.children[c]))
        return ret

    def search(self, sentence):
        cur = self.root
        for c in sentence:
            if c not in cur.children:
                return []
            cur = cur.children[c]
        return self.dfs(cur)

    def input(self, c):
        results = []
        if c != "#":
            self.keyword += c  # add ch in each input
            results = self.search(self.keyword)
        else:
            self.addRecord(self.keyword, 1)
            self.keyword = ""
        return [item[1] for item in sorted(results)[:3]]
# Your AutocompleteSystem object will be instantiated and called as such:
sentences =["AutocompleteSystem","input","input","input","input"]
obj = AutocompleteSystem(["i love you","island","iroman","i love leetcode"],[5,3,2,2])
print obj.input("i")
print obj.input(" ")
print obj.input("a")
print obj.input("#")


