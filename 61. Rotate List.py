# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cur = head
        len = 1
        #get the length of list
        while cur.next:
            cur = cur.next
            len +=1
        #make circular
        cur.next = head
        k = k% len #update k to len range
        for i in range(len-k):#move len- k from start
            cur = cur.next
        head = cur.next
        cur.next = None
        return head