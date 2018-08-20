"""
If only nums2 cannot fit in memory, put all elements of nums1 into a HashMap,
read chunks of array that fit into the memory, and record the intersections.

If both nums1 and nums2 are so huge that neither fit into the memory,
sort them individually (external sort),
then read 2 elements from each array at a time in memory, record intersections.
"""


class Solution(object):
    # def intersect(self, nums1, nums2):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: List[int]
    #     """
    #     import collections
    #     counter1 = collections.Counter(nums1)
    #     counter2 = collections.Counter(nums2)
    #     a = counter1 & counter2
    #     return list(a.elements()) #Iterator over elements repeating each as many times as its count

    #without using counter
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map = {}
        for num in nums1:
            if num in map :
                map[num] += 1
            else:
                map[num] = 1

        res  = []
        for num in nums2:
            if num in map and map[num] > 0 :
                map[num] -= 1
                res.append(num)
        return res
s = Solution()
print s.intersect([1, 2, 2, 1],[2,2])