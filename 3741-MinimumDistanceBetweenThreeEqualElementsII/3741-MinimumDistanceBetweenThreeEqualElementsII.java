// Last updated: 11/04/2026, 17:25:35
1import java.util.*;
2
3class Solution {
4
5    private HashMap<Integer,ArrayList<Integer>> map = new HashMap<>();
6
7    private HashMap<Integer,ArrayList<Integer>> build(int[] nums){
8        
9        
10        
11        int n = nums.length;
12
13        for ( int i = 0;i<n;i++){
14
15            if ( map.containsKey(nums[i])){
16                map.get(nums[i]).add(i);
17            }else{
18                ArrayList <Integer> values = new ArrayList<>();
19
20                values.add(i);
21                map.put(nums[i],values);
22            }
23        }
24
25        return map;
26
27
28    }
29
30    private int cal(){
31
32        int minVal = Integer.MAX_VALUE; 
33
34        
35        
36    
37    for ( Map.Entry<Integer, ArrayList<Integer>> entry : map.entrySet()){
38
39        ArrayList <Integer> list = entry.getValue();
40
41        if ( list.size()>=3){
42
43            for ( int i = 0;i<list.size()-2;i++){
44                int val = 2*(list.get(i+2)-list.get(i));
45                minVal = Math.min(minVal, val);
46            }
47        }
48        
49
50    } return (minVal == Integer.MAX_VALUE) ? -1 : minVal;
51
52
53    }
54    
55
56
57    public int minimumDistance(int[] nums) {
58            build(nums);
59            return cal();
60    }
61}