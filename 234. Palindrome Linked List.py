# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #1.find the mid node
        fast = slow = head
        while fast and fast.next:#using fast.next.next, so need to check fast and fast.next exists
            slow,fast = slow.next,fast.next.next
        #2.reverse the second half
        prev = None
        while slow:
            next_node = slow.next
            slow.next,prev,slow = prev,slow,next_node
        #3.compare the first and second half nodes
        node  = prev
        while node:
            if node.val != head.val:
                return False
            node,head = node.next,head.next
        return True