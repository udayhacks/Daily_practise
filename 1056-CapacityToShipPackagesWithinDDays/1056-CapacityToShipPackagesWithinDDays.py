# Last updated: 07/04/2026, 11:37:09



class Solution:
    
    def check(self,weights,ship,days) :
        load = 0 
        day = 1 
        
        for i in range(len(weights)):    
            
            if load + weights[i] > ship:
                day +=1 
                load = weights[i]
            
            else:
                load += weights[i]
                
        return day <= days 
    
            
    def shipWithinDays(self, weights, days: int) -> int:
        
        low = weights[0]
        high = weights[0]
        
        for i in weights:
            low = max(i,low)
            high+=i 
       
            
        while low <= high :
            mid = (low+high)//2
            if self.check(weights,mid,days):
                high = mid - 1
            else:
                low = mid + 1
                
        return low
            