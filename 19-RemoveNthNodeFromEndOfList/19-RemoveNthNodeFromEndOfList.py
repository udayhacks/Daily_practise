# Last updated: 07/04/2026, 11:43:20
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 

        dumy = f = s = ListNode(val = 0 , next = head )

        for i in range(n) :
            s = s.next 

        while s.next : 
            s= s.next 
            f = f.next 

        f.next = f.next.next 

        return dumy.next







        











