// Last updated: 07/04/2026, 11:33:29
class Solution {
public:
    long long maximumScore(vector<int>& nums, string s) {
        long long ans = 0;
        vector<pair<int,int>> v;
        set<int> ones;
        int n = nums.size();
        for ( int i = 0 ; i<n;i++){
            v.push_back({nums[i],i});
            if ( s[i] == '1') ones.insert(i);
        }
        auto cmp = [](auto a ,auto b) {return a.first > b.first;};
        sort(v.begin(),v.end() ,cmp);

        for ( int i = 0 ; i<n;i++){
            auto index = ones.lower_bound(v[i].second);
            if ( index == ones.end())  continue;
            ans+=v[i].first;
            ones.erase(index);
        }
        return ans;

        

        
        
        
    }
};