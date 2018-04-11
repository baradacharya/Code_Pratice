class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #T:O(n), S:O(n)
        num_hash = dict()
        for num in nums:
            if num in num_hash:
                num_hash.pop(num)
            else:
                num_hash[num] = 1

        return num_hash.keys()[0]
    #without extra space bit manpulation
    """
    If we take XOR of zero and some bit, it will return that bit
    If we take XOR of two same bits, it will return 0
    XOR is assciative
    we can XOR all bits together to find the unique number.
    """

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #T:O(n), S:O(n)
        a = 0
        for i in nums:
            a ^= i 
        return a
s =Solution()
t = s.singleNumber([1,1,2,3,2])
print t