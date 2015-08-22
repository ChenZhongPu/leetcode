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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        ListNode *res = NULL, **res_end = &res;
        while(l1 != NULL || l2 != NULL || carry == 1){
        	int temp = 0;
        	if(l1 != NULL){
        		temp += l1->val;
        		l1 = l1->next;
        	}
        	if(l2 != NULL){
        		temp += l2->val;
        		l2 = l2->next;
        	}
        	temp += carry;
        	int digit = temp % 10;
        	carry = temp / 10;

        	ListNode *node = new ListNode(digit);
        	*res_end = node;
        	res_end = (&node->next);
        }
        return res;
    }
};