// Last updated: 07/04/2026, 11:37:36
class Solution {


private :
int solve(int i , int j ,int m,vector<vector<int>>& matrix,vector<vector<int>>& dp){


    if (j <0 || j >=m ) {
        return 1e9;
    }

    if (dp[i][j] !=-1) return dp[i][j];
    if (i == 0){
        return matrix[i][j];
    }
    int dia = matrix[i][j] +solve(i-1,j+1,m,matrix,dp);
    int dia2 = matrix[i][j] +solve(i-1,j-1,m,matrix,dp);
    int str = matrix[i][j] +solve(i-1,j,m,matrix,dp);
    dp[i][j]  = min(min(dia,dia2),str);
    return dp[i][j];


}
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {

        int n = matrix.size();
        //vector<int>>dp(n,vector<int>(n,-1));
        vector<int>dp(n,-1);
        for (int j = 0 ; j<n; j++){
            dp[j] = matrix[0][j];
        }
        
        for(int i = 1;i<n;i++){
            vector<int>tmp(n,0);
            for(int j=0;j<n;j++){
                int dia = 1e9;
                int dia2 =1e9;
                int str = matrix[i][j] +dp[j];


                if (j+1<n) {
                    dia = matrix[i][j] +dp[j+1];
                }
                if (j-1>=0){
                   dia2 = matrix[i][j] +dp[j-1];
                }

                tmp[j]  = min(min(dia,dia2),str);
            }
            dp = tmp;
            
        }
        int val = 1e9;
        for(int i = 0 ;i<n;i++){
            val = min(dp[i],val);
        }
        return val;
    }
};