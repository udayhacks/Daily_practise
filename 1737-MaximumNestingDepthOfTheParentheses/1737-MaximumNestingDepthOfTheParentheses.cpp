// Last updated: 07/04/2026, 11:35:57
class Solution {
public:
    int maxDepth(string s) {
        int ans = 0 ;
        int bal = 0;

        for ( char c :s){
            if ( c =='('){
                bal++;
            }else if ( c ==')'){
                bal--;
            }
            ans = max(bal,ans);
        }
        //ans = max(bal,ans);
        return ans;
    }
};