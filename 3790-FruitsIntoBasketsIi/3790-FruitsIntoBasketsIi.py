# Last updated: 07/04/2026, 11:33:42
class Solution:
    def numOfUnplacedFruits(self, fruits, baskets) -> int:
        n = len(fruits)
        flag = True
        count =0 
        for i in fruits:
            for j in range(n):
                if i <= baskets[j] :
                    baskets[j] = 0
                    flag = False
                    break
        for i in baskets:
            if i !=0 :
                count+=1
                
      
            
        return count
    