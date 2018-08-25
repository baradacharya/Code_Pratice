#2 (Breadth-first Search)


class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if len(rooms)==0: return
        EMPTY = 2147483647
        GATE = 0
        DIRECTIONS = [(0,1),(1,0),(0,-1),(-1,0)]
        queue = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == GATE:
                    queue.append((i,j))
        while queue:
            x,y = queue.pop(0)
            for dir in DIRECTIONS:
                x_ = x + dir[0]
                y_ = y + dir[1]
                if 0 <= x_ < len(rooms) and 0 <= y_ < len(rooms[0]) and rooms[x_][y_] == EMPTY:
                    rooms[x_][y_] = rooms[x][y] + 1
                    queue.append((x_,y_))

s = Solution()
print s.wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]])

