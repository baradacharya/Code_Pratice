# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#1. cut the list to two halves
#2. sort each half
#3. merge l1 and l2
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        prev,slow,fast = None,head,head
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None #important end of 1st list
        return self.merge(self.sortList(head),self.sortList(slow))

    def merge(self,l1,l2):
        cur = head = ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                cur.next,cur,l1 = l1,l1,l1.next
            else:
                cur.next,cur,l2 = l2,l2,l2.next
        cur.next = l1 or l2
        return head.next

    def create_List(self,nums):
        if not list: return None
        cur = head = ListNode(0)
        for num in nums:
            node = ListNode(num)
            cur.next = node
            cur = cur.next
        return head.next

    def traverse_list(self,list):
        while list:
            print list.val
            list = list.next


s = Solution()
l = s.create_List([4,2,1,3])
t = s.sortList(l)
s.traverse_list(t)
