# Last updated: 07/04/2026, 11:34:04
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        
        nums.sort()
        i = 0 
        h= sys.maxsize 
        j = len(nums)-1
        while i < j:
            h = min((nums[i]+nums[j])/2,h)
            i+=1
            j-=1
            
        return h
            
            
            
        