#DFS, #207
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        #1. create adjancency list
        visited  =[0] * n
        graph =  {x:[] for x in xrange(n)}

        #undirected graph
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        count = 0
        for node in range(n):
            if not visited[node]:
                self.DFS(graph, visited, node)
                count += 1
        return count

    def DFS(self, graph, visited, node):
        visited[node] = 1
        for adjNode in graph[node]:
            if not visited[adjNode]:
                self.DFS(graph, visited, adjNode)

