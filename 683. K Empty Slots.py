class Solution(object):
    def kEmptySlots(self, flowers, k):
        active = []
        from _bisect import bisect
        for day, flower in enumerate(flowers, 1):
            i = bisect(active, flower)
            for neighbor in active[i-(i>0):i+1]:
                if abs(neighbor - flower) - 1 == k:
                    return day
            active.insert(i, flower)
        return -1

s =Solution()
print s.kEmptySlots([1,4,3,2,10],5)