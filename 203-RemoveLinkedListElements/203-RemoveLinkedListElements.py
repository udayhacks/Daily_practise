# Last updated: 07/04/2026, 11:40:24
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
            cur = head 
            prev = None
            while cur:
                if cur.val == val:
                    if cur == head: head = head.next ; 
                    else: 
                        prev.next = cur.next
                        cur = cur.next
                        continue
                prev = cur 
                cur = cur.next 
                
            return head
        
            

           







        