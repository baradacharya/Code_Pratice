#1. Greedy/Two Pointer
#like Merge Intervals
#repeatedly choose the smallest left-justified partition.
#last[char] -> index of S where char occurs last.
# let anchor and j be the start and end of the current partition.
#if we are at a label that occurs last at some index after j, we'll extend the partition j = last[c]
#if we are at the end of the partition (i == j) then we'll append a partition size to our answer,
#  and set the start of our new partition to i+1.
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        char_index = {}
        for i,c in enumerate(S):
            char_index[c] = i
        start,end = 0,0
        ans  = []
        for i,c in enumerate(S):
            end = max(end,char_index[c])
            if i == end:
                ans.append(end-start+1)
                start = i+ 1
        return ans

s = Solution()
print s.partitionLabels("ababcbacadefegdehijhklij")
