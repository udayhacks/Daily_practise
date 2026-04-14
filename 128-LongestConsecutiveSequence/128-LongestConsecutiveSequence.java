// Last updated: 14/04/2026, 10:13:06
1class Solution {
2    public int longestConsecutive(int[] nums) {
3        
4        HashSet <Integer> set = new HashSet<>();
5
6        for ( int num : nums){
7            set.add(num);
8        }
9
10        int ans = 0;
11        for ( int num : set){
12            if ( !(set.contains(num-1))){
13                int length =0 ;
14                while(set.contains(num+length)){
15                    length++;
16                }
17                ans = Math.max(length , ans);
18
19            }
20        }
21        return ans;
22
23
24    }
25}