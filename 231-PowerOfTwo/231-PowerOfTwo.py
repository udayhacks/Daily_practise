# Last updated: 07/04/2026, 11:40:08
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if  n >0 and n & (n-1) == 0  :
            return True 
        return False 
        