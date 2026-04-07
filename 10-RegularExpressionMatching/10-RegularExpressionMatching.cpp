// Last updated: 07/04/2026, 11:43:34
#include <bits/stdc++.h>
using namespace std;

class Solution {
private:
    bool dfs(int i, int j, string &s, string &p, vector<vector<int>> &dp) {
        if (dp[i][j] != -1) return dp[i][j];

        if (i >= s.size() && j >= p.size()) return dp[i][j] = true;
        if (j >= p.size()) return dp[i][j] = false;

        bool match = (i < s.size() && (s[i] == p[j] || p[j] == '.'));

        // Check if next char in pattern is '*'
        if (j+1 < p.size() && p[j+1] == '*') {
            // Either skip this `x*` OR use it if match
            dp[i][j] = (dfs(i, j+2, s, p, dp) || (match && dfs(i+1, j, s, p, dp)));
            return dp[i][j];
        }

        if (match) return dp[i][j] = dfs(i+1, j+1, s, p, dp);

        return dp[i][j] = false;
    }

public:
    bool isMatch(string s, string p) {
        int n = s.size(), m = p.size();
        vector<vector<int>> dp(n+1, vector<int>(m+1, -1));
        return dfs(0, 0, s, p, dp);
    }
};
