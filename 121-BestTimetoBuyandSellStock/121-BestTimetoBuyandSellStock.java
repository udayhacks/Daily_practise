// Last updated: 13/04/2026, 12:01:04
1class Solution {
2    public int maxProfit(int[] prices) {
3
4        int n = prices.length;
5        int [] succ = new int[n];
6        succ[n-1] = prices[n-1];
7
8        for ( int i = n-2 ; i>=0 ;i--){
9            
10            succ[i] = Math.max(succ[i+1],prices[i]);
11            
12        } 
13
14        int res = 0;
15        for ( int i = 0 ;i<n;i++){
16            int temp = succ[i] - prices[i];
17            res  = Math.max(temp,res);
18        }
19        return res;
20        
21    }
22}