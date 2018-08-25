#Time complexity : O(n)- range sum query, O(1) - update query
#TLE
class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        self.nums = nums
        print nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        original = self.nums[i]

        if i > 0:
            original -= self.nums[i-1]

        diff = original - val

        for j in range(i,len(self.nums)):
            self.nums[j] -= diff

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        sum = self.nums[j]
        if i > 0:
            sum -= self.nums[i-1]
        return sum

#Segment tree is a very flexible data structure,
# because it is used to solve numerous range query problems like finding minimum, maximum, sum, greatest common divisor,
# least common denominator in array in logarithmic time.
"""
The segment tree for array a[0,1,..,n-1] is a binary tree in which each node contains aggregate information (min, max, sum, etc.) 
for a subrange [i,..,j] of the array,as its left and right child hold information for range [i,(i+1)/2] and [(i+1)/2+1,j]
"""
#1. Build segment tree

#2. Update segment tree

#3. Range Sum Query
"""
Binary Index Tree https://www.youtube.com/watch?v=v_wj_mOAlig
#use 1 index notation
#initialization
start with zero array, insert each element with add (nlogn)
rangesum(l,r) = sum(r) - sum(l-1)
not min and max (segement tree)
"""

#BIT Implementation
class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.BITarray = [0] * (len(nums) + 1)
        self.nums = nums
        for i, val in enumerate(nums):
            self.init(i, val)

    def init(self, i, val):
        i += 1
        while i < len(self.BITarray):
            self.BITarray[i] += val
            i += i & -i #adding last bit one(to update in range containing i)

    def update(self, i, val):
        diff = val - self.nums[i];
        self.nums[i] = val;
        self.init(i, diff);

    def sum(self, i):
        i += 1
        sum = 0
        while i:
            sum += self.BITarray[i]
            i -= i & -i #removeing last bit
        return sum

    def sumRange(self, i, j):
        return self.sum(j) - self.sum(i - 1)

# Your NumArray object will be instantiated and called as such:
obj = NumArray([1,3,5])
# obj.update(i,val)
print obj.sumRange(0,2)