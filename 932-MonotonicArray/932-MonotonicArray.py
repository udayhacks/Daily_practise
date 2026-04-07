# Last updated: 07/04/2026, 11:37:39
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        a = sorted(nums)
        b = sorted(nums,reverse=True)
        if nums == a or nums == b:
            return True
        return False