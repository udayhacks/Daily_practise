// Last updated: 07/04/2026, 11:40:23
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        
        map<char,char> st;
        map<char,char> ts;
        if ( s.size() != t.size()) return false;
        int n = s.size();

        
        for (int i = 0 ;i<n;i++){

            if ( st.count(s[i])){
                if (st[s[i]] != t[i]) return false;
            }else{
                st[s[i]] = t[i];
            }

            if ( ts.count(t[i])){
                if ( ts[t[i]] != s[i]){
                    return false;
                }
            }
            else{
                ts[t[i]] = s[i];
            }




        }
        return true;

    }
};