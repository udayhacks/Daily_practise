// Last updated: 08/04/2026, 12:08:06
1class Solution {
2
3    public int xorAfterQueries(int[] nums, int[][] queries) {
4
5        final int MOD = 1_000_000_007;
6
7        // Process each query
8        for (int[] q : queries) {
9
10            int left = q[0];
11            int right = q[1];
12            int step = q[2];
13            int value = q[3];
14
15            // Apply updates
16            for (int i = left; i <= right; i += step) {
17                nums[i] = (int)((long)nums[i] * value % MOD);
18            }
19        }
20
21        // Compute XOR
22        int result = 0;
23
24        for (int num : nums) {
25            result ^= num;
26        }
27
28        return result;
29    }
30}