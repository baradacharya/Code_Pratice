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

        def DFS(node):
            if visited[node] == -1:  # being visited, cycle found
                return False
            if visited[node] == 1:  # already visited
                return True
            visited[node] = -1  # marked as being visited
            for adjNode in graph[node]:
                if not DFS(adjNode):
                    return False
            visited[node] = 1  # marked as visited
            return True

        for x, y in prerequisites:
            graph[x].append(y)
        for course in range(numCourses):
            if not DFS(course): return False
        return True

s = Solution()
print s.canFinish( 4,[[2,0],[1,0],[3,1],[3,2],[1,3]])
