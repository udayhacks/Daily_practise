// Last updated: 07/04/2026, 11:40:49
class Solution {
public:
    string reverseWords(string s) {

        vector<string>a;

        string w;
        stringstream  ss(s);

        while(ss>>w){
            a.push_back(w);
        }

        string ans ;
        int n = a.size();
        for ( int i = n-1;i>=0;i--){
            ans+=a[i];
           if ( i !=0) ans+=" ";
        }
        return ans;


    }
};