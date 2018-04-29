"""
 * Taking 1~n as root respectively:
 *      1 as root: # of trees = F(0) * F(n-1)  // F(0) == 1
 *      2 as root: # of trees = F(1) * F(n-2)
 *      3 as root: # of trees = F(2) * F(n-3)
 *      ...
 *      n-1 as root: # of trees = F(n-2) * F(1)
 *      n as root:   # of trees = F(n-1) * F(0)
 *
 * So, the formulation is:
 *      F(n) = F(0) * F(n-1) + F(1) * F(n-2) + F(2) * F(n-3) + ... + F(n-2) * F(1) + F(n-1) * F(0)
 """
class Solution(object):
    def numTrees(self, n):
        c =[0] * (n+1)
        c[0] = 1
        c[1] = 1
        for i in range(2,n+1):
            for j in range(i):
                c[i] += c[j]*c[i-j-1]
        return c[-1]