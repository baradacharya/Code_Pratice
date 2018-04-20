"""
Two pointers method
So if two linkedlist intersects, the meeting point in second iteration must be the intersection point.
If the two linked lists have no intersection at all,
then the meeting pointer in second iteration must be the tail node of both lists, which is null
"""
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
        while p != q:
            if not p : p = headB #end of 1st iteration
            else: p = p.next
            if not q: q = headA #end of 1st iteration
            else: q =  q.next

        return p

