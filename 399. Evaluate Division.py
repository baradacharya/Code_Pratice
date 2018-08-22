# Floyd–Warshall
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        import collections
        graph = collections.defaultdict(dict)
        for (x, y), val in zip(equations, values):
            graph[x][x] = graph[y][y] = 1.0
            graph[x][y] = val
            graph[y][x] = 1 / val
        for k in graph:
            for i in graph[k]:
                for j in graph[k]:
                    if i == j: continue
                    graph[i][j] = graph[i][k] * graph[k][j]
        return [graph[x].get(y, -1.0) for x, y in queries]

s = Solution()
print s.calcEquation([ ["a","b"],["b","c"] ], [2.0,3.0],[ ["a","c"],["b","c"],["a","e"],["a","a"],["x","x"] ])

# Floyd–Warshall
"""
class AllPairShortestPath
{
    final static int INF = 99999, V = 4;
 
    void floydWarshall(int graph[][])
    {
        int dist[][] = new int[V][V];
        int i, j, k;
 
        for (i = 0; i < V; i++)
            for (j = 0; j < V; j++)
                dist[i][j] = graph[i][j];
 
        for (k = 0; k < V; k++)
        {   
            for (i = 0; i < V; i++)// Pick all vertices as source one by one
            {
                for (j = 0; j < V; j++) // Pick all vertices as destination for the above picked source
                {
                    // If vertex k is on the shortest path from i to j, then update the value of dist[i][j]
                    if (dist[i][k] + dist[k][j] < dist[i][j])
                        dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
"""