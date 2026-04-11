// Last updated: 11/04/2026, 17:10:37
1import java.util.*;
2
3class Solution {
4    public int minimumDistance(int[] nums) {
5
6        HashMap<Integer, ArrayList<Integer>> mp = new HashMap<>();
7
8        int n = nums.length;
9
10        // Build map
11        for (int i = 0; i < n; i++) {
12
13            if (mp.containsKey(nums[i])) {
14                mp.get(nums[i]).add(i);
15
16            } else {
17                ArrayList<Integer> list = new ArrayList<>();
18                list.add(i);
19                mp.put(nums[i], list);
20            }
21        }
22
23        int maxVal = Integer.MAX_VALUE;
24
25        // Iterate map
26        for (Map.Entry<Integer, ArrayList<Integer>> map : mp.entrySet()) {
27
28            ArrayList<Integer> list = map.getValue();
29
30            if (list.size() >= 3) {
31
32                int m = list.size();
33
34                for (int i = 0; i < m - 2; i++) {
35
36                    int v1 = list.get(i);
37                    int v3 = list.get(i + 2);
38
39                    // Correct formula
40                    int val = 2 * (v3 - v1);
41
42                    maxVal = Math.min(val, maxVal);
43                }
44            }
45        }
46
47        return (maxVal == Integer.MAX_VALUE) ? -1 : maxVal;
48    }
49}