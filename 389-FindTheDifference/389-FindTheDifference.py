# Last updated: 07/04/2026, 11:39:09
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = 0 
        for i in s :
            c^=ord(i)

        for j in t :
            c^=ord(j)


        return chr(c)
        