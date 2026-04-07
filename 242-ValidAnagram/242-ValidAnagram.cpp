// Last updated: 07/04/2026, 11:39:46
class Solution {
public:
    bool isAnagram(string s, string t) {
        
        sort(s.begin(),s.end());
        sort(t.begin(),t.end());
        return s == t ;
    }
};