// Last updated: 07/04/2026, 11:33:23
class Solution {
public:
    int prefixConnected(vector<string>& words, int k) {
        unordered_map<string,int> mp;
        set<string>pre;
        for ( const string& word : words){
            if ( word.size()>=k){
                string s = word.substr(0,k);
                pre.insert(s);
                mp[s]++;
            }
        }
        int ans = 0;
        for ( const string & s : pre){
            if ( mp[s] >=2){
                ans++;
            }
        }
        return ans;
    }
};