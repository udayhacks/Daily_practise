# Last updated: 07/04/2026, 11:33:52
class Solution:
    def kthCharacter(self, k: int) -> str:
        def next (s):
            ans=[]
            for i in s :
                ans.append(chr(ord(i)+1))

            s.extend(ans)

        

        s = ["a"]

        while k > len(s):
            next(s)

        return s[k-1]

            
            
            


