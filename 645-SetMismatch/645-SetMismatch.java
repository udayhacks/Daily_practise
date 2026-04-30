// Last updated: 30/04/2026, 16:51:16
1class Solution {
2    public int[] smallerNumbersThanCurrent(int[] nums) {
3        
4        int n = nums.length;
5        int [] temp = nums.clone();
6
7        Arrays.sort(temp);
8        
9        Map<Integer,Integer> map = new HashMap<>();
10
11        for ( int i = 0 ; i<n;i++){
12            if ( !map.containsKey(temp[i])){
13                map.put(temp[i],i);
14            }
15        }
16
17        int[] res = new int[n];
18
19        for ( int i = 0 ;i <n;i++){
20            res[i] = map.get(nums[i]);
21        }
22        return res;
23
24
25        
26    }
27}