# Last updated: 07/04/2026, 11:38:33
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c= 0 
        curr = 0 
        hashmap = {}



        for i in range(len(nums)) :
            curr += nums[i]

            if curr == k :
                c+=1

            if curr-k in hashmap:
                c+=hashmap[curr-k]

            if curr in hashmap:
                hashmap[curr] +=1
            else:
                hashmap[curr] =1 



        return c