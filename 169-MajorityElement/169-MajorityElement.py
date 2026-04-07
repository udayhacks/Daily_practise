# Last updated: 07/04/2026, 11:40:45
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        return nums[n//2]