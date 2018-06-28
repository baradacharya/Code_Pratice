class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #two varriable methods
        if len(nums)==0: return 0
        values = {}
        for num  in nums:
            if num in values:values[num] += num
            else: values[num] = num
        cur_max,prev_max = 0,0
        min_ = min(values.keys())
        max_ = max(values.keys())
        for i in range(min_,max_+1):
            temp = cur_max
            if i in values:
                cur_max = max(prev_max + values[i], cur_max)
            else:
                cur_max = max(prev_max,cur_max)
            prev_max = temp
        return cur_max

s =  Solution()
# print s.deleteAndEarn([3, 4, 2,5,6,7,8])
print s.deleteAndEarn([2, 2, 3, 3, 3, 4])