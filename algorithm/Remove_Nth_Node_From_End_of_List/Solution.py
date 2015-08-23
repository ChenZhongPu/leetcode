# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return head
        h = head
        p = None
        i = 0
        while head is not None:
            if i == n:
                p = h
            elif i > n:
                p = p.next
            i += 1
            head = head.next
        if p is None:
            return h.next
        else:
            p.next = p.next.next
        return h