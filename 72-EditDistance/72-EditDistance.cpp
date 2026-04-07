// Last updated: 07/04/2026, 11:42:02
class Solution {

private:
int mem(int i , int j , string &s ,string &t,vector<vector<int>>&dp){
    if (j == 0 ) return i;
    if (i == 0 ) return j;
    if (dp[i][j] != -1) return dp[i][j];
    if (s[i-1] == t[j-1]) return dp[i][j] =mem(i-1,j-1,s,t,dp);
    return dp[i][j] = 1+min( mem(i-1,j-1,s,t,dp), //replace
                        min(mem(i-1,j,s,t,dp),// delete
                                mem(i,j-1,s,t,dp)));//insert
}
public:
    int minDistance(string word1, string word2) {
        int n = word1.size();
        int m = word2.size();
        vector<vector<int>>dp(n+1,vector<int>(m+1,-1));
        return mem(n,m,word1,word2,dp);
    }
};