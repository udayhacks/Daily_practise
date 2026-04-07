# Last updated: 07/04/2026, 11:38:35
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
       
        n = len(isConnected)
        vs = [0]*(n+1)

        from collections import deque




        adj = [[]for i in range(n)]



        for i in range(n) :
            for j in range(n):
                if isConnected[i][j] ==1  and i !=j :
                    adj[i].append(j)
                    adj[j].append(i)





        def path (adj,vs,k):

            q = deque()
            vs[k] = 1
            q.append(k)
            while q :
                ll = q.popleft()
                for i in adj[ll] :
                    if vs[i]== 0 :
                        q.append(i)
                        vs[i] =1  


        c = 0
    
        for i in range(n):
            if vs[i] == 0 :
                c+=1
                path (adj,vs,i)


        return c






                




            





        