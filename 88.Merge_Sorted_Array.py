"""
merge from the endside
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # l = 0
        # r = 0
        # res = []
        # while l< m and r < n:
        #     if nums1[l] < nums2[r]:
        #         res.append(nums1[l])
        #         l += 1
        #     else:
        #         res.append(nums2[r])
        #         r += 1
        # while l < m:
        #     res.append(nums1[l])
        #     l += 1
        # while r < n :
        #     res.append(nums2[r])
        #     r += 1
        # print res

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m + n -1] = nums1[m-1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        return nums1

s = Solution()
print s.merge([1,1,5,7,0,0,0],4,[2,2,6],3)