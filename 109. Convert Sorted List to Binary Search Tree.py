# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, head):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        rootNode = slow.next  # new root
        slow.next = None  # cut down the left child
        root = TreeNode(rootNode.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(rootNode.next)
        return root
