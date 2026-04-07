# Last updated: 07/04/2026, 11:37:47
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        stackT = []

        for i in s :
            if stackS and i == "#" :
                stackS.pop()
            elif i != "#":
                stackS.append(i)

        
        for i in t :
            if stackT and i == "#" :
                stackT.pop()
            elif i != "#" :
                stackT.append(i)

        if stackS == stackT  :
            return True 
        return False
        
        