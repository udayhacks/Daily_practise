// Last updated: 07/04/2026, 11:43:38
class Solution {
public:
    int myAtoi(string s) {
        int i = 0, n = s.size();
        int sign = 1;
        long ans = 0;  // use long to detect overflow

        // skip spaces
        while (i < n && s[i] == ' ') i++;

        // sign
        if (i < n && (s[i] == '+' || s[i] == '-')) {
            sign = (s[i] == '-') ? -1 : 1;
            i++;
        }

        // digits
        while (i < n && isdigit(s[i])) {
            ans = ans * 10 + (s[i] - '0');

            // overflow check
            if (sign * ans > INT_MAX) return INT_MAX;
            if (sign * ans < INT_MIN) return INT_MIN;

            i++;
        }

        return (int)(sign * ans);
    }
};