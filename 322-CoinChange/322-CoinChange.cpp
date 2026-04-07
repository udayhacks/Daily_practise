// Last updated: 07/04/2026, 11:39:29
class Solution {

private :
int f(int i , int amount, vector<int>& coins,vector<vector<int>> & dp){
    //here always check if base case is for single element in array 
    if (i == 0 ){
        if ( !(amount%coins[i])) return amount/ coins[i];
        return 1e9;
    }
    if (dp[i][amount] != -1) return dp[i][amount] ;
    int not_pick = f (i-1,amount,coins,dp );
    int pick = 1e9;
    if (amount >= coins[i]) pick = 1+f(i,amount-coins[i] ,coins,dp);
    return dp[i][amount]  = min(not_pick,pick);

}
public:
    int coinChange(vector<int>& coins, int amount) {
      int n = coins.size();
      vector<vector<int >> dp(n,vector<int>(amount+1,-1));
    
      int ans =  f(n-1,amount , coins,dp);
      if (ans >= 1e9) return -1;
      return ans ;  
    }
};