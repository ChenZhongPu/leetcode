# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 2 or head is None:
        	return head
        i = 0
        dummy = ListNode(0)
        dummy.next = head
        a = head
        while head is not None:
        	i += 1
        	if i % k == 0:
        		a = self.reserseAux(a, head.next).next
        		head = a.next
        	else:
        		head = head.next
        return dummy.next

    # def reserseAux(self, a, b):
    # 	res = None
    # 	head = a
    # 	while head != b:
    # 		next = head.next
    # 		head.next = res
    # 		res = head
    # 		head = next
    # 	return res
    def reserserAux(self, a, b):
    	# (a, b)
    	# return the resersed last one
    	res = None
    	head = a.next
    	while head != b:
    		next = head.next
    		head.next = res
    		res = 