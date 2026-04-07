# Last updated: 07/04/2026, 11:34:59
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        mini=-1
        maxi=-1
        badi=-1
        ans=0
        for i in range(len(nums)):
            if nums[i]<minK or nums[i]>maxK:
                badi=i
            if nums[i]==minK:
                mini=i
            if nums[i]==maxK:
                maxi=i
            ans+=max(0,min(mini,maxi)-badi)
        return ans