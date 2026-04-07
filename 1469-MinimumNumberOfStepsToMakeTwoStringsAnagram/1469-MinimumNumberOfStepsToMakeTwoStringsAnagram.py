# Last updated: 07/04/2026, 11:36:24
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a= Counter(s)
        b = Counter(t)
        # Count the required characters in t that are s  
        ans = 0
        for i in a :
            if b[i] < a[i]:
                ans +=a[i]-b[i]


        return ans
                