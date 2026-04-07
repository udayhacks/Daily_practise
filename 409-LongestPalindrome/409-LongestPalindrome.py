# Last updated: 07/04/2026, 11:39:02
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        res = 0
        odd = False
        for i in c:
            if c[i]%2 == 0:
                res += c[i]
            else:
                res += c[i]-1
                odd = True

        return res if not odd else res+1