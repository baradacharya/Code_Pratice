# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = dummy = ListNode(0)
        cur = dummy.next = head
        print prev.val,prev.next.val,cur.val,cur.next.val
        #prev->cur
        while cur and cur.next:
            val = cur.next.val
            if cur.val < val: #already sorted, no need to insert
                cur = cur.next
                continue
            print prev.val, prev.next.val, cur.val
            if prev.next.val > val:#Trik: don't run prev always from beginning
                prev = dummy #start from the beginning
            while prev.next.val < val:#find the insertion point
                prev = prev.next
            new = cur.next
            cur.next = new.next
            new.next = prev.next
            prev.next = new
            print prev.val, prev.next.val, cur.val
        return dummy.next

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
p = s.create_List([4,1,2,3])
# s.traverse_list(p)
r = s.insertionSortList(p)
# s.traverse_list(r)


