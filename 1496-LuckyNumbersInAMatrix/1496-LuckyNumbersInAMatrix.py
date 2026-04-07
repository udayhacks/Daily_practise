# Last updated: 07/04/2026, 11:36:20
class Solution:
    def luckyNumbers (self, matrix):

        l = []
        h = []

        c = len(matrix[0])
        r = len(matrix)


        for i in range(r):
            res = 10**5
            for j in range(c):
                res = min(res,matrix[i][j])
            l.append(res)


        for j in range(c):
            res = 0 
            for i in range(r):           
                res = max(res,matrix[i][j])
            h.append(res) 

        res = []
        
        
        for i in range(len(h)):
            if h[i] in l : res.append(h[i])
        
        return res

 


        