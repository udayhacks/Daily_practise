// Last updated: 07/04/2026, 11:34:52
class Solution {
public:
    int maximumCount(vector<int>& nums) {
        
        int pos =0 ;
        int neg = 0 ;
        for (int i = 0 ;i <nums.size();++i){
            if (nums[i] >0) pos++;
            if (nums[i]<0) neg++; 
        }

        return max(pos,neg);


    }
};