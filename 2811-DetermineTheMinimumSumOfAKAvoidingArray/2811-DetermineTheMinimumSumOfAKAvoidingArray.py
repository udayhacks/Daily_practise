# Last updated: 07/04/2026, 11:34:41
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        
        i = 1 
        ans  = 0 
        count = 1
        #l = [] 
        j = k//2
        while count <= n :
            
            
            if i < j+1 :
                #l.append(i)
                ans +=i
                i+=1
                count+=1
                
            else :
                #l.append(k)
                ans += k 
                k+=1
                count +=1
        return ans
            
        