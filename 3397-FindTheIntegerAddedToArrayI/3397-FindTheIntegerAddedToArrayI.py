# Last updated: 07/04/2026, 11:34:10
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        k = max(nums1)
        j = max(nums2)
        return j-k