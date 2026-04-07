// Last updated: 07/04/2026, 11:43:25
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        
        sort(strs.begin(),strs.end());
        string s1 = strs.front();
        string s2 = strs.back();

        int n = min(s1.size(),s2.size());

        int i = 0;
        string ans;
        
        while(i<n){
            if ( s1[i] != s2[i]){
                break;
            }
            ans+=s1[i];
            i++;
        }
        return ans;


    }
};