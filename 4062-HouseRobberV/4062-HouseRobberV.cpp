// Last updated: 07/04/2026, 11:33:30
class Solution {

private:
    vector<long long>dp;
    long long F(int n,vector<int>& nums, vector<int>& colors){
        
        if (n ==0) return nums[0];
        if ( n<0) return 0;
        if ( dp[n] != -1) return dp[n];

        long long p = 0 ;
        long long np = 0;
        long long l = 1;

        if ( n-1>=0 && colors[n] !=colors[n-1]){
            p = (nums[n]*l)+F(n-1,nums,colors);
        }else{
            p = (nums[n]*l)+F(n-2,nums,colors);
        }
        np = F(n-1,nums,colors);

        dp[n] = max(np,p);
        return dp[n];









        
    }
public:
    long long rob(vector<int>& nums, vector<int>& colors) {

        int n = nums.size();
            dp.assign(n,-1);
            return F(n-1,nums,colors);
        
    }
};