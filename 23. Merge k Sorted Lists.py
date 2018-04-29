#1 Brute Force T: O(nlogn) S:O(n)
#2 Compare one by one T:O(kn) S:O(n)
#3 Optimize Approach 2 by Priority Queue T:o(nlogk) S:O(k)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from Queue import PriorityQueue
        cur = head = ListNode(0)
        pq = PriorityQueue() #lowest first
        #add head of all nodes to prioty queue
        for l in lists:
            if l: pq.put((l.val, l))  # value,node
        #merge now
        while not pq.empty():
            val,node = pq.get()
            cur.next,cur = node,node
            if node.next:#add next node of this list to priorty queue
                pq.put((node.next.val,node.next))
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
p = s.create_List([1,4,5])
q = s.create_List([1,3,4])
r = s.create_List([2,6])
u = s.mergeKLists([p,q,r])
s.traverse_list(u)