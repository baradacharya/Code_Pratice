#Greedy,hashmap
"""
At each digit of the input number in order, if there is a larger digit that occurs later,
we know that the best swap must occur with the digit we are currently considering.
"""
class Solution(object):
    def maximumSwap(self, num):
        A = map(int, str(num)) #A = [int(i) for i in str(num)]
        last = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for d in xrange(9, x, -1):
                if last.get(d, None) > i:
                    A[i], A[last[d]] = A[last[d]], A[i] #swap numbers.
                    return int("".join(map(str, A)))
        return num

s = Solution()
print s.maximumSwap(2736)