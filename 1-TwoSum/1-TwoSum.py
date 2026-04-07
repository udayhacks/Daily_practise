# Last updated: 07/04/2026, 11:43:58
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        note = {}

        for i in range(len(nums)) :

            d = target - nums[i] 
            if d in note :
                return [note[d], i ]

            note[nums[i]] = i     
    