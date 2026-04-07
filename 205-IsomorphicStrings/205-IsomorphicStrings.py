# Last updated: 07/04/2026, 11:40:25
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ds , dt = {}, {}

        for i ,j in zip(s,t) : 
            c1 = i in ds and ds[i] != j 
            c2 = j in dt and dt[j] != i 

            if c1 or c2 :
                return False
            ds[i] = j
            dt[j]  = i 

        return True 


            
