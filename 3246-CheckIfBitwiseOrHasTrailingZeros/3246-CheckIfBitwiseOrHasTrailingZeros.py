# Last updated: 07/04/2026, 11:34:15
class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        for i in range(len(nums)) :
            for j in range(i+1 , len(nums)):
                k = bin((nums[i]|nums[j]))
                if k[-1] == '0' :
                        return True 
        return False
        