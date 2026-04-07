// Last updated: 07/04/2026, 11:35:18
class Solution {
public:
    int maxTwoEvents(vector<vector<int>>& events) {
        vector<pair< int , pair<int,int>>> list;
        int n = events.size();
        
        
        for (int i = 0 ; i<n;i++){
            list.push_back({events[i][0],{true,events[i][2]}});
            list.push_back({events[i][1]+1,{false,events[i][2]}});
        }
        sort(list.begin(),list.end());
        int maxval = 0;
        int total = 0;

        for ( auto lst :list){

            int node = lst.first;
            bool typeNode = lst.second.first;
            int val = lst.second.second;

            if ( typeNode){
                total = max(total , val+maxval);
            }else{
                maxval = max(maxval,val);
            }
        }

        return total;
        


    }

};