# Last updated: 07/04/2026, 11:34:17
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        v = len(variables)
        for i in range(v):
            j = 0 
            a = variables[i][0]
            b = variables[i][1]
            c = variables[i][2]
            m= variables[i][3]
            
            if ((((a**b)%10)**c)%m) == target :
                ans.append(i)
                
                
        return ans
            
            
        
        