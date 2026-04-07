# Last updated: 07/04/2026, 11:35:02
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #declartion 
        white = 0 
        recolor = float('inf') 
        n = len(blocks)
        l = 0 
        for r in range(n):
            if blocks[r] == 'W':
                    white+=1

            if r-l+1 >k :
                    if blocks[l] == 'W':
                        white-=1
                    l+=1
            
            if r-l+1 == k :
                    recolor = min(recolor,white)
                
                
        return recolor