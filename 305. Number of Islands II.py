#Reuse the code for Problem 200: Number of Islands,
#for each addLand operation, just call the numIslands function of Problem 200
#to get the number of islands after performing that operation.
#Time Limit Exceeded

#Union Find
"""
Make use of a Union Find data structure of size m*n to store all the nodes in the graph
and initially each node's parent value is set to -1 to represent an empty graph.
Our goal is to update Union Find with lands added by addLand operation and union lands belong to the same island.
Time O(mn+L)
s:O(mn)
"""
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        res = []
        if m<=0 or n <= 0 :
            return res
        count  = 0
        parent = [-1]*(m*n)
        for x,y in positions:
            root = n * x + y #assume new point isolated, increse count
            parent[root] = root
            count += 1

            for i,j in dirs:
                x_ = x + i
                y_ = y + j
                neighbour = n * x_ + y_
                if x_ < 0 or x_ >= m or y_ < 0 or y_ >= n or parent[neighbour] == -1:
                    continue
                parent_neighbour = self.find(parent,neighbour)
                if root != parent_neighbour: #if neighbour in another island merge
                    parent[root] = parent_neighbour
                    root = parent_neighbour
                    count -= 1
            res.append(count)
        return res

    def find(self, parent, id):
        while (id != parent[id]):
            parent[id] = parent[parent[id]]  # Path Compression
            id = parent[id];
        return id

s = Solution()
print s.numIslands2(3,3,[[0,0],[0,1],[1,2],[2,1]])