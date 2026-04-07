// Last updated: 07/04/2026, 11:33:35
class Solution {
public:
    int longestSubarray(vector<int>& nums) {
      int n = nums.size();
        if (n == 1 || n == 2) return n;
        int l = 0;
        int mx = 0;
        for (int i = 1;i<n;i++){
            
            if ( i-l+1 >2 && nums[i] != (nums[i-1]+nums[i-2])) {
                l = i-1;
                
            }
             mx = max(mx,i-l+1);
        }

       return mx;
    }
};