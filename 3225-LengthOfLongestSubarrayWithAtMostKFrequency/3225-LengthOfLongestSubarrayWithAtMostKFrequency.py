# Last updated: 07/04/2026, 11:34:20
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        i , j = 0, 0

        maxx = 1
        mapp = {}

        while i < len(nums) and j < len(nums):
            
            mapp[nums[j]] = mapp.get(nums[j], 0) + 1

            if mapp[nums[j]] > k:
                maxx = max(j-i, maxx)
                while mapp[nums[j]]>k:
                    mapp[nums[i]] -= 1
                    i = i+1
            
            j += 1 

        return max(maxx, j-i)           
