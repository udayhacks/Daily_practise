# Last updated: 07/04/2026, 11:33:45
class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        stack = []
        c= 0 
        for i in nums:
            if (len(stack) == 0 ) or (stack[-1]<= i) :
                stack.append(i)
                c+=1
                

        return c
            