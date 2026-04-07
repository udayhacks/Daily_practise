// Last updated: 07/04/2026, 11:35:22
class Solution {
public:
    string decodeCiphertext(string encodedText, int rows) {
        string ans ="";
        
        int rc = encodedText.size();
        int r = rows;
        int c = rc/r;

        vector<vector<char>> M(r,vector<char>(c,0));
        int k = 0;

        for (int i = 0 ;i<r;i++){
            for (int j = 0;j<c;j++){
                
                M[i][j] =encodedText[k++];
            }
            if ( k == rc ) break;
        }


        for ( int col = 0;col<c;col++){

            int row = 0;
            int k = col;
            while(row <r && k <c){
                
                ans+=M[row++][k++];
                
            }
        }


        int n = ans.size();
        int m = n;
        for ( int i = n-1;i>=0;i--){
            if ( ans[i] ==' ') m--;
            if ( ans[i]!=' ')break;
        }
        return ans.substr(0,m);

        
       
    }
};