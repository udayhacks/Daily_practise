# Last updated: 07/04/2026, 11:43:47
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        num = sorted(nums1+nums2) 
        b = len(num)//2
        if len(num) % 2 == 0 :
            m = (num[b]+num[b-1])/2
            return m
            
        else:
            m = num[b]
            return m 