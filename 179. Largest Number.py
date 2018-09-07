# O(nlgn)
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        num = [str(x) for x in nums]
        num.sort(cmp=lambda x, y: cmp(y+x,x+y)) #y+x should greater than x+y
        return ''.join(num).lstrip('0') or '0'

s = Solution()
print s.largestNumber([3,30,34,5,9])


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num