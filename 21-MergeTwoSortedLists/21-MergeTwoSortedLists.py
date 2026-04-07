# Last updated: 07/04/2026, 11:43:06
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:return list2 
        if list2 is None : return list1 
        if list1.val <list2.val :
            uday = list1 
            uday.next = self.mergeTwoLists(list1.next , list2)
        else :
            uday = list2 
            uday.next = self.mergeTwoLists(list2.next,list1)
        return uday 

        