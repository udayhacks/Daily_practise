// Last updated: 07/04/2026, 11:35:41
class Solution {
    public boolean check(int[] nums) {
        int flag  = 0;
        int n = nums.length;
        for ( int i = 0;i <n-1;i++){
            if ( nums[i] > nums[i+1]){
                flag ++;
            }
        }

        if ( nums[n-1] > nums[0]) flag ++;
        if ( flag >1) return false;
        return true;

    }
}