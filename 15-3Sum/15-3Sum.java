// Last updated: 15/04/2026, 19:30:46
1class Solution {
2    public List<List<Integer>> threeSum(int[] nums) {
3        HashMap <Integer, ArrayList<Integer>> map = new HashMap<>();
4
5        List<List<Integer>> res = new ArrayList<>();
6        
7        int n = nums.length;
8        Arrays.sort(nums);
9
10
11        for ( int i = 0 ; i < n ;i++ ){
12
13            if ( i >0 && nums[i] == nums[i-1]) continue; 
14
15            int left = i+1;
16            int right = n-1;
17
18            while( left < right){
19
20                // removing dulipcates here ;
21
22                int sum = nums[i]+ nums[left] + nums[right];
23
24
25
26                if ( sum == 0 ){
27                    
28                    res.add(Arrays.asList(nums[i],nums[left],nums[right]));
29                    left ++; 
30                    right--;
31                    
32
33                    // also removing dulipates;
34
35                    while( left < right && nums[left] == nums[left-1]) left ++;
36                    while(left < right && nums[right] == nums[right+1]) right--; 
37                }
38                else if ( sum <0 ){
39                    left ++;
40                    // increse sum slightly;
41                }else {
42                    right--;
43                    // decrease sum ;
44                }
45
46
47            }
48
49           
50
51
52
53            
54
55        }
56         return res;
57        
58        
59
60    }
61            
62            
63}