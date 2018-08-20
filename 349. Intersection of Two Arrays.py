#unique intersection
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))

s = Solution()
print s.intersection([1, 2, 2, 1],[2, 2])


"""
Use two hash sets

Time complexity: O(n)
"""

# public class Solution {
#     public int[] intersection(int[] nums1, int[] nums2) {
#         Set<Integer> set = new HashSet<>();
#         Set<Integer> intersect = new HashSet<>();
#         for (int i = 0; i < nums1.length; i++) {
#             set.add(nums1[i]);
#         }
#         for (int i = 0; i < nums2.length; i++) {
#             if (set.contains(nums2[i])) {
#                 intersect.add(nums2[i]);
#             }
#         }
#         int[] result = new int[intersect.size()];
#         int i = 0;
#         for (Integer num : intersect) {
#             result[i++] = num;
#         }
#         return result;
#     }
# }