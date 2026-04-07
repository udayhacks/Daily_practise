# Last updated: 07/04/2026, 11:36:33
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:

        s = ""
        cur = head 
        while cur:
            s+=str(cur.val)
            cur = cur.next

        return int(s,2)
        