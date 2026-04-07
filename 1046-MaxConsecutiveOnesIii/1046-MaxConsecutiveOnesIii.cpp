// Last updated: 07/04/2026, 11:37:19
class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int ans = 0;
        int n = nums.size();
        int left = 0 ; 
        int skip =0;
        
        int right = 0;

        for (;right <n;right++){

            if ( nums[right] == 1){
                ans = max(ans,right-left);
            }
            else if ( nums [right] == 0 && skip <=k){
                ans = max(ans,right-left);
                skip++;
            }
            while(skip >k){
                if ( nums[left] == 0) skip--;
                left++;

            }

        }
        ans = max(ans,right-left);
        return ans;

    }
};