# Last updated: 07/04/2026, 11:42:19
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        row = len(matrix)
        col = len(matrix[0])
        ans = []
        left = top = 0 
        right = col-1
        bottom = row-1

        while left <= right and top <= bottom :
            

            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top +=1

            for   i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right -=1   

            if top <= bottom : 
                for i in range(right ,left-1 ,-1) :
                    ans.append(matrix[bottom][i])
                bottom-=1 

            if left <= right :
                for i in range(bottom ,top-1,-1) :
                    ans.append(matrix[i][left])
                left +=1

        return ans 


        





            