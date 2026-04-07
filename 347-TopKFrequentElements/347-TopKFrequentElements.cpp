// Last updated: 07/04/2026, 11:39:19
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int,int> mp ;
        vector<int> ans ; 
        set<pair<int,int>> s;
        for (int i : nums)  mp[i]++;
        for (  auto &[u,v] : mp  ){
        s.insert({v,u});
    }
    auto rev_it = s.rbegin(); 
    int count = 0;

    for (; rev_it != s.rend() && count < k; ++rev_it, ++count) {
        ans.push_back(rev_it->second);
    }
    return ans;}
    
};