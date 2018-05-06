class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for row in range(vertices)]

    def printSolution(self, dist):
        print "Vertex Distance from Source"
        for node in range(self.V):
            print node, "distance", dist[node]
    """
    return edge with min distance
    """
    def minDistance(self,dist,visited):
        import sys
        min_ = sys.maxint
        min_index = 0
        for v in range(self.V):
            if dist[v] < min_ and not visited[v]:
                min_ = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        import sys
        dist = [sys.maxint] * self.V
        dist[src] = 0
        visited = [False] * self.V
        for edge_out in range(self.V):
            u = self.minDistance(dist,visited) #vertex with min distance
            visited[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and visited[v] == False:
                    if dist[v] > dist[u] + self.graph[u][v]:
                        dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)

# Driver program
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
g.dijkstra(0)

