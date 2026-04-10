// Last updated: 10/04/2026, 08:37:10
1class Solution {
2    public int majorityElement(int[] nums) {
3        int ans = -1;
4        int count = 0 ;
5
6        for ( int i : nums){
7            if ( count == 0){
8                ans = i;
9                count = 1;
10            }else if ( i == ans){
11                count++;
12            }
13            else{
14                count --;
15            }
16        }
17        return ans;
18    }
19}