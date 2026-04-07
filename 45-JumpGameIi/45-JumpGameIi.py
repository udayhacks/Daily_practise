# Last updated: 07/04/2026, 11:42:29
class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0

        res = 0 
        j = 0

        while r < len(nums)-1:
            length = 0 

            for i in range(l,r+1):
                length = max(length,i+nums[i]) 

            l = r+1
            r = length
            
           
            res+=1

        return res 

        