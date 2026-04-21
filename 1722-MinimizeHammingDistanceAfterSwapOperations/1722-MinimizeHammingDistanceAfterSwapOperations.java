// Last updated: 21/04/2026, 20:15:22
1class Solution {
2
3    private int [] parent;
4    private int find(int x ){
5        if ( parent[x] != x) parent[x] = find(parent[x]);
6        return parent[x];
7    }
8    private void unite(int a , int b){
9        parent[find(a)] = find(b);
10    }
11    public int minimumHammingDistance(int[] source, int[] target, int[][] allowedSwaps) {
12        int n = source.length;
13
14        parent = new int[n];
15        for ( int i = 0 ;i<n;i++) parent[i] = i;
16
17
18
19        for( int [] swap: allowedSwaps){
20            unite(swap[0],swap[1]);
21        }
22
23        Map<Integer, Map<Integer,Integer>>groups = new HashMap<>();
24
25        for (int i = 0; i < n; i++) {
26            int root = find(i);
27            groups.computeIfAbsent(root, k -> new HashMap<>())
28                  .merge(source[i], 1, Integer::sum);
29        }
30
31        int hammingDist = 0;
32        for (int i = 0; i < n; i++) {
33            int root = find(i);
34            Map<Integer, Integer> freq = groups.get(root);
35            if (freq.getOrDefault(target[i], 0) > 0) {
36                freq.merge(target[i], -1, Integer::sum); // matched, consume this source value
37            } else {
38                hammingDist++;                           // no match found in this component
39            }
40        }
41
42        return hammingDist;
43
44
45
46
47
48
49    }
50}