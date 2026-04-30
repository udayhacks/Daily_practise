// Last updated: 30/04/2026, 16:19:27
1class Solution {
2public:
3    vector<int> findErrorNums(vector<int>& nums) {
4
5        int n = nums.size();
6        vector<int> a (n+1,-1);
7        int r= -1;
8
9        for ( int i = 0 ; i <n;i++){
10            if(a[nums[i]] != -1)  r = nums[i];
11            if ( a[nums[i]] == -1) a[nums[i]] = nums[i];
12        }
13        int m = -1;
14        for ( int i = 1; i<=n;i++){
15            if ( a[i] == -1){
16                m = i;
17                break;
18            }
19        }
20        return {r,m};
21
22    }
23};