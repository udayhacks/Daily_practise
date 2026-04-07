// Last updated: 07/04/2026, 11:36:28
class Solution {
private:
    int lcs_count(string text1, string text2) {
      
      int n = text1.size();
      int m = text2.size();
      vector<int> prev(m+1,0);
      vector<int>cur(m+1,0);
      
      for (int i = 1;i<=n;i++) {
        for (int j = 1 ; j<=m;j++){
            if (text1[i-1] == text2[j-1])cur[j] = 1+prev[j-1];
            else cur[j] = max(prev[j],cur[j-1]);

        }
        prev = cur;
      }
      return prev[m];

    }

    int longestPalindromeSubseq(string s) {
        string t = s;
        reverse(s.begin(),s.end());
        return lcs_count(t,s);
    }

public:
    int minInsertions(string s) {
        int n = s.size();
        return n -longestPalindromeSubseq(s);
    }
};