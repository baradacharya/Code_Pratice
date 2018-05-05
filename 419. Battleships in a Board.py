
"""
count first cell of the battleship.(top-left most cell)
"""
#less time complexity
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m,n = len(board),len(board[0])
        count  = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.': continue
                if (i > 0 and board[i-1][j] == 'X'): continue #left  side exists ,not top-left
                if (j > 0 and board[i][j-1] == 'X'): continue #upper  side exists, not top-left
                count += 1
        return count


#DFS
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        def dfs(i,j):
            if i >= len(board) or i < 0 or j >= len(board[0]) or j <0 or board[i][j] == '.':
                return False
            board[i][j] = '.'
            dfs(i+1,j)
            dfs(i,j+1)
            return True
        if not board: return 0
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j):
                    count += 1
        return count