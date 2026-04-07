# Last updated: 07/04/2026, 11:39:28
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<1:
            return 0 

        else:
            if(n%3==0):
                return self.isPowerOfThree(n//3) 

            else:
                return n==1