# Last updated: 07/04/2026, 11:34:35
class Solution:
    def finalString(self, s: str) -> str:
        l = []
        for i in s :
            if i == "i":
                l= l[::-1]
            else:
                l.append(i)
                
        return "".join(l)

        