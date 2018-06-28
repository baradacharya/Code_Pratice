# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    """
    will use two pointer
    1. keep track of the left most node
    2. will traverse levelorder for traversing
    """
    # def connect(self, root):
    #     if not root: return None
    #     leftmost  = root
    #     while leftmost.left: #will stop before last level as we are connecting childlevels
    #         cur = leftmost
    #         while cur:
    #             cur.left.next = cur.right
    #             if cur.next != None:
    #                 cur.right.next = cur.next.left
    #             cur = cur.next
    #         leftmost = leftmost.left

    def connect(self, root):#will work for 116 and 117
        #simple level order traversal with extra node to keep track of the left
        if not root: return None
        left_most_child = cur_child = TreeLinkNode(0)
        parent  = root
        while parent:
            cur_child.next = parent.left #if left exists, it will assign
            if cur_child.next:
                cur_child = cur_child.next
            cur_child.next = parent.right #if left does n't exists, assign to right
            if cur_child.next:
                cur_child = cur_child.next
            parent = parent.next
            if not parent: #finished with this level, go to next level
                cur_child = left_most_child
                parent = left_most_child.next