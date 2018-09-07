"""
putting 0 is the trick
"""
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        use four pointers p,q,and cur(the result array),dummyhead to keep track of beginning.
        """
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2: return 0
        if not l1: return l2
        if not l2: return l1
        carry = 0
        cur = head = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                x = l1.val
                l1 = l1.next
            else:
                x = 0
            if l2:
                y = l2.val
                l2 = l2.next
            else:
                y = 0
            sum = x + y + carry
            cur.next = ListNode(sum % 10)
            carry = sum / 10
            cur = cur.next

        return head.next