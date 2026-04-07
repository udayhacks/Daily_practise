// Last updated: 07/04/2026, 11:40:03
class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n >0 && (n&(n-1))==0) return true;
        return false;
    }
};