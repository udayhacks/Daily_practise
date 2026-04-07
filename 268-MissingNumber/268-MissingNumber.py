# Last updated: 07/04/2026, 11:39:50
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        return (n*(n+1)//2)-sum(nums)



        

        