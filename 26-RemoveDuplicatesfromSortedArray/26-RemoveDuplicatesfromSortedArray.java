// Last updated: 08/04/2026, 10:10:42
1class Solution {
2    public int removeDuplicates(int[] nums) {
3        int k =1 ;
4        int n = nums.length;
5        for ( int i = 1;i<n;i++){
6            if ( nums[i-1] != nums[i]){
7                nums[k] = nums[i];
8                k++;
9            }
10        }
11        return k;
12
13        
14    }
15}