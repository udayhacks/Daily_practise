// Last updated: 15/04/2026, 12:20:06
1class Solution {
2    public int subarraySum(int[] nums, int k) {
3        HashMap<Integer , Integer> resdue = new HashMap<>();
4        resdue.put( 0 , 1);
5        int ans = 0 ;
6        int cur = 0 ;
7
8        for ( int i : nums){
9            cur+=i;
10
11            int res = cur-k;
12            ans +=(resdue.getOrDefault(res, 0));
13            resdue.put(cur,resdue.getOrDefault(cur,0)+1);
14
15        }
16        return ans;
17    }
18}