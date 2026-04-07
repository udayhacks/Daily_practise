// Last updated: 07/04/2026, 11:39:30
class Solution {


private:
int mem(int i ,int j,vector<int>& nums,vector<vector<int>> &dp){
    if (i>j) return 0 ;
    if (dp[i][j] != -1 ) return dp[i][j];
    int mini =0;
    for (int k = i ;k<=j ;k++){
        int cost = nums[i-1]*nums[k]*nums[j+1] +
                    mem(i,k-1,nums,dp)+
                    mem(k+1,j,nums, dp);
            mini = max(mini,cost);    
    }
    return dp[i][j] = mini;
}
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        nums.insert(nums.begin(),1);
        nums.push_back(1);
        vector<vector<int>>dp(n+2,vector<int>(n+2,0));
        //return mem(1,n,nums,dp);
        for (int i = n;i>0;i--){
            for (int j = 1;j<=n;j++){
                if (i >j) continue;
                int mini = 0 ;
                for (int k = i ;k <=j ;k++){
                    int cost = nums[i-1]*nums[k]*nums[j+1] +
                    dp[i][k-1] +
                    dp[k+1][j];
                    mini = max (mini,cost);
                }
                dp[i][j] = mini;
            }
           
        }return dp[1][n];


    }
};