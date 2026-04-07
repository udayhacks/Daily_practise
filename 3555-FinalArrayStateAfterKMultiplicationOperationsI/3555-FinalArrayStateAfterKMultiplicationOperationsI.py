# Last updated: 07/04/2026, 11:33:56
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        for i in range(k):
            l = nums[0]
            ii = 0 
            for j in range(len(nums)):
                if l > nums[j]:
                    ii = j 
                    l = nums[j]
                    
            nums[ii] = l*multiplier
            
            
        return nums
                    
    
        
        
        

            
        