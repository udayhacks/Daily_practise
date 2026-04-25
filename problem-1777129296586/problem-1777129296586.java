// Last updated: 25/04/2026, 20:31:36
1class Solution {
2    public int compareBitonicSums(int[] nums) {
3
4
5        int index = -1;
6
7        int n = nums.length;
8        for (int i = 0 ;i<n-1;i++){
9            if ( nums[i]> nums[i+1]) {
10                index = i ;
11                break;
12            }
13        }
14
15        long  left = 0 ;
16        for ( int i = 0 ;i<=index;i++){
17            left+= (long)nums[i];
18        }
19        long  right = 0 ; 
20        for ( int i = index; i<n;i++){
21            right +=(long)nums[i];
22        }
23        if ( left == right ){
24            return -1;
25        }else if ( left<right){
26            return 1;
27        }else{
28            return 0 ;
29        }
30
31
32
33        
34    }
35}