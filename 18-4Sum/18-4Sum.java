// Last updated: 16/04/2026, 11:08:13
1class Solution {
2    public List<List<Integer>> fourSum(int[] nums, int target) {
3        List<List<Integer>> result = new ArrayList<>();
4        Arrays.sort( nums);
5        
6        int n = nums.length;
7
8
9        for ( int i = 0 ; i<n;i++){
10            if ( i != 0 && nums[i] == nums[i-1]) continue;
11            
12            for ( int j = i+1 ; j <n;j++){
13                if ( j > i+1 && nums[j] == nums[j-1]) continue;
14                
15                int left = j +1;
16                int right = n-1;
17
18                while( left < right){
19                    long  sum =  (long)nums[i]+nums[j]+ nums[left]+ nums[right];
20                    if ( sum == target){
21                        
22                        result.add( Arrays.asList(nums[i], nums[j], nums[left], nums[right]));
23
24                        left ++; 
25                        right --;
26
27                        while( left < right && nums[left] == nums[left-1]) left ++; 
28                        while( left < right && nums[right] == nums[right+1]) right --;
29                    }
30                    else if ( sum < target){
31                        left ++;
32                    }else{
33                        right--;
34                    }
35                }
36            }
37        }
38        return result;
39        
40    }
41}