// Last updated: 07/04/2026, 11:42:57
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int k = 1 ;
        for (int i = 1 ; i<nums.size();i++){
            if (nums[i] !=nums[i-1]){
                nums[k] = nums[i];
                k++;
            }
        }
        return k ;
    }
};