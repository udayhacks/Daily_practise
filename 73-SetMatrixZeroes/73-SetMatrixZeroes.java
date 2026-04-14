// Last updated: 14/04/2026, 10:45:14
1class Solution {
2    public void setZeroes(int[][] matrix) {
3        int r = matrix.length;
4        int c = matrix[0].length;
5
6        // flag for if first row have 0     
7        boolean row = false;
8        // flag for if col have 0 ;
9        boolean col = false;
10
11
12        for ( int i = 0 ;i<r;i++){
13            if ( matrix[i][0] == 0) {
14                col= true;
15                break;
16            }
17        }
18
19        for ( int i  = 0;i<c;i++){
20            if ( matrix[0][i] == 0){
21                row = true;
22                break;
23            }
24        }
25
26
27        // now using first col and row is extra storage for markering 0 like matrix[i][j] = 0 then matix[o][j] = 0 and matrix[i][0] = 0 ;
28
29        for ( int i = 1 ; i<r;i++){
30            for( int j = 1 ;j <c;j++){
31                if ( matrix[i][j] == 0){
32                    matrix[i][0] = 0 ;
33                    matrix[0][j] = 0 ;
34                }
35            }
36        }
37
38        // now travesering matrix and checking if matrix[o][j] or matrix[i][0] are zero ;
39
40        for ( int i = 1; i<r;i++){
41            for ( int j = 1;j <c;j++){
42                if ( matrix[i][0] == 0  || matrix[0][j] == 0 ) matrix[i][j] = 0;
43            }
44        }
45
46        if ( col){
47            for ( int i = 0;i< r;i++){
48                matrix[i][0] = 0;
49            }
50        }
51        if ( row ){
52            for ( int i = 0 ; i <c ; i++) matrix[0][i] = 0;
53        }
54
55
56
57        
58
59
60
61
62
63
64
65
66
67
68
69
70
71    ///
72    }
73
74}