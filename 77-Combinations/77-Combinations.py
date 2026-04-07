# Last updated: 07/04/2026, 11:41:54
class Solution:
    def combine(self, n: int, k: int):
        ans = []

        def combo (i,curr):
            if len(curr)== k :
                ans.append(curr[:])
                return 


            for j in range(i,n+1):
                curr.append(j)
                combo(j+1,curr)
                curr.pop()

    
        combo(1,[])

        return ans
            