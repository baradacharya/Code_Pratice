# Trie + DFS
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isWord = False


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board: return []
        self.m, self.n = len(board), len(board[0])

        # 1. build Trie for all words
        root = TrieNode()
        for w in words:
            trie = root
            for c in w:
                if c not in trie.children:
                    trie.children[c] = TrieNode()
                trie = trie.children[c]
            trie.isWord = True

        # 2. perform DFS
        self.res = set()
        for i in range(self.m):
            for j in range(self.n):
                self.DFS(board, i, j, root, '')
        return list(self.res)

    def DFS(self, board, i, j, trie, prefix):
        if trie.isWord:
            self.res.add(prefix)

        if i < 0 or i >= self.m or j < 0 or j >= self.n or board[i][j] == '#' or board[i][j] not in trie.children:
            return
        c = board[i][j]
        board[i][j] = '#'  # mark visited
        self.DFS(board, i + 1, j, trie.children[c], prefix + c)
        self.DFS(board, i - 1, j, trie.children[c], prefix + c)
        self.DFS(board, i, j + 1, trie.children[c], prefix + c)
        self.DFS(board, i, j - 1, trie.children[c], prefix + c)
        board[i][j] = c  # back track

s = Solution()
print s.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"])
