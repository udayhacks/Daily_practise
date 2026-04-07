# Last updated: 07/04/2026, 11:36:05
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low = 0 
        high = len(arr)-1

        while low <= high :
            mid = (low+high)//2
            #eq1
            mis= (arr[mid]-(mid+1))
            if mis < k :
                low = mid+1
            else:
                high = mid-1


        #revrese track  eq1
        return k +low
            


        