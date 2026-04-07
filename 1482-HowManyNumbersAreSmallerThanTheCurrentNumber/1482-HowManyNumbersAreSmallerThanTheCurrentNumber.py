# Last updated: 07/04/2026, 11:36:21
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]: 
        k = sorted(nums)
        ans = []
        for i in nums :
            ans.append(k.index(i))


        return ans 
            


        