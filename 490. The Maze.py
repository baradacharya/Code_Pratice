#1 Depth First Search [Time Limit Exceeded]
#BFS
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        Queue = [start]
        n = len(maze)
        m = len(maze[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while Queue:
            i, j = Queue.pop(0)
            maze[i][j] = 2

            if i == destination[0] and j == destination[1]:
                return True

            for x, y in dirs:
                row = i + x
                col = j + y
                while 0 <= row < n and 0 <= col < m and maze[row][col] != 1:
                    row += x
                    col += y
                row -= x
                col -= y
                if maze[row][col] == 0:
                    Queue.append([row, col])

        return False


#DFS
class Solution(object):
    def hasPath(self, maze, start, destination):
        return self.helper(maze, destination, start[0], start[1])

    def helper(self, maze, dest, i, j):
        if [i, j] == dest:
            return True
        if maze[i][j] == 2:
            return False
        up, down, left, right = i, i, j, j
        while up > 0 and maze[up - 1][j] != 1:
            up -= 1
        while down < len(maze) - 1 and maze[down + 1][j] != 1:
            down += 1
        while left > 0 and maze[i][left - 1] != 1:
            left -= 1
        while right < len(maze[0]) - 1 and maze[i][right + 1] != 1:
            right += 1
        maze[i][j] = 2
        return self.helper(maze, dest, up, j) \
               or self.helper(maze, dest, down, j) \
               or self.helper(maze, dest, i,left) \
               or self.helper(maze, dest, i, right)