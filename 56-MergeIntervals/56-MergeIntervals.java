// Last updated: 16/04/2026, 11:32:47
1class Solution {
2    public int[][] merge(int[][] intervals) {
3        
4        // here a[0]-b[0] > 0 b comes first else a ; 
5        // sorting according to starting value ASCE 
6
7        Arrays.sort( intervals , (a,b)-> a[0]-b[0]);
8        
9        int [][] freak = new int[3][4];
10
11
12        int n = intervals.length;
13        List<int[]> result = new ArrayList<>();
14
15        int[] current = intervals[0];
16
17        for ( int i =1 ; i<n;i++){
18            int [] next = intervals[i];
19
20            if ( current[1] >= next[0]){
21                current[1] = Math.max(current[1],next[1]);
22
23            }else{
24                result.add(current);
25                current = next;
26            }
27
28        }
29        result.add(current);
30
31        return result.toArray(new int[result.size()][2]);
32
33
34
35
36
37    }
38}