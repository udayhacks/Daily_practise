# Last updated: 07/04/2026, 11:33:50
class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n = len(values)

        vs = [1 for i in range(n)]
        
        i = 0
        ans = 0
        while (i >=0 and i <n ) and (vs[i] == 1):
            vs[i] =  0
            if ( instructions[i] == "add") :
                ans+=values[i]
                
                
                i+=1
            else:
                i = i+values[i]
                
        return ans
                
        