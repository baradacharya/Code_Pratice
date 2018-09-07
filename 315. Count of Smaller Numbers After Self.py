class BinaryIndexedTree(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i, val):
        while i < len(self.sums):
            self.sums[i] += 1
            i += i & -i

    def sum(self, i):
        r = 0
        while i > 0:
            r += self.sums[i]
            i -= i & -i
        return r


class Solution(object):
    def countSmaller(self, nums):
        hashTable = {v: i for i, v in enumerate(sorted(set(nums)))} #value index

        tree, r = BinaryIndexedTree(len(hashTable)), []
        for i in xrange(len(nums) - 1, -1, -1):
            temp = hashTable[nums[i]] #index
            r.append(tree.sum(temp))
            tree.update(temp + 1, 1)
        return r[::-1]

s = Solution()
print s.countSmaller([5,2,6,1])