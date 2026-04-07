// Last updated: 07/04/2026, 11:40:51
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* sortList(ListNode* head) {
    vector<int> arr;
    ListNode* dummy = head;
    ListNode* node = head;

    while (node){
        arr.push_back(node->val);
        node = node->next;
    }

    sort(arr.begin(),arr.end());
    int i = 0 ;

    while(dummy){
        dummy->val = arr[i];
        i++;
        dummy = dummy->next;
    }
    return head;
    



    }
};