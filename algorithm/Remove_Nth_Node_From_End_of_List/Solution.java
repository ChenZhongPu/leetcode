/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode h = head;
        ListNode p = null;
        int i = 0;
        while (head != null) {
        	if(i == n){
        		p = head;
        	}
        	else if(i > n){
        		p = p.next;
        	}
        	i++;
        	head = head.next;
        }
        if(p == null){
        	return h.next;
        }
        else{
        	p.next = p.next.next;
        }
        return h;
    }
}