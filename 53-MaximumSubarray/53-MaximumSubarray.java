// Last updated: 13/04/2026, 11:20:20
1class Solution {
2    public int maxSubArray(int[] nums) {
3        int n = nums.length;
4        int left = 0;
5        int right =0;
6        int result = Integer.MIN_VALUE;
7        
8        int sum = 0 ; 
9        
10        while( right < n){
11            if ( sum <0){
12                sum = 0;
13            }
14            sum+=nums[right++];
15            result = Math.max(result,sum);
16        }
17        return result;
18    }
19
20}