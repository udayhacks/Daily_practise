// Last updated: 07/04/2026, 11:41:18

class Solution {

private:
int mem(int i,int j , int cap ,vector<int>& prices,vector<vector<vector<int>>> &dp){
    if (cap == 0 ) return 0 ;
    if (i == prices.size()) return 0 ;

    if (dp[i][j][cap] != -1) return dp[i][j][cap];
    if (j == 1){
        return dp[i][j][cap] = max(
                 -prices[i] + mem(i+1,0,cap,prices,dp),// if we buy the stock overall 
                 mem(i+1,1,cap,prices,dp) // if we dont buys//
                             );
    }
    return dp[i][j][cap] = max(prices[i]+mem(i+1,1,cap-1,prices,dp),
             mem(i+1,0,cap,prices,dp));


}

public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
     vector<vector<vector<int>>> dp(n, vector<vector<int>>(2, vector<int>(3, -1)));

        return mem(0,1,2,prices,dp);
    }
};