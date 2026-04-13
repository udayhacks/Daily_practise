// Last updated: 13/04/2026, 12:23:09
1class Solution {
2    public int[] rearrangeArray(int[] nums) {
3
4        int n = nums.length;
5
6        int[] ans = new int[n];
7
8        int positiveIndex = 0;
9        int negativeIndex = 1;
10
11        for (int num : nums) {
12
13            if (num > 0) {
14
15                ans[positiveIndex] = num;
16                positiveIndex += 2;
17
18            } 
19            else {
20
21                ans[negativeIndex] = num;
22                negativeIndex += 2;
23
24            }
25        }
26
27        return ans;
28    }
29}