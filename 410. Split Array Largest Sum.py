#https://leetcode.com/problems/split-array-largest-sum/discuss/89817/Clear-Explanation:-8ms-Binary-Search-Java
"""
2. Use binary search to approach the correct answer. We have l = max number of array;
 r = sum of all numbers in the array;Every time we do mid = (l + r) / 2;
3.Use greedy to narrow down left and right boundaries in binary search.
3.1 Cut the array from left.
3.2 make sure that the sum of numbers between each two cuts (inclusive) is large enough but still less than mid.
3.3 We'll end up with two results: either we can divide the array into more than m subarrays or we cannot.
If we can,
    it means that the mid value we pick is too small
    because we've already tried our best to make sure each part holds as many non-negative numbers as we can
    but we still have numbers left. So, it is impossible to cut the array into m parts and
    make sure each parts is no larger than mid. We should increase m. This leads to l = mid + 1;
If we can't,
    it is either we successfully divide the array into m parts and the sum of each part is less than mid,
    or we used up all numbers before we reach m.
    Both of them mean that we should lower mid because
    we need to find the minimum one. This leads to r = mid - 1;
"""
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        sum_ = sum(nums)
        max_ = max(nums)

        if m == 1: return sum_

        l,r = max_,sum_
        while l <= r:
            mid = (l+r)/2
            print mid
            if self.valid(mid,nums,m): #larger sum
                r = mid - 1
            else:#smaller sum
                l = mid + 1
        return l

    def valid(self,target,nums,m):
        count = 1
        total = 0
        for num in nums:
            total += num
            if total > target: #e can break from here
                total = num
                count += 1
                if count > m:
                    return False #already have m splits ; so taregt must be larger(l = mid+1)
        #either we successfully divide the array into m parts and
        # the sum of each part is less than mid,
        #or we used up all numbers before we reach m.
        #count < m or count == m
        return True #target is large , we can decrease
s = Solution()
print s.splitArray(nums = [7,2,5,10,8],m = 2)