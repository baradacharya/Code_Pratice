#undirected graph
class Graph():
    def dijkstra(self, n, edges, src, dst):
        """
        :type n: int
        :type edges: List[List[int]]
        :type src: int
        :type dst: int
        :rtype: int
        """
        import collections,heapq
        graph = collections.defaultdict(dict)#Imp Trick for graph use default collections

        #construct graph
        for u,v,w in edges:
            graph[u][v] = w
            graph[v][u] = w

        visited = [False] * n
        best = {} #node: dist
        heap = [(0,src)] #dist,node

        while heap:
            dist,node = heapq.heappop(heap)
            if best.get(node,float('inf')) < dist : #alreday exists lower distance
                continue

            visited[node] = True
            #check for all neighbouring unvisited nodes.
            for neighbours,wt in graph[node].iteritems():
                newdist = dist + wt
                if not visited[neighbours] and newdist < best.get(neighbours,float('inf')):
                    best[neighbours] = newdist
                    heapq.heappush(heap,(newdist,neighbours))

        return best[dst]
s = Graph()
# print s.dijkstra(3,[[0,1,100],[1,2,100],[0,2,500]],0,2)
print s.dijkstra(9,[[0,1,4],[0,7,8],[1,7,11],[1,2,8],[2,8,2],[2,5,4],[2,3,7],[3,5,14],[3,4,9],[7,8,7],[7,6,1],[8,6,6],[6,5,2],[5,4,10]],0,4)
