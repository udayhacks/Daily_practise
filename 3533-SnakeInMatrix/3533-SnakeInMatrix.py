# Last updated: 07/04/2026, 11:33:59
class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        
        
        
        i = 0 
        j  = 0 
        k = 0
        u,r,d,l = "UP", "RIGHT", "DOWN", "LEFT"
        
        while k < len(commands)  :
            if commands[k]==u :
                i-=1
            if commands[k]==r :
                j+=1
                
            if commands[k]==d :
                i+=1
                
            if commands[k]==l:
                j-=1
                
            k+=1
                
        return (i * n) + j
                
                
                
            
        