# Last updated: 07/04/2026, 11:36:53
#File create
class Solution:
   
    def shortestPathBinaryMatrix(self, grid):
        from collections import deque
        n = len(grid)
        if grid[0][0] ==1  and  n>1:
            return -1
        if grid[0][0] == 0 and n==1 :
            return 1
        

        distance = []
        for i in range(n):
            distance.append([])
            for j in range(n):
                distance[i].append(1e9)

        src = [0,0]
        dsn = [n-1,n-1]
        que = deque()
        que.append([1,0,0])
        # here the distance started with 1 from source to source 
        
        dr = [0,0,-1,1,-1,-1,1,1]
        dc = [-1,1,0,0,-1,1,-1,1]

        while que:
            top = que.popleft()
            d = top[0]
            tr = top[1]
            tc = top[2]
            for i in range(8):
                r = tr+dr[i]
                c = tc+dc[i]

                if ((r >= 0 and r < n ) and (c >= 0 and c < n ) and grid[r][c] == 0 and 
                 d+1 < distance[r][c]):
                    if [r,c] == dsn:
                        return d+1
                    distance[r][c] = d+1
                    que.append([d+1,r,c])

        return -1



