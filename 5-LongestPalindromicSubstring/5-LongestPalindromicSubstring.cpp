// Last updated: 07/04/2026, 11:43:46
class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) return "";

        // Transform string with # to handle even/odd
        string t = "#";
        for (char c : s) {
            t += c;
            t += '#';
        }

        int n = t.size();
        int Rightmost = 0, valid_center = 0;
        vector<int> radius(n, 0);

        for (int i = 0; i < n; i++) {
            int mirror = 2 * valid_center - i;

            if (i < Rightmost)
                radius[i] = min(radius[mirror], Rightmost - i);
            else
                radius[i] = 0;

            // Expand around i
            while (i + radius[i] + 1 < n && i - radius[i] - 1 >= 0 &&
                   t[i + radius[i] + 1] == t[i - radius[i] - 1]) {
                radius[i]++;
            }

            // Update center and right boundary
            if (i + radius[i] > Rightmost) {
                valid_center = i;
                Rightmost = i + radius[i];
            }
        }

        // Find max radius
        int rad = 0, cen = 0;
        for (int i = 0; i < n; i++) {
            if (radius[i] > rad) {
                rad = radius[i];
                cen = i;
            }
        }

        int start = (cen - rad) / 2;
        return s.substr(start, rad);
    }
};
