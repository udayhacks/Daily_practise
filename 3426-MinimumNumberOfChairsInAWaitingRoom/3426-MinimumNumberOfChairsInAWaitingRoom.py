# Last updated: 07/04/2026, 11:34:08
class Solution:
    def minimumChairs(self, s: str) -> int:
        k = ans = 0 
        for i in s :
            if i == 'E' :
                k+=1
            else:
                k-=1
            ans = max(ans,k)
            if k < 0 :
                k = 0 
                
        return ans 
            
        