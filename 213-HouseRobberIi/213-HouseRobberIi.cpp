// Last updated: 07/04/2026, 11:40:15
class Solution {
public:
        int rob1(vector<int>& nums) {
        int n = nums.size();
    
         int dp0 = nums[0];
         int dp1 = nums[0];
        if (n>1){
            dp1 = max(nums[0],nums[1]);
        }
        
        for(int i = 2 ; i<n ;i++){
            int tmp = dp1;
            dp1 = max(dp1 , dp0+nums[i]);
            dp0 = tmp;
        }
         return dp1;
    }
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n ==1) return nums[0];
        vector <int> arr1;
        vector<int>arr2;
        for(int i = 0 ;i<n;i++){
            if (i!= 0){
                arr1.push_back(nums[i]);
            }
        }
        for(int i = 0 ;i<n;i++){
            if (i!= n-1){
                arr2.push_back(nums[i]);
            }
        }

        return max(rob1(arr1),rob1(arr2));
        
        
    }
};