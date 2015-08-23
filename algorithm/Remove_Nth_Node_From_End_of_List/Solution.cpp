/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* h = head;
        ListNode* p = NULL;
        int i = 0;
        while (head != NULL){
        	if(i == n){
        		p = h;
        	}
        	else if(i > n){
        		p = p->next;
        	}
        	i++;
        	head = head->next;
        }
        if(p == NULL){
        	return h->next;
        }
        else{
        	p->next = p->next->next;
        }
        return h;
    }
};