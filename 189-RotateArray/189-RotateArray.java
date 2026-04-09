// Last updated: 09/04/2026, 10:38:01
1class Solution {
2    public void reverse(int [] nums, int i , int j){
3        while(i <j){
4            int temp = nums[i];
5            nums[i++] = nums[j];
6            nums[j--] = temp;
7
8        }
9    }
10    public void rotate(int[] nums, int k) {
11            int n = nums.length;
12            k = k%n;
13            reverse(nums,0,n-1);
14            reverse(nums,0,k-1);
15            reverse(nums,k,n-1);
16    }
17}