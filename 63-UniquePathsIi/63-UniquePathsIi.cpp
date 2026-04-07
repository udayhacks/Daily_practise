// Last updated: 07/04/2026, 11:42:08
class Solution {

public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
           //2vector<vector<int>> dp(m, vector<int>(n,0));
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<int> prev(n);
        //1return solve(m-1,n-1,dp);

        for (int i = 0 ;i<m ;i++){
            
            vector<int>tmp(n,0);//3
            for (int j = 0 ;j <n ; j++){
                if (i == 0 && j == 0 && obstacleGrid[i][j] != 1) {
                    tmp[j]  = 1;//3
                    //2dp[0][0]  = 1;
                    continue;
                }
                if (i >=0 && j>=0 && obstacleGrid[i][j] == 1){
                    tmp[j] = 0;
                    continue;
                }
                int left =0; 
                int up = 0 ; 
                //2 if (i-1 >=0) left = dp[i-1][j];
                if (i-1 >=0) left = prev[j];//3
                //2if (j-1 >=0) up = dp[i][j-1];   
                if (j-1 >=0) up = tmp[j-1];//3
                //2dp[i][j]  = left+up;
                tmp[j]  = left+up;//3
            }
            prev = tmp;//3
        }
        //2return dp[m-1][n-1];
        return prev[n-1]; //3 
    }
};