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
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyhead = ListNode(0)
        p = l1
        q = l2
        cur = dummyhead
        carry = 0
        while p!= None or q != None:
            if p != None:
                x = p.val
            else:
                x = 0

            if q != None:
                y = q.val
            else:
                y = 0

            sum = x + y + carry
            carry = sum/10
            cur.next = ListNode(sum%10)
            cur = cur.next
            if p!= None:
                p = p.next
            if q!= None:
                q = q.next

        if carry > 0:
            cur.next = ListNode(carry)

        return dummyhead.next