# Last updated: 07/04/2026, 11:39:22
class Solution:
    def reverseString(self, s: List[str]) -> None:
        if len(s) == 0 :
            return 
        
        
        x = s.pop(0)
        self.reverseString(s)
        s.append(x)

        
        return s
    
    
        
        
      