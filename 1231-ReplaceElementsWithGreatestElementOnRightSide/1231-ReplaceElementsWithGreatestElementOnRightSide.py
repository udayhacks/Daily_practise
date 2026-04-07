# Last updated: 07/04/2026, 11:36:50
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        
        m = - 1 
        lght = len(arr)-1 
        
        while lght >= 0 :
            
            store = arr[lght]
            arr[lght] = m
            m= max(m,store)
            lght -=1 
            
        return arr
     