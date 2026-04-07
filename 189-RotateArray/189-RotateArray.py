# Last updated: 07/04/2026, 11:40:37
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k%l 
        nums[l-k:], nums[:l-k] = nums[:l-k],nums[l-k:]