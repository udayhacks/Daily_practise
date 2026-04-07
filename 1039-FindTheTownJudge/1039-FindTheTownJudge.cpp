// Last updated: 07/04/2026, 11:37:15
class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        
        vector<int>from (n+1,0);
        vector<int>to (n+1,0);
        int maxi = 0;
        int index = -1;
        for ( auto &val : trust){
            int a = val[0];
            int b = val[1];
            to[b]++;
            from[a]++;
        }
        for ( int i =1;i<n+1;i++){

            if ( to[i] == n-1 && from [i] == 0) return i;
        }return -1;


        



    }
};