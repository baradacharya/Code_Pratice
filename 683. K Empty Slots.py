"""
Time Complexity (Python):O(N^2).
As above, except list.insert is O(N)
Space Complexity: O(N),the size of active.
"""
"""
Bisection algorithms.

This module provides support for maintaining a list in sorted order without
having to sort the list after each insertion. For long lists of items with
expensive comparison operations, this can be an improvement over the more
common approach.
"""

class Solution(object):
    def kEmptySlots(self, flowers, k):
        active = []
        from _bisect import bisect
        for day, flower in enumerate(flowers, 1):
            i = bisect(active, flower) #Return the index where to insert item x in list a, assuming a is sorted.
            for neighbor in active[i-(i>0):i+1]: #check for previous and next element
                if abs(neighbor - flower) - 1 == k:
                    return day
            active.insert(i, flower)
        return -1



"""
class Solution {
    public int kEmptySlots(int[] flowers, int k) {
        TreeSet<Integer> active = new TreeSet();
        int day = 0;
        for (int flower: flowers) {
            day++;
            active.add(flower);
            Integer lower = active.lower(flower)
            Integer higher = active.higher(flower);
            if (lower != null && flower - lower - 1 == k ||
                    higher != null && higher - flower - 1 == k)
                return day;
        }
        return -1;
    }
}
"""


class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        # 1. sorted array
        # 2. days array
        # 3. bucket

        # each bucket of size k + 1
        num_b = (len(flowers) + k) // (k + 1)  # round up
        lows = [float('inf')] * num_b
        highs = [-float('inf')] * num_b

        for i, flower in enumerate(flowers):
            bucket = (flower - 1) // (k + 1)
            if flower < lows[bucket]:
                lows[bucket] = flower
                if bucket > 0 and abs(highs[bucket - 1] - flower) == k + 1:
                    return i + 1
            if flower > highs[bucket]:
                highs[bucket] = flower
                if bucket < len(lows) - 1 and abs(lows[bucket + 1] - flower) == k + 1:
                    return i + 1

        return -1

s =Solution()
print s.kEmptySlots([1,4,3,2,10],5)