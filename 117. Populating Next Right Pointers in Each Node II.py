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
    def connect(self, root):
        #simple level order traversal with extra node to keep track of the left
        if not root: return None
        cur_child = leftmost_child  = TreeLinkNode(0)
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
                cur_child = leftmost_child
                parent = leftmost_child.next
