"""
#1 (Hash Table) T:O(n) S:O(n)
#2 (Two Pointers) T:O(n) S: O(1)
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# #1. Hash table
# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         if not head: return False
#         seen  = set()
#         while head:
#             if head in seen:
#                 return True
#             else:
#                 seen.add(head)
#             head = head.next
#         return False

#Two pointer
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return False
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
