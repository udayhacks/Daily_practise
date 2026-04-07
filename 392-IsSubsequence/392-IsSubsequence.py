# Last updated: 07/04/2026, 11:39:07
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool: 
        j = 0 

        if len(s) == 0 :
            return True
        for i in range(len(t)) :
            if t[i] == s[j]:
                j +=1
            if j == len(s) :
                return True 
        return False 
            

     

        