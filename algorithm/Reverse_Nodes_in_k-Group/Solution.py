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
        if head is None:
        	return head
        h = head
        n = 0
        while h is not None:
        	n += 1
        	h = h.next
        num_groups = n // k
        if num_groups == 0:
        	return head
        last_group = num_groups * k;
        res = None
        res_end = None
        temp = None
        temp_end = None
        i = 1
        while head is not None:
        	next_node = head.next
        	if i <= last_group:
        		if temp is None:
        			temp_end = head
        		head.next = temp
        		temp = head
        		if i % k == 0:
        			if res is None:
        				res = temp
        				res_end = temp_end
        			else:
        				res_end.next = temp
        				res_end = temp_end
        			temp = None
        	else:
        		res_end.next = head
        		break
        	i += 1
        	head = next_node
        return res