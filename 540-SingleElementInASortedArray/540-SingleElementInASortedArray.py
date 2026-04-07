# Last updated: 07/04/2026, 11:38:39
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2

            # make sure mid is always set to even
            if mid % 2 != 0:
                mid -= 1

            # search right side
            if nums[mid] == nums[mid + 1]:
                lo = mid + 2
            # search left side
            else:
                hi = mid

        return nums[lo]