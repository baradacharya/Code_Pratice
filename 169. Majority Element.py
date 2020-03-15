class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        counter = collections.Counter(nums)
        return counter.most_common(1)[0][0]

#T:O(n) S:O(1)
#Approach 6: Boyer-Moore Voting Algorithm
#https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate