#Binary Search Tree
"""
Dividing a set into two equal length subsets, that one subset is always greater than the other.
this visualization is important
A (0 --- i-1 | i --- m)
B (0 --- j-1 | j --- n)
for median : 1. len(left_part) = len(right_part)
             2. max(left_part) <= min(right_part)
             median = (max(left_part)+min(right_part))/2
left : i + j  right: m-i + n-j for handling odd even add 1=> i +j = (m+n+1)/2 => j = (m+n+1)/2 - i
 if assume n>=m so select i -[0,m], j = (m + n + 1)/2 -i
2. B[j-1] <= A[i] and A[i-1] <= B[j] #left<=right

so search for i in [0,m] to find i such that: j = (m + n + 1)/2 -i and B[j-1] <= A[i] and A[i-1] <= B[j]
"""
#T: O(log(min(m,n)))
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m,n = len(nums1), len(nums2)
        if m > n:
            nums1,nums2,m,n = nums2,nums1,n,m
        if n == 0:
            raise ValueError
        imin,imax,mid = 0, m, (m+n+1)/2

        while imin <= imax:
            i = (imin + imax)/2
            j = mid - i
            #nums2[j-1] <= nums1[i] and nums1[i-1] <= nums2[j]
            if i < m and nums2[j-1] > nums1[i]: #i is too small
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:  # i is too large
                imax = i - 1
            else: #i is perfect
                #left_max calculation #corner cases
                if i == 0: left_max = nums2[j-1] #no part of nums1 in left
                elif j ==0: left_max = nums1[i-1] #no part of nums2 in left
                else: left_max = max(nums1[i-1],nums2[j-1])

                if (m + n) % 2 == 1: #odd number exact median
                    return left_max
                #even number no exact median avg of leftmax and right min
                #right_min calculation
                if i == m: right_min = nums2[j] #no part of nums1 in right
                elif j == n: right_min = nums1[i] #all part of nums2 in right
                else: right_min = min(nums1[i],nums2[j])

                return (left_max + right_min)/2.0