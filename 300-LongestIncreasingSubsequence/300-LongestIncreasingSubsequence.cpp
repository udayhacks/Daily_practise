// Last updated: 07/04/2026, 11:39:34
class Solution {
public:
    int lengthOfLIS(vector<int>& arr) {
        int n = arr.size();
        vector<int> dp(n,1);


        for (int i = 0 ; i<n;i++){
            for(int j =0; j<i;j++){
                if( (arr[i]> arr[j]) && (dp[i] < 1+dp[j])){
                    dp[i] = 1+dp[j];
                }
            }
        }
        int maxi = dp[0];
        for(int i = 0 ;i <n;i++ ){
            maxi = max(maxi,dp[i]);
        }
        return maxi;
    }


};