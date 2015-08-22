/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode res = null;
        ListNode res_end = null;
        while(l1 != null || l2 != null || carry == 1){
        	int temp = 0;
        	if(l1 != null){
        		temp += l1.val;
        		l1 = l1.next;
        	}
        	if(l2 != null){
        		temp += l2.val;
        		l2 = l2.next;
        	}
        	temp += carry;
        	int digit = temp % 10;
        	carry = temp / 10;
        	if(res == null){
        		res = new ListNode(digit);
        		res_end = res;
        	}else{
        		res_end.next = new ListNode(digit);
                res_end = res_end.next;
        	}
        }
        return res;
    }
}