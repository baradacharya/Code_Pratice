"""
Comparison Sort and Counting Sort.
https://leetcode.com/problems/h-index/solution/
comparison sorting algorithms
such as heapsort, mergesort and quicksort have a lower bound of O(nlogn).
The most commonly used non-comparison sorting is counting sort.
"""
##After sorting in descending order, hh-index is the length of the largest square in the histogram.
#T:O(nlogn)
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        i = 0
        while i < len(citations):
            if citations[i] > i :
                i += 1
            else:
                break
        return i
    #counting sort
    # def hIndex(self, citations):
    #     """
    #     :type citations: List[int]
    #     :rtype: int
    #     """
    #     n = len(citations)
    #     count_arr = [0] * (n+1)
    #     for num in citations:
    #         count_arr[min(n,num)] += 1 #store citation num, number larger than total count limit to n
    #     h = n
    #     count = count_arr[n]
    #     while h > count:
    #         count += count_arr[h]
    #         h -= 1
    #     return h

s = Solution()
print s.hIndex([3, 0, 6, 1, 5])