# Last updated: 07/04/2026, 11:36:25
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hash = {}
        hash['a']= -1
        hash['b'] =-1
        hash['c'] = -1
        n = len(s)
        ans = 0 

        for i in range(n):
            hash[s[i]]= i 
            if hash['a'] != -1 and hash['b'] != -1 and hash['c'] != -1 :
                ans +=min(hash['a'] ,hash['b'] ,hash['c']) +1
        return ans

