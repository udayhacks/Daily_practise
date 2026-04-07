# Last updated: 07/04/2026, 11:37:28
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        out = 0 
        ls =[]
        i = 0 
        l = 0 
        pos = -1
        for j in range(len(nums)):
            if nums[j] == 0 :
                ls.append(j)
                l+=1
            if nums[j] == 0 and l >k :
                pos = ls[i]
                i+=1
                l-=1
            

            out  = max(out,j-pos)
        return out

