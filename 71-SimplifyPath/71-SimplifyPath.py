# Last updated: 07/04/2026, 11:42:03
class Solution:
    def simplifyPath(self, path: str) -> str:
        pathList = path.split("/")
        stack = [] 
        for i in pathList :
            if stack and i == '..' :
                stack.pop()
            elif i != "" and i != "."  and i != '..':
                stack .append(i)
                
        return "/"+"/".join(stack) 
                
        