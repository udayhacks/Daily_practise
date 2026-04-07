// Last updated: 07/04/2026, 11:40:39
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0 ;
        int val = 0 ;
        for (int i :nums){
            if (count == 0){
                val = i ;
            }
            if (val == i ){
                count ++;

            }else{
                count --;

            }
        }
        return val ;
    }
};