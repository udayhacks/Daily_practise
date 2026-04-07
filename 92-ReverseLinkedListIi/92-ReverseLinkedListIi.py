# Last updated: 07/04/2026, 11:41:42
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:



        lprev = dumy = ListNode(0,head)
        curr = head 
        for i in range(left-1) :
            lprev = lprev.next
            curr = curr.next 

        prev = None 
        d= (right- left) +1
        for i in range(d) :
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr= temp 


        lprev.next.next = curr
        lprev.next = prev
    

        return dumy.next 




        
        