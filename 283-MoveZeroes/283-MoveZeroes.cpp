// Last updated: 07/04/2026, 11:39:40
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int zeroes = 0 ;
        int n = nums.size();
        for ( int i = 0;i<n;i++){
            if ( nums[zeroes] == 0 && nums[i] !=0){
                swap(nums[i],nums[zeroes]);
            }
            if ( nums[zeroes] !=0) zeroes++;
        }
        
    }
};