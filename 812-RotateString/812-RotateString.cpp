// Last updated: 07/04/2026, 11:37:53
class Solution {
public:
    bool rotateString(string s, string goal) {

        if ( s.size() != goal.size()) return false;
        s = s+s;

        int n = s.size();
        int m = goal.size();
        

       return s.find(goal) != string::npos;

        
        
    }
};