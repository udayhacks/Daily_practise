# Last updated: 07/04/2026, 11:35:54
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        mx = -1
        if n == 0 :
            return 0
        l = [0]*(n+1)
        l[0] = 0
        l[1] = 1
        j = 0 

      

        for i in range(1, n) :
            if 2*i <= n :
                l[2*i] = l[i]
            if 2*i+1 <= n :
                l[2*i+1] = l[i]+l[i+1]

        return max(l)

           