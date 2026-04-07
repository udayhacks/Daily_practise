# Last updated: 07/04/2026, 11:40:21
class Solution:
    def countPrimes(self, n: int) -> int:
        if n ==1 or n== 0 :
            return 0 

        
        value = [1]*n
        value[0] = value[1] = 0 
        c = 0

        for i in range(2,n) :
            if value[i] :
                c+=1
                for j in range(i*i,n,i):
                    value[j] =0 
                    

        return c




        