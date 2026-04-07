// Last updated: 07/04/2026, 11:43:56
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char, int> mp;
        
        

        int ans = 0 ; 
        int n = s.size();
        int l = 0; 
        int count = 0 ;
        if ( n == 0) return 0 ; 
        

        for ( int j = 0 ; j<n;j++)
        {
            if (  mp.find(s[j]) != mp.end() && l <=mp[s[j]]){
                l = mp[s[j]]+1;
            }
         
        
            count = j-l+1;
            ans = max(ans,count);
            mp[s[j]] = j ;
            
        }
        return ans;
    }
};