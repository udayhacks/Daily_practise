# Last updated: 07/04/2026, 11:43:33
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        udy=""
        strs = sorted(strs)
        small = strs[0]
        big = strs[-1]

        n = min(len(small),len(big))
        i  = 0 
        while i < n :
            if small[i] != big[i] :
                return udy
            udy+=small[i]
            i +=1

        return udy
    
             
