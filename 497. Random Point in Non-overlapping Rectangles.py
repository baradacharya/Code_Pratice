import random
class Solution(object):
    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.psum = []
        self.tot = 0
        self.rects = rects
        for x in rects:
            self.tot += (x[2]-x[0]+1)*(x[3]-x[1]+1)
            self.psum.append(self.tot)
        print self.psum
    def pick(self):
        """
        :rtype: List[int]
        """
        target = random.randint(self.tot)

        l = 0
        r = len(self.psum) - 1
        while l != r:
            m = (l + r) / 2
            if target > self.psum[m]:  # >= is wrong
                l = m + 1
            else:
                r = m
        print "Rectangle : " + str(l)
        x = self.rects[l]
        width = x[2]-x[0] + 1
        height = x[3]-x[1] + 1
        area = width * height
        base = self.psum[l] - area #base point: totoal area sum - cur area
        print target,area,base,x[0] + (target-base)%width,x[1] + (target-base)/width
        return (x[0] + (target-base)%width,x[1] + (target-base)/width )



# Your Solution object will be instantiated and called as such:
obj = Solution([[1,1,5,5]])
for _ in range(10):
    param_1 = obj.pick()
print "Hi"
obj = Solution( [[1, 1, 2, 4], [3, 2, 5, 4], [2, 5, 5, 6]])
for _ in range(10):
    param_1 = obj.pick()