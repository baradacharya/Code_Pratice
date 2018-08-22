#dynamic

from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary to store graph

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def printArr(self, dist):
        print("Vertex   Distance from Source")
        for i in range(self.V):
            print("%d \t\t %d" % (i, dist[i]))

    def BellmanFord(self, src):
        import sys
        dist = [sys.maxint] * self.V
        dist[src] = 0

        #Step 2: Relax all edges |V| - 1 times.
        for i in range(self.V-1):
            #step 3. go through all edges.
            for u,v,w in self.graph:
                if dist[u] != sys.maxint and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        #negative cycle detects
        for u, v, w in self.graph:
            if dist[u] != sys.maxint and dist[u] + w < dist[v]:
                print "Graph contains negative weight cycle."
                return

        self.printArr(dist)
g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

# Print the solution
g.BellmanFord(0)
"""
Given a graph and a source vertex src in graph, find shortest paths from src to all vertices.
The graph may contain negative weight edges.
We have discussed Dijkstra’s algorithm for this problem.
Dijkstra’s algorithm is a Greedy algorithm and time complexity is O(VLogV) (with the use of Fibonacci heap).
Dijkstra doesn’t work for Graphs with negative weight edges,
Bellman-Ford works for such graphs.
Bellman-Ford is also simpler than Dijkstra and suites well for distributed systems.
But time complexity of Bellman-Ford is O(VE), which is more than Dijkstra.
"""
"""
How does this work? Like other Dynamic Programming Problems, the algorithm calculate shortest paths in bottom-up manner. 
It first calculates the shortest distances which have at-most one edge in the path. 
Then, it calculates shortest paths with at-most 2 edges, and so on. 
After the i-th iteration of outer loop, the shortest paths with at most i edges are calculated. 
There can be maximum |V| – 1 edges in any simple path, that is why the outer loop runs |v| – 1 times. 
The idea is, assuming that there is no negative weight cycle, if we have calculated shortest paths with at most i edges,
 then an iteration over all edges guarantees to give shortest path with at-most (i+1) edges"""