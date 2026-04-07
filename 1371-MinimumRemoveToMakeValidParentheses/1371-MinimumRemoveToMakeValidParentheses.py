# Last updated: 07/04/2026, 11:36:36
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        
        for i in range(len(s)) :
            if s[i] == "(":
                stack.append(i)

            else:
                if s[i] == ")":
                    if stack :
                        stack.pop()
                    else:
                        s[i] = ""  

        while stack :
            s[stack.pop()] = ""
      

      


        return "".join(s)
                
        