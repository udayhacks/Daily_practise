// Last updated: 07/04/2026, 11:43:01
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



private:

ListNode* merge(ListNode*&l1,ListNode*&l2){
    ListNode* node = new ListNode(0);
    ListNode *cur = node;

    while( l1 && l2){
        if ( l1->val <= l2->val){
            cur->next = l1;
            l1 = l1->next;
        }else{
            cur->next = l2;
            l2 = l2->next;
        }
        cur= cur->next;
    }cur->next = l1?l1:l2;
    return node->next;



}
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        
        auto cmp= [](ListNode * a , ListNode* b){
            return a->val > b->val;
        };

        priority_queue< ListNode*,vector<ListNode*>, decltype(cmp)> pq(cmp);

        for (auto l :lists){
           if (l != nullptr)
        pq.push(l);
        }

        ListNode * result = new ListNode(0);
        
         ListNode * dummy = result;


        while(!pq.empty()){

           ListNode* top = pq.top();
            pq.pop();

            dummy->next = top;
            dummy = dummy->next ;

            if ( top->next != nullptr){
                pq.push(top->next);
            }




        }return result->next;
        







    }
};