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
        graph =  {x:[] for x in xrange(n) }
        #undirected graph
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        count  = 0
        for i in range(n):
            if not visited[i]:
                self.DFS(graph,visited,i)
                count += 1
        return count
    def DFS(self,graph,visited,i):
        visited[i] = 1
        for j in graph[i]:
            if not visited[j]:
                self.DFS(graph,visited,j)


