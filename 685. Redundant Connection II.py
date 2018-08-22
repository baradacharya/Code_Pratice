"""
There are two cases for the tree structure to be invalid.
1) A node having two parents;
   including corner case: e.g. [[4,2],[1,5],[5,2],[5,3],[2,4]]
2) A circle exists
"""
# The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added.

"""
1) Check whether there is a node having two parents. 
    If so, store them as candidates A and B, and set the second edge invalid. 
2) Perform normal union find. 
    If the tree is now valid 
           simply return candidate B
    else if candidates not existing 
           we find a circle, return current edge; 
    else 
           remove candidate A instead of B.
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
                edge[1] = 0 #mark edge invalid, default cand 2 taken

        #2. union find
        #candidate 2 taken
        parent = range(n+1)
        for edge in edges:
            if edge[1] == 0:#invalid edge
                continue
            x = edge[1]
            y = edge[0]
            if x == self.find(parent,y):#cycle found, cand 2 is not soln
                if cand1[0] == -1 :#if cand 1 is  not existing
                    return edge
                return cand1
            parent[x] = y
        return cand2

    def find(self,p,x):
        if p[x]!= x:
            p[x] = self.find(p,p[x])
        return p[x]

s = Solution()
# print s.findRedundantDirectedConnection([[1,2],[1,3],[2,3]])
print s.findRedundantDirectedConnection([[1,2], [2,3], [3,4], [4,1], [1,5]])