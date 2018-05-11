class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        import collections
        targets = collections.defaultdict(list)
        tickets.sort() #imortant step

        route =[]
        for x,y in tickets[::-1]:#add reverse order so that pop element should be lexical first
            targets[x].append(y)

        def DFS(airport):
            while targets[airport]:
                next_airport = targets[airport].pop()
                DFS(next_airport)
            route.append(airport)

        DFS('JFK')
        route.reverse()
        return route


s = Solution()
# print s.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])
print s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])