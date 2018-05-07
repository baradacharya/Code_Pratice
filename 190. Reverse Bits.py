class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin_ = '{0:032b}'.format(n)
        rev_bin = bin_[::-1]
        return int(rev_bin, 2)
s = Solution()
print s.reverseBits(43261596)