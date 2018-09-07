# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or m == n: return head
        revHead = dummy = ListNode(None)
        dummy.next = head
        for i in range(m - 1): revHead = revHead.next
        tail = revHead.next

        for i in range(n - m):
            tmp = revHead.next  # a)
            revHead.next = tail.next  # b)
            tail.next = tail.next.next  # c)
            revHead.next.next = tmp  # d)
        return dummy.next
