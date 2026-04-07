# Last updated: 07/04/2026, 11:42:23
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def solv(x,n):
            if n ==0 :
                return 1
            if n == 1 :
                return x 
            if  n % 2 == 1 :
                return x*solv(x,n-1)
            else:
                 k = solv(x,n//2)
                 return k*k




        f= solv(x,abs(n))
        return float(f) if n >=0  else 1/f
        
        