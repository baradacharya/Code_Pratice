"""
deleting a node  from a linked list : modify the next pointer of the node before it, to point to the node after it.
Since we do not have access to the node before the one we want to delete,
Instead, we have to replace the value of the node we want to delete with the value in the node after it, and then delete the node after it.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next