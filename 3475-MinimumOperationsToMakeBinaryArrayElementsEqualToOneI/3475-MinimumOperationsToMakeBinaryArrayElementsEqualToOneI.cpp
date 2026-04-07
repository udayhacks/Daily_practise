// Last updated: 07/04/2026, 11:34:03
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int cnt =0 ; 
        int n = nums.size();
        for (int i = 0 ;i<n-2;i++){
           if (nums[i] ==0 ){
            cnt++;
            nums[i] ^= 1;
            nums[i+1] ^= 1;
            nums[i+2] ^= 1; 
           }
            
        }
        int sum = 0;
        for (int i = 0 ;i<n;i++){
            sum+=nums[i];
        }
        if (nums[n-1]==1 && nums[n-2]) return cnt ;
        return -1;
    }
};

