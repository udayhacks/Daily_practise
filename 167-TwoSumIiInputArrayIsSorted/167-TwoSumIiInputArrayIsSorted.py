# Last updated: 07/04/2026, 11:40:41
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    

        lft = 0 
        rght = len(numbers)-1


        while lft < rght :
            condition  = numbers[lft] + numbers[rght]

            if condition  == target :
                return [lft+1 ,rght+1 ]

            elif condition < target :
                lft+=1
            else :
                rght -=1
            

            

            
                