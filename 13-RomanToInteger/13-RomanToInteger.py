# Last updated: 07/04/2026, 11:43:36
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {


'I'  :           1,
'V'  :          5,
'X'    :         10,
'L'     :        50,
'C'      :     100,
'D'       :      500,
'M'        :     1000



        } 
        n = len(s)
        ans = 0 
        for i in range(n) :
            if  i == n -1 :
                ans += d[s[i]]
            elif d[s[i]] < d[s[i+1]] :
                ans-= d[s[i]]
            else:
                ans+= d[s[i]] 

        return ans 
                





        
        