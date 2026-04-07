// Last updated: 07/04/2026, 11:37:24
class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n = nums.size();
        int ans = 0; 
        for ( int i = 0 ;i<=n-3;i++){
            
            if (nums[i]+nums[i+1] > nums[i+2]) 
                {   int val = nums[i]+nums[i+1]+nums[i+2];
                    ans = max(ans,val);
                }
            
        }return ans;
    }
};