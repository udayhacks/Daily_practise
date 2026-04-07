# Last updated: 07/04/2026, 11:41:02
class Solution:
    def singleNumber(self, nums: List[int]) -> int: 
        
        nums.sort()
        ans = 0 
        i = 0 
        j = i+2
        

        while j < len(nums):
            if nums[i] != nums[j]:
                break
                
            i = j+1
            j +=3
            
        
        if j-i ==  2 :
            ans =nums[i]
            
        elif nums.count(nums[i]) ==3 :
            
            ans = nums[j ]
        else :
            ans = nums[i]


        return ans

                    