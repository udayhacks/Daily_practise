// Last updated: 30/04/2026, 16:23:46
1class Solution {
2    public int[] findErrorNums(int[] nums) {
3
4        int n = nums.length;
5        int[] a = new int[n + 1];
6
7        // initialize with -1
8        for (int i = 0; i <= n; i++) {
9            a[i] = -1;
10        }
11
12        int r = -1;
13
14        for (int i = 0; i < n; i++) {
15            if (a[nums[i]] != -1) r = nums[i];
16            if (a[nums[i]] == -1) a[nums[i]] = i;
17        }
18
19        int m = -1;
20
21        for (int i = 1; i <= n; i++) {
22            if (a[i] == -1) {
23                m = i;
24                break;
25            }
26        }
27
28        return new int[]{r, m};
29    }
30}