# Last updated: 07/04/2026, 11:36:42
class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        ans = -1
        n = len(nums)
        if ( k ==0 and n !=0 ) : return nums[0]
        if ( n ==1) : return nums[0] if k%2 ==0 else ans
        if (k ==1 ): return nums[1]
        if ( k  < n ) : ans = max ( ans, nums[k])
        
        
        ans = max(ans,max(nums[:k-1]))


        return ans
        
        
        