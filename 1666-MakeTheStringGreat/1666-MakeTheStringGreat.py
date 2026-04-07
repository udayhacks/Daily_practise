# Last updated: 07/04/2026, 11:36:04
class Solution:
    def makeGood(self, s: str) -> str:
        stack =[]
        for c in s:
            if stack:
                if ((c.isupper() and stack[-1].islower()) or (c.islower() and stack[-1].isupper())) and (c.lower() == stack[-1].lower()):
                    stack.pop()
                    continue
            
            stack.append(c)
                
        return "".join(stack)
                        
                        
        