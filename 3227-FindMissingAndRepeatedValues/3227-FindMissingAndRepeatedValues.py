# Last updated: 07/04/2026, 11:34:19
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        l =[]
        
        for i in range(len(grid)):
            for j in range(n) :
                l.append(grid[i][j]) 
                
        l.sort()
        ans = []
        d = {}
        for i in  l :
            if i in d :
                ans.append(i)
                break 
            else :
                d[i] =1 
                
        for i in range(1, (n*n)+1): 
            if i not in l :
                ans.append(i)
                break 
                
        return ans 
                
        
        
        
        