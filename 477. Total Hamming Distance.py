#2 Loop over the bits
#https://leetcode.com/problems/total-hamming-distance/solution/

def totalHammingDistance(nums):
    l = map('{:032b}'.format, nums) #n *32
    q = zip(*l) #32 * n

    return sum((b.count('0') * b.count('1')) for b in zip(*map('{:032b}'.format, nums)))

totalHammingDistance([4,14,2])