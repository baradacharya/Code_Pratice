"""
Twice pass:

not rob nums[n-1]
not rob nums[0]
and the other is same as House Robber.
"""

"""
This problem is a little tricky at first glance. However, if you have finished the House Robber problem, this problem can simply be decomposed into two House Robber problems.
Suppose there are n houses, since house 0 and n - 1 are now neighbors, we cannot rob them together and thus the solution is now the maximum of

Rob houses 0 to n - 2;
Rob houses 1 to n - 1.
The code is as follows. Some edge cases (n < 2) are handled explicitly.

class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size(); 
        if (n < 2) return n ? nums[0] : 0;
        return max(robber(nums, 0, n - 2), robber(nums, 1, n - 1));
    }
private:
    int robber(vector<int>& nums, int l, int r) {
        int pre = 0, cur = 0;
        for (int i = l; i <= r; i++) {
            int temp = max(pre + nums[i], cur);
            pre = cur;
            cur = temp;
        }
        return cur;
    }
};"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2 : return 0 if n == 0 else nums[0]
        return max(self.robber(nums,0,n-2),self.robber(nums,1,n-1))

    def robber(self,nums,l,r):
        pre = 0
        cur = 0
        for i in range(l,r+1):
            temp = max(cur, pre+ nums[i])
            pre = cur
            cur = temp
        return cur