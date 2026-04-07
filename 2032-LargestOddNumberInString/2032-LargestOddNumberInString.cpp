// Last updated: 07/04/2026, 11:35:32
class Solution {
public:
    string largestOddNumber(string num) {
        
        int n = num.size();
        string ans; 
        int m = -1;

        for ( int i= n-1;i>=0;i--){
            int v = num[i]-'0';
            if ( v%2 == 1){
                m = i;
                break;
               
            }
        }
        if ( m == -1) return ans;


        for ( int i = 0;i<=m;i++){
            ans+=num[i];
        }
        return ans ;




    }
};