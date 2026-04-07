// Last updated: 07/04/2026, 11:33:28
class Solution {
public:
    string mapWordWeights(vector<string>& words, vector<int>& weights) {
        vector<char> alp(26);
        for ( int i = 0 ;i<26;i++) alp[i] = 'z'-i;
        string ans ="";
        for ( const string &word: words){
            int total= 0;
            for ( char c : word){
                int val = weights[c-'a'];
                total+=val;
            }
            total = total%26;
            ans+=alp[total];
        }
        return ans;
        
    }
};