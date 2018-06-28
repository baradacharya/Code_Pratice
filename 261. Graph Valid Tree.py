# detetct cycle, undirected, #207
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(n)]
        visited = [0] * n

        def DFS(i):
            if visited[i] == -1:  # being visited, cycle found
                return False
            if visited[i] == 1:  # already visited
                return True
            visited[i] = -1  # marked as being visited
            for j in graph[i]:
                if not DFS(j):
                    return False
            visited[i] = 1  # marked as visited
            return True

        for x, y in edges:
            graph[x].append(y)
            # graph[y].append(x)

        for i in range(n):
            if not visited[i]:
                if not DFS(i):
                    return False
        return True
