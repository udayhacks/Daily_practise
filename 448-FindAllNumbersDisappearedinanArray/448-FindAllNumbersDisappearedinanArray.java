// Last updated: 01/05/2026, 07:29:53
1class Solution {
2    public List<Integer> findDisappearedNumbers(int[] nums) {
3        
4        int [] temp = new int [nums.length+1];
5
6        for ( int i :nums){
7            temp[i] = i;
8        }
9
10        List<Integer> result = new ArrayList<>();
11
12        for ( int i = 1 ; i<temp.length;i++){
13            if ( temp[i] != i) result.add(i);
14        }
15
16        return result;
17
18        
19        
20        
21    }
22}