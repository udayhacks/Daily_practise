// Last updated: 07/04/2026, 11:39:45
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int count = 0;
        int n = nums.size();
        
        int actual = n;
        for ( int i = 0;i<n;i++){
            count+=nums[i];
            actual +=i;

        }
        return actual -count;
    }
};