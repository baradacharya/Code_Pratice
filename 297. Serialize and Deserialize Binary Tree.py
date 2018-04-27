# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                val.append('#')
                return
            val.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        val =[]
        dfs(root)
        return ' '.join(val)#Trick add space after each number

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def dfs():
            val = vals.next()
            if val == '#':
                return None
            root = TreeNode(int(val))
            root.left = dfs()
            root.right = dfs()
            return root

        vals = iter(data.split(' '))
        return dfs()
    def create_Tree(self, ind , nums):
        """
        :param nums: list[int]
        :return: TreeNode
        """
        if ind >= len(nums): return None
        if nums[ind] == None:
            return None
        else:
            root = TreeNode(nums[ind])
        left_ind = 2 * ind + 1
        right_ind = 2 * ind + 2
        root.left = self.create_Tree(left_ind, nums)
        root.right = self.create_Tree(right_ind, nums)
        return root


# Your Codec object will be instantiated and called as such:
codec = Codec()
# t = codec.create_Tree(0,[1,2,3,None,None,4,5])
t = codec.create_Tree(0,[1,9,2,8,10])
print codec.serialize(t)
ts = codec.deserialize(codec.serialize(t))
print codec.serialize(ts)