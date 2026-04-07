// Last updated: 07/04/2026, 11:33:24
class Solution {
public:
    int maximumSum(vector<int>& nums) {
        
        int val = 0;
        vector<int>r0,r1,r2;
        
        for (int x :nums){
            if ( x%3 == 0) r0.push_back(x);
            if ( x%3 == 1) r1.push_back(x);
            if ( x%3 == 2) r2.push_back(x);
        }
        auto cmp = [](int a , int b){
            return a>b;
        };
        sort(r0.begin(),r0.end(),cmp);
        sort(r1.begin(),r1.end(),cmp);
        sort(r2.begin(),r2.end(),cmp);

        int ans = 0;
        if ( r0.size() >=3){
            ans =max(ans,r0[0]+r0[1]+r0[2]);
        }
        if ( r1.size() >=3){
            ans =max(ans,r1[0]+r1[1]+r1[2]);
        }
        if ( r2.size() >=3){
            ans =max(ans,r2[0]+r2[1]+r2[2]);
        }
        if (r0.size() && r1.size() && r2.size()){
            ans = max(ans, r0[0]+r1[0]+r2[0]);
        }
        return ans;
    }
        

        
};