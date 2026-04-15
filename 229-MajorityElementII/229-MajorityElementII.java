// Last updated: 15/04/2026, 12:56:34
1class Solution {
2    public List<Integer> majorityElement(int[] nums) {
3        final int n = nums.length;
4        int a = 0 , ca = 0;
5        int b = 0 , cb = 0;
6        int m = (n/3)+1;
7        List<Integer> ans= new ArrayList<>();
8        
9        for ( int num :nums){
10            if (num == a){
11                ca++;
12            }
13            else if ( num == b){
14                cb ++;
15            }
16            else if( ca == 0){
17                a = num;
18                ca =1;
19            }
20            else if ( cb ==0){
21                b = num;
22                cb = 1;
23            }
24            else {
25                ca-=1;
26                cb-=1;
27            }
28
29
30        }
31
32
33        ca = 0;
34        cb = 0;
35        for ( int num :nums){
36            if ( num == a ) ca++;
37            else if ( num == b) cb++;
38        }
39        if ( ca >=m) ans.add(a);
40        if ( cb>=m) ans.add(b);
41        return ans;
42
43        
44
45    }
46}