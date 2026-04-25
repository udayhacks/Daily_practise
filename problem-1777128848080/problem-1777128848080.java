// Last updated: 25/04/2026, 20:24:08
1class Solution {
2    public boolean validDigit(int n, int x) {
3
4
5    
6        int r = 0;
7        boolean flag = false;
8
9        while(n >0 ){
10           r = n%10;
11            if ( r == x) flag = true;
12            n = n/10;
13        }
14        if ( r == x ) flag = false;
15        return flag;
16
17    }
18
19   
20}