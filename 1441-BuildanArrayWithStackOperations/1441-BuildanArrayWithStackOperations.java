// Last updated: 01/05/2026, 07:58:31
1class Solution {
2    public List<String> buildArray(int[] target, int n) {
3
4        int N = target.length;
5
6       
7        int [] temp = new int[target[N-1]+1];
8
9        for ( int  i : target){
10            temp[i] = i;
11        }
12
13        List<String> result = new ArrayList<>();
14
15        for ( int i = 1; i<temp.length;i++){
16            result.add("Push");
17            if ( temp[i] != i ){
18                result.add("Pop");
19            }
20        }
21        return result;
22
23
24
25    }
26}