// Last updated: 07/04/2026, 11:38:53
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        int n = g.size(),m = s.size(),l=0,r=0;
        sort(g.begin(),g.end());
        sort(s.begin(),s.end());
        while(l<n && r<m){
            if(s[r]>=g[l])
                l++;
            r++;
        }
        return l;
    }
};