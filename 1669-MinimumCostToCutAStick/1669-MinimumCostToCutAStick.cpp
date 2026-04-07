// Last updated: 07/04/2026, 11:36:01
class Solution {


private:
int mem(int i ,int j ,  vector<int>& cuts,vector<vector<int>>& dp ){
    if (i>j) return 0 ;

    if (dp[i][j] != -1) return dp[i][j];
    int mini = INT_MAX;
    for (int k = i ;k <=j ;k++){
        int cost  = cuts[j+1]-cuts[i-1] +
        mem(i,k-1,cuts,dp)+
        mem(k+1,j,cuts,dp);
        mini  = min(mini,cost);

    }
    return dp[i][j] = mini;

    
}
public:
    int minCost(int n, vector<int>& cuts) {
        sort(cuts.begin(),cuts.end());
        int c = cuts.size();
        cuts.push_back(n);
        cuts.insert(cuts.begin(),0);

        vector<vector<int>> dp (c+2,vector<int>(c+2,0));

    for (int i = c; i >= 1; i--) {
        for (int j = 1; j <= c; j++) {
            if (i > j) continue;
                int mini = INT_MAX;
                for (int k = i ;k <=j ;k++){
                    int cost  = cuts[j+1]-cuts[i-1] +
                    dp[i][k-1]+
                dp[k+1][j];
                    mini  = min(mini,cost); 
                }
                dp[i][j] = mini;
            }
        }
        return dp[1][c];
 
    }
};