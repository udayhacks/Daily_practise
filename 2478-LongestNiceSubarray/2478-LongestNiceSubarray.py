# Last updated: 07/04/2026, 11:35:00
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        store = 0 
        maxlengh = 1
        n = len(nums)
        left = 0 
        for right in range(n):
            while (store & nums[right]) != 0 :
                # here we removing the all set bit of leftside element because we have to strick the window 
                store ^= nums[left]
                left+=1
            #now storing set of newly added elements 
            store|= nums[right]
            maxlengh = max(right-left+1,maxlengh)
        return maxlengh

        