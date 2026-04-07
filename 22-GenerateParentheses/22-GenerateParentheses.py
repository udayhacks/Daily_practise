# Last updated: 07/04/2026, 11:43:02
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        openN = 0 
        closeN = 0 
        ans = []
        stack = []
        def fun(openN,closeN) :
            if openN == closeN == n :
                ans.append("".join(stack))
                return 

            if openN < n :
                stack.append("(")
                fun(openN+1,closeN)
                stack.pop()

            if closeN < openN :
                stack.append(")")
                fun(openN,closeN+1)
                stack.pop()

        fun(0,0)
        return ans 


                








         