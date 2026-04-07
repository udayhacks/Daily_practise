# Last updated: 07/04/2026, 11:41:47
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None  :
            return head
        dumy = ListNode(next = head) 
        curr = dumy 
        while curr: 
            if curr.next and curr.next.next and curr.next.val == curr.next.next.val :
                temp = curr.next.next
                while temp and temp.next and temp.val == temp.next.val:
                    temp= temp.next 
                curr.next = temp.next
            else:
                curr = curr.next 
        return dumy.next 




        