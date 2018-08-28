class RangeModule(object):
    def __init__(self):
        self.ranges = []

    def _bounds(self, left, right):
        i, j = 0, len(self.ranges) - 1
        for d in (100, 10, 1):
            while i + d - 1 < len(self.ranges) and self.ranges[i + d - 1][1] < left:
                i += d
            while j - d + 1 >= 0 and self.ranges[j - d + 1][0] > right:
                j -= d
        return i, j

    def addRange(self, left, right):
        i, j = self._bounds(left, right) #get boundary index for left and right
        if i <= j:
            left = min(left, self.ranges[i][0])
            right = max(right, self.ranges[j][1])
        self.ranges[i:j + 1] = [(left, right)]

    def queryRange(self, left, right):
        import bisect
        i = bisect.bisect_left(self.ranges, (left, float('inf')))
        if i: i -= 1
        return (bool(self.ranges) and self.ranges[i][0] <= left and right <= self.ranges[i][1])

    def removeRange(self, left, right):
        i, j = self._bounds(left, right)
        # merge = []
        # for k in xrange(i, j + 1):
        #     if self.ranges[k][0] < left:
        #         merge.append((self.ranges[k][0], left))
        #     if right < self.ranges[k][1]:
        #         merge.append((right, self.ranges[k][1]))
        # self.ranges[i:j + 1] = merge

        new_range = []
        ll = min(self.ranges[i][0], left)
        rr = max(self.ranges[i][1], right)
        if ll < left:
            new_range.append((ll, left))
        if rr > right:
            new_range.append((right, rr))
        self.ranges[i : i + 1] = new_range




# Your RangeModule object will be instantiated and called as such:
obj = RangeModule()
obj.addRange(10,20)
print obj.queryRange(10,14)
obj.removeRange(14,16)
print obj.queryRange(13,15)
print obj.queryRange(16,17)
#
# #test area
# l = [(1,2),(3,4),(5,6)]
# print l
# l[0:3] = [(1,6)]
# print l