# Last updated: 07/04/2026, 11:41:55
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0 
        l = {}
        for i in nums:
            if i not in  l :

                nums[k] = i
                l[i] =1
                k +=1 
            elif l[i] <2 :
                nums[k] = i
                k+=1
                l[i]+=1
            

        return k


