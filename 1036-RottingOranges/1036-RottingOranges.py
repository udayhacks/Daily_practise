# Last updated: 07/04/2026, 11:37:16
class Solution:
    def orangesRotting(self, grid):
        
        m = len(grid)
        n = len(grid[0])
        rot= [[0 for i in range(n)] for j in range(m)]
        from collections import deque
        q = deque()
        mc = 0 
        frsh = frshR= 0
    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2 :
                    rot[i][j] =2
                    q.append([i,j,0])
                elif grid[i][j] ==1 :
                    frsh +=1

        if frsh ==0 :
            return 0
                               
        while q :
            k = q.popleft()
            r = k[0]
            c = k [1]
            t = k[2]
            mc = max(mc,t)
            dr = [0,-1,0,1]
            dc = [-1,0,1,0]
            
            for i in range(4):
                ar = r+dr[i]
                ac = c+dc[i]
                if (ar >= 0 and ar < m) and (ac >= 0 and ac < n)   and    (rot[ar][ac]!=2 and grid[ar][ac]==1 ):
                    q.append([ar,ac,t+1])
                    rot[ar][ac] = 2 
                    frshR+=1
                    
                    
                    
            
            
            
            
        if frshR != frsh :
                return -1
            
        return mc             
                    
                    
    
          
















        