# Last updated: 07/04/2026, 11:42:22
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0 
        m = -sys.maxsize
        for i in nums :
            s+=i
            if s > m :
                 m = s 
            if s<0 :
                s= 0 


        return m
        