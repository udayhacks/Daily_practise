// Last updated: 10/04/2026, 08:23:38
1class Solution {
2    public int minimumDistance(int[] nums) {
3
4        int ans =Integer.MAX_VALUE;
5        int n = nums.length;
6
7
8        for ( int i = 0; i<n;i++){
9            for ( int j = 0;j<n;j++){
10                for ( int k = 0;k<n;k++){
11                    if (  (i!= j) && (j!= k) && (i!=k) ){
12                        if ( nums[i] == nums[j] && nums[j] == nums[k]){
13                            int temp = Math.abs(i-j)+Math.abs(j-k)+Math.abs(k-i);
14                            ans = Math.min(ans,temp);
15                        }
16                        
17                    } 
18                }
19            }
20        }
21        return ( ans == Integer.MAX_VALUE)? ans = -1: ans;
22
23        
24    }
25}