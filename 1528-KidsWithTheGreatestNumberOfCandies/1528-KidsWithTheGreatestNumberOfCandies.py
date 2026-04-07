# Last updated: 07/04/2026, 11:36:17
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        k= max(candies)
        res= [False]*len(candies)
        for i in range(len(candies)) : 
            if candies[i]+extraCandies >= k :
                res[i] = True
        return res

        