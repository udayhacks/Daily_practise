// Last updated: 07/04/2026, 11:33:46
class Solution {
public:
    long long calculateScore(vector<string>& instructions, vector<int>& values) {

    int n = values.size();

        vector<int>vs(n,1);

        int i = 0 ;
        long long ans = 0;
        while ((i>=0 && i <n) && vs[i]==1){
             vs[i] = 0;
            if ( instructions[i] =="add"){
                ans+=values[i];
               
                i++;
                continue;
            }
            i= i+values[i];
            
        }
        return ans;
    }
};