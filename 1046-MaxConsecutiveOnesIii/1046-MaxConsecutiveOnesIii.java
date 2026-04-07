// Last updated: 07/04/2026, 11:37:14
class Solution {
    public int longestOnes(int[] nums, int k) {
        int n = nums.length;
        int ans =0 ;
        int skip = 0;
        int right = 0 ;
        int left = 0;
        for ( ; right<n;right++){
            if ( (nums[right] == 1) || (nums[right] == 0 && skip<=k)){
                ans = Math.max(ans,right-left);
                if ( nums[right] ==0) skip++;
            }
            while( skip>k){
                if ( nums[left] == 0) skip--;
                left++;
            }
        }
        ans = Math.max(ans,right-left);
        return ans;

    }
}