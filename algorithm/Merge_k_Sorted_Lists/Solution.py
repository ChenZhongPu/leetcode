import heapq
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = []
        res = None
        end = None
        for l in lists:
        	if l is not None:
        		heapq.heappush(h, (l.val, l))
        while h:
        	l = heapq.heappop(h)[1]
        	if res is None:
        		res = l
        		end = l
        	else:
        		end.next = l
        		end = end.next
        	if l.next is not None:
        		l = l.next
        		heapq.heappush(h, (l.val, l))
        return res