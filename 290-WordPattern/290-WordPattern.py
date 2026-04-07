# Last updated: 07/04/2026, 11:39:36
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ds , dt = {} , {}
        t = s.split(" ")
        s = list (pattern) 
        if len(s) != len(t) :
            return False  


        for i ,j in zip(s,t) : 
            c1 = i in ds and ds[i] != j 
            c2 = j in dt and dt[j] != i 

            if c1 or c2 :
                return False
            ds[i] = j
            dt[j]  = i 

        return True 




    
        
        