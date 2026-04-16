// Last updated: 16/04/2026, 11:31:44
1class Solution {
2    public int[][] merge(int[][] intervals) {
3        
4        // here a[0]-b[0] > 0 b comes first else a ; 
5        // sorting according to starting value ASCE 
6
7        Arrays.sort( intervals , (a,b)-> a[0]-b[0]);
8
9
10        int n = intervals.length;
11        List<int[]> result = new ArrayList<>();
12
13        int[] current = intervals[0];
14
15        for ( int i =1 ; i<n;i++){
16            int [] next = intervals[i];
17
18            if ( current[1] >= next[0]){
19                current[1] = Math.max(current[1],next[1]);
20
21            }else{
22                result.add(current);
23                current = next;
24            }
25
26        }
27        result.add(current);
28
29        return result.toArray(new int[result.size()][2]);
30
31
32
33
34
35    }
36}