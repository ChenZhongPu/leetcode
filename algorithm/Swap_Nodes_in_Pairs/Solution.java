/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        if(head == null || head.next == null){
        	return head;
        }
        else{
        	ListNode t = head.next;
            head.next = swapPairs(t.next);
        	t.next = head;
        	return t;
        }
    }
}