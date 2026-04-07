# Last updated: 07/04/2026, 11:37:00
class Solution:
    def heightChecker(self, heights) -> int:
        k = heights.copy()
        count = 0 
        swap = True 
        while swap :
            swap = False
            for i in range(len(heights)-1):
                if heights[i] > heights[i+1] :
                    heights[i] ,heights[i+1] =heights[i+1] ,heights[i]  
                    swap = True
                    
                    
        for i in range(len(heights)) :
            if k [i] != heights[i] :
                count +=1
        
                    
        return count 
        