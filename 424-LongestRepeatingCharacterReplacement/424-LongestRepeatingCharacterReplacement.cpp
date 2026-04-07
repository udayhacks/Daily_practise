// Last updated: 07/04/2026, 11:38:58
class Solution {
public:
    int characterReplacement(string s, int k) {
        int freq[26] = {0};
        int left = 0;
        int maxFreq = 0;
        int ans = 0;
        int n = s.size();

        for (int right = 0; right < n; right++) {
            // step 1 — add right char
            freq[s[right] - 'A']++;

            // step 2 — update maxFreq
            maxFreq = max(maxFreq, freq[s[right] - 'A']);

            // step 3 — invalid window → shrink by 1
            if ((right - left + 1) - maxFreq > k) {
                freq[s[left] - 'A']--;
                left++;
            }

            // step 4 — update ans
            ans = max(ans, right - left + 1);
        }
        return ans;
    }
};