class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers : return None
        i = 0
        j = len(numbers)-1
        while i <= j:
            sum_ = numbers[i] + numbers[j]
            if sum_ == target:
                return i+1,j+1
            elif sum_ < target:
                i += 1
            else:
                j -= 1