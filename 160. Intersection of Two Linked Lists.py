# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        p,q = headA,headB
        flag  = True
        while p and q:
            p = p.next
            q = q.next
            if flag:
                if not p: p = headB
                if not q: q= headA
                flag  = False
            if p == q:
                return p
        return None

