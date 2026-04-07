# Last updated: 07/04/2026, 11:34:05
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        c = 0 
        for i in nums2 :
            i = i*k
            for j in nums1:
                if j%i == 0 :
                    c +=1
                    
                
                
        return c
        
        