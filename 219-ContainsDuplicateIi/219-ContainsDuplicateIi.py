# Last updated: 07/04/2026, 11:40:11
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}

        for i in range(len(nums) ):
            if nums[i] not in d :
                d[nums[i] ]  = i 
            elif nums[i] in d :
                if abs(d[nums[i]] - i) <= k : 
                    return True 
                else :
                    d[nums[i]]  = i 


        return False
