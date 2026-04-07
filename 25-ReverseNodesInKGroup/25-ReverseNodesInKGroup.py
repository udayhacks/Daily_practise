# Last updated: 07/04/2026, 11:42:59
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr=head
        for _ in range(k):
            if not curr:return head
            curr=curr.next
        

        #simply put code for reversing a link list which is a LC easy problem.
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        #then simply put recursion for every k count
        head.next = self.reverseKGroup(curr, k)
        return prev