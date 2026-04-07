# Last updated: 07/04/2026, 11:36:31
class Solution:
    
    def check (self, nums,thresold,mid):
        
        
        res = 0 
        
        from math import ceil
        for i in nums :
            res+=ceil(i/mid)
            
        return res <= thresold
    
            
            
        
    
    
    def smallestDivisor(self, nums, threshold: int) -> int:
        
        
    
        mx = nums[0]
        for i in nums :
            mx = max(mx,i)
           
        mn = 1  
        while mn <= mx :
            mid = (mn+mx)//2
            if self.check(nums,threshold,mid) :
                mx = mid-1
            else:
                mn = mid+1
                
        return mn
                
                