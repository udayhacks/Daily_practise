# Last updated: 07/04/2026, 11:41:11
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        f = set(nums)
        ans= 0 
        
        for i in nums :
            if i-1 not in f :
                l = 0 
                while (i+l)in f :
                    l+=1 
                ans = max (l,ans)


        return ans 
                
        