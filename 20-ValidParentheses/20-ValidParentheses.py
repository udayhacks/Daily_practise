# Last updated: 07/04/2026, 11:43:09
class Solution:

    def match(self,a,b):
        if ((a == '{' and b == '}' ) or (a == '(' and b == ')' ) or  (a == '[' and b ==']')) :
            return True 
        return False
      
    def isValid(self, s: str) -> bool:

        stack = []
        for i in s :
            if i in ('(','[','{') :
                stack.append(i)

            else:
                if not stack :
                    return False

                
                elif self.match(stack[-1],i) == False:
                        return False
                else:
                        stack.pop()

        if stack :
            return False

        return True

                    
        