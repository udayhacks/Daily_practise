# Last updated: 07/04/2026, 11:42:05
class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        while i*i <= x :
            if i*i == x :
                return i 
            i+=1 

        return i-1

        