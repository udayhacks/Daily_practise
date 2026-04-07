# Last updated: 07/04/2026, 11:40:20
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:



        def ref (head):
            
            if head is None or head.next is None :
                return head

            newhead = ref(head.next)
            f = head.next 
            f.next = head 
            head.next = None

            return newhead

        return ref(head)
