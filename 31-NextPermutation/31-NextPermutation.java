// Last updated: 13/04/2026, 13:42:37
1class Solution {
2    public void nextPermutation(int[] nums) {
3        int n = nums.length;
4
5        // Step 1: Find pivot
6        int i = n - 2;
7        while (i >= 0 && nums[i] >= nums[i + 1]) {
8            i--;
9        }
10
11        // Step 2: Find element just larger than nums[i]
12        if (i >= 0) {
13            int j = n - 1;
14            while (nums[j] <= nums[i]) {
15                j--;
16            }
17
18            // Swap
19            int temp = nums[i];
20            nums[i] = nums[j];
21            nums[j] = temp;
22        }
23
24        // Step 3: Reverse suffix
25        reverse(nums, i + 1, n - 1);
26    }
27
28    private void reverse(int[] nums, int start, int end) {
29        while (start < end) {
30            int temp = nums[start];
31            nums[start] = nums[end];
32            nums[end] = temp;
33
34            start++;
35            end--;
36        }
37    }
38}