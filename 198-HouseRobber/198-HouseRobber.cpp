// Last updated: 07/04/2026, 11:40:28
class Solution {
    vector<int>dp;
    int F(int n ,vector<int>&nums){
        if ( n <0) return 0;
        if ( n ==0) return nums[0];
        if ( dp[n] != -1) return dp[n];
        int p = nums[n] +F(n-2,nums);
        int np = F(n-1,nums);
        return dp[n] =  max(np,p);
    }

public:

    int rob(vector<int>& nums) {
        
        int n = nums.size();
        dp.assign(n+1,-1);

        dp[0] = nums[0];
        if ( n>1) dp[1] = max(nums[1],nums[0]);
        for ( int i= 2 ; i<n;i++){
            int cost = nums[i] + dp[i-2];

            dp[i] = max(cost , dp[i-1]);

        }return dp[n-1];
    


        return F(n-1,nums);
    
    }
};