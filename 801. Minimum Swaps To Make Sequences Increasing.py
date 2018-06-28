#like stock buy and sell problem.
#n1: the cost of making the first i-1 columns increasing and not swapping the i-1th column
#s1 (swapped1), the cost of making the first i-1 columns increasing
class Solution(object):
    def minSwap(self, A, B):
        n1, s1 = 0, 1 #natural,one swapped
        for i in xrange(1, len(A)):
            n2 = s2 = float("inf")
            # if a1 < a2 and b1 < b2, then it is allowed to have both of these columns natural (unswapped),
            # or both of these columns swapped
            if A[i-1] < A[i] and B[i-1] < B[i]:
                n2 = n1
                s2 = s1 + 1
            #(not exclusive) possibility is
            #This means that it is allowed to have exactly one of these columns swapped.
            if A[i-1] < B[i] and B[i-1] < A[i]:
                n2 = min(n2, s1) #i-1 swap
                s2 = min(s2, n1 + 1)#ith swap
            #Note that it is important to use two if statements separately, because both of the above possibilities might be possible.
            n1, s1 = n2, s2
        return min(n1, s1)

s = Solution()
#print s.minSwap([1,3,5,4],[1,2,3,7])
print s.minSwap([1,3,4,5],[1,2,3,7])
print s.minSwap([1,2,3,4],[5,6,7,8])