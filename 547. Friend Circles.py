class Solution(object):
    #number of  connected components of a graph
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited  = set()
        ans  = 0
        for i in range(len(M)):
            if i not in visited:
                visited.add(i)
                self.DFS(i,visited,M)
                ans += 1
        return ans

    def DFS(self,i,visited,M):
        for j,connected in enumerate(M[i]):
            if connected and j not in visited:
                visited.add(j)
                self.DFS(j,visited,M)

