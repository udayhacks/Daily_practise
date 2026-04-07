# Last updated: 07/04/2026, 11:40:53
class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = 1e5
        for i, num in enumerate(nums):
            if num < min_val:
                min_val = num
            if i > 0 and num < nums[i-1]:
                break
        return min_val
           