# Last updated: 07/04/2026, 11:37:37
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        even = 0 
        for i in range(len(nums)):
            if nums[i] %2 == 0  and nums[even] %2 != 0 :
                nums[even] , nums[i] = nums[i] , nums[even]
                
            if nums[even] %2 == 0 :
                even+=1
                
        return nums
                
                
            
        