# Last updated: 07/04/2026, 11:40:18
class Solution:
    def minSubArrayLen(self, target: int, nums):
        i = 0 
        j= 0 
        s = 0 
        ans = 10**6
        for j in range(len(nums)):
            if s < target :
                s+=nums[j]
            if s >= target :
                while s>= target :
                    ans = min(ans ,j-i)
                    s-=nums[i]
                    i +=1
        if ans==10**6:
            return 0
        return ans+1
            
            