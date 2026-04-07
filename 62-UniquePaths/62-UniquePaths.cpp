// Last updated: 07/04/2026, 11:42:10
class Solution {


private:

vector<vector<int>>dp;

int F(int r,int c){
    if( r ==0 && c ==0){
        return 1;
    }

    if ( dp[r][c] != -1) return dp[r][c];


    dp[r][c] = 0;

    if ( r-1 >=0) dp[r][c] = dp[r][c] + F(r-1,c);
    
    if ( c-1>=0) dp[r][c] = dp[r][c] + F(r,c-1);

    return dp[r][c];



}




public:
    int uniquePaths(int m, int n) {
        
        dp.assign(m,vector<int>(n,-1));

        return F(m-1,n-1);
    }
};