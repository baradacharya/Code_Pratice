"""
There are two cases for the tree structure to be invalid.
1) A node having two parents;
   including corner case: e.g. [[4,2],[1,5],[5,2],[5,3],[2,4]]
2) A circle exists
"""
class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        parent = [0] * (n+1)
        cand1 = cand2 = (-1,-1)
        #1. check whether there is a node with two parents
        for edge in edges:
            if parent[edge[1]] == 0:
                parent[edge[1]] = edge[0]
            else:#multiple parents
                cand1 = (parent[edge[1]],edge[1])
                cand2 = tuple(edge)
                edge[1] = 0

        #2. union find
        parent = range(n+1)
        for edge in edges:
            if edge[1] == 0:#invalid edge
                continue
            x = edge[1]
            y = edge[0]
            if x == self.find(parent,y):#cycle found
                if cand1[0] == -1 :
                    return edge
                return cand1
            parent[x] = y
        return cand2


    def find(self, parent, id):
        while (id != parent[id]):
            parent[id] = parent[parent[id]]  # Path Compression
            id = parent[id];
        return id

s = Solution()
# print s.findRedundantDirectedConnection([[1,2],[1,3],[2,3]])
print s.findRedundantDirectedConnection([[1,2], [2,3], [3,4], [4,1], [1,5]])