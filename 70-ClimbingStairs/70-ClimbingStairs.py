# Last updated: 07/04/2026, 11:42:11
class Solution:
    def climbStairs(self, n: int) -> int:
        s,l = 1 , 2
        for _ in range(2, n): 
            # swapping `s` and `l`
            s, l = l, s + l 
        return l if n > 1 else s