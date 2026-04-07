// Last updated: 07/04/2026, 11:42:32
class Solution {
private:
    bool isAllStars(string &p, int j) {
        for (int i = 0; i <= j; i++) {
            if (p[i] != '*')
                return false;
        }
        return true;
    }

    bool mem(int i, int j, string &s, string &p, vector<vector<int>> &dp) {
        // base cases
        if (i < 0 && j < 0)
            return true;
        if (i < 0 && j >= 0)
            return isAllStars(p, j);
        if (j < 0 && i >= 0)
            return false;

        if (dp[i][j] != -1)
            return dp[i][j];

        if (s[i] == p[j] || p[j] == '?')
            return dp[i][j] = mem(i - 1, j - 1, s, p, dp);

        if (p[j] == '*') {
            return dp[i][j] = mem(i - 1, j, s, p, dp) || mem(i, j - 1, s, p, dp);
        }

        return dp[i][j] = false;
    }

public:
    bool isMatch(string s, string p) {
        int n = s.size();
        int m = p.size();
        vector<vector<int>> dp(n, vector<int>(m, -1));
        return mem(n - 1, m - 1, s, p, dp);
    }
};
