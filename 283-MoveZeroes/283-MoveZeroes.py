# Last updated: 07/04/2026, 11:39:44
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        
        
        """
        zero = 0 
        for i in range(len(nums)):
            
            if nums[zero] == 0 and nums[i] != 0 :
                nums[zero], nums[i] = nums[i] , nums[zero]
            if nums[zero] != 0 :
                zero +=1
                
        return nums

                
                
                
            
                
        