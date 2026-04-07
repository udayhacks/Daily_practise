# Last updated: 07/04/2026, 11:34:54
class Solution:
    
    def SieveOfEratosthenes(n):
        prime = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        return prime
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def SieveOfEratosthenes(n):
            prime = [True for i in range(n+1)]
            p = 2
            while (p * p <= n):
                if (prime[p] == True):
                    for i in range(p * p, n+1, p):
                        prime[i] = False
                p += 1
            return prime
        l= SieveOfEratosthenes(right)
        k = []
        for i in range(left,right+1):
            if i>1 and l[i] == True:
                k.append(i)
        mn =100000
        a = -1
        b = -1
        for i in range(len(k)-1,0,-1):
            
            if k[i] - k[i-1] <= mn:
                mn = min(k[i] - k[i-1],mn)
                a = k[i]
                b = k[i-1]
        return [b,a]
        
    
        
        