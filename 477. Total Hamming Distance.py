#2 Loop over the bits
#https://leetcode.com/problems/total-hamming-distance/solution/
#K_C_1 * n-k_C_1 = k(n-k) = count(0)*count(1)
def totalHammingDistance(nums):
    l = map('{:032b}'.format, nums) #n *32
    q = zip(*l) #32 * n
    sum = 0
    for b in q:
        sum += b.count('0') * b.count('1')
    return sum
    # return sum((b.count('0') * b.count('1')) for b in zip(*map('{:032b}'.format, nums)))

print totalHammingDistance([4,14,2])


