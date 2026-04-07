# Last updated: 07/04/2026, 11:38:57
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        c = 0 
        S = G = 0 
        while S <len(s)  and G < len(g) :
            if s[S] >= g[G] :
                c+=1
                S+=1
                G+=1
            else:
                S+=1

        return c




       