// Last updated: 07/04/2026, 11:41:06
class Solution {
private:
    bool check(string &s, int i, int j) {
        while (i < j) {
            if (s[i] != s[j]) return false;
            i++;
            j--;
        }
        return true;
    }

    int minCutsFrom(int i, string &s, vector<int> &dp) {
        if (i == s.size()) return 0;

        if (dp[i] != -1) return dp[i];

        int mini = INT_MAX;
        for (int k = i; k < s.size(); k++) {
            if (check(s, i, k)) {
                int cost = 1 + minCutsFrom(k + 1, s, dp);
                mini = min(mini, cost);
            }
        }

        return dp[i] = mini;
    }

public:
    int minCut(string s) {
        int n = s.size();
        vector<int> dp(n + 1, -1);
        return minCutsFrom(0, s, dp) - 1; // subtract 1 because last cut isn't needed
    }
};
