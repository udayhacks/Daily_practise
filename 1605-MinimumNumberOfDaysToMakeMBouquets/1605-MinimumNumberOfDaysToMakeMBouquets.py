# Last updated: 07/04/2026, 11:36:09
class Solution:
    def check(self,arr,day,m,k) :
        res = 0 
        cnt = 0 
        for i in arr :
            if i <= day :
                cnt+=1
            else:
                res +=(cnt//k)
                cnt = 0 
        res+=(cnt//k)
        return res >= m 

    def minDays(self, bloomDay, m: int, k: int) -> int:
        
        
        if len(bloomDay) < m*k :
            return -1

        mx = mn = bloomDay[0]
        for i in bloomDay :
            mx = max(mx,i)
            mn = min(mn,i)
            
            
            
        while mn <= mx :
            mid = (mn+mx)//2
            if self.check(bloomDay,mid,m,k) :
                mx = mid-1
            else:
                mn = mid+1
                
        return mn
                
         