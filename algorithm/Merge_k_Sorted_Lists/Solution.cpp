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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int n = lists.size();
        if(n == 0){
        	return NULL;
        }
        if(n == 1){
        	return lists[0];
        }
        int mid = n / 2;
        vector<ListNode*> left(lists.begin(), lists.begin() + mid);
        vector<ListNode*> right(lists.begin() + mid, lists.end());
        ListNode* a = mergeKLists(left);
        ListNode* b = mergeKLists(right);
        return merge(a, b);
    }
private:
	ListNode* merge(ListNode* a, ListNode* b){
		ListNode *res = NULL;
		ListNode *end = NULL;
		ListNode *cur = NULL;
		if(a == NULL){
			return b;
		}
		if(b == NULL){
			return a;
		}
		while(a && b){
			if(a->val < b->val){
				cur = a;
				a = a->next;
			}
			else{
				cur = b;
				b = b->next;
			}
			if(res == NULL){
				res = cur;
				end = cur;
			}
			else{
				end->next = cur;
				end = end->next;
			}
		}
		if(a){
			end->next = a;
		}
		if(b){
			end->next = b;
		}
		return res;
	}
};