# Last updated: 07/04/2026, 11:35:34
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        from math import prod
        n = prod(nums)
        if n > 0 :
            return 1 
        elif n<0 :
            return -1 
        else :
            return 0        
        