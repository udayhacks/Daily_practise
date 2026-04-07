// Last updated: 07/04/2026, 11:42:12
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !head->next || k == 0)
            return head;

        // Step 1: Find the length of the list
        int length = 1;
        ListNode* tail = head;
        while (tail->next) {
            tail = tail->next;
            length++;
        }

        // Step 2: Normalize k
        k = k % length;
        if (k == 0)
            return head;

        // Step 3: Find the new tail: node at (length - k - 1)
        int steps_to_new_tail = length - k;
        ListNode* new_tail = head;
        for (int i = 1; i < steps_to_new_tail; i++) {
            new_tail = new_tail->next;
        }

        // Step 4: Rearrange pointers
        ListNode* new_head = new_tail->next;
        new_tail->next = nullptr;
        tail->next = head;

        return new_head;
    }
};
