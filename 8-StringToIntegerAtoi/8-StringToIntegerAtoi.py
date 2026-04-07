# Last updated: 07/04/2026, 11:43:44
class Solution:
    def myAtoi(self, s: str) -> int:

        ans = i =  0 
        sign = 1 

        s = s.lstrip()
        if not s :
            return ans

        if s[0] == "-" :
            sign = -1
            i+=1
        elif s[0] == "+":
            i+=1

        
        while i < len(s):
            if not s[i].isdigit():
                break
            else:
                ans = (ans *10) + int(s[i])
            i+=1

        ans = ans *sign
        if ans > 2**31-1:
            return 2**31-1
        elif ans <= -2**31 :
            return -2**31
        else:
            return ans

        


        