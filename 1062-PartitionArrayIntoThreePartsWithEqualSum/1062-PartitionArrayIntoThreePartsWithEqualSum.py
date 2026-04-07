# Last updated: 07/04/2026, 11:37:08
class Solution:
    def canThreePartsEqualSum(self, arr):
        kk = sum(arr)
        k = kk//3
        c= 0
        s = 0
        for i in range(len(arr)):
            s+=arr[i]
            if s == k :
                c+=1
                s = 0 
                
        if c >= 3 and kk%3 == 0  :
            return True
        return False
            
            
            
        