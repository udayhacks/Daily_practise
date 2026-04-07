# Last updated: 07/04/2026, 11:35:01
class Solution:
    def removeStars(self, s: str) -> str:
        stack  = []
        for i in s :
            if stack and i == "*" :
                stack.pop()
                continue 
            stack.append(i)

        return ''.join(stack) 