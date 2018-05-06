class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False

        #check for word from each i,j position of board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.DFS(board,i,j,word):
                    return True
        return False

    def DFS(self,board,i,j,word):

        if len(word) == 0: #1. word is found
            return True

        #2.check for validity of board
        if i < 0 or i >= len(board) or j < 0  or j >= len(board[0]) or board[i][j] != word[0]:
            return False

        temp = board[i][j] #3. 1st char found
        board[i][j] = "#"#to avoid retraverse
        #4. Call recursively.
        if self.DFS(board,i+1,j,word[1:]) or self.DFS(board,i-1,j,word[1:]) \
            or self.DFS(board,i,j+1,word[1:])  or self.DFS(board,i,j-1,word[1:]) :
            return True
        board[i][j] = temp #backtrack
        return False
s = Solution()
board = \
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
# print s.exist(board,"ABCCED")
print s.exist(board,"SEE")
# print s.exist(board,"ABCB")
# print s.exist(board,"ABCCED")