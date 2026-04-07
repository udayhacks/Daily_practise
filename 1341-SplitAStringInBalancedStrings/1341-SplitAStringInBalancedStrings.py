# Last updated: 07/04/2026, 11:36:41
class Solution:
    def balancedStringSplit(self, s):
        ans = 0 
        c = 0 
        for i in s :
            if i == "L":
                c-=1 
            elif i == "R":
                c+=1
            if c == 0 :
                ans+=1

        return ans 
            