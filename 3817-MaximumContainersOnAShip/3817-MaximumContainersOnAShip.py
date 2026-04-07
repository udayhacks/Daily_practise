# Last updated: 07/04/2026, 11:33:40
class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        n = n *n 
        cap = n*w
        if cap <maxWeight:
            return n
        else:
            return maxWeight//w
        
        