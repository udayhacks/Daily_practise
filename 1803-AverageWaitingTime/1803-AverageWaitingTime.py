# Last updated: 07/04/2026, 11:35:48
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        prev = 0 
        wait= 0 
        for i in customers :
            j ,k = i 
            temp = 0 

            if prev > j :
                temp = (prev- j)
                wait+=temp

            wait+=(k)
            prev = (temp+(j+k))
            

        return round(wait/len(customers),5)
        