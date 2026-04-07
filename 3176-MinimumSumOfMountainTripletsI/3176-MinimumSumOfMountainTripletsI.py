# Last updated: 07/04/2026, 11:34:24
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        sum = 10**7
        lgth = len(nums) 
        for i in range(lgth) :
            for j in range(lgth):
                for k in range(lgth) :
                    if nums[i] <nums[j] and nums[k] <nums[j] and i<j<k :
                        sum = min(sum,(nums[i]+nums[j]+nums[k]))
        if sum == 10**7 :
            return -1
        return sum
        