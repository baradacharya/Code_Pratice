"""
The idea is to do inorder traversal of the binary tree.
While doing inorder traversal, keep track of the previously visited node in a variable say prev.
 For every visited node, make it next of prev and previous of this node as prev.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree(object):
    head = None
    prev  = None
    def BinaryTree2DoubleLinkedList(self,root):
        if not root:
            return
        self.BinaryTree2DoubleLinkedList(root.left)
        if self.prev == None:
            self.head = root
        else:
            root.left = self.prev
            self.prev.right = root
        self.prev = root
        self.BinaryTree2DoubleLinkedList(root.right)

    def create_Tree(self, ind, nums):
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

    def in_order_traversal(self,root):
        if not root: return None
        self.in_order_traversal(root.left)
        print (root.val)
        self.in_order_traversal(root.right)

    def printList(self,head):
        while head:
            print head.val
            head = head.right

bt = BinaryTree()
tree = bt.create_Tree(0,[1,2,3,4,5,6,7])
bt.in_order_traversal(tree)
bt.BinaryTree2DoubleLinkedList(tree)
print("DOubleLinkedlist")
bt.printList(bt.head)