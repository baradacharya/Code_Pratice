class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        merged = []
        for point in points:
            if not merged or point[0] > merged[-1][1]:#cann't merge
                merged.append(point)
            else: #can merge
                merged[-1][1] = min(point[1],merged[-1][1])
                merged[-1][0] = max(point[0],merged[-1][0])
        return len(merged)