# Last updated: 07/04/2026, 11:34:13
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        k = {}
        for i in nums :
            if i in k :
                k[i] +=1
                if k[i]> 2 :
                    return False
                
            else:
                k[i] = 1
                
        return True
        
        