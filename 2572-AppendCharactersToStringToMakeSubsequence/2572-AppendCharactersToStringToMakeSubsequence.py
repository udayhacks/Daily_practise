# Last updated: 07/04/2026, 11:34:57
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ans = j = i =0 
        ss= len(s)
        tt = len(t)

        while i <ss and j < tt :
            if s[i] == t[j] :
                i+=1
                j+=1
            else:
                i+=1

        if tt - j :
            return tt-j
        return 0 

                

        