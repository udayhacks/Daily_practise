# Last updated: 07/04/2026, 11:41:59
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        stack = []
        ans = []
        
        def fun(i,stack):
            if i == n :
                ans.append(stack[:n])
                return 

            stack.append(nums[i])
            fun(i+1,stack)
            stack.pop()
            fun(i+1,stack)

        fun(0,stack)
        return ans



        