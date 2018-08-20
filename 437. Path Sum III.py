"""
Typical recursive DFS.
Space: O(n) due to recursion.
Time: O(n^2) in worst case (no branching); O(nlogn) in best case (balanced tree).
"""
class SolutionBruteForce(object):
    def pathSum(self, root, target):
        if root:
            return self.DFS(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        else:
            return 0

    def DFS(self, root, sum):
        if root:
            return int(root.val == sum) + self.DFS(root.left, sum - root.val) + self.DFS(root.right, sum - root.val)
        else:
            return 0

#Using Hashmap
#T: O(n)
class SolutionBruteForce(object):
    def pathSum(self, root, target):
        preSum = {}
        preSum[0] = 1
        return self.helper(root,0,sum,preSum)

    def helper(self,root,curSum, target, preSum):
        if not root:
            return 0

        curSum += root.val
        res = preSum.get(curSum - target,0)
        preSum[curSum] = preSum.get(curSum,0) + 1

        res += self.helper(root.left,curSum,target,preSum) + self.helper(root.right,curSum,target,preSum)
        preSum[curSum] = preSum.get(curSum) - 1 #done with this node
        return res

"""
 public int pathSum(TreeNode root, int sum) {
        HashMap<Integer, Integer> preSum = new HashMap();
        preSum.put(0,1);
        return helper(root, 0, sum, preSum);
    }
    
    public int helper(TreeNode root, int currSum, int target, HashMap<Integer, Integer> preSum) {
        if (root == null) {
            return 0;
        }
        
        currSum += root.val;
        int res = preSum.getOrDefault(currSum - target, 0);
        preSum.put(currSum, preSum.getOrDefault(currSum, 0) + 1);
        
        res += helper(root.left, currSum, target, preSum) + helper(root.right, currSum, target, preSum);
        preSum.put(currSum, preSum.get(currSum) - 1);
        return res;
    }
"""