// Last updated: 07/04/2026, 11:43:11
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // Create a dummy node to handle edge cases
        ListNode* dummy = new ListNode(0, head);
        ListNode* fast = dummy;
        ListNode* slow = dummy;

        // Move fast n steps ahead
        for (int i = 0; i < n; ++i) {
            fast = fast->next;
        }

        // Move fast to the end, maintaining the gap
        while (fast->next != nullptr) {
            fast = fast->next;
            slow = slow->next;
        }

        // Remove the nth node from end
        slow->next = slow->next->next;

        // Return the updated head
        return dummy->next;
    }
};

