# Last updated: 07/04/2026, 11:33:47
class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        count = 1
        if len(s) == 1 and k ==1 :
            return True
        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                count+=1   
            else:
                if count == k :
                    return True
                count =1 
            
            
            
        if count ==k :
                return True     
        return False
            
        