# Last updated: 07/04/2026, 11:41:22
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        n = numRows
        ans = []

        for i in range(1,n+1):
            row =[1]
            k = 1
            for j in range(1,i):
                k = k*(i-j)
                k = k//j
                row.append(k)
            ans.append(row)
        return ans

