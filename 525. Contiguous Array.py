#Use Hashmap
#store the entries in the form of (count,index)
#same count means letters between these index contain equal numbers.

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index_map = {}
        count  = 0
        index_map[0] = -1
        max_len = 0
        for i,num in enumerate(nums):
            if num == 1: count += 1
            else: count -= 1

            if count in index_map:
                max_len = max(max_len,i-index_map[count])
            else:
                index_map[count] = i

        return max_len
