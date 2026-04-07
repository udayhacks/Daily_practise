# Last updated: 07/04/2026, 11:40:38
class Solution:
    def trailingZeroes(self, n: int) -> int:
        i = 5
        ans = 0  
        while i<= n :
            ans +=n//i
            i*=5
        return ans

        