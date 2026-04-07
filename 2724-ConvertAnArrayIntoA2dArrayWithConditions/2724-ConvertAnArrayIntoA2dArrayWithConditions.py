# Last updated: 07/04/2026, 11:34:51
class Solution:
    def findMatrix(self, nums):
        d = {} 
        m = 1 
        for i in nums :
            if i in d :
                d[i] +=1
                m = max(d[i],m)
            else:
                d[i]  = 1
        ans = []

        for i in range(m) :
            ans.append([])
            
            

        for i in d :
            while d[i] > 0:
                
                ans[d[i]-1].append(i)
                d[i]-=1


        return ans
    
           









    

            
