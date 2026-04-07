# Last updated: 07/04/2026, 11:35:27
class Solution:
    def countGoodNumbers(self, n: int) -> int:


        mod = (10**9+7)
        def power(x,n,mod) :
            if n == 1 :
                return x 
            if n == 0 :
                return 1
            if n % 2 == 1 :
                k = x*power(x,n-1,mod)
                return (k )% mod
            else:
                j = power(x,n//2,mod)
                return (j%mod)*(j%mod)

        even = (n//2)+(n%2)
        od = n//2
        return (power(5,even,mod)*power(4,od,mod))%mod
                


        