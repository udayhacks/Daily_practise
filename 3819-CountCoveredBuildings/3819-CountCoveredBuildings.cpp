// Last updated: 07/04/2026, 11:33:38
class Solution {
public:
    int countCoveredBuildings(int n, vector<vector<int>>& buildings) {
        
        vector<pair<int,int>> r(n+1,{INT_MAX,INT_MIN});
        vector<pair<int,int>> c(n+1,{INT_MAX,INT_MIN});

        for ( auto &build :buildings){
            

            r[build[0]].first = min(r[build[0]].first,build[1]);
             r[build[0]].second = max(r[build[0]].second,build[1]);

        }

        for ( auto &build :buildings){

            c[build[1]].first = min(c[build[1]].first,build[0]);
            c[build[1]].second = max(c[build[1]].second,build[0]);

        }





        

        int ans = 0;
        for ( int i = 0 ;i<buildings.size();i++){

            auto build = buildings[i];
            int minvalx = r[build[0]].first;
            int maxvalx = r[build[0]].second;
            int minvaly = c[build[1]].first;
            int maxvaly = c[build[1]].second;

           
            if ( build[1] > minvalx && build[1] < maxvalx &&  
            build[0] >minvaly  && build[0] <maxvaly){
                ans++;
            }
            }
             return ans;
        }  
       
};