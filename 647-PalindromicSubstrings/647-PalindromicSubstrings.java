// Last updated: 28/04/2026, 08:06:01
1class Solution {
2
3    private int check(String s , int l , int r){
4         
5        int res = 0 ;
6
7        while( l >=0 && r <s.length() && s.charAt(l) == s.charAt(r)){
8            res ++;
9            l -- ; 
10            r++;
11        }
12        return res;
13
14    }
15
16    public int countSubstrings(String s) {
17
18        int result = 0 ;
19        
20        for ( int i = 0 ;i <s.length();i++){
21            result+=check(s,i,i);
22            result+=check(s,i,i+1);
23
24        }
25        return result;
26    }
27}