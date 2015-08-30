/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        int n = lists.length;
        if(n == 0){
        	return  null;
        }
        if(n == 1){
        	return lists[0];
        }
        int mid = n / 2;
        ListNode a = mergeKLists(Arrays.<ListNode>copyOfRange(lists, 0, mid));
        ListNode b = mergeKLists(Arrays.<ListNode>copyOfRange(lists, mid, n));
        return merge(a, b);
    }

    private ListNode merge(ListNode a, ListNode b){
    	ListNode res = null;
    	ListNode end = null;
    	ListNode cur = null;
    	if(a == null){
    		return b;
    	}
    	if(b == null){
    		return a;
    	}
    	while (a != null && b!= null) {
    		if(a.val < b.val){
    			cur = a;
    			a = a.next;
    		}
    		else{
    			cur = b;
    			b = b.next;
    		}
    		if(res == null){
    			res = cur;
    			end = cur;
    		}
    		else{
    			end.next = cur;
    			end = end.next;
    		}
    	}
    	if(a != null){
    		end.next = a;
    	}
    	if(b != null){
    		end.next = b;
    	}
    	return res;
    }
}