# Last updated: 07/04/2026, 11:37:41
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head 
        count = 0 
        while temp :
            count+=1
            temp = temp.next 
        
        temp = head 
        ans = ceil(count//2)
        
        count = 0 

        while temp :
            if ans == count:
                return temp
            temp = temp.next
            count+=1

        

        