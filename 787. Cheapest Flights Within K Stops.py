# Dijkstra with priorty queue + map
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        import collections,heapq
        graph = collections.defaultdict(dict)#Imp Trick for graph use default collections
        for u,v,w in flights:
            graph[u][v] = w

        best = {} #<stop,dest> dist
        heap = [(0,0,src)]#cost,stops,place
        while heap:
            cost,stop,place = heapq.heappop(heap)
            if stop > K+1 or cost > best.get((stop,place),float('inf')) : continue
            if place == dst:
                return cost
            for neighbour,wt in graph[place].iteritems():
                newcost = cost + wt
                if newcost < best.get((stop+1,neighbour),float('inf')):
                    heapq.heappush(heap,(newcost,stop+1,neighbour))
                    best[(stop+1,neighbour)] = newcost
        return -1
s = Solution()
print s.findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1)