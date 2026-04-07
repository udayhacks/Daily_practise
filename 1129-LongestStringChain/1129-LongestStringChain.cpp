// Last updated: 07/04/2026, 11:37:01
class Solution {
    // Check if s is a valid predecessor of t (by adding one letter)
    bool fun(string &s, string &t) {
         // True if all characters in s are matched
        int ss = s.size();
        int tt = t.size();

        if (ss +1 != tt) return false;
        int i = 0 , j = 0 ;
        while(j<tt){
            if (j<tt && s[i] == t[j]) {
                i++;
            }
            j++;
        } 
        return i == ss;
    }

public:
    int longestStrChain(vector<string>& arr) {
        int n = arr.size();
        // Sort strings by length (small to large)
        sort(arr.begin(), arr.end(), [](const string &a, const string &b) {
            return a.size() < b.size();
        });

        vector<int> dp(n, 1);
        int maxi = 1;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (fun(arr[j], arr[i]) && dp[i] < dp[j] + 1) {
                    dp[i] = dp[j] + 1;
                }
            }
            
        }
        for (int i = 0 ;i<n;i++) maxi = maxi = max(maxi, dp[i]);
        return maxi;
    }
};
