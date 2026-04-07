# Last updated: 07/04/2026, 11:37:59
class Solution:
    
    
    
    def dfs(self,start,col,color,graph):
        
        color[start]= col
        for i in graph[start] :  
            if color[i] == -1 :
                if self.dfs(i,1-col,color,graph) == False:
                    return False
            elif color[i] == col:
                return False
            
        return True            
    
    
    def isBipartite(self, graph) -> bool: 
        
        n = len(graph)
        color = []
        
        for i in range(n) :
            color.append(-1)
            
        
        for i in range(n) :
            
            
            if color[i]  == -1 :
    
                if self.dfs(i,0,color,graph) == False :
                    return False
                
        return True
            
        
         
                    