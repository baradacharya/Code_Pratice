#1: Dynamic Programming
def findNumberOfLIS(nums):
    N = len(nums)
    if N <= 1: return N
    lengths = [0] * N  # lengths[i] = longest ending in nums[i]
    counts = [1] * N  # count[i] = number of longest ending in nums[i]

    for i, num in enumerate(nums):
        for j in xrange(i):
            if nums[i] > nums[j]:
                if lengths[j] >= lengths[i]:
                    lengths[i] = 1 + lengths[j]
                    counts[i] = counts[j]
                elif lengths[j] + 1 == lengths[i]:
                    counts[i] += counts[j] #alredy have counts[j] way

    longest = max(lengths)
    ans  = 0
    for i, c in enumerate(counts):
        if lengths[i] == longest:
            ans += c
    return ans
# print findNumberOfLIS([1,3,5,4,7])
print findNumberOfLIS([2,2,2,2,2])