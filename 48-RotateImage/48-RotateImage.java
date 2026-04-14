// Last updated: 14/04/2026, 22:17:50
1class Solution {
2    public int[] reverse(int[] arr){
3        int n = arr.length;
4        int left = 0 ;
5        int right = n-1;
6
7        while( left < right){
8            int temp  = arr[left];
9            arr[left] = arr[right];
10            arr[right] = temp;
11            left++ ;
12            right--;
13        }
14        return arr;
15    }
16
17    public void rotate(int[][] matrix) {
18        int rows = matrix.length;
19        int cols = matrix[0].length;
20        // diagonal swapping
21        for ( int row = 0 ;row <rows;row++){
22            for ( int col = row  ;col <cols; col++){
23                int tmp = matrix[row][col];
24                matrix[row][col] = matrix[col][row];
25                matrix[col][row] = tmp;
26            }
27        }
28
29        for (int row = 0 ;row <rows;row ++){
30            matrix[row] = reverse(matrix[row]);
31        }
32
33
34
35
36    }
37}