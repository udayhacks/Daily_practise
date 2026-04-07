# Last updated: 07/04/2026, 11:37:21
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        k = [] 
        for i in nums :
            k.append(i*i)
        k.sort()
        return k