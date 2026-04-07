// Last updated: 07/04/2026, 11:39:53
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
    void deleteNode(ListNode* node) {

        node->val = node->next->val;
        // here clearly mention that node is not last node .
        node->next = node->next->next;

        
    }
};