# Last updated: 07/04/2026, 11:43:04
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0 
        l = []
        for i in nums:
            if i not in  l:
                nums[k] = i
                l.append(i)
                k +=1 

        return k




       


        