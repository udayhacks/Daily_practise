// Last updated: 07/04/2026, 11:38:14
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string,int> mp;
        for ( string word: words) mp[word]++;
        vector<pair<int,string>> lst;
        for ( auto [u,v] : mp){
            lst.push_back({-v,u});
        }
        make_heap(begin(lst),end(lst),greater<>());
        vector<string>ans;
        while(k--){
            pop_heap(begin(lst),end(lst),greater<>());
            ans.push_back(lst.back().second);
            lst.pop_back();
        }
        return ans;
        
        
    }
};