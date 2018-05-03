class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        hash_map = {}
        for i in A:
            for j in B:
                if i+j in hash_map:
                    hash_map[i+j] += 1
                else:
                    hash_map[i+j] = 1
        count  = 0
        for i in C:
            for j in D:
                if -i-j in hash_map:
                    count += hash_map[-i-j]
        return count