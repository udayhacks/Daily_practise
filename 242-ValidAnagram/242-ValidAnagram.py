# Last updated: 07/04/2026, 11:39:51
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d = {}
        h = {}
        if len(s)  != len(t)  :
            return False
        for i in range(len(s)):
            k = s[i]
            if k not in d :
                d[k] =1
            else:
                d[k]+=1 
                
                
        for i in t :
            if i not in h :
                h[i] = 1
            else:
                h[i]+=1
           
      
       
        for i in h :
                if h[i] != d.get(i) :
                    return False
        return True 

    

      
     
            




            
           
            