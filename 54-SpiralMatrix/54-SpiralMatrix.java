// Last updated: 15/04/2026, 12:03:07
1class Solution {
2    public List<Integer> spiralOrder(int[][] matrix) {
3        
4        int row = matrix.length;
5        int col = matrix[0].length;
6
7        int left = 0 ; 
8        int right = col-1 ;
9        int top = 0 ; 
10        int down = row-1;
11        ArrayList<Integer> ans = new ArrayList<>();
12
13
14
15        while( left <= right && top <= down){
16            for ( int i = left ; i<=right;i++){
17                    ans.add(matrix[top][i]);
18            }
19            top++;
20            for ( int i = top ; i<=down;i++){
21                ans.add(matrix[i][right]);
22            }
23            right--;
24
25            // if matirx is has single col base condition 
26
27            if ( top <= down){
28                for( int i = right ; i >=left;i--){
29                    ans.add( matrix[down][i]);
30                }
31                down --;
32
33            }
34
35            // if  matrix is single row also base case ; 
36
37            if ( left <= right){
38                for ( int i = down ; i>=top;i--){
39                    ans.add( matrix[i][left]);
40                }
41                left++;
42            }
43
44            
45        }
46
47        return ans;
48    }
49}