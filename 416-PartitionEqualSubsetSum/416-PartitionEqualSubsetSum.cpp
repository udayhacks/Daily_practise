// Last updated: 07/04/2026, 11:39:00
class Solution {

private:
 bool isSubsetSum(vector<int>& arr, int sum) {        
        int n = arr.size();
        vector<bool>dp(sum+1,false);
        for (int i = 0 ;i <n ;i++) dp[0]  = true;
        // if arr[0] is valid index 
        if (arr[0] <= sum) dp[arr[0]] = true;
        
        for(int i = 1 ;i<n ;i++){
             vector<bool>tmp(sum+1,false);
             tmp[0] = true;
            for (int target = 1 ; target<=sum;target++){
                bool notPick = dp[target];
                 bool pick = false;
                 if (target>= arr[i]) pick = dp[target-arr[i]];
                 tmp[target] = notPick||pick;
            }
            dp = tmp;
        }
    
        return dp[sum];

 }
public:
    bool canPartition(vector<int>& nums) {
        int val = 0;
        for(int i = 0 ;i <nums.size();i++){
            val+=nums[i];
        }
        if (val&1) return false;

        return isSubsetSum(nums,val/2);

    }
};