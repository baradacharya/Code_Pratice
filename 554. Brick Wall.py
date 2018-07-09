class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        map = {}
        for row in wall :
            sum = 0
            for i in range(len(row)-1):
                sum += row[i]
                map[sum] = map.get(sum,0) + 1
        res = len(wall)
        for key in map:
            res = min(res,len(wall)-map[key])
        return res

s = Solution()
print s.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]])
