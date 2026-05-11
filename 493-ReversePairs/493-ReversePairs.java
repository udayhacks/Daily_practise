// Last updated: 11/05/2026, 20:37:23
1class Solution {
2
3    private void merge(int[] nums, int left, int mid, int right) {
4
5        int[] temp = new int[right - left + 1];
6
7        int i = left;
8        int j = mid + 1;
9        int k = 0;
10
11        while (i <= mid && j <= right) {
12            if (nums[i] <= nums[j]) {
13                temp[k++] = nums[i++];
14            } else {
15                temp[k++] = nums[j++];
16            }
17        }
18
19        while (i <= mid) temp[k++] = nums[i++];
20        while (j <= right) temp[k++] = nums[j++];
21
22        for (int p = 0; p < temp.length; p++) {
23            nums[left + p] = temp[p];
24        }
25    }
26
27    private int countPair(int[] nums, int left, int mid, int right) {
28
29        int count = 0;
30        int j = mid + 1;
31
32        for (int i = left; i <= mid; i++) {
33
34            while (j <= right && (long) nums[i] > 2L * nums[j]) {
35                j++;
36            }
37
38            count += (j - (mid + 1));
39        }
40
41        return count;
42    }
43
44    private int mergeSort(int[] nums, int left, int right) {
45
46        if (left >= right) return 0;
47
48        int mid = (left + right) / 2;
49
50        int count = 0;
51
52        count += mergeSort(nums, left, mid);
53        count += mergeSort(nums, mid + 1, right);
54
55        count += countPair(nums, left, mid, right);
56
57        merge(nums, left, mid, right);
58
59        return count;
60    }
61
62    public int reversePairs(int[] nums) {
63        return mergeSort(nums, 0, nums.length - 1);
64    }
65}