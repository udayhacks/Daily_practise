// Last updated: 07/04/2026, 11:38:41
class Solution {

private:
int f(int i , int amount, vector<int>& coins,vector<vector<int>> & dp){
    //here always check if base case is for single element in array 
    if (i == 0 ){
        if ( !(amount%coins[i])) return 1;
        return amount == 0;
    }
    if (dp[i][amount] != -1) return dp[i][amount] ;
    int not_pick = f (i-1,amount,coins,dp );
    int pick = 0;
    if (amount >= coins[i]) pick = f(i,amount-coins[i] ,coins,dp);
    return dp[i][amount]  = (not_pick+pick);

}
public:
    int coinChange(vector<int>& coins, int amount) {
      int n = coins.size();
      //vector<vector<int >> dp(n,vector<int>(amount+1,-1));
      vector<vector<int>> dp(n, vector<int>(amount + 1, 0));


for (int j = 0; j <= amount; ++j) {
    if (j % coins[0] == 0) dp[0][j] = 1;
}
    
    for(int i = 1;i<n;i++){
        for(int j = 0;j<=amount;j++){
            long long int not_pick = dp[i-1][j];
            long long int pick = 0;
            if (j >= coins[i]) pick = dp[i][j-coins[i]];
             dp[i][j]  =(int) (not_pick+pick); 
        }
    }


    return dp[n-1][amount];






     // int ans =  f(n-1,amount , coins,dp);
      ///return ans ;  
    }
public:
    int change(int amount, vector<int>& coins) {
        return coinChange(coins,amount); 
    }
};