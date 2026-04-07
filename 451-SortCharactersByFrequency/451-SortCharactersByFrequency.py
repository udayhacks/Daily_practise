# Last updated: 07/04/2026, 11:39:01
class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        
        count = Counter(s)
        
        k = sorted(count.items() ,key=lambda x:x[1],reverse=True)
        
        
        ans = ""
        for i in k :
            q ,w = i 
            ans +=(q*w)
            
            
        return ans 
            
        
        
        

        
        