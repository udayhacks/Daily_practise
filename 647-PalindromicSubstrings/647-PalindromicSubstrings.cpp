// Last updated: 28/04/2026, 08:08:46
1class Solution {
2
3private : 
4    int check(string s, int l ,int r){
5        int res = 0 ; 
6        while( l >=0 && r<s.size()&& s[l] == s[r]){
7            res ++;
8            l--;
9            r++;
10        }
11        return res;
12    }
13public:
14    int countSubstrings(string s) {
15        int result = 0 ;
16        for ( int i = 0 ; i<s.size();i++){
17            result +=check(s,i,i);
18            result+=check(s,i,i+1);
19        }
20        return result;
21    }
22};