// Last updated: 07/04/2026, 11:38:12

class Solution {
int mem(int fee,int i,int j ,vector<int>& prices,vector<vector<int>> &dp){
    if (i >= prices.size()) return 0 ;
    if (dp[i][j] != -1) return dp[i][j];
    if (j == 1){
        return dp[i][j] = max(
                 -prices[i] + mem(fee,i+1,0,prices,dp),// if we buy the stock overall 
                 mem(fee,i+1,1,prices,dp) // if we dont buys//
                             );
    }
    return dp[i][j] = max(prices[i]- fee+mem(fee,i+1,1,prices,dp),
             mem(fee,i+1,0,prices,dp));


}

public:
    int maxProfit(vector<int>& prices, int fee) {
        vector<vector<int>> dp(prices.size(),vector<int>(2,-1));
        return mem(fee,0,1,prices,dp); 
    }
};