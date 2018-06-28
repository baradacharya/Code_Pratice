"""
finding if a cycle exists in a directed graph
topological sort
DFS
"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses

        def DFS(i):
            if visited[i] == -1:  # being visited, cycle found
                return False
            if visited[i] == 1:  # already visited
                return True
            visited[i] = -1  # marked as being visited
            for j in graph[i]:
                if not DFS(j): return False
            visited[i] = 1  # marked as visited
            return True

        for x, y in prerequisites:
            graph[x].append(y)
        for i in range(numCourses):
            if not visited[i]:
                if not DFS(i):
                    return False
        return True

s = Solution()
print s.canFinish( 4,[[2,0],[1,0],[3,1],[3,2],[1,3]])
