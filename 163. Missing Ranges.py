class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        nums.append(upper+1) #for the last digit
        pre = lower -1
        for num in nums:
            if num == pre + 2: #one missing
                res.append(str(pre+1))
            elif num > pre + 2: #more than one missing
                res.append(str(pre+1) + "->" + str(num-1))
            pre = num
        return res