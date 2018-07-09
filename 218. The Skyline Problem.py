"""
critical point

for each rectangle r:
    for each critical point c:
        if c.x >= r.left && c.x < r.right:
            c.y gets the max of r.height and the previous value of c.y

for each rectangle r:
    for each critical point c below r (except the one at r.right):
        c.y gets the max of r.height and the previous value of c.y
"""
#removing element from heap is time consuminge


#problem with python heap implementation is we cannot remove a particular key from heap we have to pop the root always.
#so we just marked the element which we have used and pop them at once.
#one concern is there may be building with same height,se we have to add building height with apartment number.

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        height = []
        building_num = 0
        for building in buildings:  # L,R,H
            height.append((building[0], -building[2], building_num))  # L,H #start point negative height value
            height.append((building[1], building[2], building_num))   # R,H end point normal height value
            building_num += 1
        height.sort()

        # Use a maxHeap to store possible heights, so use -ve values
        import heapq
        heap = []  # height,building_num
        prev = 0 #A key point is the left endpoint of a horizontal line segment.  prev,cur to keep track of it
        used = set()
        for h in height:
            if h[1] < 0:  # starting point add height
                heapq.heappush(heap, (h[1], h[2]))
            else:
                used.add(h[2])  # add building num to used
                if len(heap) != 0 and heap[0][0] == -h[1]:  # remove root from heap
                    while len(heap) != 0 and heap[0][1] in used:
                        heapq.heappop(heap)

            if len(heap) == 0: # cur is current max height
                cur = 0
            else:
                cur = -heap[0][0]

            #  compare current max height with previous max height, update result
            # A key point is the left endpoint of a horizontal line segment.
            if prev != cur:
                result.append((h[0], cur))
                prev = cur
        return result

s = Solution()
print s.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])
print s.getSkyline([[0,2,3],[2,5,3]]) #[[0,3],[5,0]]
print s.getSkyline([[0,5,7],[5,10,7],[5,10,12],[10,15,7],[15,20,7],[15,20,12],[20,25,7]])


# height = [[1,3],[2,1],[4,5],[1,2]]
# height.sort()
# print height
# height = [[1,3],[2,1],[4,5],[1,2]]
# height.sort(key=lambda i: (i[0], i[1]))
# print height
