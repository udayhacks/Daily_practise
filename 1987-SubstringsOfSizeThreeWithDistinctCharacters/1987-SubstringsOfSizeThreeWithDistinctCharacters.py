# Last updated: 07/04/2026, 11:35:31
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c=0

        i = 0 
        j = 3 
        while j <= len(s) :
            k= s[i:j]
            if len(k) == len(set(k)) :
                c+=1
            i+=1
            j+=1

        
        return c

