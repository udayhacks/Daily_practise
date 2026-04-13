// Last updated: 13/04/2026, 10:51:27
1class Solution {
2    public void sortColors(int[] nums) {
3       int n = nums.length;
4       int cur = 0;
5       int left = 0;
6       int right = n-1;
7
8       while( cur <= right){
9        if ( nums[cur] == 0 ){
10            nums[cur] = nums[left];
11            nums[left] = 0;
12            left++;
13            cur++;
14        }
15        else if (nums[cur] == 2 ){
16
17            nums[cur] = nums[right];
18            nums[right] = 2;
19            right--;
20        }
21        else {
22            cur++;
23        }
24
25       }
26
27
28    }
29}