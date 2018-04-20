"""
#1 Sorting.
T: O(nlogn) S:O(1)
2.set T: O(n) S:O(n)
"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        number = set()
        for num in nums:
            if num not in number:
                number.add(num)
            else:
                return num