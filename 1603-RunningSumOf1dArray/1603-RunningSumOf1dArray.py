# Last updated: 07/04/2026, 11:36:11
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        j =[]
        for i in range(len(nums)):
            j.append(sum(nums[0:i+1]))

        return j
            