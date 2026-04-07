# Last updated: 07/04/2026, 11:41:58
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if len(matrix) ==1 and len(matrix[0]) ==1 :
            if matrix[0][-1] == target :
                return True 
            return False
        k = -1

        for i in range(len(matrix)):
            if target == matrix[i][-1] :
                return True
            if target < matrix[i][-1] :
                k = i 
                break 
            

        if k == -1 :
            return False

        i = 0
        j = len(matrix[k])-1

        while i <= j :
            m = (( i+j )//2 ) 
            if matrix[k][m] == target :
                return True 
            if matrix[k][m] < target :
                i = m+1
            else :
                j = m-1



        return False



            
            
        