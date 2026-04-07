# Last updated: 07/04/2026, 11:40:58
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rabbit = head 
        hare = head 

        while hare is not None and hare.next is  not None :
            rabbit = rabbit.next 
            hare = hare.next.next 
            if rabbit == hare :
                return True
        return False
        