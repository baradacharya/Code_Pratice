# https://leetcode.com/problems/linked-list-random-node/discuss/85662/Java-Solution-with-cases-explain
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        if not self.head:
            return
        node = self.head
        ans = node.val
        count = 0
        while node.next:
            node = node.next
            count += 1
            import random
            if random.randint(0, count) == count:
                ans = node.val
        return ans

