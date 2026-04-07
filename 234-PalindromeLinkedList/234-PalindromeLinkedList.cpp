// Last updated: 07/04/2026, 11:39:56
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
    bool isPalindrome(ListNode* head) {
        ListNode *mid = head;
        ListNode *last = head;
        
        //now finding the mid point using slow and fast pointer trick
        while (last != nullptr && last->next != nullptr){
            last = last->next->next;
            mid = mid->next;
            
        }

        ListNode *prev = nullptr;
        while(mid != nullptr){
            ListNode*tmp = mid->next;
            mid->next = prev;
            prev = mid;
            mid = tmp;

        }



        while(prev){
            if (prev->val != head->val){
                return false;
            }
            prev= prev->next;
            head= head->next;
        }
        return true;
        
    }
};