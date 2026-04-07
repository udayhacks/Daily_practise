# Last updated: 07/04/2026, 11:42:14
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = -1
        l =0 
        n = len(s)-1
        
        while  n >= 0 :
            

            if s[n] != " " :
                l +=1
            if s[n] == " " and l > 0:
                return l 
            n-=1

        return l 
        


       

