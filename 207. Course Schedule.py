"""
finding if a cycle exists in a directed graph
topological sort
"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for x,y in prerequisites:
            graph[x].append(y)
        for i in range(numCourses):
            if i not in visited:
                if not self.dfs(graph, visited, i): return False
        return True
    def dfs(self,graph,visited,i):
        if visited[i] == -1: #being visited, cycle found
            return False
        if visited[i] == 1: #already visited
            return True

        visited[i] = -1 #marked as being visited
        for adj in graph[i]:
            if not self.dfs(graph,visited,adj): return False
        visited[i] = 1 #marked as visited
        return True
