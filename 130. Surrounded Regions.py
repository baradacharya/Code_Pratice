"""
First, check the four border of the matrix. If there is a element is
'O', alter it and all its neighbor 'O' elements to '1'.
Then ,alter all the 'O' to 'X'
At last,alter all the '1' to 'O'
"""
# BFS
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: return None
        import collections
        queue = collections.deque()
        m, n = len(board), len(board[0])
        # 1. add all boarder 'O' to queue.
        for i in range(m):
            if board[i][0] == 'O': queue.append((i, 0))
            if board[i][n - 1] == 'O': queue.append((i, n - 1))
        for j in range(1, n - 1):
            if board[0][j] == 'O': queue.append((0, j))
            if board[m - 1][j] == 'O': queue.append((m - 1, j))

        # change those points anf their neighbours to '1'
        while queue:
            i, j = queue.popleft()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = '1'
                queue.append((i + 1, j))
                queue.append((i - 1, j))
                queue.append((i, j + 1))
                queue.append((i, j - 1))
        # alter all O to x and 1 to O
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O': board[i][j] = 'X'
                if board[i][j] == '1': board[i][j] = 'O'
s = Solution()
# print s.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
print s.solve([["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]])

