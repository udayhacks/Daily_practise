# Last updated: 07/04/2026, 11:40:00
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        last = mid = head

        while last and last.next :
            last = last.next.next
            mid = mid.next 

        prev = None 

        while mid :
            tmp = mid.next 
            mid.next = prev 
            prev = mid 
            mid = tmp
        

        lft , rght = head , prev 
        while rght :
            if rght.val != lft.val :
                return False 

            lft = lft.next 
            rght = rght.next
        return True 
        
     



        