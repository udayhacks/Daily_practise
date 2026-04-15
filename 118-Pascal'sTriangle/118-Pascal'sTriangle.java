// Last updated: 15/04/2026, 12:47:21
1class Solution {
2    public List<List<Integer>> generate(int numRows) {
3
4              List<List<Integer>> pascal = new ArrayList<>();
5            
6            ArrayList <Integer> f = new ArrayList<>();
7            f.add(1);
8            pascal.add(f);
9
10            for ( int i = 1;i<numRows;i++){
11                
12                ArrayList<Integer> temp = new ArrayList<>();
13
14
15                for ( int j =0;j <i+1;j++){
16
17                    int left = 0 ; 
18                    int top= 0 ; 
19                    if ( j-1 >= 0) left = pascal.get(i - 1).get(j - 1);
20                    if ( j < i)  top = pascal.get(i - 1).get(j );
21                    temp.add(left+top);
22
23                }
24                pascal.add(temp);
25                
26
27            
28            }
29            return pascal;
30
31
32
33
34    }
35}