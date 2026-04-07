# Last updated: 07/04/2026, 11:41:03
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = 0 
        for i in nums :
            s ^=i

        return s

        