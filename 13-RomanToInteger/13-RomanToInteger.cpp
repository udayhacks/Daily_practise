// Last updated: 07/04/2026, 11:43:27
class Solution {
public:
    int romanToInt(string s) {
        int total = 0 ; 
        map<char,int> mp;
        mp['I'] = 1;
        mp['V'] = 5;
        mp['X'] = 10;
        mp['L'] = 50;
        mp['C'] = 100;
        mp['D'] = 500;
        mp['M'] = 1000;

        int n = s.size();
        if ( n == 0) return total;

        total+=mp[s[0]];

        for ( int i = 1;i<n;i++){
            total+=mp[s[i]];
            if ( mp[s[i-1]] < mp[s[i]]){
                total-=(2*mp[s[i-1]]);
            }
            
        }
        return total;


    }
};