class Solution(object):
    # #1.sorting O(nlogn)
    # def longestConsecutive(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if not nums: return 0
    #     nums.sort()
    #     max_len,len = 1,1
    #     for i,num in enumerate(nums):
    #         if i >0 and nums[i] == nums[i-1]:
    #             continue
    #         elif i >0 and num == nums[i-1] + 1 :
    #             len += 1
    #         else:
    #             max_len = max(len, max_len)
    #             len = 1
    #     return max(len, max_len)
    #2.hashmap O(n)
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        num_set = set(nums)
        len,max_len = 1,1
        for num in num_set:
            if num - 1 in num_set: #already visited
                continue
            else:
                cur_num,len = num,1
                while cur_num + 1 in num_set:
                    cur_num += 1
                    len += 1
                max_len = max(len, max_len)
        return max_len




s = Solution()
print s.longestConsecutive([1,2,0,1])
