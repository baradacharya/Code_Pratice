#https://leetcode.com/problems/game-of-life/discuss/73223/Easiest-JAVA-solution-with-explanation
"""
[2nd bit, 1st bit] = [next state, current state]

- 00  dead (next) <- dead (current)
- 01  dead (next) <- live (current)
- 10  live (next) <- dead (current)
- 11  live (next) <- live (current)

To get the current state, simply do board[i][j] & 1
To get the next state, simply do  board[i][j] >> 1
"""
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or len(board)==0:
            return
        m,n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                lives = self.liveNeighbors(board,m,n,i,j)
                #In the beginning, every 2nd bit is 0; So we only need to care about when will the 2nd bit become 1.
                if board[i][j] == 1 and 2 <= lives <= 3:
                    board[i][j] = 3 #make 2nd bit 1: 01-> 11

                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2 #make 2nd bit 1: 00-> 10

        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j] >> 1 #get 2nd state

    def liveNeighbors(self,board,R,C,r,c):
        lives = 0
        for nr in (r - 1, r, r + 1):
            for nc in (c - 1, c, c + 1):
                if 0 <= nr < R and 0 <= nc < C:
                    lives += board[nr][nc] & 1
        lives -= board[r][c]
        return lives

s = Solution()
print s.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])