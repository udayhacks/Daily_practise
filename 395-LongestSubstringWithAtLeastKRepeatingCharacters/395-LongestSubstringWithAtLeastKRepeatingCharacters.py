# Last updated: 07/04/2026, 11:39:06
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n < k or n == 0 : return 0 
        if k <=1 :return n
        count = Counter(s)
        l = 0 
        while l<n and count[s[l]] >= k :l+=1
        if l>= n-1 : return l
        ls1 = self.longestSubstring(s[0:l],k)
        while l<n and count[s[l]] <k : l+=1
        ls2 =  self.longestSubstring(s[l:], k) if (l<n) else 0
        return max(ls1,ls2)





        