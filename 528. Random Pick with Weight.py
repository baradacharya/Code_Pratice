#Approach 1: Prefix Sum and Binary Search
"""
p(x) = sum_x_i W_i
tot= sum_N_i W_i where N = len(w)
targ < p(x)
T: O(N) preprocessing O(LogN)pickIndex
S:O(N)
"""
import random
class Solution(object):
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.psum  = []
        self.tot = 0
        for x in w:
            self.tot += x
            self.psum.append(self.tot)

    def pickIndex(self):
        """
        :rtype: int
        """
        target = random.randint(1,self.tot)
        l = 0
        r = len(self.psum)-1
        while l != r:
            m = (l+r)/2
            if target > self.psum[m]: #>= is wrong
                l = m + 1
            else:
                r = m
        return l



# Your Solution object will be instantiated and called as such:
obj = Solution([1,5])
for _ in range(10):
    print obj.pickIndex()

