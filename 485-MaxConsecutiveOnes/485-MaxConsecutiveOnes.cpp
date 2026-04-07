// Last updated: 07/04/2026, 11:38:50
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
       int count = 0 ;
       int ans = 0 ;
       for ( int i : nums){
        if ( i == 1){
            count ++;
        }
        ans = max(count,ans);
        if ( i == 0 ) count = 0;
       } return ans;
    }
};