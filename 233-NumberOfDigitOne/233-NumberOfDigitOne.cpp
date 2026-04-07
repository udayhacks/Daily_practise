// Last updated: 07/04/2026, 11:39:57
class Solution {
public:
    long long dp[20][2][20]; // [idx][tight][cnt]

    long long algo(string &s , int idx , int tight , int cnt){
        if (idx == s.size()) return cnt; 
        if (dp[idx][tight][cnt] != -1) return dp[idx][tight][cnt];

        int limit = (tight == 1 ? s[idx] - '0' : 9);
        long long total = 0; 
        for (int dig = 0; dig <= limit; dig++){
            int newTight = tight & (dig == (s[idx]-'0'));
            int ones = cnt + (dig == 1 ? 1 : 0);
            total += algo(s, idx+1, newTight, ones); 
        }
        return dp[idx][tight][cnt] = total;
    }

    int countDigitOne(int n) {
        string s = to_string(n);
        memset(dp,-1,sizeof(dp));
        return algo(s,0, 1, 0);
    }
};
