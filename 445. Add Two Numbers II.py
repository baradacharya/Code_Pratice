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
        p, q = [], []
        cur = None
        carry = 0
        while l1 != None:
            p.append(l1.val)
            l1 = l1.next

        while l2 != None:
            q.append(l2.val)
            l2 = l2.next
        sum = 0
        while p or q:
            if p:
                x = p.pop()
            else:
                x = 0
            if q:
                y = q.pop()
            else:
                y = 0
            sum = x + y + carry
            carry = sum / 10
            prev = ListNode(sum % 10)
            prev.next = cur
            cur = prev

        if carry > 0:
            prev = ListNode(carry)
            prev.next = cur
        return prev