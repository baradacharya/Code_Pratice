# detetct cycle, undirected, #207
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        self.p = range(n)
        if len(edges) != n - 1:#all node should be connected
            return False
        for edge in edges:
            x = self.find(edge[0])
            y = self.find(edge[1])
            if x == y:
                return False
            self.union(x,y)
        return True

    def find(self, i):
        if self.p[i] != i:  # i is not root
            i = self.find(self.p[i])  # find the parent
        return i

    # A utility function to do union of two subsets
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)  # we can do vice-versa




s = Solution()
print s.validTree(5,[[0,1],[1,2],[2,3],[1,3],[1,4]])
print s.validTree(5,[[0,1], [0,2], [0,3], [1,4]])