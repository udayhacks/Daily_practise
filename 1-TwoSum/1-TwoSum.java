// Last updated: 09/04/2026, 12:52:53
1class Solution {
2    public int[] twoSum(int[] nums, int target) {
3        HashMap <Integer,Integer> mp = new HashMap<>();
4        for ( int i  =0;i<nums.length;i++){
5            int j = target-nums[i];
6            if ( mp.containsKey(j)){
7                return new int[] { mp.get(j),i};
8            }
9            mp.put(nums[i], i);
10            }
11            return new int[] {-1,-1};
12    }
13}