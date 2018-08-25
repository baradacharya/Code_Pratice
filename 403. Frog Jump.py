#Hashmap + DP
#https://leetcode.com/problems/frog-jump/solution/
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        stoneMap = {} #key: stone position, value: possible jump size
        for stone in stones:
            stoneMap[stone] = set()
        stoneMap[0].add(0) #start
        for stone in stones:
            for jumpSize in stoneMap[stone]:
                for step in {jumpSize-1,jumpSize,jumpSize+1}:
                    if step > 0 and (stone + step) in stoneMap:
                        stoneMap[stone + step].add(step)
        return len(stoneMap[stones[-1]]) > 0
s = Solution()
print s.canCross([0,1,3,5,6,8,12,17])
"""
public class Solution {
    public boolean canCross(int[] stones) {
        HashMap<Integer, Set<Integer>> map = new HashMap<>();
        for (int i = 0; i < stones.length; i++) {
            map.put(stones[i], new HashSet<Integer>());
        }
        map.get(0).add(0);
        for (int i = 0; i < stones.length; i++) {
            for (int k : map.get(stones[i])) {
                for (int step = k - 1; step <= k + 1; step++) {
                    if (step > 0 && map.containsKey(stones[i] + step)) {
                        map.get(stones[i] + step).add(step);
                    }
                }
            }
        }
        return map.get(stones[stones.length - 1]).size() > 0;
    }
}
"""
