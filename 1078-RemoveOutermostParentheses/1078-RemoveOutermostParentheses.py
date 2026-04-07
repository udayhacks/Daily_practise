# Last updated: 07/04/2026, 11:37:11
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opened = 0 
        k = ""
        closed = 0 
        start = 0
        for i in range(len(s)):
            if s[i] == "(":
                opened+=1
            if s[i] == ")" :
                closed +=1
            if opened == closed :
                k+=s[start+1:i]
                start = i+1

        return k


        