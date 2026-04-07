# Last updated: 07/04/2026, 11:37:38
from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums, goal) -> int:
        s = 0 
        c =0 
        scrap = 0 
        l =defaultdict(int)
        l[0] = 1
        n = len(nums)
        for a,b in enumerate(nums):
            s +=b
            scrap = s-goal
            
            c+=l[scrap]
            
            l[s] +=1
        return c
            
              