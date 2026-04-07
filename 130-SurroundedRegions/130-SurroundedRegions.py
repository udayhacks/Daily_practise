# Last updated: 07/04/2026, 11:41:09
class Solution:
    
    
    def bfs (self,vs,r,c,board) :
        
        from collections import deque
        
        q = deque()
        q.append([r,c])
        row = len(board)
        col = len(board[0])
        
        vs[r][c] = 1 
        dr = [0,-1,0,1]
        dc = [-1,0,1,0]  
       
            
        while q :
            k = q.popleft()
            rr = k[0]
            cc = k [1]
          
            
            for i in range(4):
                ar = rr+dr[i]
                ac = cc+dc[i]
                if (ar >= 0 and ar < row) and (ac >= 0 and ac < col) and vs[ar][ac] ==0 and board[ar][ac] == "O":
                    q.append([ar,ac])
                    vs[ar][ac] = 1
                    
                    
                
                    
        
        
        
        

    def solve(self, board):
        
        row = len(board)
        col = len(board[0])
        
        vs= [[0 for i in range(col)] for j in range(row)]
        
        for i in range(col) :
            if board[0][i] == 'O' :
                self.bfs(vs,0,i,board) 
                
            if board[row-1][i] == 'O' : 
                self.bfs(vs,row-1,i,board) 
                
                
        for i in range(row) :
            if board[i][0] == 'O' :
                self.bfs(vs,i,0,board)  
            if board[i][col-1] == "O" :
                self.bfs(vs,i,col-1,board)
                
                
                
        for i in range(row) :
            for j in range(col) :
                if vs[i] [j]  ==  0  and board[i][j] == 'O' :
                    board[i][j] = "X"
                
        
                
                