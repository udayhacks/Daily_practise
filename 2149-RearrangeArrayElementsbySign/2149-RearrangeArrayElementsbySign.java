// Last updated: 13/04/2026, 12:17:33
1class Solution {
2    public int[] rearrangeArray(int[] nums) {
3        int n = nums.length;
4        int m = n/2;
5        int [] neg = new int[m];
6        int [] pos = new int[m];
7        int j= 0;
8        int l= 0;
9
10        for ( int i : nums){
11            if ( i >0){
12                pos[l] = i;
13                l++;
14            }else{
15                neg[j] = i;
16                j++;
17            }
18        }
19        int [] ans = new int[n];
20        int k = 0 ;
21        l = 0;
22        for ( int i =  0 ;i<n;i++){
23            
24            if ( i %2 ==0) ans[i] = pos[k++];
25            if ( i %2 !=0) ans[i] = neg[l++];
26        }
27        return ans;
28
29    }  
30}