# Last updated: 07/04/2026, 11:36:37
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        hs = defaultdict(int)
        for i in range(len(nums)) :
            if nums[i]%2 == 0 :
                nums[i] = 0
            else:
                nums[i] = 1
        s = 0 
        ans = 0

        hs[0] = 1
        for i in nums :
            s+=i
            r = s-k 
            ans+=hs[r]
            hs[s]+=1  

        return ans  






        