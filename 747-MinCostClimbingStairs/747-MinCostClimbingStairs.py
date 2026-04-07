# Last updated: 07/04/2026, 11:38:03
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        



        
        def ans (n,cache={}):
            if n < 2 :
                return cost[n]
            if n in cache:
                return cache[n] 
            cache[n] = cost[n]+min(ans(n-1),ans(n-2))
            return cache[n]
            
        n = len(cost)

        return min(ans(n-1),ans(n-2))
        