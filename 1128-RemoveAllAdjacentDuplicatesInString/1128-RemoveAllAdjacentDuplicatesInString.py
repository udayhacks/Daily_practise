# Last updated: 07/04/2026, 11:37:03
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s :
            if len(stack) == 0 :
                stack.append(i)
            elif stack and stack[-1]  != i:
                stack.append(i) 
            else :
                if stack :
                    stack.pop()
        return ''.join(stack)
