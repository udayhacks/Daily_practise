// Last updated: 16/04/2026, 12:40:55
1class Solution {
2    public void merge(int[] nums1, int m, int[] nums2, int n) {
3
4
5        if ( m == 0 ) {
6            
7            for ( int i = 0 ; i<n;i++){
8                nums1[i] = nums2[i];
9            }
10
11
12            return ; 
13        }
14        if ( n == 0) return ; 
15
16
17        int I = n+m-1 ; 
18        int i = m-1;
19        int j = n-1;
20
21
22        while( i >=0 && j >=0 ){
23
24            if ( nums1[i] > nums2[j]){
25                nums1[I] = nums1[i];
26                i --;  
27            }
28            else {
29                nums1[I] = nums2[j];
30                j--;
31            }
32            I --;
33            
34        }
35
36        while( j >=0){
37            nums1[I] = nums2[j];
38            I--;
39            j--;
40        }
41
42
43
44
45
46        
47
48    
49        
50    }
51}