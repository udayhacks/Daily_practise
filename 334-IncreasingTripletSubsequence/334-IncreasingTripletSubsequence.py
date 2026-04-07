# Last updated: 07/04/2026, 11:39:25
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f = s = float("inf")
        for i in nums:

            if  f >= i :
                f = i
            elif s >= i :
                s = i 
            else:
                return True 

                      

        return False

        