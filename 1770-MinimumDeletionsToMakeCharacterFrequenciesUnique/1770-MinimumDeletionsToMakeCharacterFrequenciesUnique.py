# Last updated: 07/04/2026, 11:35:52
class Solution:
    def minDeletions(self, s: str) -> int:

        
        k = Counter(s)
        f= defaultdict(bool)
        d =0 
        for i in k.values():
            if f[i] :
                i-=1
                d+=1
                while i > 0 and f[i]:
                    i-=1 
                    d+=1
                f[i] = True 
            else :
                f[i] = True
        return d 