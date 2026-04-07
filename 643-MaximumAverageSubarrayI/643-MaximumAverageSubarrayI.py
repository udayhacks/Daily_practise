# Last updated: 07/04/2026, 11:38:23
class Solution:
    def findMaxAverage(self, nums, k) -> float:

        i = j = 0
        sums = 0 
        m =a = -10**5

        while j < len(nums):
            
            cond = j-i+1
            if cond <k :
                sums+=nums[j]
                j+=1
            elif cond == k :
                sums+=nums[j]
                a= sums/k 
                sums-=nums[i]
                i+=1
                j+=1
            if a > m :
                m =a 
        return m


            