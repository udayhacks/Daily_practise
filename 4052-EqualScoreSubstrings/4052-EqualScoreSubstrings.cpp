// Last updated: 07/04/2026, 11:33:33
class Solution {
public:
    bool scoreBalance(string s) {
       int n = s.size();
    int total = 0;

   
    for (char c : s) {
        total += (c - 'a' + 1);
    }

    int left_sum = 0;

    
    for (int i = 0; i < n - 1; i++) {
        left_sum += (s[i] - 'a' + 1);
        int right_sum = total - left_sum;

        if (left_sum == right_sum)
            return true;
    }

    return false;
    }
};