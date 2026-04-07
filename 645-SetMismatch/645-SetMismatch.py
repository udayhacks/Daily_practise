# Last updated: 07/04/2026, 11:38:21
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hash = {}
        res= []
        for i in nums :
            if i in hash :
                hash[i] = 1
                if hash[i] == 1 :
                    res.append(i)
            else:
                hash[i] = 0 


        n = len(nums)
        j = ((n*(n+1))//2 ) - sum(set(nums))
        res.append(j)
        return res


            

            

            
            


        